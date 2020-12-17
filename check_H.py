def check_H(lst, strc_all):
    strc = []
    for i in strc_all:
        if i not in {'F', 'Cl', 'Br', 'I'}:
            strc.append(i)
    lst_1 =[]
    for i in range(len(lst)):
        if len(lst[i]) <= len(strc):
            lst_1.append(lst[i])
   
    i = 0
    while i < len(lst_1):
        j = 0
        while j < len(lst_1[i]):
            if lst_1[i][j] >= 4:
                lst_1.remove(lst_1[i])
                j = 0
                if i >= len(lst_1):
                    break
            else:
                j += 1
        i += 1
    
           
    return lst_1
        
