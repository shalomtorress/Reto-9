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


