li = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in li if x%2==0]
# even = list(filter(lambda x:x%2==0,li)) #verificações de verdadewiro ou falso
square = list(map(lambda x:x**2,even)) #itera por cada item para retornar algo
print(square)