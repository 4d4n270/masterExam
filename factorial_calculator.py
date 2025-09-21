#!/usr/bin/env python3
"""
Factorial Calculator Program

This program accepts a number from the user and calculates its factorial.
Factorial of n (written as n!) is the product of all positive integers 
from 1 to n.

Examples:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1 (by mathematical definition)
- 1! = 1

Author: Educational Programming Example
Purpose: Demonstrate loops, input validation, and mathematical calculations
"""

def get_number_input():
    """
    Function to get a valid non-negative integer from user input.
    
    Returns:
        int: Valid non-negative integer for factorial calculation
        
    Raises:
        None (handles errors internally with retry mechanism)
    """
    while True:
        try:
            # Get input from user
            number_input = input("Enter a non-negative integer: ")
            
            # Convert string input to integer
            number = int(number_input)
            
            # Validate that number is non-negative
            # Factorial is only defined for non-negative integers
            if number < 0:
                print("❌ Error: Factorial is not defined for negative numbers.")
                print("   Please enter a non-negative integer (0, 1, 2, 3, ...).\n")
                continue
            
            # Check for very large numbers to prevent long computation times
            if number > 1000:
                print("⚠️  Warning: Computing factorial of very large numbers")
                print("   might take a long time and result in huge numbers.")
                
                while True:
                    confirm = input("   Do you want to continue? (y/n): ").lower().strip()
                    if confirm in ['y', 'yes']:
                        return number
                    elif confirm in ['n', 'no']:
                        print("   Returning to number input...\n")
                        break
                    else:
                        print("   Please enter 'y' for yes or 'n' for no.")
                continue
            
            # If we reach here, input is valid
            return number
            
        except ValueError:
            # This handles cases where input cannot be converted to integer
            print("❌ Error: Please enter a valid integer.")
            print("   Examples: 5, 10, 0, 25\n")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n👋 Program terminated by user. Goodbye!")
            exit(0)


def calculate_factorial_iterative(n):
    """
    Function to calculate factorial using iterative method.
    
    This method uses a loop to multiply numbers from 1 to n.
    It's more memory-efficient than recursive method for large numbers.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    # Initialize result to 1 (multiplicative identity)
    # This also handles the case when n = 0 (0! = 1)
    factorial = 1
    
    # Loop from 1 to n (inclusive) and multiply each number
    for i in range(1, n + 1):
        factorial = factorial * i
        # Alternative shorter syntax: factorial *= i
    
    return factorial


def calculate_factorial_recursive(n):
    """
    Function to calculate factorial using recursive method.
    
    This method calls itself with smaller values until reaching base case.
    Note: This is for educational purposes - iterative method is preferred
    for large numbers due to recursion depth limits in Python.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    # Base cases
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n × (n-1)!
        return n * calculate_factorial_recursive(n - 1)


def display_calculation_steps(n, method="iterative"):
    """
    Function to display the step-by-step calculation process.
    
    Args:
        n (int): Number for which factorial is calculated
        method (str): Calculation method used
    """
    print(f"\n📝 Step-by-step calculation of {n}! using {method} method:")
    print("-" * 60)
    
    if n == 0:
        print("0! = 1 (by mathematical definition)")
    elif n == 1:
        print("1! = 1")
    else:
        # Show the multiplication sequence
        sequence = " × ".join(str(i) for i in range(n, 0, -1))
        print(f"{n}! = {sequence}")
        
        # Show intermediate calculations for small numbers
        if n <= 10:
            result = 1
            calculation_steps = []
            for i in range(1, n + 1):
                result *= i
                calculation_steps.append(f"Step {i}: {' × '.join(str(j) for j in range(1, i + 1))} = {result}")
            
            print("\nIntermediate steps:")
            for step in calculation_steps:
                print(f"  {step}")


def format_large_number(number):
    """
    Function to format large numbers with thousand separators for readability.
    
    Args:
        number (int): Number to format
        
    Returns:
        str: Formatted number string
    """
    return f"{number:,}"


def display_result(n, factorial):
    """
    Function to display the final result in a formatted manner.
    
    Args:
        n (int): Original number
        factorial (int): Calculated factorial
    """
    print("\n" + "="*60)
    print("               🧮 FACTORIAL CALCULATION RESULT")
    print("="*60)
    print(f"Number (n):        {n}")
    print(f"Factorial (n!):    {format_large_number(factorial)}")
    
    # Add some interesting facts for small numbers
    if n <= 20:
        digit_count = len(str(factorial))
        print(f"Number of digits:  {digit_count}")
        
        # Show some factorial facts
        if n == 10:
            print("💡 Fun fact: 10! = 3,628,800 (number of ways to arrange 10 people)")
        elif n == 13:
            print("💡 Fun fact: 13! is the largest factorial that fits in 32-bit integer")
        elif n == 20:
            print("💡 Fun fact: 20! = 2,432,902,008,176,640,000")
    
    print("="*60)


def display_factorial_info():
    """
    Function to display educational information about factorials.
    """
    print("\n" + "="*60)
    print("                  📚 ABOUT FACTORIALS")
    print("="*60)
    print("• Factorial (n!) is the product of all positive integers from 1 to n")
    print("• Special cases: 0! = 1, 1! = 1")
    print("• Used in: permutations, combinations, probability, calculus")
    print("• Examples:")
    print("  - 3! = 3 × 2 × 1 = 6")
    print("  - 4! = 4 × 3 × 2 × 1 = 24")
    print("  - 5! = 5 × 4 × 3 × 2 × 1 = 120")
    print("="*60)


def main():
    """
    Main function that orchestrates the factorial calculation process.
    """
    # Display welcome message and program information
    print("🧮 FACTORIAL CALCULATOR")
    print("="*60)
    print("This program calculates the factorial of a non-negative integer.")
    print("Factorial of n (n!) = n × (n-1) × (n-2) × ... × 2 × 1")
    
    # Display educational information about factorials
    display_factorial_info()
    
    # Main program loop - allows multiple calculations
    while True:
        try:
            print("\n" + "-"*60)
            
            # Step 1: Get valid number from user
            number = get_number_input()
            
            # Step 2: Calculate factorial using iterative method
            # (We use iterative for better performance and to avoid recursion limits)
            factorial_result = calculate_factorial_iterative(number)
            
            # Step 3: Display calculation steps (educational purpose)
            display_calculation_steps(number, "iterative")
            
            # Step 4: Display the result in a formatted manner
            display_result(number, factorial_result)
            
            # Optional: Show comparison with recursive method for small numbers
            if number <= 10:
                print(f"\n🔄 Verification using recursive method: {calculate_factorial_recursive(number)}")
                print("   (Both methods produce the same result)")
            
            # Step 5: Ask if user wants to calculate another factorial
            print("\nWould you like to calculate another factorial?")
            
            while True:
                choice = input("Enter 'y' for yes or 'n' for no: ").lower().strip()
                
                if choice in ['y', 'yes']:
                    break  # Continue to next iteration
                elif choice in ['n', 'no']:
                    print("\n👋 Thank you for using the Factorial Calculator!")
                    print("   Mathematics is fun! Keep exploring! 🔢✨")
                    return  # Exit the program
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully in main loop
            print("\n\n👋 Program terminated by user. Goodbye!")
            return
        except Exception as e:
            # Handle any unexpected errors
            print(f"\n❌ An unexpected error occurred: {e}")
            print("   Please try again or contact support if the problem persists.")


# Program entry point
if __name__ == "__main__":
    # This block ensures the main() function only runs when the script
    # is executed directly, not when imported as a module
    main()