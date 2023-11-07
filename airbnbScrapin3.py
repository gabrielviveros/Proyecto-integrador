import re
from colorama import Fore
import requests

website = "https://www.airbnb.com.ar/cordoba-argentina/stays/apartments"
resultado = requests.get(website)
content = resultado.text

patron = r"[\w-]"
dpto = re.findall (patron, str (content))
sin_duplicados = list(set(dpto))

dpto_final = []

for i in sin_duplicados:
    nombre_dpto = i.replace("//", "")
    dpto_final.append(nombre_dpto)
    print(nombre_dpto)
    