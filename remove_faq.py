import os
import re

def remove_faq_schema(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match the script block containing FAQPage
    # It looks for <script type="application/ld+json"> ... "@type": "FAQPage" ... </script>
    pattern = re.compile(r'<script type="application/ld\+json">\s*\{[^\}]*"@context":\s*"https://schema\.org",\s*"@type":\s*"FAQPage"[\s\S]*?</script>', re.MULTILINE)
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed FAQ schema from {filepath}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.astro'):
                remove_faq_schema(os.path.join(root, file))

if __name__ == "__main__":
    process_directory('src/pages')
