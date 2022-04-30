def show_fibonacci_number():
    try:
        value = 0
        is_not_right_answer = True
        while(is_not_right_answer):
            try:
                value = input("Enter position of the fibonacci sequence number\n")
            except EOFError:
                print("Error with input. Maybe, you didn't connect program to console")
                return
            try:
                value = int(value)
                if(value <= 0):
                    raise ValueError()
            except ValueError:
                print("Please, input natural number")
            else:
                is_not_right_answer = False
        print(f"Required number is {fibonacci_bine(value)}")
    except OverflowError as e:
        print("You input very big position. We can't calculate this number.")
    except BaseException as e:
        print(f"Something is wrong. {e}")
      
def fibonacci_bine(n=0):
    FI = (1 + 5**(0.5)) / 2
    num = ((FI**n) - (1 / ((-FI)**n))) / (2*FI - 1)
    return round(num)

def main():
    show_fibonacci_number()

if __name__ == "__main__":
    main()