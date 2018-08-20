import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://scholar.google.es/citations?user=GlM971cAAAAJ&hl=es&oi=ao")
bsObj = BeautifulSoup(html, "html.parser")
perfil = bsObj.findAll("div",{"id":"gsc_prf_i"})
contenido = bsObj.findAll("table",{"id":"gsc_a_t"})
grafica = bsObj.findAll("div", {"class": "gsc_md_hist_b"})
filename = "prueba3.csv"
f = open(filename, "w", newline='')

headers = "nombre, contenido, indice\n"
f.write(headers)

for info in perfil:
    nombre= info.findAll("div")
    name = nombre[0].get_text()
    print(name)

for texto in contenido:
        todo = []
        titulo = texto.findAll("tr")
        todo.append(texto.get_text())
        print(todo)
for indice in grafica:
    guardar = []
    cont = indice.findAll("span")
    guardar.append(indice.get_text())
    print(guardar)


    f.write(str(name)+","+"\n"+str(todo)+" ,"+"\n"+str(guardar) + "\n")

    f.close()
