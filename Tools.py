def smart_calculator(expression):
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    expr = input("Enter math expression: ")
    print(smart_calculator(expr))
