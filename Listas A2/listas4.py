list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

minimo = list_num[0]
maximo = list_num[0]

for i in list_num:
    if i < minimo:
        minimo = i
    if i > maximo:
        maximo = i 

print(minimo)
print(maximo)
