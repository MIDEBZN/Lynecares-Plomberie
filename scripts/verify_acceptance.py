import os
import re
import json
from bs4 import BeautifulSoup

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
dist_dir = os.path.join(workspace, "dist")

def run_checks():
    print("=== STARTING COMPREHENSIVE ACCEPTANCE VALIDATION ===")
    errors = []
    warnings = []

    # 1. Gather all HTML files
    html_files = {}
    for root, dirs, files in os.walk(dist_dir):
        for f in files:
            if f == "index.html" or (f.endswith(".html") and not f.startswith("404")):
                fp = os.path.join(root, f)
                rel_path = os.path.relpath(fp, dist_dir).replace("\\", "/")
                if rel_path == "index.html":
                    url_path = "/"
                elif rel_path.endswith("/index.html"):
                    url_path = "/" + rel_path[:-10]
                else:
                    url_path = "/" + rel_path
                full_url = f"https://www.plomberieliegeoise.be{url_path}"
                html_files[full_url] = fp

    print(f"Total HTML pages built in dist: {len(html_files)}")

    # Parse all pages
    page_data = {}
    all_links = []
    canonical_map = {}
    h1_map = {}
    title_map = {}
    desc_map = {}

    for url, fp in html_files.items():
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        soup = BeautifulSoup(content, "html.parser")

        # Canonical
        canon_tag = soup.find("link", attrs={"rel": "canonical"})
        canon = canon_tag["href"].strip() if canon_tag and "href" in canon_tag.attrs else None
        canonical_map[url] = canon

        # Title
        t_tag = soup.find("title")
        title = t_tag.text.strip() if t_tag else ""
        title_map[url] = title

        # Description
        d_tag = soup.find("meta", attrs={"name": "description"})
        desc = d_tag["content"].strip() if d_tag and "content" in d_tag.attrs else ""
        desc_map[url] = desc

        # H1
        h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
        h1_map[url] = h1s

        # Links
        for a in soup.find_all("a", href=True):
            href = a["href"]
            all_links.append((url, href, a.get_text(strip=True)))

        # Structured data
        ld_scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
        parsed_schemas = []
        for s in ld_scripts:
            try:
                sd = json.loads(s.string)
                parsed_schemas.append(sd)
            except Exception as e:
                errors.append(f"Invalid JSON-LD on {url}: {e}")

        # Check unsupported claims
        body_text = soup.get_text()
        if "4.9/5" in body_text and "200 avis" in body_text:
            errors.append(f"Found unverified review claim '4.9/5 basé sur plus de 200 avis' on {url}")
        if "95% des pannes" in body_text:
            errors.append(f"Found unverified claim '95% des pannes' on {url}")
        if "garantie en 30 minutes" in body_text.lower():
            errors.append(f"Found unverified guarantee 'garantie en 30 minutes' on {url}")

        # Check phone and email consistency
        if "contact@plomberieliégeoise.be" in content:
            errors.append(f"Found typo email contact@plomberieliégeoise.be on {url}")

        page_data[url] = {
            "soup": soup,
            "title": title,
            "desc": desc,
            "canon": canon,
            "h1s": h1s,
            "schemas": parsed_schemas
        }

    # CHECK 1: Broken Internal Links
    broken_links = 0
    for source_url, href, anchor in all_links:
        # ignore external, tel, mailto, anchor-only
        if href.startswith("http://") or href.startswith("https://") or href.startswith("tel:") or href.startswith("mailto:") or href.startswith("#"):
            continue
        clean_href = href.split("#")[0].split("?")[0]
        if not clean_href:
            continue
        if not clean_href.startswith("/"):
            clean_href = "/" + clean_href
        target_url = f"https://www.plomberieliegeoise.be{clean_href}"
        # Normalize trailing slash
        if not target_url.endswith("/") and (target_url + "/") in html_files:
            target_url = target_url + "/"
        elif target_url.endswith("/") and target_url[:-1] in html_files:
            target_url = target_url[:-1]
            
        if target_url not in html_files:
            errors.append(f"Broken internal link from {source_url} to '{href}' (anchor: '{anchor}')")
            broken_links += 1

    print(f"Internal link check complete. Checked {len(all_links)} links. Broken: {broken_links}")

    # CHECK 2: Footer service links to generic hub
    for url, data in page_data.items():
        soup = data["soup"]
        footer = soup.find("footer")
        if footer:
            for a in footer.find_all("a", href=True):
                anchor = a.get_text(strip=True).lower()
                href = a["href"]
                if "rénovation" in anchor and href == "/services/":
                    errors.append(f"Footer link '{anchor}' on {url} points to generic /services/ instead of dedicated page!")
                if "urgence" in anchor and href == "/services/":
                    errors.append(f"Footer link '{anchor}' on {url} points to generic /services/ instead of dedicated page!")
                if "sanitaire" in anchor and href == "/services/":
                    errors.append(f"Footer link '{anchor}' on {url} points to generic /services/ instead of dedicated page!")
                if "débouchage" in anchor and href == "/services/":
                    errors.append(f"Footer link '{anchor}' on {url} points to generic /services/ instead of dedicated page!")

    # CHECK 3: Canonical consistency (self-canonical)
    for url, canon in canonical_map.items():
        if not canon:
            errors.append(f"Missing canonical on {url}")
        else:
            # normalize trailing slash comparison
            norm_url = url if url.endswith("/") else url + "/"
            norm_canon = canon if canon.endswith("/") else canon + "/"
            if norm_url != norm_canon:
                errors.append(f"Canonical mismatch on {url}: points to {canon}")

    # CHECK 4: Priority pages single H1 & unique titles
    priority_urls = [
        "https://www.plomberieliegeoise.be/",
        "https://www.plomberieliegeoise.be/services/urgences-plomberie/",
        "https://www.plomberieliegeoise.be/services/renovation-salle-de-bain-liege/",
        "https://www.plomberieliegeoise.be/services/chauffagiste-liege/",
        "https://www.plomberieliegeoise.be/services/installations-sanitaires/",
        "https://www.plomberieliegeoise.be/services/debouchage/",
        "https://www.plomberieliegeoise.be/services/entretien-plomberie-chauffage/",
        "https://www.plomberieliegeoise.be/blog/tarif-prix-plombier-liege-depannage/",
        "https://www.plomberieliegeoise.be/contact/",
        "https://www.plomberieliegeoise.be/locations/plombier-liege/",
        "https://www.plomberieliegeoise.be/locations/plombier-beyne-heusay/",
        "https://www.plomberieliegeoise.be/locations/plombier-grivegnee/",
        "https://www.plomberieliegeoise.be/locations/plombier-aywaille/",
        "https://www.plomberieliegeoise.be/locations/plombier-trooz/",
        "https://www.plomberieliegeoise.be/locations/plombier-juprelle/"
    ]

    for purl in priority_urls:
        if purl not in page_data:
            errors.append(f"Priority URL missing from build: {purl}")
            continue
        h1s = page_data[purl]["h1s"]
        if len(h1s) != 1:
            errors.append(f"Priority URL {purl} has {len(h1s)} H1 tags: {h1s}")
        if not page_data[purl]["title"]:
            errors.append(f"Priority URL {purl} has empty title")
        if not page_data[purl]["desc"]:
            errors.append(f"Priority URL {purl} has empty description")

    # CHECK 5: Titles duplication check among priority pages
    priority_titles = [page_data[p]["title"] for p in priority_urls if p in page_data]
    if len(priority_titles) != len(set(priority_titles)):
        errors.append("Duplicate titles detected among priority pages!")

    # CHECK 6: Sitemap validation
    sitemap_path = os.path.join(dist_dir, "sitemap-0.xml")
    if not os.path.exists(sitemap_path):
        sitemap_path = os.path.join(dist_dir, "sitemap-index.xml")
    
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            soup_s = BeautifulSoup(f.read(), "html.parser")
            s_locs = [l.text.strip() for l in soup_s.find_all("loc")]
            print(f"Sitemap found with {len(s_locs)} URLs.")
            for loc in s_locs:
                norm_loc = loc if loc.endswith("/") else loc + "/"
                if norm_loc not in html_files and norm_loc[:-1] not in html_files:
                    errors.append(f"Sitemap contains non-existent URL: {loc}")
    else:
        errors.append("Sitemap file not found in dist/")

    # CHECK 7: Check Structured Data
    # Homepage LocalBusiness
    hp_data = page_data.get("https://www.plomberieliegeoise.be/")
    if hp_data:
        has_lb = False
        for s in hp_data["schemas"]:
            if isinstance(s, dict) and s.get("@type") in ["PlumbingService", "Plumber", "LocalBusiness"]:
                has_lb = True
                if "aggregateRating" in s:
                    errors.append("Homepage schema contains unverified AggregateRating!")
                if s.get("telephone") not in ["+32466265895", "+32 466 26 58 95", "0466 26 58 95", "0466265895"]:
                    errors.append(f"Homepage telephone schema mismatch: {s.get('telephone')}")
                if s.get("email") != "contact@plomberieliegeoise.be":
                    errors.append(f"Homepage email schema mismatch: {s.get('email')}")
        if not has_lb:
            errors.append("Homepage missing LocalBusiness/PlumbingService schema!")

    # Article on price blog
    blog_data = page_data.get("https://www.plomberieliegeoise.be/blog/tarif-prix-plombier-liege-depannage/")
    if blog_data:
        has_art = False
        for s in blog_data["schemas"]:
            if isinstance(s, dict) and s.get("@type") == "Article":
                has_art = True
                if not s.get("headline"):
                    errors.append("Price blog Article schema missing headline")
                if not s.get("author"):
                    errors.append("Price blog Article schema missing author")
        if not has_art:
            errors.append("Price blog missing Article schema!")

    print("\n=== VALIDATION SUMMARY ===")
    if errors:
        print(f"FAIL: Found {len(errors)} error(s):")
        for e in errors:
            safe_e = e.encode("ascii", "replace").decode("ascii")
            print(f"  [X] {safe_e}")
    else:
        print("SUCCESS: All acceptance criteria checks passed! 0 errors detected.")

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            safe_w = w.encode("ascii", "replace").decode("ascii")
            print(f"  [!] {safe_w}")

if __name__ == "__main__":
    run_checks()
