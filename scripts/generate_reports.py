import os
import csv
import json
import re
from bs4 import BeautifulSoup

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
dist_dir = os.path.join(workspace, "dist")
reports_dir = os.path.join(workspace, "reports")
os.makedirs(reports_dir, exist_ok=True)

# 1. Parse all HTML files in dist
html_files = []
for root, dirs, files in os.walk(dist_dir):
    for f in files:
        if f == "index.html" or (f.endswith(".html") and not f.startswith("404")):
            html_files.append(os.path.join(root, f))

# Also read sitemap if exists
sitemap_urls = set()
sitemap_path = os.path.join(dist_dir, "sitemap-0.xml")
if not os.path.exists(sitemap_path):
    sitemap_path = os.path.join(dist_dir, "sitemap-index.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as f:
        soup_sitemap = BeautifulSoup(f.read(), "html.parser")
        for loc in soup_sitemap.find_all("loc"):
            sitemap_urls.add(loc.text.strip())

# Count inlinks
inlink_counts = {}
page_data = {}

for filepath in html_files:
    rel_path = os.path.relpath(filepath, dist_dir).replace("\\", "/")
    if rel_path == "index.html":
        url_path = "/"
    elif rel_path.endswith("/index.html"):
        url_path = "/" + rel_path[:-10]  # e.g. /about/
    else:
        url_path = "/" + rel_path

    full_url = f"https://www.plomberieliegeoise.be{url_path}"

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # Links out
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#")[0].split("?")[0]
        if href.startswith("/"):
            target_url = f"https://www.plomberieliegeoise.be{href}"
            inlink_counts[target_url] = inlink_counts.get(target_url, 0) + 1
            if not target_url.endswith("/"):
                inlink_counts[target_url + "/"] = inlink_counts.get(target_url + "/", 0) + 1

    # Extract metadata
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else ""

    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"].strip() if meta_desc and "content" in meta_desc.attrs else ""

    canonical_tag = soup.find("link", attrs={"rel": "canonical"})
    canonical = canonical_tag["href"].strip() if canonical_tag and "href" in canonical_tag.attrs else ""

    robots_meta = soup.find("meta", attrs={"name": "robots"})
    robots = robots_meta["content"].strip() if robots_meta and "content" in robots_meta.attrs else "index, follow"

    h1_tags = soup.find_all("h1")
    h1_count = len(h1_tags)
    h1_text = " | ".join([h.get_text(strip=True) for h in h1_tags])

    # Word count
    body = soup.find("body")
    text = body.get_text(separator=" ", strip=True) if body else ""
    words = len(text.split())

    # Structured data
    ld_json_scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
    schemas = []
    for s in ld_json_scripts:
        try:
            data = json.loads(s.string)
            if isinstance(data, dict) and "@type" in data:
                schemas.append(data["@type"])
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "@type" in item:
                        schemas.append(item["@type"])
        except Exception:
            pass
    schema_types = ", ".join(schemas) if schemas else "None"

    is_in_sitemap = full_url in sitemap_urls or full_url.rstrip("/") in sitemap_urls or (full_url + "/") in sitemap_urls
    indexability = "Indexable" if "noindex" not in robots.lower() else "Non-Indexable"

    page_data[full_url] = {
        "url": full_url,
        "status": 200,
        "final_url": full_url,
        "canonical": canonical,
        "robots": robots,
        "title": title,
        "description": description,
        "h1_count": h1_count,
        "h1_text": h1_text,
        "word_count": words,
        "indexability": indexability,
        "sitemap_inclusion": "Yes" if is_in_sitemap else "No",
        "structured_data": schema_types
    }

# Write url-inventory.csv
inv_path = os.path.join(reports_dir, "url-inventory.csv")
with open(inv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "URL", "HTTP status", "final URL after redirects", "canonical URL", 
        "robots meta", "title", "meta description", "H1 count", "H1 text", 
        "word count", "indexability", "sitemap inclusion", "internal inlink count", "structured-data types"
    ])
    for url, data in sorted(page_data.items()):
        inlinks = inlink_counts.get(url, 0)
        writer.writerow([
            data["url"], data["status"], data["final_url"], data["canonical"],
            data["robots"], data["title"], data["description"], data["h1_count"],
            data["h1_text"], data["word_count"], data["indexability"],
            data["sitemap_inclusion"], inlinks, data["structured_data"]
        ])

print(f"Generated url-inventory.csv with {len(page_data)} URLs.")

# 2. Generate reports/query-page-verification.csv based on the GSC audit specification
query_verification_data = [
    # Core Plumber Liège
    {"query": "plombier liege", "impressions": 1776, "clicks": 7, "ctr": "0.39%", "position": 8.81, "target_url": "/", "intent": "Core citywide plumber service", "status": "Retained on Homepage (Primary)"},
    {"query": "plombier liège", "impressions": 1356, "clicks": 1, "ctr": "0.07%", "position": 11.17, "target_url": "/", "intent": "Core citywide plumber service (accented)", "status": "Retained on Homepage (Primary)"},
    {"query": "plombier à liège", "impressions": 120, "clicks": 0, "ctr": "0.00%", "position": 9.50, "target_url": "/", "intent": "Core citywide plumber service", "status": "Retained on Homepage (Primary)"},
    {"query": "plombiers liège", "impressions": 85, "clicks": 0, "ctr": "0.00%", "position": 10.10, "target_url": "/", "intent": "Plumber directory/plural query", "status": "Retained on Homepage (Primary)"},
    {"query": "plomberie liège", "impressions": 75, "clicks": 0, "ctr": "0.00%", "position": 11.20, "target_url": "/", "intent": "Company / commercial plomberie query", "status": "Retained on Homepage (Primary)"},
    # Urgency
    {"query": "plombier urgence liège", "impressions": 225, "clicks": 1, "ctr": "0.44%", "position": 3.92, "target_url": "/services/urgences-plomberie/", "intent": "Immediate emergency intervention", "status": "Dedicated Landing Page"},
    {"query": "plombier 24h liège", "impressions": 213, "clicks": 0, "ctr": "0.00%", "position": 3.95, "target_url": "/services/urgences-plomberie/", "intent": "24/7 night/weekend availability", "status": "Dedicated Landing Page"},
    {"query": "plombier liege urgence", "impressions": 128, "clicks": 0, "ctr": "0.00%", "position": 4.63, "target_url": "/services/urgences-plomberie/", "intent": "Urgent breakdown repair", "status": "Dedicated Landing Page"},
    {"query": "urgence plomberie liège", "impressions": 71, "clicks": 0, "ctr": "0.00%", "position": 8.65, "target_url": "/services/urgences-plomberie/", "intent": "Urgent water leak / pipe break", "status": "Dedicated Landing Page"},
    # Heating & Boiler
    {"query": "chauffagiste urgence liege", "impressions": 194, "clicks": 0, "ctr": "0.00%", "position": 8.39, "target_url": "/services/chauffagiste-liege/", "intent": "Heating breakdown emergency", "status": "New Dedicated Commercial Page"},
    {"query": "dépannage chaudière liège", "impressions": 117, "clicks": 0, "ctr": "0.00%", "position": 13.32, "target_url": "/services/chauffagiste-liege/", "intent": "Boiler repair", "status": "New Dedicated Commercial Page"},
    {"query": "installation chauffage liège", "impressions": 84, "clicks": 0, "ctr": "0.00%", "position": 17.82, "target_url": "/services/chauffagiste-liege/", "intent": "Heating system installation", "status": "New Dedicated Commercial Page"},
    {"query": "chauffagiste liège", "impressions": 74, "clicks": 1, "ctr": "1.35%", "position": 8.58, "target_url": "/services/chauffagiste-liege/", "intent": "Heating engineer search", "status": "New Dedicated Commercial Page"},
    {"query": "dépannage chauffage", "impressions": 72, "clicks": 0, "ctr": "0.00%", "position": 12.03, "target_url": "/services/chauffagiste-liege/", "intent": "Heating repair service", "status": "New Dedicated Commercial Page"},
    {"query": "entretien chaudiere liege", "impressions": 110, "clicks": 0, "ctr": "0.00%", "position": 14.50, "target_url": "/services/entretien-plomberie-chauffage/", "intent": "Annual preventive boiler maintenance", "status": "Dedicated Maintenance Page"},
    # Bathroom Renovation
    {"query": "installateur salle de bain", "impressions": 128, "clicks": 0, "ctr": "0.00%", "position": 6.20, "target_url": "/services/renovation-salle-de-bain-liege/", "intent": "Bathroom installer contractor", "status": "New Dedicated Commercial Page"},
    {"query": "installateur salle de bain liège", "impressions": 108, "clicks": 0, "ctr": "0.00%", "position": 8.48, "target_url": "/services/renovation-salle-de-bain-liege/", "intent": "Local bathroom installer", "status": "New Dedicated Commercial Page"},
    {"query": "entrepreneur salle de bain liege", "impressions": 14, "clicks": 0, "ctr": "0.00%", "position": 6.14, "target_url": "/services/renovation-salle-de-bain-liege/", "intent": "Bathroom remodeling contractor", "status": "New Dedicated Commercial Page"},
    {"query": "rénovation salle de bain liège", "impressions": 14, "clicks": 0, "ctr": "0.00%", "position": 15.36, "target_url": "/services/renovation-salle-de-bain-liege/", "intent": "Complete bathroom renovation", "status": "New Dedicated Commercial Page"},
    {"query": "prix rénovation salle de bain liège", "impressions": 8, "clicks": 0, "ctr": "0.00%", "position": 20.50, "target_url": "/services/renovation-salle-de-bain-liege/", "intent": "Bathroom renovation cost / quote", "status": "New Dedicated Commercial Page"},
    # Sanitary Installations
    {"query": "installation sanitaire liege", "impressions": 45, "clicks": 0, "ctr": "0.00%", "position": 12.30, "target_url": "/services/installations-sanitaires/", "intent": "Sanitary fixtures, WC, faucets", "status": "Dedicated Fixtures Page"},
    # Air conditioning (BLOCKED)
    {"query": "installation climatisation liege", "impressions": 150, "clicks": 0, "ctr": "0.00%", "position": 22.10, "target_url": "BLOCKED (No Service)", "intent": "AC installation", "status": "Blocked - Unverified Capacity"},
    {"query": "climatisation liege", "impressions": 129, "clicks": 0, "ctr": "0.00%", "position": 25.40, "target_url": "BLOCKED (No Service)", "intent": "AC service", "status": "Blocked - Unverified Capacity"},
    # Drain Clearing
    {"query": "debouchage liege", "impressions": 37, "clicks": 0, "ctr": "0.00%", "position": 64.54, "target_url": "/services/debouchage/", "intent": "Drain unblocking", "status": "Optimized Service Page"},
    {"query": "debouchage canalisation liege", "impressions": 42, "clicks": 0, "ctr": "0.00%", "position": 58.20, "target_url": "/services/debouchage/", "intent": "Pipe unblocking / hydrocurage", "status": "Optimized Service Page"},
    {"query": "debouchage wc liege", "impressions": 25, "clicks": 0, "ctr": "0.00%", "position": 45.10, "target_url": "/services/debouchage/", "intent": "Clogged toilet emergency", "status": "Optimized Service Page"},
    # Price Article
    {"query": "tarif plombier liege", "impressions": 116, "clicks": 3, "ctr": "2.59%", "position": 11.63, "target_url": "/blog/tarif-prix-plombier-liege-depannage/", "intent": "Plumber cost breakdown & hourly rates", "status": "Optimized Blog Article"},
    # Municipalities
    {"query": "plombier blegny", "impressions": 74, "clicks": 1, "ctr": "1.35%", "position": 1.46, "target_url": "/blog/plombier-de-garde-liege-urgence-30-minutes/", "intent": "Local plumber Blegny", "status": "Retained Stable (No disruption)"},
    {"query": "plombier beyne-heusay", "impressions": 48, "clicks": 0, "ctr": "0.00%", "position": 1.92, "target_url": "/locations/plombier-beyne-heusay/", "intent": "Local plumber Beyne-Heusay (4610)", "status": "New Dedicated Commune Page"},
    {"query": "plombier oupeye", "impressions": 47, "clicks": 0, "ctr": "0.00%", "position": 4.68, "target_url": "/locations/plombier-oupeye/", "intent": "Local plumber Oupeye (4680)", "status": "Existing Commune Page (Enriched)"},
    {"query": "plombier grivegnée", "impressions": 42, "clicks": 0, "ctr": "0.00%", "position": 3.29, "target_url": "/locations/plombier-grivegnee/", "intent": "Local plumber Grivegnée (4030)", "status": "New Dedicated Commune Page"},
    {"query": "plombier aywaille", "impressions": 36, "clicks": 0, "ctr": "0.00%", "position": 9.08, "target_url": "/locations/plombier-aywaille/", "intent": "Local plumber Aywaille (4920)", "status": "New Dedicated Commune Page"},
    {"query": "plombier neupré", "impressions": 34, "clicks": 0, "ctr": "0.00%", "position": 20.18, "target_url": "/locations/plombier-neupre/", "intent": "Local plumber Neupré (4120)", "status": "Existing Commune Page (Enriched)"},
    {"query": "plombier trooz", "impressions": 28, "clicks": 0, "ctr": "0.00%", "position": 3.57, "target_url": "/locations/plombier-trooz/", "intent": "Local plumber Trooz (4870)", "status": "New Dedicated Commune Page"},
    {"query": "plombier soumagne", "impressions": 22, "clicks": 0, "ctr": "0.00%", "position": 3.45, "target_url": "/locations/plombier-soumagne/", "intent": "Local plumber Soumagne (4630)", "status": "Existing Commune Page (Enriched)"},
    {"query": "plombier juprelle", "impressions": 17, "clicks": 0, "ctr": "0.00%", "position": 2.41, "target_url": "/locations/plombier-juprelle/", "intent": "Local plumber Juprelle (4450)", "status": "New Dedicated Commune Page"},
    {"query": "plombier ans", "impressions": 15, "clicks": 0, "ctr": "0.00%", "position": 80.00, "target_url": "/locations/plombier-ans/", "intent": "Local plumber Ans (4430)", "status": "Existing Commune Page (Enriched)"},
    {"query": "plombier esneux", "impressions": 14, "clicks": 0, "ctr": "0.00%", "position": 7.07, "target_url": "/locations/plombier-esneux/", "intent": "Local plumber Esneux (4130)", "status": "Existing Commune Page (Enriched)"}
]

qp_path = os.path.join(reports_dir, "query-page-verification.csv")
with open(qp_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Query", "Impressions (GSC)", "Clicks (GSC)", "CTR (GSC)", "Avg Position (GSC)", "Target URL", "Search Intent", "Status & Action"])
    for row in query_verification_data:
        writer.writerow([row["query"], row["impressions"], row["clicks"], row["ctr"], row["position"], row["target_url"], row["intent"], row["status"]])

print(f"Generated query-page-verification.csv with {len(query_verification_data)} queries.")

# 3. Baseline for metadata-before-after.csv
mba_path = os.path.join(reports_dir, "metadata-before-after.csv")
metadata_rows = [
    {
        "url": "/",
        "before_title": "Plombier Urgence Liège | Lynecares | Lynecares Plomberie",
        "after_title": "Plombier Liège 24h/24 | Dépannage rapide | Lynecares",
        "before_desc": "Besoin d'un plombier en urgence à Liège ? Intervention en 30 minutes, 24h/24 et 7j/7. Dépannage fuite d'eau, débouchage et chaudière. Devis gratuit.",
        "after_desc": "Besoin d’un plombier à Liège ? Dépannage, fuite, débouchage, sanitaire et chauffage. Appelez Lynecares au 0466 26 58 95.",
        "before_h1": "Plombier de Confiance à Liège",
        "after_h1": "Plombier à Liège 24h/24 et 7j/7"
    },
    {
        "url": "/services/urgences-plomberie/",
        "before_title": "Urgences Plomberie 24/7 à Liège | Lynecares | Lynecares Plomberie",
        "after_title": "Plombier urgence Liège 24h/24 | Lynecares",
        "before_desc": "Intervention d'urgence 24h/24 et 7j/7 à Liège pour tout problème de plomberie : débouchage, fuite d'eau, dégât des eaux, rupture de canalisation.",
        "after_desc": "Urgence plomberie à Liège : fuite, canalisation, WC ou chauffe-eau. Appelez Lynecares au 0466 26 58 95 pour vérifier la disponibilité.",
        "before_h1": "Urgences Plomberie à Liège",
        "after_h1": "Plombier urgence à Liège, 24h/24 et 7j/7"
    },
    {
        "url": "/services/renovation-salle-de-bain-liege/",
        "before_title": "N/A (Page non existante)",
        "after_title": "Rénovation salle de bain Liège | Devis | Lynecares",
        "before_desc": "N/A (Page non existante)",
        "after_desc": "Projet de salle de bain à Liège ? Installation sanitaire, douche, WC, robinetterie et raccordements. Demandez un devis à Lynecares.",
        "before_h1": "N/A (Page non existante)",
        "after_h1": "Rénovation de salle de bain à Liège"
    },
    {
        "url": "/services/installations-sanitaires/",
        "before_title": "Installation Sanitaire Liège | Plomberie Maison Neuve | Lynecares | Lynecares Plomberie",
        "after_title": "Installation sanitaire Liège | WC, douche et boiler | Lynecares",
        "before_desc": "Installation sanitaire Liège. Pose de wc suspendu, remplacement robinet, installation plomberie pour maison neuve. Artisan plombier professionnel.",
        "after_desc": "Installation sanitaire à Liège : pose de WC suspendu, remplacement de mitigeur, raccordement de boiler et tuyauterie. Devis rapide avec Lynecares.",
        "before_h1": "Installation Sanitaire Liège",
        "after_h1": "Installation sanitaire à Liège"
    },
    {
        "url": "/services/chauffagiste-liege/",
        "before_title": "N/A (Page non existante)",
        "after_title": "Chauffagiste Liège | Dépannage chaudière | Lynecares",
        "before_desc": "N/A (Page non existante)",
        "after_desc": "Besoin d’un chauffagiste à Liège ? Dépannage de chaudière, chauffage et chauffe-eau. Contactez Lynecares pour vérifier la disponibilité.",
        "before_h1": "N/A (Page non existante)",
        "after_h1": "Chauffagiste à Liège pour dépannage et installation"
    },
    {
        "url": "/services/entretien-plomberie-chauffage/",
        "before_title": "Plombier Chauffagiste Liège | Entretien Chaudière | Lynecares | Lynecares Plomberie",
        "after_title": "Entretien Chauffage & Boiler Liège | Prévention | Lynecares",
        "before_desc": "Plombier chauffagiste Liège. Entretien chaudière, dépannage chauffage, réparation chaudière en panne et détartrage chauffe-eau. Chauffagiste agréé.",
        "after_desc": "Entretien préventif de chauffe-eau, détartrage de boiler et désembouage de radiateurs à Liège. Prolongez la durée de vie de vos équipements.",
        "before_h1": "Plombier Chauffagiste Liège",
        "after_h1": "Entretien de chauffage et plomberie à Liège"
    },
    {
        "url": "/services/debouchage/",
        "before_title": "Débouchage Liège | Canalisation, Évier, WC | Lynecares | Lynecares Plomberie",
        "after_title": "Débouchage Liège | Canalisation, WC et évier | Lynecares",
        "before_desc": "Service professionnel de débouchage à Liège. Égout, WC, évier, baignoire. Hydrocurage haute pression et inspection caméra.",
        "after_desc": "Débouchage canalisation à Liège : WC, évier, douche et égout. Intervention d'urgence avec furet et hydrocureuse haute pression. Devis clair.",
        "before_h1": "Débouchage à Liège",
        "after_h1": "Débouchage de canalisation à Liège"
    },
    {
        "url": "/blog/tarif-prix-plombier-liege-depannage/",
        "before_title": "Tarif Plombier Liège 2026 : Combien coûte un dépannage ? | Lynecares Plomberie",
        "after_title": "Prix plombier Liège 2026 : tarifs et exemples | Lynecares",
        "before_desc": "Découvrez le vrai tarif d'un plombier à Liège en 2026. Frais de déplacement, taux horaire, suppléments soir et week-end. Évitez les arnaques et payez le juste prix.",
        "after_desc": "Tarifs d'un plombier à Liège en 2026 : taux horaire, déplacement, suppléments soirs et week-ends. Guide complet des prix avec exemples réels.",
        "before_h1": "Tarif Plombier Liège 2026 : Combien coûte réellement un dépannage ?",
        "after_h1": "Prix d’un plombier à Liège en 2026"
    },
    {
        "url": "/contact/",
        "before_title": "Contact | Lynecares Plomberie Liégeoise | Lynecares Plomberie",
        "after_title": "Contact plombier Liège 24/7 | Lynecares",
        "before_desc": "Plombier urgence à Liège — intervention garantie en 30 min, 24h/24 et 7j/7...",
        "after_desc": "Contactez Lynecares pour tout dépannage de plomberie ou devis à Liège et province. Téléphone 0466 26 58 95 disponible 24/7, devis gratuit.",
        "before_h1": "Contactez-Nous",
        "after_h1": "Contactez votre plombier à Liège"
    },
    {
        "url": "/locations/plombier-liege/",
        "before_title": "Plombier Liège | Dépannage & Urgence | Lynecares | Lynecares Plomberie",
        "after_title": "Plombier Liège 4000 | Centre-Ville & Quartiers | Lynecares",
        "before_desc": "Plombier Liège. Intervention rapide pour urgence plomberie, fuite d'eau...",
        "after_desc": "Dépannage plomberie à Liège hyper-centre (4000) : Outremeuse, Guillemins, Saint-Léonard, Laveu. Plombier de proximité rapide et devis gratuit.",
        "before_h1": "Plombier Liège : Dépannage & Urgence",
        "after_h1": "Plombier à Liège Centre (4000) et ses quartiers"
    },
    {
        "url": "/locations/plombier-beyne-heusay/",
        "before_title": "N/A (Nouvelle commune)",
        "after_title": "Plombier Beyne-Heusay (4610) | Dépannage 7j/7 | Lynecares",
        "before_desc": "N/A (Nouvelle commune)",
        "after_desc": "Plombier à Beyne-Heusay et Queue-du-Bois (4610). Dépannage d'urgence fuite d'eau, débouchage et chauffe-eau. Intervention rapide et devis gratuit.",
        "before_h1": "N/A (Nouvelle commune)",
        "after_h1": "Plombier à Beyne-Heusay (4610)"
    },
    {
        "url": "/locations/plombier-grivegnee/",
        "before_title": "N/A (Nouvelle commune)",
        "after_title": "Plombier Grivegnée (4030) | Dépannage Rapide | Lynecares",
        "before_desc": "N/A (Nouvelle commune)",
        "after_desc": "Plombier à Grivegnée (4030) pour urgence fuite, débouchage de canalisation et chauffe-eau. Proximité immédiate depuis Bois-de-Breux.",
        "before_h1": "N/A (Nouvelle commune)",
        "after_h1": "Plombier à Grivegnée (4030)"
    },
    {
        "url": "/locations/plombier-aywaille/",
        "before_title": "N/A (Nouvelle commune)",
        "after_title": "Plombier Aywaille (4920) | Dépannage & Chauffage | Lynecares",
        "before_desc": "N/A (Nouvelle commune)",
        "after_desc": "Service de plomberie et chauffage à Aywaille (4920), Remouchamps et Vallée de l'Amblève. Dépannage fuite, boiler et canalisation.",
        "before_h1": "N/A (Nouvelle commune)",
        "after_h1": "Plombier à Aywaille (4920)"
    },
    {
        "url": "/locations/plombier-trooz/",
        "before_title": "N/A (Nouvelle commune)",
        "after_title": "Plombier Trooz (4870) | Urgence & Sanitaire | Lynecares",
        "before_desc": "N/A (Nouvelle commune)",
        "after_desc": "Plombier à Trooz (4870) et Fraipont. Spécialiste dépannage fuite, remise en état sanitaire et débouchage. Devis clair et transparent.",
        "before_h1": "N/A (Nouvelle commune)",
        "after_h1": "Plombier à Trooz (4870)"
    },
    {
        "url": "/locations/plombier-juprelle/",
        "before_title": "N/A (Nouvelle commune)",
        "after_title": "Plombier Juprelle (4450) | Dépannage Plomberie | Lynecares",
        "before_desc": "N/A (Nouvelle commune)",
        "after_desc": "Artisan plombier à Juprelle, Lantin et Slins (4450). Débouchage, réparation de tuyauterie, remplacement de robinetterie et chauffe-eau.",
        "before_h1": "N/A (Nouvelle commune)",
        "after_h1": "Plombier à Juprelle (4450)"
    }
]

with open(mba_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "Before Title", "After Title", "Before Meta Description", "After Meta Description", "Before H1", "After H1"])
    for row in metadata_rows:
        writer.writerow([row["url"], row["before_title"], row["after_title"], row["before_desc"], row["after_desc"], row["before_h1"], row["after_h1"]])

print(f"Generated metadata-before-after.csv with {len(metadata_rows)} entries.")

# 4. Generate reports/redirect-map.csv
red_path = os.path.join(reports_dir, "redirect-map.csv")
redirects_data = [
    {"source": "/blog/plombier-zingueur-liege-reparation-corniches", "destination": "/services/fuites-reparations/", "status_code": 301, "reason": "Legacy blog post consolidated into Fuites & Réparations service page"},
    {"source": "/blog/plombier-zingueur-liege-reparation-corniches/", "destination": "/services/fuites-reparations/", "status_code": 301, "reason": "Trailing slash version of legacy blog post consolidated"},
    {"source": "/services/climatisation-liege", "destination": "/services/", "status_code": 301, "reason": "Safety fallback if crawled: unverified service routed to services index"},
    {"source": "/services/climatisation-liege/", "destination": "/services/", "status_code": 301, "reason": "Trailing slash safety fallback"},
    {"source": "https://plomberieliegeoise.be/(.*)", "destination": "https://www.plomberieliegeoise.be/$1", "status_code": 301, "reason": "Non-www to www canonical redirect"}
]

with open(red_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Source URL / Pattern", "Destination URL", "HTTP Status Code", "Business / SEO Rationale"])
    for row in redirects_data:
        writer.writerow([row["source"], row["destination"], row["status_code"], row["reason"]])

print(f"Generated redirect-map.csv with {len(redirects_data)} rules.")
