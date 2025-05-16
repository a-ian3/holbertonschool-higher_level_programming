#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # Décrémenter n à chaque tour
    return result

# Récupérer l'argument depuis la ligne de commande
f = factorial(int(sys.argv[1]))
print(f)

