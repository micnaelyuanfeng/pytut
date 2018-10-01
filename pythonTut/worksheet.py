import math

#worksheet 1 = Function Definition
#worksheet 2 = Function Design Recipe


#To DO
#String manipulation
#Round Power function

def double(num : float) -> float:

    return float(2 * num)

def percentage(num : int, out_of : int) -> int:

    return round(int((num/out_of) * 100))

def max_of_min(num1 : float, num2 : float, value1 : float, value2 : float ) -> float:

    return max(min(num1, num2), min(value1, value2))

def repeat_words(word: str) -> str:
    word = word + ' ' + word
    return word

def num_of_cents(change: float) -> int:
    dollor = int(change)
    float_part = change - float(dollor)

    return round(float_part * 100)

def calculate_tax(bill: float, rate: float) -> float:

    return bill + bill * rate

def format_name(first_name: str, second_name: str) -> str:
    return second_name + ',' + first_name

def to_listting(first_name: str, second_name: str, phone_number: str) ->str:
    
    temp = format_name(first_name, second_name)

    return temp + ': ' + phone_number

#string start at index = 0
#[start_index:end_index] end_index wil not be shown
def str_operation(str_input: str) -> str:
    slice1 = str_input[0:3]
    slice2 = str_input[-4:]
    slice3 = str_input[3:8]
    slice4 = str_input[::2]
    slice5 = str_input[::-1]
    slice6 = str_input[::-2]

    print(slice1)
    print(slice2)
    print(slice3)
    print(slice4)
    print(slice5)
    print(slice6)

def same_abs(num1: float, num2: float) -> bool:
    return abs(num1) == abs(num2)

#Bool type = True, False, Not
#object type is most basic type in python and can accept any type of var and class_var if you
#specify the type of input
def different_type(obj1: object, obj2: object) -> bool:
    return type(obj1) == type(obj2)

def is_right_triangle(side1: int, side2: int, side3: int) -> bool:
    return (pow(side1, 2) + pow(side2, 2) == pow(side3, 2))

def can_vote(age: int) -> bool:
    if(age >= 18):
        return True
    else:
        return False

def is_tennager(age: int) -> bool:
    if(age >= 13 & age <= 18):
        return True
    else:
        return False

def earlier_name(name1: str, name2: str) -> str:
    initial_name1 = name1[0:1]
    initial_name2 = name2[0:1]

    if(initial_name1 > initial_name2):
        print(initial_name1)
        print(initial_name2)
        return name2
    else:
        return name1

if __name__ == '__main__':
    print(double(7.0))
    print(double(5.7))

    print(percentage(10, 200))
    print(percentage(151, 300))

    print(max_of_min(4.0, 3.7, 6.0, 3.5))

    print(repeat_words('a'))

    print(num_of_cents(1.25))

    print(str_operation('big orange cat'))
    print(str_operation('Jacqueline'))

    print(is_right_triangle(3, 4, 5))
    print(is_tennager(17))

    print(earlier_name('Kaveh', "Anya"))