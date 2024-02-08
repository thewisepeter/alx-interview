# 0x09. Island Perimeter 🏝️

Welcome to the Island Perimeter challenge! This problem often pops up in interviews to gauge your understanding of grid-based algorithms. Let's dive in and tackle it together.

### The Challenge 🌊

You're tasked with crafting a Python function, `island_perimeter(grid)`, which calculates the perimeter of an island described in a grid. Here are the key details:

- The grid is represented as a list of lists of integers.
- 0 signifies water, while 1 signifies land.
- Each cell in the grid is a square with a side length of 1.
- Land cells are connected horizontally and vertically (no diagonals).
- The grid is rectangular, with dimensions not exceeding 100.
- The grid is entirely surrounded by water.
- There's only one island (or nothing at all).
- The island doesn't contain "lakes" (water within the island not connected to the surrounding water).

Let's craft a solution that navigates these waters smoothly!

### Approach 🛶

To tackle this challenge, we'll sail through the grid, counting the perimeter as we encounter land cells. We'll adjust the perimeter based on adjacent land cells to handle internal edges. With this approach, we'll smoothly navigate the intricacies of the island's shape and calculate its perimeter accurately.

Are you ready to set sail and conquer this challenge? Let's embark on this coding voyage together! 🚢💻