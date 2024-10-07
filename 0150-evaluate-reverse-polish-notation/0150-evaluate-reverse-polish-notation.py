class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cur = 0
        stack = []

        def arth(num1, num2, symbol):
            if symbol == "+":
                return num1 + num2
            elif symbol == "*":
                return num1 * num2
            elif symbol == "/":
                return int(num2 / num1)
            else:
                return num2 - num1

        for token in tokens:
            if not token in ['+', '*', '/', '-'] :
                stack.append(int(token))
            else:
                cur = arth(stack.pop(), stack.pop(), token)
                stack.append(cur)
        
        return stack[0]
            
                    
                

