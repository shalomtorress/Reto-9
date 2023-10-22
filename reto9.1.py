
if __name__ == "__main__":
  N = float(input("número de gallinas:"))
  M = float(input(" número de gallos:"))
  K = float(input(" número de pollitos:"))

  cantidad_carne_gallinas = lambda N: 6*N
  cantidad_carne_gallos = lambda M: 7*M
  cantidad_carne_pollitos = lambda K: 1*K

  total_carne = cantidad_carne_gallinas(N) + cantidad_carne_gallos(M) + cantidad_carne_pollitos(K)

  print("La cantidad de carne es:" + str(total_carne))
  
