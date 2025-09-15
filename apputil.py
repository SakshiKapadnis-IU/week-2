def ways(n):
    count = 0
    for num_nickels in range(n // 5 + 1):  # Iterate through possible number of nickels
        remaining_amount = n - num_nickels * 5
        if remaining_amount >= 0:  # Check if the remaining amount can be made with pennies
            count += 1
    return count

print(f"ways(12): {ways(12)}")
print(f"ways(20): {ways(20)}")
print(f"ways(3): {ways(3)}")
print(f"ways(0): {ways(0)}")

import numpy as np

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

# Part 1: Find the name of the student with the lowest score
    lowest_score_index = np.argmin(scores)
    return names[lowest_score_index]

print(f"Student with the lowest score: {lowest_score(names, scores)}")

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

# Part 2: Sort names by score in descending order
    sorted_indices = np.argsort(scores)[::-1]  # Get indices that would sort scores in descending order
    return names[sorted_indices].tolist()

print(f"Names sorted by score (descending): {sort_names(names, scores)}")