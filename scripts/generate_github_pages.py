#!/usr/bin/env python3
"""Generate GitHub Pages HTML files for test reports."""

import os

def create_github_pages_files():
    """Create the necessary HTML files for GitHub Pages deployment."""
    
    # Create directories
    os.makedirs('gh-pages/allure', exist_ok=True)
    os.makedirs('gh-pages/coverage/frontend', exist_ok=True)
    os.makedirs('gh-pages/coverage/backend', exist_ok=True)
    
    # Create .nojekyll
    open('gh-pages/.nojekyll', 'w').close()
    
    # Main index.html
    main_html = """<!DOCTYPE html>
<html lang="ja">
<head><meta charset="UTF-8"><title>Test App - Reports</title>
<style>
body{font-family:sans-serif;max-width:800px;margin:50px auto;line-height:1.6}
h1{color:#333}
.info{background:#f0f0f0;padding:15px;border-radius:5px;margin:20px 0}
a{color:#0066cc;text-decoration:none}
a:hover{text-decoration:underline}
ul{list-style-type:none;padding:0}
li{padding:8px 0}
</style>
</head>
<body>
<h1>📊 Test App - Reports</h1>
<div class="info">
  <p><strong>📍 Location:</strong> This page is deployed to GitHub Pages</p>
  <p><strong>🔄 Updates:</strong> Reports are updated after each e2e test run on the main branch.</p>
</div>
<h2>📋 Available Reports</h2>
<ul>
  <li><a href="allure/index.html">📊 Allure E2E Test Report</a></li>
  <li><a href="coverage/index.html">📈 Coverage Reports</a></li>
</ul>
</body>
</html>"""
    
    with open('gh-pages/index.html', 'w') as f:
        f.write(main_html)
    print("✓ Main index.html created")
    
    # Coverage index.html
    coverage_html = """<!DOCTYPE html>
<html lang="ja">
<head><meta charset="UTF-8"><title>E2E Coverage Reports</title>
<style>
body{font-family:sans-serif;max-width:800px;margin:50px auto;line-height:1.6}
h1{color:#333}
.info{background:#f0f0f0;padding:15px;border-radius:5px;margin:20px 0}
a{color:#0066cc;text-decoration:none}
a:hover{text-decoration:underline}
ul{list-style-type:none;padding:0}
li{padding:8px 0}
</style>
</head>
<body>
<h1>📊 E2E Coverage Reports</h1>
<div class="info">
  <p><strong>📍 Location:</strong> <code>https://cocomomojo.github.io/test_app/coverage/</code></p>
  <p><strong>🔄 Updates:</strong> Reports are updated after each e2e test run on the main branch.</p>
</div>
<h2>Reports</h2>
<ul>
  <li><a href="frontend/index.html">🎨 Frontend Coverage (Playwright + Istanbul)</a></li>
  <li><a href="backend/index.html">☕ Backend Coverage (JaCoCo)</a></li>
</ul>
<p><a href="../">← Back to main page</a></p>
</body>
</html>"""
    
    with open('gh-pages/coverage/index.html', 'w') as f:
        f.write(coverage_html)
    print("✓ Coverage index.html created")

    # Create fallback pages for coverage subdirectories
    fallback_frontend = os.path.join('gh-pages', 'coverage', 'frontend', 'index.html')
    fallback_backend = os.path.join('gh-pages', 'coverage', 'backend', 'index.html')
    if not os.path.exists(fallback_frontend):
        with open(fallback_frontend, 'w') as f:
            f.write('<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><title>Frontend Coverage</title></head><body><h1>No frontend coverage report available</h1></body></html>')
        print("⚠ Fallback frontend coverage placeholder created")
    if not os.path.exists(fallback_backend):
        with open(fallback_backend, 'w') as f:
            f.write('<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><title>Backend Coverage</title></head><body><h1>No backend coverage report available</h1></body></html>')
        print("⚠ Fallback backend coverage placeholder created")

    # Verify
    if os.path.exists('gh-pages/coverage/index.html'):
        size = os.path.getsize('gh-pages/coverage/index.html')
        print(f"✓ VERIFIED: gh-pages/coverage/index.html exists ({size} bytes)")
    else:
        print("✗ ERROR: gh-pages/coverage/index.html was NOT created!")
        exit(1)

if __name__ == '__main__':
    create_github_pages_files()
