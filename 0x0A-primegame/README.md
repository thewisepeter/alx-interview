# Prime Game

## Description
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The chosen prime number and its multiples are then removed from the set. The player who cannot make a move loses the game. This script implements a function to determine the winner of multiple rounds of this game, where each round may have a different upper limit.

## Problem Statement
Given a set of consecutive integers starting from 1 up to and including n, Maria and Ben play x rounds of the game. Assuming Maria always goes first and both players play optimally, the task is to determine the winner of each game.

**Prototype:** 
```python
def isWinner(x, nums):
```

**Parameters:**
- `x` (int): The number of rounds.
- `nums` (list): An array of upper limits for each round.

**Returns:**
- str or None: The name of the player who won the most rounds, or None if the winner cannot be determined.

**Constraints:**
- `x` and the elements of `nums` will not be larger than 10,000.
- No external packages are allowed.

## Example

```python
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

print("Winner: {}".format(isWinner(x, nums)))  # Output: "Maria" or "Ben" or None
```

# Function `isWinner`

This function determines the winner of multiple rounds of the prime game according to the provided rules.

## Algorithm
1. Initialize counters for Maria's wins and Ben's wins.
2. For each round `r` from 1 to `x`:
   - Initialize a set of integers from 1 to `nums[r]`.
   - While the set is not empty:
     - Maria selects the smallest remaining prime number from the set and removes it along with its multiples.
     - If the set becomes empty, Ben wins the round.
     - Ben selects the smallest remaining prime number from the set and removes it along with its multiples.
     - If the set becomes empty, Maria wins the round.
   - Update the counters based on the winner of the round.
3. Determine the player with the most wins.
4. Return the name of the player with the most wins or None if it's a tie.

## Usage
```python
isWinner(x, nums)
```

- `x` (int): The number of rounds.
- `nums` (list): An array of upper limits for each round.

Returns:
- str or None: The name of the player who won the most rounds, or None if the winner cannot be determined.