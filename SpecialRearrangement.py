
# A Python function that takes a list of integers as a parameter and rearranges it so that even numbers
# in this list are before odd numbers

def special_rearrangement(numbers):
    rearranged_list = []
    for i in range(len(numbers)):
        if((numbers[i] % 2) == 0):
            rearranged_list.append(numbers[i])
            
    for i in range(len(numbers)):
        if((numbers[i] % 2) != 0):
            rearranged_list.append(numbers[i])    

    numbers = rearranged_list        
    return numbers
