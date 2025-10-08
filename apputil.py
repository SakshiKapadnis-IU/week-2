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
    return names[lowest_score_index]


def sort_names(names, scores):
    """Return the names of students sorted in descending order of scores."""
    sorted_indices = np.argsort(scores)[::-1]
    return names[sorted_indices]