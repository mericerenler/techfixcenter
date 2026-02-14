import os
import re

DIRECTORY = r'c:\Users\meric\Desktop\rehber_site\techfixcenter'

NEW_FOOTER = """        <footer>
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Popular iPhone Fixes</h3>
                    <ul>
                        <li><a href="fix-iphone-black-screen-but-still-on.html">Fix iPhone Black Screen</a></li>
                        <li><a href="fix-iphone-not-charging-after-update.html">Fix iPhone Not Charging</a></li>
                        <li><a href="fix-iphone-storage-full-but-empty.html">Fix System Data Full</a></li>
                        <li><a href="fix-iphone-keeps-restarting.html">Fix iPhone Restart Loop</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>TechFix Center</h3>
                    <ul>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms of Service</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="sitemap.xml">Sitemap</a></li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2026 TechFix Center. All rights reserved.</p>
            </div>
        </footer>"""

def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find existing footer
    # Matches <footer>...</footer> including newlines
    footer_pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    
    if footer_pattern.search(content):
        new_content = footer_pattern.sub(NEW_FOOTER, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer in: {os.path.basename(filepath)}")
        else:
            print(f"Footer already up to date in: {os.path.basename(filepath)}")
    else:
        print(f"No footer found in: {os.path.basename(filepath)}")

def main():
    print(f"Scanning directory: {DIRECTORY}")
    for root, dirs, files in os.walk(DIRECTORY):
        for file in files:
            if file.endswith('.html'):
                update_footer(os.path.join(root, file))

if __name__ == "__main__":
    main()
