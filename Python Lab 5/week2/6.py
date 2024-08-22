def search_element(arr, x):
    if x in arr:
        return arr.index(x)
    return -1

arr = [10, 3, 5, 7, 21, 14]
element_to_search = 7
index = search_element(arr, element_to_search)
print(index)
