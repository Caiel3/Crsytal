import os
import sys
from os import listdir
from os.path import isfile, isdir, join
import xml.etree.ElementTree as et
import shutil


def listdir_recurd(files_list, root, d, checked_folders):
    pass

#Retorna todas las direcciones en un directorio
def RecorrerDirectorio(files_list, root, folder, checked_folders):

    if (folder != root):
        checked_folders.append(folder)

    for f in listdir(folder):
        d = join(folder, f)

        if isdir(d) and d not in checked_folders:
            listdir_recurd(files_list, root, d, checked_folders)
        else:
            if isfile(d):  # si no hago esto, inserta en la lista el nombre de las carpetas ignoradas
                files_list.append(join(folder, f))

    return files_list

#retorna la direccion del directorio posteior a leerlo
def Leer (texto):
    url=input(texto)
    return url.replace("\\","/").replace("‪","")

#Retorna una matriz con todos las etiquetas de un xml "Name"
def RecorrerXML(url,destino,etiquetas,archivos):
    matrizXML=et.parse(url)
    root= matrizXML.getroot()
    for hijo in root.findall('object'):
       for nieto in hijo.findall('name'):
            if ValidarEtiquetas(nieto.text,etiquetas)==0:
                urlTemp=url.replace(archivos,destino)
                MoverArchivo(url,urlTemp)
                urlActImg=url.replace(".xml",".jpg")
                urlTempImg=urlActImg.replace(archivos,destino)
                MoverArchivo(urlActImg, urlTempImg)


#Compara la etiqueta enviada con la del archivo txt
def ValidarEtiquetas(etiqueta,etiquetas):
    txt=open(etiquetas)
    for linea in txt:
        if etiqueta.strip()==linea.strip():
            return 1

    return 0
#Mueve un archivo de un lugar a otro
def MoverArchivo(act,prx):
    shutil.copy(act,prx)


def Main():
    print("recuerde que las rutas de los archivos deben ser completas terminando por / o \\: \n")
    rutaArchivos=Leer("Ingrese la Direccion del directorio de los archivos: ").strip()
    rutaDestino=Leer("Ingrese la direccion del destino para almacenar defectuosos: ").strip()
    rutaEtiquetas=Leer("Ingrese la direcciond del txt que ocntiene las etiquetas: ").strip()

    matriz=RecorrerDirectorio([],rutaArchivos,rutaArchivos,[])

    for ruta in matriz:
        if ".xml" in ruta:
            RecorrerXML(ruta,rutaDestino,rutaEtiquetas,rutaArchivos)


if __name__ == "__main__":
    Main()