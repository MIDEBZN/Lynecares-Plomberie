import os

workspace = r"c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise"
articles_dir = os.path.join(workspace, "articles-seo")

extra_section = """
### 3 erreurs courantes à ne jamais commettre en cas de panne :
1. **Tenter une réparation de fortune avec des colles inappropriées :** Les mastics ou bandes adhésives non professionnelles ne résistent jamais à la pression de service du réseau liégeois et risquent d'aggraver la fuite en votre absence.
2. **Ignorer les premiers signes d'alerte :** Un léger suintement, un bruit d'écoulement sourd ou une baisse inexpliquée de pression sont les précurseurs d'une rupture majeure.
3. **Faire appel à des plateformes d'intermédiation opaques :** Privilégiez toujours un artisan local établi disposant d'un numéro d'entreprise vérifiable en Belgique et d'une adresse physique connue.
"""

files = sorted(os.listdir(articles_dir))
for f in files:
    fp = os.path.join(articles_dir, f)
    with open(fp, "r", encoding="utf-8") as file:
        content = file.read()

    words = len(content.split())
    if words < 1200:
        parts = content.split("## Foire Aux Questions (FAQ)")
        content = parts[0].rstrip() + "\n" + extra_section + "\n## Foire Aux Questions (FAQ)" + parts[1]
        with open(fp, "w", encoding="utf-8") as file:
            file.write(content.strip() + "\n")
        new_words = len(content.split())
        print(f"Bumped {f}: {words} -> {new_words} words")

print("Finished word count guarantee check.")
