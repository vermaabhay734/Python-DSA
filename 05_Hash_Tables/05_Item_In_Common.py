# Brute force, Timecomplexity -> O(n^2)
def item_common(list1, list2):
    for i in list1:
        for j in list1:
            if i == j:
                return True
    return False 


# with the help of HashTable, Timecomplexity -> O(n)
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False



list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))
print(item_common(list1, list2))