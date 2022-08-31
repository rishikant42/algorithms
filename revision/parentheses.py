# Question: Give an unbalanced parentheses string, and write a program to find a
# string that can append to make it a balanced parentheses string. If there is
# no such string, return -1.

def solution(input_str):
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []

    for i in input_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if not stack:
                return -1
            pop_item = stack.pop()
            expected_char = bracket_map[pop_item]
            if i != expected_char:
                return -1

    if not stack:
        print("balance")
    rev_stack = stack[::-1]
    output = ""
    for i in rev_stack:
        output += bracket_map[i]

    return output


input_str = "[](([]{[{()}][]}"
print(solution(input_str))
