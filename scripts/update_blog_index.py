import os
import re

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
articles_dir = os.path.join(workspace, "articles-seo")
index_astro_path = os.path.join(workspace, "src", "pages", "blog", "index.astro")

with open(index_astro_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract existing URLs
existing_urls = set(re.findall(r'url:\s*"(.*?)"', content))

# Load all 30 articles
files = sorted(os.listdir(articles_dir))
new_entries = []

for f in files:
    if not f.endswith(".md"):
        continue
    slug = f[3:-3]
    url = f"/blog/{slug}/"
    if url in existing_urls:
        continue
    
    fp = os.path.join(articles_dir, f)
    with open(fp, "r", encoding="utf-8") as file:
        raw = file.read()
    
    h1_m = re.search(r"^# (.*?)$", raw, re.M)
    title = h1_m.group(1) if h1_m else slug.replace("-", " ").capitalize()
    
    desc_m = re.search(r"\*\*Méta-description.*?:\*\* `(.*?)`", raw)
    excerpt = desc_m.group(1) if desc_m else "Guide et conseils professionnels de plomberie d'urgence à Liège."
    
    safe_title = title.replace('"', '\\"')
    safe_excerpt = excerpt.replace('"', '\\"')
    
    entry = f"""  {{
    title: "{safe_title}",
    url: "{url}",
    excerpt: "{safe_excerpt}",
    category: "Urgence"
  }},"""
    new_entries.append(entry)

if new_entries:
    # Insert new entries right after `const articles = [`
    insert_pos = content.find("const articles = [") + len("const articles = [")
    new_content = content[:insert_pos] + "\n" + "\n".join(new_entries) + content[insert_pos:]
    with open(index_astro_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Added {len(new_entries)} new articles to blog/index.astro")
else:
    print("All articles are already present in blog/index.astro")
