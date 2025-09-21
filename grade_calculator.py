#!/usr/bin/env python3
"""
Grade Calculator Program

This program accepts student marks (1-100) and displays grades according to:
- Grade F: marks < 50
- Grade E: 50-60
- Grade D: 61-70
- Grade C: 71-80
- Grade B: 81-90
- Grade A: 91-100

Author: Educational Programming Example
Purpose: Demonstrate input validation, conditional logic, and error handling
"""

def get_student_marks():
    """
    Function to get student marks from user input with validation.
    
    Returns:
        float: Valid marks between 1-100
        
    Raises:
        None (handles errors internally with retry mechanism)
    """
    while True:
        try:
            # Get input from user and attempt to convert to float
            marks_input = input("Enter student marks (1-100): ")
            
            # Convert string input to float to handle decimal marks
            marks = float(marks_input)
            
            # Validate that marks are within acceptable range
            if marks < 1 or marks > 100:
                print("❌ Error: Marks must be between 1 and 100.")
                print("   Please try again.\n")
                continue
                
            # If we reach here, input is valid
            return marks
            
        except ValueError:
            # This handles cases where input cannot be converted to float
            print("❌ Error: Please enter a valid number.")
            print("   Examples: 85, 72.5, 90\n")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n👋 Program terminated by user. Goodbye!")
            exit(0)


def calculate_grade(marks):
    """
    Function to calculate grade based on marks.
    
    Args:
        marks (float): Student marks between 1-100
        
    Returns:
        str: Grade letter (A, B, C, D, E, or F)
    """
    # Use if-elif-else structure to determine grade
    # Note: We check from highest to lowest for efficiency
    
    if marks >= 91:
        return 'A'
    elif marks >= 81:
        return 'B'
    elif marks >= 71:
        return 'C'
    elif marks >= 61:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'


def get_grade_description(grade):
    """
    Function to provide descriptive feedback for each grade.
    
    Args:
        grade (str): Grade letter
        
    Returns:
        str: Description of the grade performance
    """
    grade_descriptions = {
        'A': "Excellent! Outstanding performance! 🌟",
        'B': "Very Good! Well done! 👏",
        'C': "Good! Satisfactory performance! ✅",
        'D': "Average! Room for improvement! 📈",
        'E': "Below Average! Needs more effort! ⚠️",
        'F': "Fail! Significant improvement needed! 📚"
    }
    
    return grade_descriptions.get(grade, "Unknown grade")


def display_grade_chart():
    """
    Function to display the grading chart for reference.
    """
    print("\n" + "="*50)
    print("           📊 GRADING CHART REFERENCE")
    print("="*50)
    print("Grade A: 91-100 marks  (Excellent)")
    print("Grade B: 81-90 marks   (Very Good)")
    print("Grade C: 71-80 marks   (Good)")
    print("Grade D: 61-70 marks   (Average)")
    print("Grade E: 50-60 marks   (Below Average)")
    print("Grade F: 1-49 marks    (Fail)")
    print("="*50)


def display_result(marks, grade):
    """
    Function to display the final result in a formatted manner.
    
    Args:
        marks (float): Student marks
        grade (str): Calculated grade
    """
    print("\n" + "="*50)
    print("               📋 GRADE CALCULATION RESULT")
    print("="*50)
    print(f"Student Marks: {marks}")
    print(f"Letter Grade:  {grade}")
    print(f"Performance:   {get_grade_description(grade)}")
    print("="*50)


def main():
    """
    Main function that orchestrates the grade calculation process.
    """
    # Display welcome message and program information
    print("🎓 STUDENT GRADE CALCULATOR")
    print("="*50)
    print("This program calculates letter grades based on numerical marks.")
    print("Valid input range: 1-100 marks")
    
    # Show grading chart for user reference
    display_grade_chart()
    
    # Main program loop - allows multiple calculations
    while True:
        try:
            print("\n" + "-"*50)
            
            # Step 1: Get valid marks from user
            marks = get_student_marks()
            
            # Step 2: Calculate the grade based on marks
            grade = calculate_grade(marks)
            
            # Step 3: Display the result in a formatted manner
            display_result(marks, grade)
            
            # Step 4: Ask if user wants to calculate another grade
            print("\nWould you like to calculate another grade?")
            
            while True:
                choice = input("Enter 'y' for yes or 'n' for no: ").lower().strip()
                
                if choice in ['y', 'yes']:
                    break  # Continue to next iteration
                elif choice in ['n', 'no']:
                    print("\n👋 Thank you for using the Grade Calculator!")
                    print("   Keep up the good work in your studies! 📚✨")
                    return  # Exit the program
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully in main loop
            print("\n\n👋 Program terminated by user. Goodbye!")
            return


# Program entry point
if __name__ == "__main__":
    # This block ensures the main() function only runs when the script
    # is executed directly, not when imported as a module
    main()