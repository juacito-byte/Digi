textdna =  "atggatcattta"

contadorletras = 0

for l in range(len(textdna)):#l es cada iteracion osea cada posicion
    if textdna[l] == "a":# sirve para pasar de que la variable local este en numeros(el indice) a que me lo de en letras
        contadorletras +=1# acumular
        print(f"la posicion de a es {l}")
print(f"hay {contadorletras} a")