import numpy as np

def ways(n):
    """Return the number of ways to make n cents using pennies (1) and nickels (5)."""
    count = 0
    for num_nickels in range(n // 5 + 1):
        remaining_amount = n - num_nickels * 5
        if remaining_amount >= 0:
            count += 1
    return count


def lowest_score(names, scores):
    """Return the name of the student with the lowest score."""
    # Ensure both are numpy arrays
    names = np.array(names)
    scores = np.array(scores)
    lowest_score_index = int(np.argmin(scores))  # convert to int for safe indexing
    return str(names[lowest_score_index])  # return plain string


def sort_names(names, scores):
    """Return the names of students sorted in descending order of scores."""
    # Ensure both are numpy arrays
    names = np.array(names)
    scores = np.array(scores)
    sorted_indices = np.argsort(scores)[::-1]
    return names[sorted_indices]  # return numpy array


# -------------------------------------------------------
# ✅ TEST CASES (safe for autograder)
# -------------------------------------------------------
if __name__ == "__main__":
    # Exercise 1 test cases
    print("Exercise 1: ways()")
    print(f"ways(12): {ways(12)}  # Expected: 3")
    print(f"ways(20): {ways(20)}  # Expected: 5")
    print(f"ways(3): {ways(3)}    # Expected: 1")
    print(f"ways(0): {ways(0)}    # Expected: 1\n")

    # Exercise 2 test cases
    print("Exercise 2: lowest_score() and sort_names()")
    names = ['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung']
    scores = [99, 71, 85, 62, 91]

    print(f"Lowest score student: {lowest_score(names, scores)}  # Expected: Mauve")
    print(f"Names sorted by descending score: {sort_names(names, scores)}")
    # Expected order: ['Hannah' 'Jung' 'Abdul' 'Astrid' 'Mauve']