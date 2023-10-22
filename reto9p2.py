
def calcular_carne_aves(*args) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))
  total_carne = calcular_carne_aves(N, M, K)
  print("La cantidad de carne es:" + str(total_carne))
