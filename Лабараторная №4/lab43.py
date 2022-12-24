list_a = [1,2,3,4,5,6,7,8,9,10]
def replace(list):
    max_ = list.index(max(list))
    min_ = list.index(min(list))
    list[max_], list[min_] = list[min_], list[max_]
    print(list)
replace(list_a)