# -*- coding: utf-8 -*-
from PIL import Image

def newton(f,derf,z0,epsilon,max_steps):
    steps=0
    z=z0
    if abs(derf(z))!=0:
        inc=-f(z)/derf(z)
            #print z
    else:
        steps=max_steps
    while steps<max_steps and  abs(f(z))>epsilon:
        z=z+inc
        steps=steps+1
        if abs(derf(z))!=0:
            inc=-f(z)/derf(z)
            #print z
        else:
            steps=max_steps
    return z,steps


def mas_cercana(z,l):
    result=0
    dist=abs(z-l[0])
    for i in range(1,len(l)):
        dist_act=abs(z-l[i])
        if dist_act<dist:
            result=i
            dist=dist_act
    return result

def newton_fractal(f,derf,roots,colors,max_img,max_real,prec):
    xpoints=2*int(round(max_real/prec))
    ypoints=2*int(round(max_real/prec))
    im=Image.new("RGB",(xpoints+1,ypoints+1),"white")
    cont=0
    for x in xrange(xpoints+1):
        for y in xrange(ypoints+1):
            z0=complex((x-xpoints/2)*prec,(ypoints/2-y)*prec)
            aprox,steps=newton(f,derf,z0,2**(-32),100)
            if steps<100:
                im.putpixel((x,y),colors[mas_cercana(aprox,roots)])
            #cont=cont+1
            #if cont%10000==0:
            #   print steps,x,y
            #   print aprox
    return im


#esto define la función para la que queremos hacer el fractal de newton y su derivada

##def f(z):
##    return z**4-1
##def derf(z):
##    return 4*(z**3)
##
###buscamos aproximaciones de las 4 raices (puede requerir más pruebas)
##
##print newton(f,derf,complex(0,2),2**(-64),100000)
##print newton(f,derf,complex(0,-2),2**(-64),100000)
##print newton(f,derf,complex(2,0),2**(-64),100000)
##print newton(f,derf,complex(-2,0),2**(-64),100000)
##
##
###preparamos las cosas para llamar a newton_fractal
##
##r0=newton(f,derf,complex(0,2),2**(-32),100000)[0]
##r1=newton(f,derf,complex(0,-2),2**(-32),100000)[0]
##r2=newton(f,derf,complex(2,0),2**(-32),100000)[0]
##r3=newton(f,derf,complex(-2,0),2**(-32),100000)[0]
##
##raices=[r0,r1,r2,r3]
##fractal=newton_fractal(f,derf,raices,[(255,0,0),(0,255,0),(0,0,255),(255,0,255)],2,2,0.005)
##
##fractal.show()
#si no funciona sustituir por:
#  name='tmp.jpeg'
#  fractal.save(name)
#  import os
#  os.startfile(name)
def f1(z):
    return z**3-2*z+2
def derf1(z):
    return 3*z**2-2

print newton(f1,derf1,complex(0,2),2**(-32),100000)
print newton(f1,derf1,complex(0,-2),2**(-32),100000)
print newton(f1,derf1,complex(2,0),2**(-32),100000)
s0=newton(f1,derf1,complex(0,2),2**(-32),100000)[0]
s1=newton(f1,derf1,complex(0,-2),2**(-32),100000)[0]
s2=newton(f1,derf1,complex(2,0),2**(-32),100000)[0]
raices=[s0,s1,s2]
colores=[(255,0,0),(0,255,0),(0,0,255)]
fractal=newton_fractal(f1,derf1,raices,colores,2,2,0.005)
