import requests
import shutil

logos = {
    # Official PDF/Image path on LaSalina website usually involves /presupuestos or similar, but let's try a simpler one found or guess.
    # From search: https://www.lasalina.es/presupuestos2014/img/logodipu.png
    "recursos/logo-diputacion.png": "https://www.lasalina.es/presupuestos2014/img/logodipu.png",
    
    # Leotec URL found in search
    "recursos/logo-pcbox.jpg": "https://www.leotec.com/wp-content/uploads/2019/02/logo-pcbox-2.jpg"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

for path, url in logos.items():
    print(f"Downloading {url} to {path}")
    try:
        r = requests.get(url, headers=headers, stream=True, timeout=20, verify=False)
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print("Success")
        else:
            print(f"Failed with status {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
