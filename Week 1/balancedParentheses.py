def longest_balanced(string):
    counter = 0
    trap_counter = 0
    p_list = []
    length_tracker = []
    for char in string:
        if char == '(' and counter != 0:
            if len(p_list) == 0:
                length_tracker.append(counter)
                counter = 0
            else:
                trap_counter += 2
            p_list.append(char)
        elif char == '(':
            p_list.append(char)
            if counter == 0 and char is string[-1]:
                length_tracker.append(counter)
        elif char == ')':
            if counter == 0 and char is string[-1] and len(p_list) == 0:
                length_tracker.append(counter)
            elif len(p_list) == 0:
                continue
            else:
                p_list.pop()
                counter += 2
    length_tracker.append(counter)
    if len(p_list) != 0:
        for i in range(len(length_tracker)):
            length_tracker[i] -= trap_counter
    return max(length_tracker)