# 1

def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)
print(output_list)


# 2 

def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_lst.append(reverse_list(item))
        else:
            reversed_lst.append(item)
    return reversed_lst
    
input_list = [[1, 2, 3], [4, 5, 6], [7, [8, 9]]]
output_list = reverse_list(input_list)
print(output_list)