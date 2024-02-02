#!/usr/bin/python3

"""
rain_trap.py - A script to calculate the amount of rainwater retained
between walls represented by a list of non-negative integers.
"""

def rain(walls):
    """
    Calculate the total amount of rainwater retained between walls.

    Args:
        walls (List[int]): A list of non-negative integers representing wall heights.

    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Calculate the maximum height to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    # Calculate the amount of water that can be trapped at each position
    trapped_water = 0
    for i in range(n):
        trapped_water += max(0, min(left_max[i], right_max[i]) - walls[i])

    return trapped_water


if __name__ == "__main__":
    # Example usage:
    walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = rain(walls)
    print(result)  # Output: 6

