def arithmetic_arranger(*problems):
    if (problems[1] != True):
        val = problems[0][0]
        return eval(val)
        # return (f'{val[0]}\n {val[1]} \t{val[2]}\n{"----"}')
    # else :
       
    
    


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))