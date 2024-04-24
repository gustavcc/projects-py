import math
list = [3,0,1,4,2,8,7,5]

for index in range(len(list)):
    #* operator ternary
    if list[index] > list[index+1] if index+1 < len(list) else None:
        anchor_1 = list[index]
        anchor_2 = list[index+1]
        list[index] = anchor_2
        list[index+1] = anchor_1
    # index_central = math.floor(len(list)/2)
# if len(list)%2==0:
#     anchor_central_2 = list[index_central]
#     anchor_central_1 = list[index_central-1]
#     list[index_central] = anchor_central_1
#     list[index_central-1] = anchor_central_2
# else:
#     print(index_central)
print(list)