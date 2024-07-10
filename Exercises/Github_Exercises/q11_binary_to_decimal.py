binarys = [n for n in input('number: ').split(',')]
decimais = []
# decimais = {}
# def binary_to_decimal(list):
#     for bi in binarys:
#         decimal = 0
#         for i, al in enumerate(bi):
#             decimal+= int(al)*2**i
#         decimais[bi] = decimal
#     return decimais
# dic = binary_to_decimal(binarys)
# dic_valid = []
# for key,value in dic.items():
#     if value % 5 == 0:
#         dic_valid.append(key)

for p in binarys:
    intp = int(p, 2)
    print(intp)
    if intp % 5 == 0:
        decimais.append(p)

print(','.join(decimais))