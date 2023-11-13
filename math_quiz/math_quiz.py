import random


def create_random_int(min, max):
    """
    returns a random integer between a min and max value which are user defined
    
    Args:
    min (integer): random minimum value
    max (integer): random maximum value
    
    Returns:
    
    integer: returns a random integer number from our function random.ranint(min,max)
    """
    try:
        return random.randint(min, max)
    except ValueError:
        print("please enter an integer value to create a random integer value")


def create_random_math_operation():
    """
    returns a random mathematical operation
    
    Args:
    None
    
    Returns:
    
    string: returns a mathematical operation
    """
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o):
    """
    3 mathematical operations are accepted (+, -, *) for calculation.
    
    Args: 
    n1 (integer): first input number 
    n2 (integer): second input number
    o (string): mathematical operation
    
    Returns:
    string p the mathematical equation
    integer a the solution of the calculation
    """
    
    
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3 #3.14159265359 I changed the value (lazy way)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = create_random_int(1, 10); n2 = create_random_int(1, 5); o = create_random_math_operation()

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
