p=float(input("Ingrese la nota 1.\n"))
p+=float(input("Ingrese la nota 2.\n"))
p+=float(input("Ingrese la nota 3.\n"))
p*=0.55/3
e= float(input("Ingrese el examen.\n"))*0.3
t= float(input("Ingrese el trabajo final.\n"))*0.15
print("El promedio del estudiante:",round((p+e+t), 2))
