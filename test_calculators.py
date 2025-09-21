#!/usr/bin/env python3
"""
Test script to verify the grade calculator and factorial calculator logic
"""

# Import functions from our programs
import sys
import os

# Add current directory to path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from grade_calculator import calculate_grade, get_grade_description
from factorial_calculator import calculate_factorial_iterative, calculate_factorial_recursive

def test_grade_calculator():
    """Test grade calculator with edge cases"""
    print("🧪 TESTING GRADE CALCULATOR")
    print("="*50)
    
    # Test cases: (marks, expected_grade)
    test_cases = [
        (1, 'F'),      # Minimum fail
        (49, 'F'),     # Maximum fail
        (50, 'E'),     # Minimum E
        (60, 'E'),     # Maximum E
        (61, 'D'),     # Minimum D
        (70, 'D'),     # Maximum D
        (71, 'C'),     # Minimum C
        (80, 'C'),     # Maximum C
        (81, 'B'),     # Minimum B
        (90, 'B'),     # Maximum B
        (91, 'A'),     # Minimum A
        (100, 'A'),    # Maximum A
        (75.5, 'C'),   # Decimal marks
        (88.9, 'B'),   # Decimal marks
    ]
    
    all_passed = True
    
    for marks, expected in test_cases:
        result = calculate_grade(marks)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"Marks: {marks:6} → Grade: {result} (Expected: {expected}) {status}")
    
    print("\n" + "="*50)
    print(f"Overall result: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    return all_passed

def test_factorial_calculator():
    """Test factorial calculator with various cases"""
    print("\n🧪 TESTING FACTORIAL CALCULATOR")
    print("="*50)
    
    # Test cases: (n, expected_factorial)
    test_cases = [
        (0, 1),        # Special case: 0! = 1
        (1, 1),        # Special case: 1! = 1
        (2, 2),        # 2! = 2
        (3, 6),        # 3! = 6
        (4, 24),       # 4! = 24
        (5, 120),      # 5! = 120
        (6, 720),      # 6! = 720
        (10, 3628800), # 10! = 3,628,800
    ]
    
    all_passed = True
    
    print("Testing iterative method:")
    for n, expected in test_cases:
        result = calculate_factorial_iterative(n)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"{n:2}! = {result:>10,} (Expected: {expected:>10,}) {status}")
    
    print("\nTesting recursive method (small numbers only):")
    for n, expected in test_cases[:7]:  # Test smaller numbers for recursion
        result = calculate_factorial_recursive(n)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"{n:2}! = {result:>10,} (Expected: {expected:>10,}) {status}")
    
    # Test that both methods produce same results
    print("\nTesting consistency between methods:")
    for n in range(0, 11):
        iter_result = calculate_factorial_iterative(n)
        rec_result = calculate_factorial_recursive(n)
        status = "✅ PASS" if iter_result == rec_result else "❌ FAIL"
        if iter_result != rec_result:
            all_passed = False
        print(f"{n:2}!: Iterative={iter_result:>8,}, Recursive={rec_result:>8,} {status}")
    
    print("\n" + "="*50)
    print(f"Overall result: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    return all_passed

def main():
    """Run all tests"""
    print("🔬 AUTOMATED TESTING OF CALCULATOR PROGRAMS")
    print("="*60)
    
    grade_tests_passed = test_grade_calculator()
    factorial_tests_passed = test_factorial_calculator()
    
    print("\n" + "="*60)
    print("                    📊 FINAL TEST RESULTS")
    print("="*60)
    print(f"Grade Calculator:    {'✅ PASSED' if grade_tests_passed else '❌ FAILED'}")
    print(f"Factorial Calculator: {'✅ PASSED' if factorial_tests_passed else '❌ FAILED'}")
    
    if grade_tests_passed and factorial_tests_passed:
        print("\n🎉 ALL TESTS PASSED! Both programs are working correctly!")
    else:
        print("\n⚠️  Some tests failed. Please review the code.")
    
    print("="*60)

if __name__ == "__main__":
    main()