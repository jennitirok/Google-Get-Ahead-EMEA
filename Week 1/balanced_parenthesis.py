def longest_balanced(string):
    counter = 0
    trap_counter = 0
    p_list = []
    length_tracker = []

    for char in string:
        if char == '(' and counter != 0:
            # Check if a '(' is encountered directly after a ')'
            if len(p_list) == 0:
                length_tracker.append(counter)
                counter = 0
            else:
                trap_counter += 2
            p_list.append(char)
        elif char == '(':
            p_list.append(char)
            # Check if it is the last parenthesis in the string
            if counter == 0 and char is string[-1]:
                length_tracker.append(counter)
        elif char == ')':
            if counter == 0 and char is string[-1] and len(p_list) == 0:
                length_tracker.append(counter)
            # Check if a ')' is encountered without any prior '(' encountered
            elif len(p_list) == 0:
                continue
            else:
                p_list.pop()
                counter += 2

    length_tracker.append(counter)
    # Subtract misleading set of parenthesis from each length
    if len(p_list) != 0:
        for i in range(len(length_tracker)):
            length_tracker[i] -= trap_counter
            
    return max(length_tracker)