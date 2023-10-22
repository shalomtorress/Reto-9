if __name__ == "__main__":
  C = float(input("Capital inicial: "))
  i = float(input("Tasa de interés anual: "))
  n = int(input("Número de meses: "))

  interes_mensual = lambda i: i / 12
  valor_final = lambda C, i, n: C * (1 + interes_mensual(i)) ** n

  print("El valor del préstamo al final del período es:", valor_final(C, i, n))
