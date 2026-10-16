import os
import re
import glob

locations_dir = r'c:\Users\MEDLO\Desktop\coding projects\Lynecares Plomberie Liégeoise\src\pages\locations'

count = 0
for filepath in glob.glob(os.path.join(locations_dir, '*.astro')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract city name from H1 or filename
    city_match = re.search(r'<h1>Plombier ([^:]+) :', content)
    if not city_match:
        print(f"Skipping {filepath}: No city match found in H1")
        continue
    city = city_match.group(1).strip()
    
    # 1. Update Title
    content = content.replace(
        f'<Layout title="Plombier {city} | Dépannage & Urgence | Lynecares"',
        f'<Layout title="Plombier {city} | Artisan Plombier Urgence & Débouchage"'
    )
    
    # 2. Update intro paragraph
    old_intro = f'<p>Que vous habitiez au cœur de <strong>{city}</strong> ou dans les quartiers environnants, Lynecares Plomberie est votre partenaire de proximité pour toute urgence sanitaire ou projet d\'installation.</p>'
    new_intro = f'<p>Que vous habitiez au cœur de <strong>{city}</strong> ou dans les quartiers environnants, Lynecares Plomberie est votre <strong>artisan plombier {city}</strong> de proximité pour tout besoin de <strong>plombier urgence {city}</strong>, d\'intervention de <strong>chauffagiste {city}</strong> ou d\'installation sanitaire.</p>'
    content = content.replace(old_intro, new_intro)
    
    # 3. Update service headers
    content = content.replace('<h3>🚨 Dépannage Urgence</h3>', f'<h3>🚨 Plombier Urgence {city}</h3>')
    content = content.replace('<h3>🌪️ Débouchage</h3>', f'<h3>🌪️ Débouchage {city}</h3>')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count += 1

print(f"Optimized {count} local pages successfully!")
