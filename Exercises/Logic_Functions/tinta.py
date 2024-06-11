import math

metros = float(input("Tamanho em metros quadrados da área\n:"))
litros = metros/6
latas = math.ceil(litros/18)
galao = math.ceil(litros/3.6)
print(galao)
restoLata = latas%18

print(f'{"-"*30}\n{" Apenas latas ":^30}\n{"-"*30}')
print(f"Preço: R$ {(latas*80):.2f}")

print(f'{"-"*30}\n{" Apenas galões ":^30}\n{"-"*30}')
print(f"Preço: R$ {(galao*25):.2f}")

print(f'{"-"*30}\n{" Galões e latas ":^30}\n{"-"*30}')
galaoIdeal = math.ceil(restoLata/3.6)
lataideal = latas - 1
print(f"Preço: R$ {((galaoIdeal*25+lataideal*80)):.2f}")