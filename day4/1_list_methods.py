data = [(1, 2, 12), (3, 1, 14), (1, 1), (5, 2, 0)]
def get_second_element(x): 
    
    return x[1]
a= data;
a.sort(key=get_second_element)
print(a) #[(3, 0), (4, 1), (12, 10), (1,12)]




# sort the above list based on last item of the each tuple!