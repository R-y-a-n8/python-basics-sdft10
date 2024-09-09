#sort a list of tuples sorting with age in ascending order
#use a sort method sort() 
def sort_by_age(tuples_list):
   
    tuples_list.sort(key=lambda x: x[1])


tuples_list = [("grace", 100), ("Brian", 27), ("Chloe", 5)]
sort_by_age(tuples_list)
print(tuples_list)  
