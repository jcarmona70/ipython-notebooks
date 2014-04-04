# -*- coding: utf-8 -*-
import urllib2
import string 
def root(s):
    #s es un strig que representa una dirección http, se queda con la raíz (incluyendo el caracter "/")
    x=s.find('//')
    final=s.find('/',x+2)
    if final==-1:
        return s+'/'
    else:
        return s[:final+1]
def path(s):
    #s es un strig que representa una dirección http
    #devuelve la ruta hasta el archivo representado por s (incluyendo el caracter "/")  
    pos=len(s)-1
    while s[pos]!='/':
        pos=pos-1
    if s[pos-1]=='/':
        return s+'/'
    else:
        return s[:pos+1]

def enlaces(s,url):
    #s es un string con el contenido de una página html
    #url es un string que corresponde a la dirección de la página (se usa para componer los enlaces absolutos a partir de los relativos)
    #devuelve una lista con todos los enlaces que aparecen en s
    raiz=root(url)
    camino=path(url)
    result=[]
    next_label=s.find('<a href')
    while next_label!=-1:
        inic_url=s.find("\"",next_label)+1
        fin_url=s.find("\"",inic_url)
        enlace=s[inic_url:fin_url]
    
        if enlace[0:4]=='http':
          result.append(s[inic_url:fin_url])
        elif len(enlace)>0 and enlace[0]=='/':
          result.append(raiz+enlace[1:])
        #else:
        #  result.append(camino+s[inic_url:fin_url])  
        next_label=s.find('<a href',fin_url)
    return result

def quita_labels(s):
    #s es un string con el contenido de una página html
    #devuelve el resultado de eliminar las etiquetas html de s
    escribir=True
    result=''
    for c in s:
        if c=='<':
            escribir=False
            result=result+' '
        elif c=='>':
            escribir=True
        else:
            if escribir:
                result=result+c
    return result

def es_letra(c):
    #nos dice si un caracter es una letra
    return c not in string.punctuation and c not in string.whitespace and c not in string.digits

def palabras(s):
    #s es un string 
    #devuelve una lista con todas las palabras de s
    limpio=quita_labels(s)
    pos=0
    result=[]
    while pos<len(s) and not es_letra(s[pos]):
        pos=pos+1
    while pos<len(s):
        inic=pos
        while pos<len(s) and es_letra(s[pos]):
            pos=pos+1
        palabra=s[inic:pos].lower()
        if palabra not in result:
            result.append(palabra)
        while pos<len(s) and not es_letra(s[pos]):
            pos=pos+1
    return result


def busca_bin(ind,palabra):
    #ind es un índice
    #devueve un par esta,pos
    # esta es un booleano que nos indica si la palabra está en el índice
    # pos indica: la posición de la palabra en el índice (si está) o
    #             la posición que ocuparía palabra en índica (si no está)
    i=0
    j=len(ind)-1
    while i<=j:
        med=(i+j)/2
        if ind[med][0]>=palabra:
            j=med-1
        else:
            i=med+1
    return (i<len(ind) and ind[i][0]==palabra),i





def aniadir(ind,palabra,pagina):
    #añade el par palabra,pagina al índice
    esta,pos=busca_bin(ind,palabra)
    if esta:
        ind[pos][1].append(pagina)
    else:
        ind.insert(pos,[palabra,[pagina]])
    
    
def visita_paginas(visitadas,por_visitar,rotos,dic,max):
    while len(por_visitar)!=0 and len(visitadas)<max:
        actual=por_visitar[0]
        del por_visitar[0]
        visitadas.append(actual)
        try:
            pag=urllib2.urlopen(actual,timeout=10)
            contenido=pag.read()
            pag.close()
            links=enlaces(contenido,actual)
            words=palabras(contenido)
            for l in links:
                if l not in visitadas and l not in por_visitar and l not in rotos:
                    por_visitar.append(l)
            for p in words:
                aniadir(dic,p,actual)
            #print 'visitadas:',len(visitadas)
        except urllib2.HTTPError:
            rotos.append(actual)
def busca(palabra,indice):
    esta,pos=busca_bin(indice,palabra)
    if esta:
        return indice[pos][1]
    else:
        return []
    
