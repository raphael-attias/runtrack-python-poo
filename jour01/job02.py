# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
# email : raphael.attias@laplateforme.io

class Operation:
    def __init__(self, nombre1=1, nombre2=22):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_instance = Operation()

print("le nombre 1 est :", operation_instance.nombre1)
print("le nombre 2 est :", operation_instance.nombre2)
