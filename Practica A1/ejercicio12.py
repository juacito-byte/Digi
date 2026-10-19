text =  "Hello World"
text2 = "Hola mon!!!" 
coincidencias = 0
for i in range(len(text)):
    if text[i] == text2[i]:
        coincidencias += 1
print(f"las concidencias de los textos son {coincidencias}")