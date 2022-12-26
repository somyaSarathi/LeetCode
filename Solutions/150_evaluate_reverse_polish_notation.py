class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {
            '+': lambda a, b: int(a)+int(b),
            '-': lambda a, b: int(a)-int(b),
            '*': lambda a, b: int(a)*int(b),
            '/': lambda a, b: int(a)/int(b)
        }

        i = 0
        while i < len(tokens):
            if tokens[i] in operators:
                tokens[i-2] = operators[tokens[i]](tokens[i-2], tokens[i-1])

                i -= 2

                tokens.pop(i+1)
                tokens.pop(i+1)

            i += 1

        return int(tokens[0])
