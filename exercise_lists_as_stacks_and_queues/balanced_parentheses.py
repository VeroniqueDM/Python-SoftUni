expression = input()
parentheses_stack = []
balanced = True
for ch in expression:
    if ch in "({[":
        parentheses_stack.append(ch)
    elif not parentheses_stack:
        balanced = False
        break
    else:
        last_opening_bracket = parentheses_stack.pop()
        if f'{last_opening_bracket}{ch}' not in '(){}[]':
            balanced = False
            break
if balanced and not parentheses_stack:
    print('YES')
else:
    print('NO')