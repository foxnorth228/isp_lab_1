FI = (1 + 5**(0.5)) / 2

def call_the_function():
    value = 0
    is_not_right_answer = True
    while(is_not_right_answer):
        value = input("Enter position of the fibonacci sequence number\n")
        try:
            value = int(value)
            if(value <= 0):
                raise ValueError()
        except ValueError:
            print("Please, input natural number")
        else:
            is_not_right_answer = False
    print(f"Required number is {fibonacci_bine(value)}")


def fibonacci_bine(n=0):
    num = ((FI**n) - (1 / ((-FI)**n))) / (2*FI - 1)
    return round(num)

def main():
    call_the_function()

if __name__ == "__main__":
    main()