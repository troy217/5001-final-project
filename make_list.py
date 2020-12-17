def make_list(strc_str):
    element = []
    for i in range(len(strc_str)-1):
        if strc_str[i].isupper() and strc_str[i+1].islower():
            element.append(strc_str[i]+strc_str[i+1])
        elif strc_str[i].isupper():
            element.append(strc_str[i])
    if strc_str[len(strc_str)-1].isupper():
        element.append(strc_str[len(strc_str)-1])
    
    return element
