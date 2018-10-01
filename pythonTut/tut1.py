def max_of_min(num1, num2, num3, num4):
    return max(min(num1, num2), min(num3, num4))

def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    
    penguin.append("property of the zoo")
    
    return penguin

def ask_ok(prompt, retries = 4, reminder='Please try again!'):
    while True:
        ok = input(prompt)

        if ok in ('y', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        
        retries = retries - 1

        print(reminder)

def get_input():
    x = int(input("Please enter an integer: "))

    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

if __name__ == '__main__':

    a = 1
    b = 2
    c = 3
    d = 4

    max_min = max_of_min(a, b, c, d)

    str1 = whats_on_the_telly()
    print(str1)
    print('max is %f' % (max_min))

    range(5, 6)
    range(5)

    get_input()

    for i in range(10):
        print('Number is %d' % (i))

    a = ['Mary', 'Had', 'a', 'little', 'lamb']

    for i in range(len(a)):
        print(i, a[i])