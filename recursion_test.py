import math

def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result


# تست تابع با ورودی 3
# a= int(input("enter a"))
# print(generate_parentheses(a))
def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result, len(result)

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        a = int(user_input)
        parentheses, count = generate_parentheses(a)
        print(f"Generated parentheses: {parentheses}")
        print(f"Number of combinations: {count}")
    except ValueError:
        print("Please enter a valid number.")
