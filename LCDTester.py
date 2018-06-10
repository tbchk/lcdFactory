from LCDFactory import *


def isInteger(number):
    """Method to see if some string is an integer. """

    try:
        int(number)
        return True
    except ValueError:
        return False

def validateSpacing(input_spacing):
    """Method for validating user spacing input."""

    if not isInteger(input_spacing):
        print('Error: %s No es un entero. ' % (input_spacing), type(input_spacing))
        exit(1)

    spacing_number = int(input_spacing)

    if spacing_number <0 or spacing_number>5:
        print('Error: El espacio entre digitos debe estar entre 0 y 5')
        exit(1)

    return spacing_number

def validateSequence(sequence):
    """Method for validating user sequences input."""

    arguments = []
    orders = sequence.split(' ')
    for order in orders:
        # Validation exit filter
        if order == '0,0':
            arguments.append(None) # Termination Character
            return arguments

        cmd = order.split(',')

        # Filters for the commands
        if len(cmd) != 2: continue
        if not isInteger(cmd[0]) or not isInteger(cmd[1]): continue

        # Control to the size limit (1-10)
        size = int(cmd[0])
        if size<1 or size>10: continue 
        arguments.append((size, cmd[1]))
    
    return arguments

        

if __name__ == '__main__':

    spacing = input('Espacio entre Digitos (0 a 5): ')
    spacing_number = validateSpacing(spacing)

    #(sequence, size) Tuples
    total_orders = []

    # Infinite input loop
    while True:
        sequence = input('Entrada: ')
        orders = validateSequence(sequence)
        total_orders += orders

        if len(total_orders) == 0: continue
        
        # 0,0 command entered
        if total_orders[-1] is None:
            total_orders.pop()
            break

    f = LCDFactory(spacing_number)

    # Printing correctly formatted orders
    for size, sequence in total_orders:
        f.printSequence(sequence, size)
        

    
        


