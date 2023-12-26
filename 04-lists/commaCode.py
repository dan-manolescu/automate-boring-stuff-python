# Comma code

def comma_code(inputList):
    '''
    Takes a list of values as <inputList> and
    returns a string containing all values in the input list
    separated by comma and a space, with and inserted
    before the last item.
    '''
    inputListLength = len(inputList)

    if inputListLength == 0:
        return ''
    elif inputListLength == 1:
        return str(inputList[0])
    else:
        return ', '.join([str(item) for item in inputList[:-1]]) + ' and ' + str(inputList[-1])

# Main program loop
while True:
    print('Please input a list of values separated by space: (press CTRL+C to terminate)')
    inputList = input().split()
    print('Result of comma code is: ' + comma_code(inputList))
    print()
