# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio_circulo = float(input("Informe o raio do círculo: "))

area_circulo = math.pi * (raio_circulo**2)

print(
    f"O círculo com raio igual a {area_circulo} possui uma área igual a {area_circulo}"
)
