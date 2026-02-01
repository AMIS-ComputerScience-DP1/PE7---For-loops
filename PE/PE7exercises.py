# Task 1: Sum of Range
# Calculate the sum of all integers from 1 to 50 (inclusive).
def sum_fifty():
    total = 0
    # TODO: Write your for loop here
    return total

# Task 2: Square Numbers
# Create a list containing the squares of numbers 1 through 10.
def get_squares():
    squares = []
    # TODO: Use a for loop and range(1, 11)
    return squares

# Task 3: Filtering a List
# Given a list of temperatures, return a new list containing 
# only temperatures above 30 degrees.
def filter_temps():
    temps = [25, 32, 18, 40, 28, 35, 22]
    hot_days = []
    # TODO: Iterate through 'temps' and append to 'hot_days' if > 30
    return hot_days

# ==========================================
# AUTOCHECK - DO NOT EDIT BELOW THIS LINE
# ==========================================
def run_tests():
    print("--- Autocheck Results ---")
    
    # Test 1
    t1 = sum_fifty()
    print(f"Task 1: {'✅ Pass' if t1 == 1275 else '❌ Fail (Expected 1275)'}")
    
    # Test 2
    t2 = get_squares()
    expected_t2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(f"Task 2: {'✅ Pass' if t2 == expected_t2 else '❌ Fail'}")
    
    # Test 3
    t3 = filter_temps()
    expected_t3 = [32, 40, 35]
    print(f"Task 3: {'✅ Pass' if t3 == expected_t3 else '❌ Fail'}")

if __name__ == "__main__":
    run_tests()
