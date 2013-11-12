#definimos funciones para calcular radios de circunferencias
#tangentes. Ilustrando el teorema de Descartes ver:
#    http://en.wikipedia.org/wiki/Descartes'_theorem


import math
import cmath

def raiz1(a,b,c):
    #a,b,c son de tipo float o int
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo + de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b+math.sqrt(d))/(2*a)

def raiz2(a,b,c):
    #a,b,c son de tipo float o int
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo - de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b-math.sqrt(d))/(2*a)


def craiz1(a,b,c):
    #a,b,c son de tipo float,int o complex
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo + de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b+cmath.sqrt(d))/(2*a)

def craiz2(a,b,c):
    #a,b,c son de tipo float,int o complex
    #b**2-4*a*c>=0
    #devuelve una raiz (la que toma signo - de la raiz del disc.)
    #de la ecuacion: a*x**2+b*x+c=0
    d=b**2-4*a*c
    return (-b-cmath.sqrt(d))/(2*a)




def radio1(r1,r2,r3):
    s1=1.0/r1
    s2=1.0/r2
    s3=1.0/r3
    a=s1+s2+s3
    b=s1**2+s2**2+s3**2
    return 1.0/raiz1(1,-2*a,2*b-a**2)

def radio2(r1,r2,r3):
    s1=1.0/r1
    s2=1.0/r2
    s3=1.0/r3
    a=s1+s2+s3
    b=s1**2+s2**2+s3**2
    return 1.0/raiz2(1,-2*a,2*b-a**2)



