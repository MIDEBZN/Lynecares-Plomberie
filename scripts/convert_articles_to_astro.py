import os
import re
import markdown

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
articles_dir = os.path.join(workspace, "articles-seo")
blog_dir = os.path.join(workspace, "src", "pages", "blog")
os.makedirs(blog_dir, exist_ok=True)

files = sorted(os.listdir(articles_dir))
created_slugs = []

for f in files:
    if not f.endswith(".md"):
        continue
    
    slug = f[3:-3] # remove "01-" and ".md"
    fp = os.path.join(articles_dir, f)
    with open(fp, "r", encoding="utf-8") as file:
        raw = file.read()

    # Title
    title_m = re.search(r"\*\*Balise Title SEO.*?:\*\* `(.*?)`", raw)
    title = title_m.group(1) if title_m else ""

    # Desc
    desc_m = re.search(r"\*\*Méta-description.*?:\*\* `(.*?)`", raw)
    desc = desc_m.group(1) if desc_m else ""

    # H1
    h1_m = re.search(r"^# (.*?)$", raw, re.M)
    h1 = h1_m.group(1) if h1_m else ""

    # Clean local file:/// links into canonical web URLs
    raw_cleaned = re.sub(
        r"file:///c:/Users/MEDLO/Desktop/coding%20projects/Lynecares%20Plomberie%20Li%C3%A9geoise/src/pages/(.*?)\.astro",
        r"/\1/",
        raw
    )
    raw_cleaned = raw_cleaned.replace("/src/pages/", "/")

    # Extract body content below the technical header
    # Usually starts after the ASCII box
    content_parts = raw_cleaned.split("└────────────────────────────────────────────────────────────────────────┘\n```\n\n")
    if len(content_parts) > 1:
        body_md = content_parts[1]
    else:
        # fallback
        body_md = raw_cleaned

    # Separate FAQ if present to style it
    faq_html = ""
    if "## Foire Aux Questions (FAQ)" in body_md:
        body_before_faq, faq_md = body_md.split("## Foire Aux Questions (FAQ)", 1)
        # Parse FAQ items
        # Format: ### Question \n Answer
        faq_items = re.findall(r"### (.*?)\n(.*?)(?=\n### |\n---|\n### Besoin|$)", faq_md, re.S)
        if faq_items:
            faq_boxes = []
            for q, a in faq_items:
                clean_q = q.strip()
                clean_a = a.strip()
                faq_boxes.append(f"""        <div class="faq-item glass">
          <h3>{clean_q}</h3>
          <p>{clean_a}</p>
        </div>""")
            faq_html = f"""
    <section class="faq-section container py-5">
      <h2 class="section-title">Foire Aux Questions (FAQ)</h2>
      <div class="faq-grid">
{chr(10).join(faq_boxes)}
      </div>
    </section>"""
            # Keep body_before_faq
            body_md = body_before_faq

    # Convert body_md to HTML
    body_html = markdown.markdown(body_md, extensions=['tables', 'fenced_code', 'nl2br'])

    # Escape any curly braces in Astro JSX
    body_html = body_html.replace("{", "&#123;").replace("}", "&#125;")
    faq_html = faq_html.replace("{", "&#123;").replace("}", "&#125;")
    safe_title = title.replace('"', '\\"')
    safe_desc = desc.replace('"', '\\"')
    safe_h1 = h1.replace('"', '\\"')

    astro_content = f"""---
import Layout from '../../layouts/Layout.astro';
import Navbar from '../../components/Navbar.astro';
import Footer from '../../components/Footer.astro';

const seoTitle = "{safe_title}";
const seoDescription = "{safe_desc}";
---

<Layout title={{seoTitle}} description={{seoDescription}}>
  <Navbar />
  
  <main>
    <section class="page-header">
      <div class="container text-center">
        <h1>{safe_h1}</h1>
        <p>Guide d'intervention & conseils d'experts par Lynecares Plomberie</p>
      </div>
    </section>

    <article class="container py-5 blog-content">
      <div class="content-body">
{body_html}
      </div>
    </article>
{faq_html}
  </main>
  <Footer />
</Layout>

<style>
  .page-header {{ background-color: var(--navy); color: white; padding: 150px 0 80px; text-align: center; }}
  .page-header h1 {{ color: white; font-size: 2.3rem; margin-bottom: 15px; max-width: 900px; margin-inline: auto; line-height: 1.25; }}
  .page-header p {{ color: var(--cyan); font-size: 1.15rem; }}
  .blog-content {{ max-width: 850px; margin: 0 auto; }}
  .content-body h2 {{ color: var(--navy); font-size: 1.75rem; margin-top: 40px; margin-bottom: 18px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
  .content-body h3 {{ color: var(--cyan); font-size: 1.3rem; margin-top: 28px; margin-bottom: 12px; }}
  .content-body p {{ font-size: 1.05rem; line-height: 1.8; color: #475569; margin-bottom: 18px; }}
  .content-body ul, .content-body ol {{ margin-bottom: 20px; padding-left: 24px; }}
  .content-body li {{ font-size: 1.05rem; color: #475569; margin-bottom: 8px; line-height: 1.6; }}
  .content-body table {{ width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 0.95rem; }}
  .content-body th, .content-body td {{ border: 1px solid #cbd5e1; padding: 12px 14px; text-align: left; }}
  .content-body th {{ background-color: var(--navy); color: white; }}
  .content-body tr:nth-child(even) {{ background-color: #f8fafc; }}
  .faq-section {{ max-width: 850px; margin: 0 auto; padding-top: 20px; }}
  .faq-grid {{ display: grid; grid-template-columns: 1fr; gap: 18px; margin-top: 20px; }}
  .faq-item {{ padding: 20px 24px; border-radius: 8px; border-left: 4px solid var(--cyan); background: #f8fafc; }}
  .faq-item h3 {{ font-size: 1.15rem; color: var(--navy); margin-bottom: 8px; }}
  .faq-item p {{ font-size: 1rem; color: #475569; line-height: 1.6; margin: 0; }}
</style>
"""

    astro_target = os.path.join(blog_dir, f"{slug}.astro")
    with open(astro_target, "w", encoding="utf-8") as f_out:
        f_out.write(astro_content)
    
    created_slugs.append((slug, h1))
    print(f"Created Astro page: src/pages/blog/{slug}.astro")

print(f"\nSuccessfully converted all {len(created_slugs)} articles to live Astro routes!")
