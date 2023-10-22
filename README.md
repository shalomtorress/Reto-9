# Reto-9
## Punto 1:
De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
+ **Reto 6 punto 3**:
  + una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

sin lamdas
````python
def calcular_carne_aves(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))
  total_carne = calcular_carne_aves(N, M, K)
  print("La cantidad de carne es:" + str(total_carne))
````
con lamdas 
````python
if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))

  cantidad_carne_gallinas = lambda N: 6*N
  cantidad_carne_gallos = lambda M: 7*M
  cantidad_carne_pollitos = lambda K: 1*K

  total_carne = cantidad_carne_gallinas(N) + cantidad_carne_gallos(M) + cantidad_carne_pollitos(K)

  print("La cantidad de carne es:" + str(total_carne))
  
````
+ **Reto 6 punto 5**
   + un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
 
sin lamdas
````python
def calcular_interes(C, i, n):

  interes_mensual = i / 12
  valor_final = C * (1 + interes_mensual) ** n
  return valor_final


if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  valor_final = calcular_interes(C, i, n)

  print("El valor del préstamo al final del período es:", valor_final)
````
con lamdas 
````python
if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  interes_mensual = lambda i: i / 12
  valor_final = lambda C, i, n: C * (1 + interes_mensual(i)) ** n

  print("El valor del préstamo al final del período es:", valor_final(C, i, n))
````
+ **Reto 6 punto 6**
  + El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

sin lamdas
````python
def calcular_contagios(C, D):
  contagiados = C
  for i in range(D):
    contagiados = contagiados * 2
  return contagiados


if __name__ == "__main__":
  C = int(input("Número de contagiados actuales: "))
  D = int(input("Número de días: "))

  contagiados = calcular_contagios(C, D)

  print("El número total de contagiados es:", contagiados)
````
con lamdas 
````python
if __name__ == "__main__":
  C = int(input("Número de contagiados actuales: "))
  D = int(input("Número de días: "))

  contagios = lambda C, D: C * 2 ** D

  print("El número total de contagiados es:", contagios(C, D))
````
## Punto 2
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

+ **reto 6 punto 3**
  + una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

sin *args
````python
def calcular_carne_aves(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))
  total_carne = calcular_carne_aves(N, M, K)
  print("La cantidad de carne es:" + str(total_carne))
````
con *args
````python
def calcular_carne_aves(*args) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))
  total_carne = calcular_carne_aves(N, M, K)
  print("La cantidad de carne es:" + str(total_carne))
````
+ **Reto 6 punto 5**
   + un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
sin *args
````python
def calcular_interes(C, i, n):

  interes_mensual = i / 12
  valor_final = C * (1 + interes_mensual) ** n
  return valor_final


if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  valor_final = calcular_interes(C, i, n)

  print("El valor del préstamo al final del período es:", valor_final)
````



con *args
````python
def calcular_interes(*args):
  interes_mensual = i / 12
  valor_final = C * (1 + interes_mensual) ** n
  return valor_final

if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  valor_final = calcular_interes(C, i, n)

  print("El valor del préstamo al final del período es:", valor_final)
````
+ **Reto 6 punto 6**
  + El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

sin *args
````python
def calcular_contagios(C, D):
  contagiados = C
  for i in range(D):
    contagiados = contagiados * 2
  return contagiados


if __name__ == "__main__":
  C = int(input("Número de contagiados actuales: "))
  D = int(input("Número de días: "))

  contagiados = calcular_contagios(C, D)

  print("El número total de contagiados es:", contagiados)
````
con *args
````python
def calcular_contagios(*args):
  contagiados = C
  for i in range(D):
    contagiados = contagiados * 2
  return contagiados


if __name__ == "__main__":
  C = int(input("Número de contagiados actuales: "))
  D = int(input("Número de días: "))

  contagiados = calcular_contagios(C, D)

  print("El número total de contagiados es:", contagiados)
````
## Punto 3
Escriba una función recursiva para calcular la operación de la potencia.
````def potencia(base, exponente):
  if exponente == 0:
    return 1
  else:
    return base * potencia(base, exponente - 1)

if __name__ == "__main__":
  exponente = int(input("Ingrese la potencia: "))
  base = float(input("Ingrese la base: "))
  resultado = potencia(base, exponente)
  print("Si elevamos " + str(base) + " a " + str(exponente) + " es igual a: " + str(resultado))
````

La función ````potencia```` calcula la potencia de un número, funciona llamando a sí mismo para calcular la potencia de la base con un exponente uno menos.

Si el exponente es igual a 0, el resultado es 1.
Si el exponente es mayor que 0, el resultado es la base multiplicada por la potencia de la base con un exponente uno menos.
## Punto 4 
Utilice la siguiente plantilla de code para contar el tiempo:
````python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
````
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
````python
import time

def fibo_recursivo(n: int) -> int:
  if n <= 1:
    return n
  else:
    return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)


def main():

  start_time = time.time()
  serie_fibonacci = []
  for i in range(n):
    serie_fibonacci.append(fibo_recursivo(i))
  end_time = time.time()
  timer = end_time - start_time
  return serie_fibonacci, timer


if __name__ == "__main__":
  n = int(input("Ingrese el número hasta el que desea calcular la serie de Fibonacci: "))
  serie_fibonacci, timer = main()
  print("La serie de Fibonacci hasta el número {} es: {}".format(n, serie_fibonacci))
  print("El tiempo de ejecución fue de {} segundos".format(timer))
````
La función ````fibo_recursivo()```` calcula el término n-ésimo de la sucesión de Fibonacci, Si n es menor o igual a 1, el término n-ésimo es n.
De lo contrario, el término n-ésimo es la suma de los términos n-1 y n-2.

La función ````main()```` primero calcula el tiempo de inicio del programa. Luego, crea una lista vacía para almacenar la serie de Fibonacci. Por último, la función main() itera desde 0 hasta n, calculando el término n-ésimo de la sucesión de Fibonacci y agregándolo a la lista, la función ````main()```` utiliza la función ````time.time```` para calcular el tiempo de inicio del programa.
La función ````main()```` utiliza la función ````list```` para crear una lista vacía. Despues se utiliza un bucle ````for```` para iterar desde 0 hasta n. el main utiliza la funcion ````time.time```` para calcular el tiempo de finalizacion del programa 

## Punto 5 
[![image.png](https://github.com/shalomtorress/imagenes/blob/main/Captura%20de%20pantalla%202023-10-21%20233255.png)
## Punto 6
https://www.linkedin.com/in/shalom-torres-molina-237548297/
