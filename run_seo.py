import subprocess
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_cmd(cmd, out_file):
    with open(out_file, 'w', encoding='utf-8') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/parse_html.py", "page.html", "--url", "https://www.plomberieliegeoise.be", "--json"], "parse_html_utf8.json")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/readability.py", "page.html", "--json"], "readability_utf8.json")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/pagespeed.py", "https://www.plomberieliegeoise.be", "--strategy", "mobile", "--json"], "pagespeed_utf8.json")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/robots_checker.py", "https://www.plomberieliegeoise.be"], "robots_checker_utf8.txt")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/llms_txt_checker.py", "https://www.plomberieliegeoise.be"], "llms_txt_checker_utf8.txt")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/security_headers.py", "https://www.plomberieliegeoise.be"], "security_headers_utf8.txt")
run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/social_meta.py", "https://www.plomberieliegeoise.be"], "social_meta_utf8.txt")
