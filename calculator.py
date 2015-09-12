#input = "5 - 2"
#array = input.split(" ")
#left_number = int(array[0])
#right_number = int(array[-1])
#sign = array[1]


def calculate(left_number, sign, right_number):
    if sign == "+":
        result = left_number + right_number

    elif sign == "/":
        result = left_number / right_number
    elif sign == "-":
        result = left_number - right_number
    else:
        result = left_number * right_number

    return result



while True:
    number=int(raw_input("Enter a number"))
    num=int(raw_input("Enter a second number"))
    sig=raw_input("Enter the sign")
    print calculate(number,sig,num)
