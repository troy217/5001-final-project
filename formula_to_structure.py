def formula_to_structure(formula):
    ''' recieve a molecular formula, and transfer it to a possible structure
        C2H6O --> CH3CH2OH or CH3OCH3
        C2H5Cl --> CH3CH2Cl
        C2H4O2 --> CH3COOH
    '''
    #make a dictionary:
    element = []
    number = []
    for i in range(len(formula)-1):
        if formula[i].isdigit():
            number.append(int(formula[i]))
        elif formula[i].isupper() and formula[i+1].isupper():#C2H3FBrCl
            element.append(formula[i])
            number.append(1)
        elif formula[i].isupper() and formula[i+1].isdigit():#C2H3FBrCl
            element.append(formula[i])
        elif formula[i].islower() and formula[i+1].isupper():
            number.append(1)
        elif formula[i+1].islower():
            element.append(formula[i]+formula[i+1])
    if formula[len(formula)-1].isupper():
        element.append(formula[len(formula)-1])
        number.append(1)
    elif formula[len(formula)-1].islower():
        number.append(1)
    elif formula[len(formula)-1].isdigit():
        number.append(int(formula[len(formula)-1]))
    dic_formula = dict(zip(element, number))
    #print(element, number,dic_formula)
    
    
    #get structure without H
    strc_lst = []
    strc_str = ''
    H_atom = dic_formula.pop('H')
    for k, v in dic_formula.items():
        strc_str += k * v
    #print(strc_str)
    from make_list import make_list
    strc_list = make_list(strc_str)
    #print(strc_list)
    
    
##    from no_rep import remove_same_structure
##    strc_perm = list(set(''.join(p) for p in permutations(strc_list)))
##    strc_no_rep = remove_same_structure(strc_perm)
##    for i in range(len(strc_no_rep)):
##        strc_no_rep[i] = make_list(strc_no_rep[i])
##    print(strc_no_rep)

    #all possibility of H
    from subset_sum import print_all_sum
    H_lst = print_all_sum(H_atom)
    
    from check_H import check_H
    H_lst = check_H(H_lst, strc_list)
    
    for i in range(len(H_lst)):
        for j in range(len(H_lst[i])):
            if H_lst[i][j] == 1:
                H_lst[i][j] = 'H'
            else:
                H_lst[i][j] = 'H' + str(H_lst[i][j])
    #print(H_lst)
    
    #def strcture
    from itertools import permutations
    file = open(formula+'_all.txt', 'w')
    for i in range(len(H_lst)):
        strcture_guess = list(set(''.join(p) for p in permutations(strc_list + H_lst[i])))
        for n in strcture_guess:
            file.write(n)
            file.write('\n')
    
    file.close()
    file = open(formula+'_all.txt', 'r')
    file_2 = open(formula+'.txt', 'w')
    for line in file:
        strc_guess = str(line.strip())
        if strc_guess[0] == 'C' and  strc_guess[1] != 'O' and not strc_guess[1].islower() and 'HH' not in strc_guess and 'HH2' not in strc_guess and 'HH3' not in strc_guess and \
        'H2H' not in strc_guess and 'H3H' not in strc_guess and 'ClH3' not in strc_guess and 'BrH3' not in strc_guess and\
        'BrH2' not in strc_guess and 'ClH2'not in strc_guess and 'HOH' not in strc_guess and 'OH3' not in strc_guess and 'OH2' not in strc_guess and\
        'ClH' not in strc_guess and 'BrH' not in strc_guess and 'H3OO' not in strc_guess and 'H2OO' not in strc_guess and 'OHO' not in strc_guess and\
        'HOC' not in strc_guess and 'OHC' not in strc_guess and 'HOO' not in strc_guess and 'OCHO' not in strc_guess and 'OCOH' not in strc_guess:
            
            file_2.write(strc_guess)
            file_2.write('\n')

    file.close
    file_2.close
    
    
                        
    

##def main():
##    formula_to_structure('C2H4O2')
##    print('\n')
##    formula_to_structure('C2H5Cl')
##    print('\n')
##    formula_to_structure('C2H6O')
##    print('\n')
##    formula_to_structure('C2H6')
##    print('\n')
##    formula_to_structure('C3H6O2')
##main()
##
##    
    
 
        
    
