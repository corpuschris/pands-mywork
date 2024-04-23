#This program takes a positive floating-point number as input and outputs an approximation of its square root.

#Author: Christiano Ferreira





def sqrt(x):
    if x < 0:
        return "Error: Negative number"
    guess = x / 2.0
    while True:
        better_guess = (guess + x / guess) / 2
        if abs(better_guess - guess) < 1e-10:
            return better_guess
        guess = better_guess

def main():
    num = float(input("Please enter a positive number: "))
    if num < 0:
        print("Error: Negative number")
    else:
        approx_sqrt = sqrt(num)
        print(f"The square root of {num} is approx. {approx_sqrt:.1f}.")

if __name__ == "__main__":
    main()