import requests
import os

logos = {
    "recursos/logo-diputacion.png": "https://seeklogo.com/images/D/diputacion-de-salamanca-logo-8D7C860156-seeklogo.com.png",
    "recursos/logo-pcbox.png": "https://seeklogo.com/images/P/pcbox-logo-B4699C8D46-seeklogo.com.png"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

for path, url in logos.items():
    try:
        print(f"Downloading {url} to {path}...")
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=15)
        
        ct = r.headers.get('Content-Type', '').lower()
        print(f"  Content-Type: {ct}")
        
        if r.status_code == 200 and len(r.content) > 1000:
            with open(path, 'wb') as f:
                f.write(r.content)
            print(f"Success: {path} ({len(r.content)} bytes)")
        else:
            print(f"Failed: {path} (Status: {r.status_code}, Length: {len(r.content)})")
    except Exception as e:
        print(f"Error downloading {path}: {e}")
