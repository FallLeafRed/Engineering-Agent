```python
import re
from math import gcd

def calculator(expression):
    try:
        expression = re.sub('[\s+]', '', expression)
        expression = ['+' if char == '+' or char == '-' else 'x'*int(char) if char.isdigit() else '/' if char == '/' else '*' for i, char in enumerate(expression) if char != None]
        result = eval(''.join(map(str,expression)))
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except NameError:
        return "Invalid input. Please provide a valid expression like '2 + 3' or '10 / 5'."
    except ValueError as e:
        return f"Error in calculation: {str(e)}"
    
    def lcm(a, b):
        if a == 0:
            return 1
        c = gcd (a , b)
        while a != c:
            a -= c
        while b != c:
            b-=c 
        return abs(a* b) //abs(c)

    if '+' in expression or '-' in expression or '*' in expression:
        return "This expression is to be done in order of priority"
    try:
        return f"Multiplication and Division result is {result[0]} and addition and subtraction result is {expression.index('/')>0 and ''.join(result[result.index('/'):]) and ''}. Final LCM number  :{lcm(int(''.join(c for c in expression if c.lstrip('-').isdigit())),int(''.join(c for c in expression if 'x'==c)))*int(''.join(c for c in expression if c.lstrip('-').isdigit()))}"
    except ZeroDivisionError:
        return "This expression will give division by zero error"
    except IndexError:
        return "The problem is too big with more than one input"

def main():
  while(1):
      user_input = input("Enter an expression (or 'exit' to quit): ")
      if user_input.lower() == 'exit':
          break
      try:
          print(calculator(user_input))
      except Exception as e:
          print(str(e))

if __name__ == "__main__":
  main()

```