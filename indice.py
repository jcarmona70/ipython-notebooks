
def esLetra(c):
    #nos dice si un caracter es una letra
    esEspecial=(c in 'áéíóúñüÁÉÍÓÚÑÜ')
    esLetra=(c>='a' and c<='z') or (c>='A' and c<='Z')
    return esEspecial or esLetra

def listaPalabras(s):
    #devuelve la lista de palabras del string s,
    #consideramos palabra una sucesion de letras entre dos caracteres que no
    #sean letras
    result=[]
    i=0
    #nos colocamos al comienzo de la primera palabra
    while i<len(s) and not esLetra(s[i]):
        i=i+1
    while i<len(s):
        #construimos la siguiente palabra
        palabra=''
        while i<len(s) and esLetra(s[i]):
            palabra=palabra+s[i]
            i=i+1
        result.append(palabra)
        #nos colocamos al comienzo de la siguiente palabra
        while i<len(s) and not esLetra(s[i]):
            i=i+1
    return result        
        


            
def aniadir(l,palabra,linea):
    #l es de la forma
    #[[palabra_1,[linea_1_1,linea_1_2..,linea_1_n_1]],...,
    #[palabra_k,[linea_k_1,linea_k_2..,linea_k_n_k]]]
    #con palabra_1<palabra_2....<palabra_k
    #
    #si palabra esta en la lista, añade linea a su lista de lineas, si
    #no añade palabra con la lista de lineas [linea] manteniendo la lista
    #ordenada
    pos=0
    while pos<len(l) and palabra>l[pos][0]:
        pos=pos+1
    if pos<len(l):
        if l[pos][0]==palabra:
            l[pos][1].append(linea)
        else:
            l.insert(pos,[palabra,[linea]])
    else:
        l.append([palabra,[linea]])
    
        
def listaPalabrasLineas(nombre):
    #nombre es el nombre de un fichero de texto existente.
    #devuelve el índice de palabras del texto del fichero.
    #El índice es una lista con las  palabras y los números de línea
    #con el formato siguiente:
    #[[palabra_1,[linea_1_1,linea_1_2..,linea_1_n_1]],...,
    #[palabra_k,[linea_k_1,linea_k_2..,linea_k_n_k]]]
    f=open(nombre,'r')
    s=f.readline()
    result=[]
    linea=0
    while s!='':
        l=listaPalabras(s)
        for palabra in l:
            aniadir(result,palabra,linea)
        s=f.readline()
        linea=linea+1
    f.close()
    return result

def listaPalabrasLineasLim(nombre,n):
    #como listaPalabrasLineas
    #pero sólo considerando las n primeras lineas del fichero
    f=open(nombre,'r')
    s=f.readline()
    result=[]
    linea=0
    while s!='' and linea<n:
        l=listaPalabras(s)
        for palabra in l:
            aniadir(result,palabra,linea)
        s=f.readline()
        linea=linea+1
    f.close()
    return result

def guardar(lista,nombre):
    #lista es un indice de palabras como el devuelto por
    # listaDePalabrasLineas
    #Lo guarda en un fichero que se llama nombre.
    #Si ya existe será sobreescrito
    f=open(nombre,'w')
    for item in lista:
        f.write(item[0]+':')
        f.write(str(item[1]))
        f.write('\n')
    f.close()
def mostrar(lista):
    #Muestra por pantalla el indice de palabras representado por lista
    for item in lista:
        print item[0]+':',
        print item[1]
        

def main():
    #escribe el indice de palabras del fichero con el nombre
    #indicado por el usuario 
    #en el fichero con nombre indicado por el usuario.
    #El fichero indicado por usuario debe existir,
    #si existe un fichero con el mismo nombre que el de salida éste
    #se sobreescribe.
    entrada=raw_input('De qué fichero quieres hacer el índice?')
    salida=raw_input('Introduce el nombre del fichero de salida:')
    l=listaPalabrasLineasLim(entrada,100)
    guardar(l,salida)
    print 'el siguiente índice de palabras ha sido guardado:'
    #mostrar(l)
main()
