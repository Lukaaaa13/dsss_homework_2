import math
import random


def make_random_number(min, max):
    """
    Returns a random integer bigger than min and smaller than max.
    
    Args:
        min (int): minimal value
        max (int): maximal value
        
    Returns:
        int: a random integer bigger than min and smaller than max
    """
    
    # input numbers are converted to int for the random function to work
    
    try:
        return random.randint(min, max)
    except:
        min = int(min)
        max = int(max)
        return random.randint(min, max)


def choose_math_symbol():
    """
    Chooses the plus, minus or astrix symbol randomly and returns it

    Returns:
        str: randomly a '+', '-' or '*'
        """
    return random.choice(['+', '-', '*'])


def generate_problem_and_solution(number1, number2, math_symbol):
    """
        creates a string representation of a math problem and calculates its solution

        Args:
            number1 (int): a number
            number2 (int): another number
            math_symbol (str): one of the following: '+', '-' or '*'

        Returns:
            str: string representation of a math problem
            int: solution of math problem
        """
    # raises a typeerror if the input numbers aren't integers
    if type(number1) is not int or type(number2) is not int:
        raise TypeError("the input numbers have to be integers!")
    
    # calculating the solution based on the chosen math symbol
    if math_symbol == '+':
        solution = number1 + number2
    elif math_symbol == '-':
        solution = number1 - number2
    elif math_symbol == '*':
        solution = number1 * number2
    else:
        
        # setting asterisk as math symbol in case of an invalid input
        print('Your math symbol is not valid. We will replace it with "*".')
        solution = number1 * number2
        math_symbol = '*'
    
    # creating a string representation of the math problem
    math_problem = f"{number1} {math_symbol} {number2}"
    
    return math_problem, solution


def math_quiz():
    # counter for earned points
    points = 0
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    # creating three game rounds of math problems
    for _ in range(3):
        
        # creating random numbers and the math symbol
        number1 = make_random_number(1, 10)
        number2 = make_random_number(1, 5.5)
        math_symbol = choose_math_symbol()
        
        # creating the math problem and calculating its solution
        string_representation, solution = generate_problem_and_solution(number1, number2, math_symbol)
        
        # tell the user the math problem and fetch their answer
        print(f"\nQuestion: {string_representation}")
        user_answer = input("Your answer: ")
        
        # try converting the user input to int
        try:
            user_answer = int(user_answer)
        except:
            # if the conversion doesn't work, the user gets a second chance for their answer before the game ends
            try:
                print("Try again! Tip: the solution is a number.")
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
            except:
                print("womp womp womp, you failed to make a sensible input :(")
                break
        
        # checking whether the user's solution is correct and give a point if positive
        if user_answer == solution:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.")
    
    # sowing the users achieved points (as a fraction of pi because why not)
    print(f"\nGame over! Your score is: {points}/{math.pi}")


if __name__ == "__main__":
    math_quiz()
