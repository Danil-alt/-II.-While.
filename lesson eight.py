my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
index = -1
while index < len(my_list):
    index += 1
    if my_list[index] < 0:
        break
    elif my_list[index] == 0:
        continue
    print(my_list[index])
    