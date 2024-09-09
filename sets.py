#merging two directories that have their common keys value summed up
#we going to iterate through the keys and values of both dictionaries
#add values of common keys

def merge_dicts(dict1, dict2):
   
    merged_dict = dict1.copy()  

    for key, value in dict2.items():
        if key in merged_dict:
            
            merged_dict[key] += value
        else:
           
            merged_dict[key] = value

    return merged_dict


dict1 = {'a': 9, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 8, 'd': 5}

result = merge_dicts(dict1, dict2)
print(result)  



