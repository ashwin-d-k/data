# This program takes in a list of mathematical operations and formats them in a clear pictorial view for ease
# of calculation purpose

def arithmetic_arranger(problems, sol = False) :
    """
    This function takes in a list of strings representing mathematical
    operations. Take no more than five list elements in the list. A second argument in the function call
    is used to indicate whether to perform the mathematical operation or not
    """
    if len(problems) > 5 : # Check for number of elements in the input list
        return "Error: Too many problems"
    
    # Initialize the strings that need to be displayed
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''

    for i, problem in enumerate(problems): # Extract the string elements within list in form of tuple
        num_1, op, num_2 = problem.split()
        l1, l2 = len(num_1), len(num_2)
    
        # Check for the legality of operator
        if op not in ['+', '-'] :
            return "Error: Operator should be '+' or '-'"
    
        # Check whether strings consist of numbers or not
        if not(num_1.isdigit() and num_2.isdigit()):
            return "Error: List strings should contain only natural numbers"

        # Check for the number of digits in the number
        if l1 > 4 and l2 > 4:
            return "Error: Numbers must not exceed three digits"
    
        space = max(l1, l2) # Define the space width
        result = int(num_1) + int(num_2) if op == '+' else int(num_1) - int(num_2) # Perform operation

        line_1 = line_1 + num_1.rjust(space + 2) # First line displays first number
        line_2 = line_2 + op + num_2.rjust(space + 1) # Second line displays operand and second number
        line_3 = line_3 + ''.rjust(space + 2, '-')  # Third line has dashes
        line_4 = line_4 + str(result).rjust(space + 2) # Fourth line has the solution

        if i < len(problems) -1:
            line_1 += '     '
            line_2 += '     '
            line_3 += '     '
            line_4 += '     '
        
    if sol == True:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4
    else:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3  
    return arranged_problems


