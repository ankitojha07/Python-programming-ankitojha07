def pop(stack):
    s=0
    if len(stack)==0:
        print("Empty Stack")
    
    else:
        s = stack.pop()
    return s

def push(stack,e):
    stack.append(e)

def top(stack):
    if not stack:
        print('Empty stack')
    else :
        print(stack[-1])

stack = []

push(stack, 3)
push(stack, 4)
push(stack, 6)
push(stack, 9)
push(stack, 6)
print(stack)
print(pop(stack))

print(top(stack))