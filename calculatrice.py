"""
La bibliothèque calculatrice offre la possibilité d'effectuer des opérations de calcul de base entre deux nombres réels.
"""

def addition(arg1,arg2):
    try:
        return float(arg1) + float(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un nombre réel.") 

def soustraction(arg1,arg2):
    try:
        return float(arg1) - float(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un nombre réel.") 

def multiplication(arg1,arg2):
    try:
        return float(arg1) * float(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un nombre réel.") 

def division(arg1,arg2):
    try:
        return float(arg1) / float(arg2)
    except ValueError: 
        print("Un des arguments n'est pas un nombre réel.") 
    except ZeroDivisionError:
        print("Vous divisez par 0.")

def modulo(arg1,arg2):
    try:
        return float(arg1) % float(arg2)
    except ValueError:
        print("Un des arguments n'est pas un nombre réel.")    

def operation(operateur,arg1,arg2):   
    if operateur == '+':
        return addition(arg1,arg2)        
    elif operateur == "%":
        return modulo(arg1,arg2)
    elif operateur == "-":
        return soustraction(arg1,arg2)
    elif operateur == "*":
        return multiplication(arg1,arg2)
    elif operateur == "/":
        return division(arg1,arg2)
    else:
        print("L'opérateur {} n'est pas reconnu.".format(operateur))

# Exemple d'utilisation
#print(operation('+', 5, 3))  # Addition
#print(operation('-', 5, 3))  # Soustraction
#print(operation('*', 5, 3))  # Multiplication
#print(operation('/', 5, 3))  # Division
#print(operation('%', 5, 3))  # Modulo
#print(operation('?', 5, 3))  # Opération non reconnue
