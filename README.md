# Python Calculator Programs

This repository contains two beginner-friendly Python programs with detailed explanations and robust error handling.

## Programs Included

### 1. Grade Calculator (`grade_calculator.py`)

A comprehensive program that converts numerical student marks (1-100) into letter grades.

#### Features:
- **Input Validation**: Ensures marks are within valid range (1-100)
- **Grade Calculation**: Implements the following grading scale:
  - Grade A: 91-100 marks (Excellent)
  - Grade B: 81-90 marks (Very Good)
  - Grade C: 71-80 marks (Good)
  - Grade D: 61-70 marks (Average)
  - Grade E: 50-60 marks (Below Average)
  - Grade F: 1-49 marks (Fail)
- **Error Handling**: Gracefully handles invalid inputs (non-numbers, out-of-range values)
- **User-Friendly Interface**: Clear prompts, formatted output, and helpful error messages
- **Educational Content**: Displays grading chart and descriptive feedback

#### Usage:
```bash
python3 grade_calculator.py
```

#### Example Output:
```
🎓 STUDENT GRADE CALCULATOR
==================================================
Enter student marks (1-100): 85

==================================================
               📋 GRADE CALCULATION RESULT
==================================================
Student Marks: 85.0
Letter Grade:  B
Performance:   Very Good! Well done! 👏
==================================================
```

### 2. Factorial Calculator (`factorial_calculator.py`)

A comprehensive program that calculates the factorial of a non-negative integer.

#### Features:
- **Input Validation**: Ensures input is a non-negative integer
- **Dual Implementation**: 
  - Iterative method (recommended for large numbers)
  - Recursive method (educational purpose, shown for verification)
- **Step-by-Step Calculation**: Shows the mathematical process
- **Large Number Handling**: Formats large results with thousand separators
- **Educational Content**: Explains factorial concept and provides examples
- **Performance Safeguards**: Warns about very large numbers that may take time

#### Usage:
```bash
python3 factorial_calculator.py
```

#### Example Output:
```
🧮 FACTORIAL CALCULATOR
============================================================
Enter a non-negative integer: 5

📝 Step-by-step calculation of 5! using iterative method:
------------------------------------------------------------
5! = 5 × 4 × 3 × 2 × 1

============================================================
               🧮 FACTORIAL CALCULATION RESULT
============================================================
Number (n):        5
Factorial (n!):    120
Number of digits:  3
============================================================
```

## Code Quality Features

Both programs include:

### 🔒 Robust Error Handling
- Input validation with clear error messages
- Graceful handling of edge cases
- Protection against infinite loops
- Keyboard interrupt (Ctrl+C) handling

### 📚 Educational Design
- Extensive comments explaining each step
- Clear variable names and function documentation
- Step-by-step calculation display
- Mathematical background information

### 🎨 User Experience
- Colorful emoji indicators for better visual feedback
- Formatted output with clear sections
- Interactive retry mechanisms
- Professional-looking results display

### 🧪 Testing
A comprehensive test suite (`test_calculators.py`) is included to verify:
- Grade calculation accuracy for all boundary conditions
- Factorial calculation correctness for both iterative and recursive methods
- Edge cases (0!, 1!, boundary grades)
- Consistency between different calculation methods

#### Running Tests:
```bash
python3 test_calculators.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## File Structure

```
├── grade_calculator.py      # Grade calculation program
├── factorial_calculator.py  # Factorial calculation program
├── test_calculators.py     # Automated test suite
└── README.md               # This documentation file
```

## Learning Objectives

These programs demonstrate:

1. **Input/Output Operations**: Using `input()` and `print()` effectively
2. **Data Types**: Working with integers, floats, and strings
3. **Control Structures**: if-elif-else statements and loops
4. **Functions**: Modular code organization and reusability
5. **Error Handling**: try-except blocks and validation
6. **String Formatting**: Professional output formatting
7. **Mathematical Operations**: Implementing mathematical algorithms
8. **Code Documentation**: Writing clear comments and docstrings

## Educational Notes

### Grade Calculator Concepts:
- Conditional logic with multiple conditions
- Range checking and validation
- User interface design principles
- Data type conversion (string to float)

### Factorial Calculator Concepts:
- Iterative vs. recursive algorithms
- Loop structures (for loops)
- Mathematical algorithm implementation
- Performance considerations for large numbers
- Number formatting and display

## Author

Created as educational programming examples to demonstrate best practices in:
- Code organization and documentation
- User input validation and error handling
- Clear and informative user interfaces
- Mathematical algorithm implementation