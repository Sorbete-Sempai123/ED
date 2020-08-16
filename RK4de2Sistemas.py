#Yober Maycol Mendoza Surco
import numpy

from matplotlib import pyplot as mp

def funcion3r(x,y1,y2):
    return -y2/5

def funcion4r(x,y1,y2):
    return y1

def funcion3Integrada(x):
    c1 = 0
    c2 = 1
    return c2*numpy.cos(x/numpy.sqrt(5)) - c1*numpy.sin(x/numpy.sqrt(5))/numpy.sqrt(5)
def funcion4Integrada(x):
    c1 = 0
    c2 = 1
    return 5**(1/2) * c2 * numpy.sin(x/numpy.sqrt(5)) + c1*numpy.cos(x/numpy.sqrt(5))


def SistemRK4orden(x,y1,y2,xf,h,F1,F2):
    arr = [[x],[y1],[y2]]
    it = int((xf-x)/h) #it = iteraciones
    #Todo el for realiza el metodo de euler
    for i in range(it):
        #se usa un auxliar como apoyo para la derivada de la segunda funcion
        auxy1 = y1
        k11 = F1(x,y1,y2)
        k12 = F2(x,y1,y2)

        k21 = F1(x+h/2,y1+k11*h/2,y2+k12*h/2)
        k22 = F2(x+h/2,y1+k11*h/2,y2+k12*h/2)

        k31 = F1(x+h/2,y1+k21*h/2,y2+k22*h/2)
        k32 = F2(x+h/2,y1+k21*h/2,y2+k22*h/2)

        k41 = F1(x+h,y1+k31*h,y2+k32*h)
        k42 = F2(x+h,y1+k31*h,y2+k32*h)

        ks1 = k11 + 2*k21 + 2*k31 + k41
        ks2 = k12 + 2*k22 + 2*k32 + k42
        #Realizamos las operaciones
        y1 = y1 + ks1*h/6
        y2 = y2 + ks2*h/6
        #Hacemos que x avance en h
        x = x + h
        #Se agregan los datos al arr para facilitar recuperar los datos
        arr[0].append(x)
        arr[1].append(y1)
        arr[2].append(y2)
    #Imprime los valores finales
    return arr
#Parametros inciales
x = 0
y1 = 1
y2 = 0
xf = 5
h = 0.5
#Res retorna una lista con las aproximaciones del metodo de euler
res = SistemRK4orden(x,y1,y2,xf,h,funcion3r,funcion4r)
#Imprimo los datos para poder escribirlos en el excel
print(res[0])
print(res[1])
print(res[2])

xpruebas = numpy.arange(0,2,0.001)
#Ploteando la funcion de la primera integral
mp.plot(xpruebas,[funcion3Integrada(i) for i in xpruebas],label="Funcion y1")
#Ploteando las aproximaciones de euler
mp.plot(res[0], res[1],label="Runge Kutta 4to Orden y1")

#Ploteando la funcion de la segunda integral
mp.plot(xpruebas, [funcion4Integrada(i) for i in xpruebas],label="Funcion y2")
#Ploteando las aproximaciones de euler
mp.plot(res[0], res[2],label="Runge Kutta 4to Orden y2")

mp.legend()
mp.show()
