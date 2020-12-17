def structure_to_formula(strc):
    ''' recieve a molecular formula, and transfer it to a possible structure
        CH3CH2OH or CH3OCH3 --> C2H6O
        CH3CH2Cl --> C2H5Cl
        CH3COOH --> C2H4O2
    '''
    element = ''
    for i in range(len(strc)-1):
        if strc[i].isupper() and strc[i+1].isupper():
            element += strc[i]
        elif strc[i].isupper() and strc[i+1].isdigit():
            element += strc[i] * int(strc[i+1])
        elif strc[i].islower() and strc[i+1].isupper():
            element += strc[i-1]+strc[i]
        elif strc[i].islower() and strc[i+1].isdigit():
            element += (strc[i-1]+strc[i]) * int(strc[i+1])
        
    if strc[len(strc)-1].isupper():
        element += strc[len(strc)-1]
    elif strc[len(strc)-1].islower():
        element += strc[len(strc)-2] + strc[len(strc)-1]

    from make_list import make_list
    ele_all = make_list(element)
    ele_norep = list(set(ele_all))
    
##    print(ele_all)
##    print(ele_norep)
    num = [0] * len(ele_norep)
    for i in range(len(ele_norep)):
        for j in range(len(ele_all)):
            if ele_norep[i] == ele_all[j]:
                num[i] += 1
    return dict(zip(ele_norep,num))
    
            

##def main():
##    print(structure_to_formula('CH3CH2OH'))
##main()
