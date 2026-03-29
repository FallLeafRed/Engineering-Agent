```python
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed'
    except SyntaxError:
        return 'Invalid input format. Please use numbers and basic arithmetic operators (+, -, *, /)'
    except NameError:
        return 'Invalid number format'

def main():
    while True:
        expression = input('Enter an expression (or "quit" to exit): ')
        if expression.lower() == 'quit':
            break
        result = calculate(expression)
        print(f'Expression: {expression} -> Result: {result}')

if __name__ == '__main__':
    main()
```