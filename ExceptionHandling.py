# try:
#     numerator=20
#     denominator=0
#     result=numerator/denominator
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# try:
#     user_input=input("enter a number:")
#     number=int(user_input)
#     print("Number entered:", number)
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")


#raising exception with try/except
# def check_number(number):
#     if number < 10:
#         raise ValueError("Number must be greater than or equal to 10.")
#     return number
# try:
#     number=int(input("Enter a number:"))
#     check_number(number)
# except ValueError as e:
#     print("Error:", e)



# def check_posnum(number):
#     if number <0:
#         raise ValueError("Number must be positive.")
#     print("number:",number)
#     return number
# check_posnum(-1)