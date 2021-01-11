import os
import pdb
import sys
from os import listdir, replace
from os.path import isfile, isdir, join
import xml.etree.ElementTree as et
import shutil
from os import remove
from xml.etree.ElementTree import XML

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
def RecorrerXML(url,destino,etiquetas,archivos,rutaMalos,matriz):
  try:
      matrizXML = et.parse(url)
      root = matrizXML.getroot()

      t = len(url.split('/'))
      filenameurl=url.split('/')[t-1]  

      
      filename = root.findall('filename')[0].text
      if ('jpg' or 'png ') not in filename:
          filename = filename+'.xml'
          pass
    
      
      if 'jpg' in filename:          
          filenamexml=filename.replace('jpg','xml')
          pass
      else:
          filenamexml=filename.replace('png','xml')
          pass

     
      
      tan=len(filenameurl.split('\\'))

      if filenameurl.split('\\')[tan-1]!=filenamexml:
        print('::::::::::::::::::::::::::::::Nombre archivo diferente a nombre dentro {}'.format(filename))
        try:
            shutil.move(url,rutaMalos+'diferente/'+filenameurl)
            shutil.move(url.replace('xml','jpg'),rutaMalos+'diferente/'+filenameurl.replace('xml','jpg'))
            pass
        except Exception as e:
            pass

      for hijo in root.findall('object'):
          
          for nieto in hijo.findall('name'):
              if ValidarEtiquetas(nieto.text, etiquetas) == 0:
                  urlTemp = url.replace(archivos, destino)
                  MoverArchivo(url, urlTemp)
                  urlActImg = url.replace(".xml", ".jpg")
                  urlTempImg = urlActImg.replace(archivos, destino)
                  MoverArchivo(urlActImg, urlTempImg)
                  remove(url)
                  remove(urlActImg)
  except:
      urlMalosNew=url.replace(archivos,rutaMalos)
      MoverArchivo(url, urlMalosNew)
      urlMalosImg=url.replace(".xml", ".jpg")
      urlMalosNewImg=urlMalosImg.replace(archivos,rutaMalos)
      MoverArchivo(urlMalosImg,urlMalosNewImg)
      remove(urlMalosImg)
      remove(url)

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
    #rutaArchivos=Leer("Ingrese la Direccion del directorio de los archivos: ").strip()
    #rutaDestino=Leer("Ingrese la direccion del destino para almacenar defectuosos: ").strip()
    #rutaEtiquetas=Leer("Ingrese la direcciond del txt que contiene las etiquetas: ").strip()
    #rutaMalos = Leer("Ingrese la direccion Para almacenar malos: ").strip()

    rutaArchivos="D:\Blackboxf2\maquina/"
    """ rutaArchivos="D:\Blackboxf2\png/" """
    rutaDestino="D:\Blackboxf2\defetuosos/"
    rutaEtiquetas="D:\Crystal S.A.S\Practicante TI 3 - BLACKBOX 2020\windows_v1.8.0\data\predefined_classes.txt"
    rutaMalos = "D:\Blackboxf2\Malos/"

    matriz=RecorrerDirectorio([],rutaArchivos,rutaArchivos,[])
   
    mat=convertir_matriz(matriz=matriz)
    
    """ xml(mat,rutaArchivos) """#cambia XML a xml
    

    """  for ruta in matriz: #valida etiqueta y nombres de archivos
        if ".xml" in ruta:
            RecorrerXML(ruta,rutaDestino,rutaEtiquetas,rutaArchivos,rutaMalos,mat) """
    pares(mat,rutaMalos,rutaArchivos)     #valida que todo este por pares

    
    

def convertir_matriz(matriz):

    mat=[]
    for pos in matriz:
        t = len(pos.split('/'))
        mat.append(pos.split('/')[t-1])
    return mat

def xml(mat, url):#cambia todos los XML a xml
    for pos in mat:
        if 'xml' or 'XML' in pos:
            print(pos)
            shutil.move(url+pos,url+pos.replace('XML','xml'))
            pass
        else:
            print('Imagen')
            pass
        pass
    pass

def pares(mat,malos,url):    
    
    for item in mat:
        if ('jpg' or 'png') in item:
            if item.replace('png','xml').replace('jpg','xml') in mat:
                print('::Tiene pareja {}'.format(item))
                pass
            else:               
                print('::::::::::::No Tiene pareja {}'.format(item))
                shutil.move(url+item,malos+'diferente/'+item)
                pass
            pass
        else:
            if item.replace('xml','jpg') in mat:
                print('::Tiene pareja {}'.format(item))
                pass
            elif item.replace('xml','png') in mat:
                print('::Tiene pareja {}'.format(item))
                pass
            else:
                shutil.move(url+item,malos+'diferente/'+item)
                pass            
            pass
        pass
    
    

if __name__ == "__main__":
    Main()
