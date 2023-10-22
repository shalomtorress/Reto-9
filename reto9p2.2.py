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
