import requests
import shutil
import os

candidates_dip = [
    "https://www.salamancahoy.es/wcs/img/logo_diputacion.png", # Guess
    "https://www.psoe-salamanca.es/wp-content/uploads/2019/07/Logotipo-Diputacion-Salamanca.jpg",
    "https://i0.wp.com/salamancartvaldia.es/wp-content/uploads/2019/09/dipufrisona.jpg?fit=696%2C391&ssl=1" # Maybe
]

candidates_pcbox = [
    "https://yt3.googleusercontent.com/ytc/AIdro_nCKKqHhUo8kM7lq5HkCKKqKqKqKqKqKqKqKqKq=s900-c-k-c0x00ffffff-no-rj", # YouTube Avatar (often full logo)
    "https://www.muycomputerpro.com/wp-content/uploads/2015/05/PCBoX.jpg",
    "https://hardzone.es/app/uploads/2019/02/PCBox-Logo.jpg"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def try_download(candidates, dest):
    for url in candidates:
        try:
            print(f"Trying {url}...")
            r = requests.get(url, headers=headers, stream=True, timeout=10, verify=False)
            if r.status_code == 200:
                with open(dest, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                print(f"Success: {dest}")
                return True
            else:
                print(f"Failed {r.status_code}")
        except Exception as e:
            print(f"Error {e}")
    return False

try_download(candidates_dip, "recursos/logo-diputacion.jpg")
try_download(candidates_pcbox, "recursos/logo-pcbox.jpg")
