import requests
import shutil

# Defined with very specific, likely-to-work URLs
logos = {
    "recursos/logo-diputacion.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Escudo_de_la_Diputaci%C3%B3n_Provincial_de_Salamanca.svg/482px-Escudo_de_la_Diputaci%C3%B3n_Provincial_de_Salamanca.svg.png",
    "recursos/logo-pcbox.jpg": "https://pbs.twimg.com/profile_images/1283675034/Logo_PCBOX_400x400.jpg"
}

# The Twitter PCBox one failed before, let's try a different one if possible, or retry with headers
# Alternative PCBox: https://yt3.googleusercontent.com/ytc/AIdro_nCKKqHhUo8kM7lq5HkCKKqKqKqKqKqKqKqKqKq=s900-c-k-c0x00ffffff-no-rj
logos["recursos/logo-pcbox.jpg"] = "https://yt3.googleusercontent.com/ytc/AIdro_nCKKqHhUo8kM7lq5HkCKKqKqKqKqKqKqKqKqKq=s900-c-k-c0x00ffffff-no-rj"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for path, url in logos.items():
    print(f"Downloading {url} to {path}")
    try:
        r = requests.get(url, headers=headers, stream=True, timeout=10)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print("Success")
        else:
            print(f"Failed with status {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
