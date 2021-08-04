def syntax_analyze(action_table, token, stack):
    while True:
        stack_top = stack[-1]
        if stack_top == token[-1]:
            if stack_top == '$':
                return
            else:
                stack_top.pop()
                token.pop()
        if None != action_table[stack_top, token[-1]]:
            new_top = action_table[stack_top, token[-1]]
            stack.pop()
            stack.append(new_top)
        else:
            print("syntax error")
