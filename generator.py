print("Bienvenido al generador ")
print("""
            ___           ___           ___           ___           ___            
     /  /\         /  /\         /  /\         /__/\         /  /\           
    /  /:/_       /  /:/_       /  /:/         \  \:\       /  /::\          
   /  /:/ /\     /  /:/ /\     /  /:/           \  \:\     /  /:/\:\         
  /  /:/_/::\   /  /:/_/::\   /  /:/  ___   ___  \  \:\   /  /:/~/:/         
 /__/:/__\/\:\ /__/:/__\/\:\ /__/:/  /  /\ /__/\  \__\:\ /__/:/ /:/          
 \  \:\ /~~/:/ \  \:\ /~~/:/ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\/:/           
  \  \:\  /:/   \  \:\  /:/   \  \:\  /:/   \  \:\  /:/   \  \::/            
   \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\            
    \  \::/       \  \::/       \  \::/       \  \::/       \  \:\           
     \__\/         \__\/         \__\/         \__\/         \__\/           
      """)

diccionario_final = set()

nombre = input("Ingrese nombre (O presione enter para omitir): ")
apellido = input("Ingrese apellido (O presione enter para omitir): ")
anio =  input("Ingrese año de nacimiento (O presione enter para omitir): ")
empresa = input("Ingrese nombre de empresa (O presione enter para omitir): ")
nombre_mascota = input("Ingrese nombre de la mascota (O presione enter para omitir): ")
equipo = input("Ingrese equipo favorito (O presione enter para omitir): ")
color = input("Ingrese color favorito (O presione enter para omitir): ")
alias = input("Ingrese el alias de la persona (O presione enter para omitir): ")
name_archive = input("Que nombre quiere ponerle al archivo: ") 
name_archive += ".txt"

if not name_archive.endswith(".txt"):
    name_archive += ".txt"

inputs = [nombre, apellido, anio, empresa, nombre_mascota, equipo, color, alias]

palabras = [p.strip() for p in inputs if p.strip() != ""]

if anio != "" and len(anio) == 4:
    palabras.append(anio[2:])
    
final_sgs = ["!", "@", "*", ".", "123", "2026", "$"]
separadores = [".", "_", "-"]

for palabra in inputs:
    if palabra != "":
        palabras.append(palabra)

for p1 in palabras:
    diccionario_final.add(p1)
    diccionario_final.add(p1.capitalize())
    diccionario_final.add(p1.lower())
    diccionario_final.add(p1.upper())
    
    for p2 in palabras:
        if p1 != p2:
            diccionario_final.add(p1 + p2)
            diccionario_final.add(p1 + "." + p2)
            diccionario_final.add(p1.upper() + p2)
            diccionario_final.add(p1.capitalize() + p2)
            
            if len(p1)> 0:
                diccionario_final.add(p1[0] + p2)
                diccionario_final.add(p1[0] + "." + p2)
                diccionario_final.add(p1[0].lower() + p2)
                diccionario_final.add(p1[0].upper() + p2)
            for sim in final_sgs:
                diccionario_final.add(p1 + p2 + sim)
                diccionario_final.add(p1.capitalize() + p2 + sim)

    for sim in final_sgs:
        diccionario_final.add(p1 + sim)
        diccionario_final.add(p1.capitalize() + sim)
    
print(f"\n [!]se generaron {len(diccionario_final)} passwords")

with open(name_archive, "w") as archivo:
    for password in diccionario_final:
        archivo.write(password + "\n")