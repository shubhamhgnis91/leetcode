class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        operators = {"+","-","*","/"}

        for token in tokens:
            if token not in operators:

                if token[0] == "-":
                    num = int(token.lstrip('-')) * (-1)

                else:
                    num = int(token)  

                stack.append(num)                
                    

            else:
                operand1 = stack.pop()
                operand2 = stack.pop()

                if token == "+" :
                    stack.append(operand2 + operand1)
                    
                elif token == "-":
                    stack.append(operand2 - operand1)

                elif token == "*":
                    stack.append(operand2 * operand1)

                else:
                    if operand2 * operand1 < 0 and operand2 % operand1 != 0:
                        stack.append(operand2 // operand1 + 1)
                    
                    else:
                        stack.append(operand2 // operand1)
        
        return stack[0]
