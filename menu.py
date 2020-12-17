from reaction import guess_reaction
from formula_to_structure import formula_to_structure
from structure_to_formula import structure_to_formula
def main():
    print('Welcome to Organic chemistry')
    choice = '0'
    while choice != '4':
        #check input of option
        choice = 'a'
        while not choice.isdigit()or int(choice) > 4 or int(choice) < 1:
            try:
                choice = input('Please select one of the options: \n'
                               '1. Convert formula to structure \n'
                               '2. Convert structure to formula \n'
                               '3. What reaction can happen? \n'
                               '4. I do not need help now.'
                               '\n')
                if not choice.isdigit():
                    raise TypeError('Please enter an integer number\n')
                if int(choice) > 4 or int(choice) < 1:
                    raise ValueError('Please enter number 1-4 only\n')
            except TypeError as ex:
                print(ex)
            except ValueError as ex:
                print(ex)
                
        #menu part
        if choice == '1':
            formula = input('Please enter the formula(eg.C2H6): ')
            formula_to_structure(formula)
            file = open(formula+'.txt', 'r')
            print('Here is the most possible structure: ')
            for line in file:
                print(line.strip())
        elif choice == '2':
            structure = input('Please enter the structure(eg. CH3CH3): ')
            print('Here is the formula dictionary: ')
            print(structure_to_formula(structure))
        elif choice == '3':
            structure = input('Please enter the structure(eg. CH3CH3): ')
            print('Here are the reactions may happen: ')
            print(guess_reaction(structure))
        elif choice == '4':
            break
        
        #check if want to call the menu again
        check = 0
        while check != 'Yes' and check != 'No':
            try:
                check = input('Is there more that you would like to do? (Yes/No)\n')
                if check != 'Yes' and check != 'No':
                    raise ValueError(' Please answer Yes or No, Thank you!\n')
            except ValueError as ex:
                print(ex)
        if check == 'Yes':
            choice = 'a'
        elif check == 'No':
            choice = '4'

            
    print('Thank you!')
            
    
main()
