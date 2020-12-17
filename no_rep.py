import copy
from make_list import make_list
def remove_same_structure(lst):
    for n in range(len(lst)):
        lst[n] = make_list(lst[n])
    lst_2 = copy.deepcopy(lst)
    for i in range(len(lst_2)):
        lst_2[i].reverse()

    for i in range(len(lst)):
        for j in range(len(lst_2)):
            if lst[i] == lst_2[j]:
                lst[j] = lst_2[j]
    lst_new = list(set(''.join(i) for i in lst))
        
            
    return lst_new
                   
            


        
        
