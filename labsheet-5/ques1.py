# Lab Sheet 5 - Both Programs Combined in One File

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


# --- PART 1: Infix to Postfix Conversion ---[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span)
def precedence(operator):
    if operator == '^':
        return 3
    elif operator in ('*', '/'):
        return 2
    elif operator in ('+', '-'):
        return 1
    return 0

def infix_to_postfix(infix):
    stack = Stack()
    postfix = ""
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty() and stack.peek() != '(' and precedence(stack.peek()) >= precedence(ch)):
                postfix += stack.pop()
            stack.push(ch)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix


# --- PART 2: Postfix Expression Evaluation ---[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)
def evaluate_postfix(postfix):
    stack = Stack()
    for ch in postfix:
        if ch.isdigit():
            stack.push(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if ch == '+':
                result = operand1 + operand2
            elif ch == '-':
                result = operand1 - operand2
            elif ch == '*':
                result = operand1 * operand2
            elif ch == '/':
                result = operand1 // operand2
            stack.push(result)
    return stack.pop()


# --- Execution Section ---
if __name__ == "__main__":
    print("=== PROGRAM 1: Infix to Postfix ===")
    infix_expr = input("Enter infix expression: ")
    postfix_result = infix_to_postfix(infix_expr)
    print("Postfix expression:", postfix_result)

    print("\n=== PROGRAM 2: Postfix Evaluation ===")
    eval_expr = input("Enter postfix expression (digits only): ")
    final_ans = evaluate_postfix(eval_expr)
    print("Final result:", final_ans)