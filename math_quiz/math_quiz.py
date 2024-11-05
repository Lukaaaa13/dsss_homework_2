import math
import random


def make_random_number(min, max):
    """
    Returns a random integer bigger than min and smaller than max.
    
    Args:
        min (any number format): minimal value
        max (any number format): maximal value
        
    Returns:
        int: a random integer bigger than min and smaller than max
    """
    min, max = int(min), int(max)
    
    return random.randint(min, max)


def choose_math_symbol():
    return random.choice(['+', '-', '*'])


def calculate_solution(number1, number2, math_symbol):
    string_representation = f"{number1} {math_symbol} {number2}"
    
    if math_symbol == '+':
        solution = number1 + number2
    elif math_symbol == '-':
        solution = number1 - number2
    else:
        solution = number1 * number2
    return string_representation, solution


def math_quiz():
    points = 0
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(int(math.pi)):
        number1 = make_random_number(1, 10)
        number2 = make_random_number(1, 5.5)
        math_symbol = choose_math_symbol()
        
        string_representation, solution = calculate_solution(number1, number2, math_symbol)
        print(f"\nQuestion: {string_representation}")
        user_answer = int(input("Your answer: "))
        
        if user_answer == solution:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.")
    
    print(f"\nGame over! Your score is: {points}/{math.pi}")


if __name__ == "__main__":
    math_quiz()
