#definimos funciones para calcular raices de ecuaciones de segundo grado


import math



def raiz1(a,b,c):
    #a,b,c son de tipo float o int
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo + de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b+math.sqrt(d))/(2*a)

def raiz1(a,b,c):
    #a,b,c son de tipo float o int
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo - de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b-math.sqrt(d))/(2*a)

