class BracketValidator:
    def __init__(self, s: str):
        
        self.s = s

    def is_valid(self) -> bool:
        
        stack = []
        
        # Dictionary 
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in self.s:

            if char in bracket_map:

                
                top_element = stack.pop() if stack else '#'
                
                
                if bracket_map[char] != top_element:
                    return False
            else:
                
                stack.append(char)
        
        # After processing all characters, the stack should be empty if the string is valid
        return not stack


validator = BracketValidator("()[]{}")
print(validator.is_valid())  # Output: True

validator = BracketValidator("([)]")
print(validator.is_valid())  # Output: False
