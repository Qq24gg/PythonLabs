any_list = [1,2,3,4,3,2,1,1,2,3,4,6,789,0,99999]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)