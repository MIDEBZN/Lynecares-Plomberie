import subprocess
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_cmd(cmd, out_file):
    with open(out_file, 'w', encoding='utf-8') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

run_cmd(["python", "C:/Users/MEDLO/.gemini/antigravity/skills/seo/scripts/redirect_checker.py", "https://www.plomberieliegeoise.be/"], "redirects_utf8.txt")
