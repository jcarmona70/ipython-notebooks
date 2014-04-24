##SUDOKU
#Abre un fichero de texto donde hay un sudoku escrito.
def leerSudoku(nombre):
    f=open(nombre,'r')
    a=f.readline()
    m=[]
    while a!='':
        r=a.split()
        a=f.readline()
        m.append(r)
    return m
#Convierte las listas en Matrices
def matriz(m):
    s=[]
    i=0
    k=0
    r=[]
    while i<9:
        while k<9:
            s.append(int(m[i][k]))
            k=k+1
        k=0
        r.append(s)
        s=[]
        i=i+1
    return r
#Nos indica si es (True) o no (False) posible,
#que un numero (elem) valla en una casilla ([fil][col]),
#mirando en la fila y en la columna en la que se encuentra
def esposible(mat, elem, fil, col):
    a=True
    i=0
    j=0
    if mat[fil][col]!=0:
        a=False
    else:
        while i<len(mat) and a==True:
            if mat[fil][i]!=elem:
                i=i+1
            else:
                a=False
        while j<len(mat) and a==True:
            if mat[j][col]!=elem:
                j=j+1
            else:
                a=False
        io=fil-fil%3
        jo=col-col%3
        c=io
        b=jo
        while c<io+3 and a==True:
            b=jo
            while b<jo+3 and a==True:
                if mat[c][b]!=elem:
                    b=b+1
                else:
                    a=False
            c=c+1
    return a
#Escribe el Sudoku de tal forma que se pueden ver bien
#los posibles valores para las casillas vacias
def escribir(m):
    s=''
    j=1
    for i in range(9):
        for j in range(9):
            if j==0:
                s=s+'||'
            if m[i][j]==0:
                for k in range(1,4):
                    if esposible(m,k,i,j):
                        s=s+str(k)
                    else:
                        s=s+'*'
            else:
                s=s+3*str(m[i][j])              
            if j==2 or j==5:
                s=s+'||'
            elif j==8:
                s=s+'||'+'\n'
            else:
                s=s+'|'
        for j in range(9):
            if j==0:
                s=s+'||'
            if m[i][j]==0:
                for k in range(4,7):
                    if esposible(m,k,i,j):
                        s=s+str(k)
                    else:
                        s=s+'*'
            else:
                s=s+3*str(m[i][j])              
            if j==2 or j==5:
                s=s+'||'
            elif j==8:
                s=s+'||'+'\n'
            else:
                s=s+'|'
        for j in range(9):
            if j==0:
                s=s+'||'
            if m[i][j]==0:
                for k in range(7,10):
                    if esposible(m,k,i,j):
                        s=s+str(k)
                    else:
                        s=s+'*'
            else:
                s=s+3*str(m[i][j])              
            if j==2 or j==5:
                s=s+'||'
            elif j==8:
                s=s+'||'+'\n'
            else:
                s=s+'|'
        if i==2 or i==5 or i==8:
            s=s+2*('+'+3*'+---+---+---+'+'+'+'\n')
        else:
            s=s+'||'+2*('---+---+---+'+'+')+'---+---+---'+'||'+'\n'
    s=2*('+'+3*'+---+---+---+'+'+'+'\n')+s
    print s
def listaPosibles(m, i ,j):
    result=[]
    for elem in range(1,10):
        if esposible(m, elem , i,j):
            result.append(elem)
    return result
def colocarUnicos(m):
    for i in range(len(m)):
        for j in range(len(m)):
            s=listaPosibles(m, i ,j)
            if len(s)==1:
                m[i][j]==s[0]
    return m
def borrar(m,m_inicial,i,j,n):
    #Borra un elemento que hayamos aÃ±adido
    # si el nÂº seleccionado pertenece a alguno de los valores
    # iniciales del sudoku, devuelve un mensaje que nos dice que
    # no podemos modificar ese nÂº
    # m = matriz del sudoku (puede contener valores que hayamos aÃ±adido)
    # m_inicial = matriz del sudoku sin modificar (original)
    # i = fila
    # j = columna
    # n = nÂº entre 1 y 9 que queremos comprobar
  
    i0=(i/3)*3+i%3
    j0=(j/3)*3+j%3
    if esposible(m,n,i,j)==False and m[i0][j0]==m_inicial[i0][j0]:
       print 'No es posible borrar ese valor. Pertenece al sudoku original'
    else:
       m[i0][j0]=0
    return m
def insertarValor(m,n,i,j):
    #Inserta el valor n en la caja 3x3
    # del sudoku que nosotros elijamos
    # m = matriz del sudoku
    # i = fila
    # j = columna
    # n = nÂº entre 1 y 9 que queremos comprobar
  
    i0=(i/3)*3+i%3
    j0=(j/3)*3+j%3
    if esposible(m,n,i,j)==True:
       m[i0][j0]=n
       print 'aaaa'
    else:
        print  'No se puede'
    return m
def Menu():
    # MenÃº principal del programa
    # Muestra por pantalla las diferentes opciones que el usuario
    # podrÃ¡ elegir para interactuar con un fichero que contenga
    # los valores ordenados de un sudoku 9x9
   nombre=raw_input('Escribe el nombre del fichero que quieras que lea el programa\n')
   a=matriz(leerSudoku(nombre))
   m_inicial=leerSudoku(nombre)
   #La razÃ³n de 'copiar' la matriz dos veces es para
   # utilizarlas despuÃ©s en la funciÃ³n <borrar>
   terminar=False
   while not terminar:
       print 'Â¿QuÃ© quieres hacer?'
       print '1.Probar un valor para una caja'
       print '2.Visualizar el tablero con todos los valores posibles'
       print '3.Borrar un valor que hemos introducido'
       print '4.Salir\n'
       opcion=int(raw_input('Elija un nÃºmero\n'))
       if (opcion==1):
           fila= int(raw_input('Escriba la fila (entre 0 y 8)\n'))
           columna= int(raw_input('Escriba la columna (entre 0 y 8)\n'))
           valor=int(raw_input('Escriba el valor que quiere introducir\n'))
           insertarValor(a,valor,fila,columna)
       elif (opcion==2):
           escribir(a)
       elif (opcion==3):
           fila= int(raw_input('Escriba la fila (entre 0 y 8)\n'))
           columna= int(raw_input('Escriba la columna (entre 0 y 8)\n'))
           valor=int(raw_input('Escriba el valor que quiere borrar\n'))
           borrar(a,m_inicial,fila,columna,valor)
       elif (opcion==4):
           terminar=True
           print
Menu()
print
