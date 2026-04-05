print("Bienvenido al generador ")

diccionario_final = set()

nombre = input("Ingrese nombre (O presione enter para omitir): ")
apellido = input("Ingrese apellido (O presione enter para omitir): ")
anio =  input("Ingrese año de nacimiento (O presione enter para omitir): ")
empresa = input("Ingrese nombre de empresa (O presione enter para omitir): ")
nombre_mascota = input("Ingrese nombre de la mascota (O presione enter para omitir): ")
equipo = input("Ingrese equipo favorito (O presione enter para omitir): ")
color = input("Ingrese color favorito (O presione enter para omitir): ")
name_archive = input("Que nombre quiere ponerle al archivo: ") 
name_archive += ".txt"

inputs = [nombre, apellido, anio, empresa, nombre_mascota, equipo, color]

palabras = []
for palabra in inputs:
    if palabra != "":
        palabras.append(palabra)

for p1 in palabras:
    diccionario_final.add(p1)
    diccionario_final.add(p1.capitalize())
    
    for p2 in palabras:
        if p1 != p2:
            diccionario_final.add(p1 + p2)
            diccionario_final.add(p1 + "." + p2)
            
            if len(p1)> 0:
                diccionario_final.add(p1[0] + p2)
                diccionario_final.add(p1[0] + "." + p2)

    caracteres = ["!", "@", "123", "2026", "*"]
    for caract in caracteres:
        diccionario_final.add(p1 + caract)
        diccionario_final.add(p1.capitalize() + caract)
    
print(f"\n [!]se generaron {len(diccionario_final)} passwords")

with open(name_archive, "w") as archivo:
    for password in diccionario_final:
        archivo.write(password + "\n")