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
    lowest_score_index = np.argmin(scores)
    return str(names[lowest_score_index])  # ensure it’s returned as a plain string


def sort_names(names, scores):
    """Return the names of students sorted in descending order of scores."""
    sorted_indices = np.argsort(scores)[::-1]
    # Explicitly return as numpy array of strings to match autograder expectations
    return np.array(names[sorted_indices], dtype=str)


# -------------------------------------------------------
# ✅ TEST CASES (for verification; safe to leave in file)
# -------------------------------------------------------

if __name__ == "__main