import os
import re
import glob

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
locations_dir = os.path.join(workspace, "src", "pages", "locations")
services_dir = os.path.join(workspace, "src", "pages", "services")

# 1. OPTIMIZE LOCATION PAGES
for filepath in glob.glob(os.path.join(locations_dir, "plombier-*.astro")):
    filename = os.path.basename(filepath)
    town = filename.replace("plombier-", "").replace(".astro", "").capitalize()
    
    # Handle compound names like grace-hollogne -> Grâce-Hollogne
    if town.lower() == "grace-hollogne":
        town = "Grâce-Hollogne"
    elif town.lower() == "liege":
        town = "Liège"
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Title and Description
    new_layout = f'<Layout title="Plombier {town} | Dépannage & Urgence | Lynecares" description="Plombier {town}. Intervention rapide pour urgence plomberie, fuite d\'eau, débouchage canalisation et dépannage chaudière à {town}. Devis gratuit.">'
    content = re.sub(r'<Layout title="[^"]*" description="[^"]*">', new_layout, content)
    
    # Replace H1
    new_h1 = f'<h1>Plombier {town} : Dépannage & Urgence</h1>'
    content = re.sub(r'<h1>.*?</h1>', new_h1, content, count=1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Optimized location: {town}")

# 2. OPTIMIZE SERVICE PAGES
services_seo = {
    "detection-fuite-diagnostic.astro": {
        "title": "Recherche de Fuite Liège | Détection non destructive | Lynecares",
        "desc": "Recherche de fuite Liège. Détection de fuite d'eau non destructive, gaz traceur, caméra thermique. Rapport pour assurance. Urgence fuite d'eau Liège.",
        "h1": "Recherche de Fuite Liège"
    },
    "fuites-reparations.astro": {
        "title": "Réparation Fuite d'Eau Liège | Urgence Plombier | Lynecares",
        "desc": "Réparation fuite d'eau Liège. Dépannage urgent pour tuyau percé, infiltration d'eau, fuite de gaz ou réparation plomberie. Devis gratuit.",
        "h1": "Réparation Fuite d'Eau Liège"
    },
    "entretien-plomberie-chauffage.astro": {
        "title": "Plombier Chauffagiste Liège | Entretien Chaudière | Lynecares",
        "desc": "Plombier chauffagiste Liège. Entretien chaudière, dépannage chauffage, réparation chaudière en panne et détartrage chauffe-eau. Chauffagiste agréé.",
        "h1": "Plombier Chauffagiste Liège"
    },
    "installations-sanitaires.astro": {
        "title": "Installation Sanitaire Liège | Plomberie Maison Neuve | Lynecares",
        "desc": "Installation sanitaire Liège. Pose de wc suspendu, remplacement robinet, installation plomberie pour maison neuve. Artisan plombier professionnel.",
        "h1": "Installation Sanitaire Liège"
    },
    "renovation-salle-de-bain-pmr.astro": {
        "title": "Rénovation Salle de Bain Liège | Installation Douche | Lynecares",
        "desc": "Rénovation salle de bain Liège. Devis gratuit pour création ou remplacement baignoire par douche. Installation PMR et sanitaire design.",
        "h1": "Rénovation Salle de Bain Liège"
    },
    "desembouage-radiateur-liege.astro": {
        "title": "Désembouage Radiateur Liège | Entretien Chauffage | Lynecares",
        "desc": "Désembouage radiateur Liège. Nettoyage de circuit de chauffage, radiateur qui fuit, amélioration du rendement de votre chaudière.",
        "h1": "Désembouage Radiateur Liège"
    }
}

for filename, seo in services_seo.items():
    filepath = os.path.join(services_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_layout = f'<Layout title="{seo["title"]}" description="{seo["desc"]}">'
    # Fallback to replace only title if description is missing in original
    content = re.sub(r'<Layout title="[^"]*"(?: description="[^"]*")?>', new_layout, content)
    
    new_h1 = f'<h1>{seo["h1"]}</h1>'
    content = re.sub(r'<h1>.*?</h1>', new_h1, content, count=1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Optimized service: {filename}")

print("SEO Optimization Complete!")
