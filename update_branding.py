import os
import re

directory = r'c:\Users\meric\Desktop\rehber_site'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    filename = os.path.basename(filepath)

    # 1. Update Title Tag (Global Suffix)
    # Replace " - TechFix</title>" with " - TechFix Center</title>"
    # Prevent double replacement if run multiple times
    if " - TechFix Center</title>" not in content:
        content = content.replace(" - TechFix</title>", " - TechFix Center</title>")

    # 2. Update Footer (Global)
    # Replace "© 2026 TechFix. All rights reserved." -> "© 2026 TechFix Center. All rights reserved."
    content = content.replace("© 2026 TechFix. All rights reserved.", "© 2026 TechFix Center. All rights reserved.")

    # 3. Update Canonical (Global)
    # Replace "https://techfix.com" -> "https://techfixcenter.com"
    content = content.replace("https://techfix.com", "https://techfixcenter.com")

    # 4. Update Meta Description (Global)
    # Append " - TechFix Center" if not present.
    # Regex to find content attribute.
    # Note: simple regex, assuming standard format created by me.
    def meta_replacer(match):
        desc = match.group(1)
        if "TechFix Center" not in desc:
            return f'name="description" content="{desc} - TechFix Center"'
        return match.group(0)
    
    content = re.sub(r'name="description"\s+content="([^"]+)"', meta_replacer, content)


    # 5. SPECIAL: index.html updates
    if filename == 'index.html':
        # Update Title specifically
        # Request: "TechFix Center | Simple Fixes for iPhone, Windows & Tech Problems"
        # It might have been partially updated by the global suffix replacer, so let's force set it.
        content = re.sub(r'<title>.*?</title>', '<title>TechFix Center | Simple Fixes for iPhone, Windows & Tech Problems</title>', content)

        # Update Hero
        # Request: Update hero to include subtitle: "TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems"
        # Current: <h1>Tech Problems Explained. Simple Fixes.</h1>
        # Target: <h1>TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems</h1>
        content = content.replace('<h1>Tech Problems Explained. Simple Fixes.</h1>', '<h1>TechFix Center – Simple Fixes for iPhone, Windows & Tech Problems</h1>')


    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

# Iterate all files
count = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            update_file(os.path.join(root, file))
            count += 1

print(f"Processed {count} files.")
