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