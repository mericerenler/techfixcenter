import os
import re

DIRECTORY = r'c:\Users\meric\Desktop\rehber_site'

def update_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Update Title Tag
    if filename == 'index.html':
        # Homepage specific
        new_title = "<title>TechFix Center | Simple Fixes for iPhone, Windows & Tech Problems</title>"
        content = re.sub(r'<title>.*?</title>', new_title, content)
    else:
        # Subpages: " - TechFix" -> " - TechFix Center"
        # Avoid double replacement
        if " - TechFix Center</title>" not in content:
            content = content.replace(" - TechFix</title>", " - TechFix Center</title>")
    
    # 2. Update Meta Description
    # Replace " - TechFix" at the end of description with " - TechFix Center"
    # Regex to capture content inside meta description
    def meta_desc_sub(match):
        desc = match.group(1)
        if "TechFix Center" in desc:
            return match.group(0) # Already good
        if desc.endswith(" - TechFix"):
            new_desc = desc.replace(" - TechFix", " - TechFix Center")
            return f'meta name="description" content="{new_desc}"'
        # If it doesn't end with TechFix but we want to brand it?
        # User said: Update meta descriptions to consistently reference "TechFix Center"
        # Let's assume replacement of brand name is the key.
        return match.group(0).replace("TechFix", "TechFix Center")

    content = re.sub(r'meta name="description" content="(.*?)"', meta_desc_sub, content)

    # 3. Update Footer
    # "© 2026 TechFix. All rights reserved." -> "© 2026 TechFix Center. All rights reserved."
    # Handle both © and &copy;
    # We want the output to be consistent. Let's use &copy; if that's what was there, or just standardize?
    # User asked for "© 2026 TechFix Center. All rights reserved." in the text.
    # Usually in HTML &copy; is safer. Let's look at what the files currently have. 
    # They have &copy;.
    # Let's simple regex for both and replace with the text containing the preferred symbol/entity.
    # Pattern: (&copy;|©) \d{4} TechFix\. All rights reserved\.
    content = re.sub(r'(&copy;|©) \d{4} TechFix\. All rights reserved\.', r'\1 2026 TechFix Center. All rights reserved.', content)
    # Also handle the variant without the year if it exists, or just the exact string user mentioned?
    # User said: Update footer text to: "© 2026 TechFix Center. All rights reserved."
    
    # 4. Update Canonical URLs
    # Base domain switch
    content = content.replace("https://techfix.com", "https://techfixcenter.com")
    
    # 5. Homepage Hero Subtitle
    if filename == 'index.html':
         # Look for the h1 or p in hero
         # Based on view_file: <h1>TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems</h1>
         # It was: <h1>Tech Problems Explained. Simple Fixes.</h1> in original assumption, but previous script might have run.
         # Let's verify the H1.
         # The requirement: Update homepage hero section to include a subtitle: "TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems"
         # Wait, "include a subtitle" implies existing H1 + subtitle? Or replace H1?
         # Looking at the prev update_branding.py logic: it replaced H1.
         # Let's assume the H1 IS the hero text to be updated.
         # Regex for H1
         content = re.sub(r'<h1>.*?</h1>', '<h1>TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems</h1>', content)

    # 6. Update Header Site Title (Global)
    # <div class="site-title"><a href="index.html">TechFix</a></div> -> TechFix Center
    # Be careful not to double replace if it's already TechFix Center
    if 'class="site-title"><a href="index.html">TechFix</a></div>' in content:
        content = content.replace('class="site-title"><a href="index.html">TechFix</a></div>', 'class="site-title"><a href="index.html">TechFix Center</a></div>')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"Skipped (No changes): {filename}")

def main():
    print(f"Scanning directory: {DIRECTORY}")
    for root, dirs, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith('.html'):
                update_file(os.path.join(root, file))
    
    # Sitemap check
    sitemap_path = os.path.join(DIRECTORY, 'sitemap.xml')
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            scontent = f.read()
        
        original_scontent = scontent
        scontent = scontent.replace("https://techfix.com", "https://techfixcenter.com")
        
        # Check if already correct logic
        if scontent != original_scontent:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(scontent)
            print("Updated sitemap.xml")
        else:
            print("sitemap.xml already up to date")

if __name__ == "__main__":
    main()
