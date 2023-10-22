def potencia(base, exponente):
  if exponente == 0:
    return 1
  else:
    return base * potencia(base, exponente - 1)

if __name__ == "__main__":
  exponente = int(input("Ingrese la potencia: "))
  base = float(input("Ingrese la base: "))
  resultado = potencia(base, exponente)
  print("Si elevamos " + str(base) + "a" + str(exponente) + " es igual a: " + str(resultado))


