import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

dict_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    first_number = int(input("Enter the first number: "))
    should_accumulate = True

    while should_accumulate:
        operation = input("Enter the choice of mathematical operator ('+', '-', '*', '/'): ")
        second_number = int(input("Enter the second number: "))
        result = dict_operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        continue_with_previous = input("Do you want to continue with previous result? yes or no: ").lower()
        if continue_with_previous == "yes":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            print(art.logo)
            calculator()
calculator()