#!/usr/bin/env python3
"""
Generate velli.bib from index_cards.json + PDF filenames + arXiv API.
Phase 1: Generate skeleton BibTeX from index_cards + filenames.
Phase 2: Enrich via arXiv API (batch).
"""
import json
import re
import os
import urllib.request
import urllib.parse
import time
import sys

INDEX_PATH = "/Users/huangzesen/work/lingtai-projects/marco_velli/.lingtai/paper-librarian/index/index_cards.json"
OUTPUT_PATH = "/Users/huangzesen/work/lingtai-projects/marco_velli/.lingtai/zhipu_intl/persona-marco-velli/velli.bib"

def generate_citekey(entry):
    """Generate a stable citekey from id."""
    eid = entry.get("id", "unknown")
    year = entry.get("year", "")
    # Extract first author surname from id
    # IDs like "Verdini_Velli_2007", "Pucci2013", "Badman2026"
    parts = re.split(r'[_\s]+', eid)
    # Remove year-like parts
    non_year = [p for p in parts if not re.match(r'^\d{4}$', p)]
    if non_year:
        first_author = re.sub(r'[^a-zA-Z]', '', non_year[0]).lower()
    else:
        first_author = "unknown"
    
    # Try to get second author
    second = ""
    if len(non_year) > 1:
        second = re.sub(r'[^a-zA-Z]', '', non_year[1]).lower()
        if second in ("velli",):
            second = "velli"
        elif len(second) > 10:
            second = second[:6]
    
    citekey = f"{first_author}{year}"
    if second and second != first_author:
        citekey = f"{first_author}{second}{year}"
    
    return citekey

def lookup_arxiv(arxiv_id):
    """Look up paper metadata from arXiv API."""
    if not arxiv_id:
        return None
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  arXiv lookup failed for {arxiv_id}: {e}", file=sys.stderr)
        return None

def parse_arxiv_response(xml_text):
    """Extract authors and title from arXiv XML response."""
    if not xml_text:
        return {}
    result = {}
    # Extract authors
    authors = re.findall(r'<name>(.*?)</name>', xml_text)
    if authors:
        result['authors'] = [a.strip() for a in authors]
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', xml_text, re.DOTALL)
    if title_match:
        result['title'] = title_match.group(1).strip().replace('\n', ' ')
    # Extract doi
    doi_match = re.search(r'<arxiv:doi[^>]*>(.*?)</arxiv:doi>', xml_text)
    if doi_match:
        result['doi'] = doi_match.group(1).strip()
    # Extract journal ref
    journal_match = re.search(r'<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>', xml_text)
    if journal_match:
        result['journal'] = journal_match.group(1).strip()
    return result

def format_authors_bibtex(authors_list):
    """Format authors for BibTeX."""
    if not authors_list:
        return "Velli, Marco and others"
    parts = []
    for a in authors_list:
        # Already "First Last" format usually
        a = a.strip()
        if ',' not in a:
            # Try to split into last, first
            words = a.split()
            if len(words) > 1:
                parts.append(f"{words[-1]}, {' '.join(words[:-1])}")
            else:
                parts.append(a)
        else:
            parts.append(a)
    return " and ".join(parts)

def generate_bibtex_entry(citekey, entry, arxiv_meta=None):
    """Generate a BibTeX entry string."""
    title = entry.get("title", "Unknown Title")
    year = entry.get("year", "")
    authors = []
    
    if arxiv_meta and arxiv_meta.get('authors'):
        authors = arxiv_meta['authors']
        if arxiv_meta.get('title'):
            title = arxiv_meta['title']
    
    # Determine entry type
    entry_type = "article"
    
    # Build fields
    fields = []
    fields.append(f"  title = {{{title}}}")
    fields.append(f"  author = {{{format_authors_bibtex(authors)}}}")
    fields.append(f"  year = {{{year}}}")
    
    if arxiv_meta:
        if arxiv_meta.get('doi'):
            fields.append(f"  doi = {{{arxiv_meta['doi']}}}")
        if arxiv_meta.get('journal'):
            fields.append(f"  journal = {{{arxiv_meta['journal']}}}")
    
    # Add topics as keywords
    topics = entry.get("topics", [])
    if topics:
        fields.append(f"  keywords = {{{', '.join(topics)}}}")
    
    fields.append(f"  note = {{Velli-related paper, indexed in persona-marco-velli}}")
    
    return f"@{entry_type}{{{citekey},\n" + ",\n".join(fields) + "\n}"

def main():
    phase = sys.argv[1] if len(sys.argv) > 1 else "skeleton"
    
    with open(INDEX_PATH) as f:
        papers = json.load(f)
    
    print(f"Loaded {len(papers)} papers from index_cards.json")
    
    if phase == "skeleton":
        # Phase 1: Generate skeleton from index data only
        entries = []
        for p in papers:
            ck = generate_citekey(p)
            bib = generate_bibtex_entry(ck, p)
            entries.append(bib)
        
        content = "% velli.bib — Auto-generated from index_cards.json\n"
        content += f"% {len(entries)} entries — SKELETON VERSION\n"
        content += "% TODO: Enrich with arXiv API (run with 'enrich' argument)\n\n"
        content += "\n\n".join(entries)
        
        with open(OUTPUT_PATH, 'w') as f:
            f.write(content)
        print(f"Wrote {len(entries)} entries to {OUTPUT_PATH}")
    
    elif phase == "enrich":
        # Phase 2: Try to enrich via arXiv API
        # Only do a batch (arXiv has rate limits)
        batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        start = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        
        # Try to extract arXiv IDs from paper IDs or titles
        enriched = 0
        for i, p in enumerate(papers[start:start+batch_size]):
            # Try common arXiv ID patterns from the id field
            arxiv_id = None
            pid = p.get("id", "")
            title = p.get("title", "")
            
            # Check if id contains arXiv-like pattern
            arxiv_match = re.search(r'(\d{4}\.\d{4,5}(?:v\d+)?)', pid)
            if not arxiv_match:
                # Try old format
                arxiv_match = re.search(r'(astro-ph/\d{7})', pid)
            
            if arxiv_match:
                arxiv_id = arxiv_match.group(1)
            
            if arxiv_id:
                print(f"  [{start+i}] Looking up {pid} -> arXiv:{arxiv_id}")
                xml = lookup_arxiv(arxiv_id)
                meta = parse_arxiv_response(xml)
                if meta:
                    ck = generate_citekey(p)
                    enriched += 1
                    # Print enriched entry
                    print(f"    Found: {meta.get('authors', [])[:2]}... ({meta.get('journal', 'no journal')})")
                time.sleep(0.5)  # Rate limit
            else:
                print(f"  [{start+i}] No arXiv ID for {pid}: {title[:60]}")
        
        print(f"\nEnriched {enriched}/{batch_size} entries from arXiv")

if __name__ == "__main__":
    main()
