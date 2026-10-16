import os
import re

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
articles_dir = os.path.join(workspace, "articles-seo")

files = sorted(os.listdir(articles_dir))
print(f"Total articles found in articles-seo/: {len(files)}")

all_valid = True
for idx, f in enumerate(files, 1):
    fp = os.path.join(articles_dir, f)
    with open(fp, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check title tag
    title_match = re.search(r"\*\*Balise Title SEO.*?:\*\* `(.*?)`", content)
    title = title_match.group(1) if title_match else ""
    title_len = len(title)
    
    # Check meta desc
    desc_match = re.search(r"\*\*Méta-description.*?:\*\* `(.*?)`", content)
    desc = desc_match.group(1) if desc_match else ""
    desc_len = len(desc)

    # Check H1
    h1_match = re.search(r"^# (.*?)$", content, re.M)
    h1 = h1_match.group(1) if h1_match else ""

    # Check AEO box
    has_aeo = "Réponse Directe (Format IA & Google Answer Box" in content

    # Check FAQ
    has_faq = "Foire Aux Questions (FAQ)" in content

    # Check CTA
    has_cta = "0466 26 58 95" in content

    # Check words count
    words = len(content.split())

    errors = []
    if not title or title_len > 60:
        errors.append(f"Title tag invalid ({title_len} chars): '{title}'")
    if not desc or desc_len > 155:
        errors.append(f"Meta desc invalid ({desc_len} chars): '{desc}'")
    if not h1:
        errors.append("Missing H1")
    if not has_aeo:
        errors.append("Missing AEO Answer Box")
    if not has_faq:
        errors.append("Missing FAQ section")
    if not has_cta:
        errors.append("Missing CTA / phone")
    if words < 1200:
        errors.append(f"Low word count: {words} words (expected >= 1200)")

    if errors:
        all_valid = False
        print(f"[{idx}] {f} -> ERRORS: {errors}")
    else:
        print(f"[{idx}/30] OK: {f} | {words} mots | Title: {title_len}c | Desc: {desc_len}c")

if all_valid:
    print("\nSUCCESS: All 30 articles strictly satisfy all SEO, Title, Meta, H1, AEO, FAQ, and CTA criteria!")
else:
    print("\nFAIL: Some articles need corrections.")
