""" Algorthim Complexity """
"""
Algorithm complexity, also known as time complexity or computational complexity, measures the efficiency of an algorithm by analyzing the growth rate of its resource usage (usually time and space) as the input size increases. It provides an estimation of how the algorithm's performance scales with larger inputs.

There are commonly used notations to describe algorithm complexity:

1. Big O notation (O): It represents the upper bound or worst-case scenario of the algorithm's time or space complexity. It describes the maximum amount of resources required by the algorithm as the input size approaches infinity.

2. Omega notation (Ω): It represents the lower bound or best-case scenario of the algorithm's time or space complexity. It describes the minimum amount of resources required by the algorithm as the input size approaches infinity.

3. Theta notation (Θ): It represents the tight bound or average-case scenario of the algorithm's time or space complexity. It describes the expected amount of resources required by the algorithm as the input size approaches infinity.

Here are some common time complexity notations and their meanings:

- O(1) - Constant time: The algorithm's runtime or resource usage remains constant, regardless of the input size.

- O(log n) - Logarithmic time: The algorithm's runtime or resource usage grows logarithmically with the input size. Example: Binary search on a sorted list.

- O(n) - Linear time: The algorithm's runtime or resource usage grows linearly with the input size. Example: Iterating through a list.

- O(n log n) - Linearithmic time: The algorithm's runtime or resource usage grows in between linear and logarithmic. Example: Merge sort, quicksort.

- O(n^2) - Quadratic time: The algorithm's runtime or resource usage grows quadratically with the input size. Example: Nested loops.

- O(2^n) - Exponential time: The algorithm's runtime or resource usage grows exponentially with the input size. Example: Recursive algorithm without memoization.

These notations provide a relative comparison of algorithms' efficiency and help in selecting appropriate algorithms for solving problems based on the input size. However, it's important to note that algorithm complexity analysis doesn't provide precise measurements of actual execution time or resource usage, but rather an estimation of their growth rates.
"""

"""
What is efficiency in programming ? 
ans =time and space

Time Measure Techniques
1-Measuring time to execute
2-Counting operations involved
3-Abstract notion of order of growth

Problems with this approach

a-Different time for different algorithm
b-Time varies if implementation changes
c-Different machines different time 
d-Does not work for extremely small input
e-Time varies for different inputs, but can't establish a relationship

What do we want ?
a-We want to evaluate the algorithm
b-We want to evaluate scalability
c-We want to evaluate in terms of input size

Orders of Growth 

=>Want to evaluate program's efficiency when "input is very big"
=>Want to express the "growth of program's run time" as input size grows
=>Want to put an "upper bound" on growth -as tight as possible 
=>Do not need to be precise: "order of" not "exact" growth
=>We will look at "largest factors" in run time (which section of the program will take the longest to run ?)
=>"Thus, generally we want tight upper bound on growth, as function of size of input, in worst case"

"""

import time
start = time.time()  # get current time (start time)
for i in range(1101):
    print(i)

# i = 1
# while i < 1101:
#     print(i)
#     i += 1

print(time.time() - start)  # get exact time (end time)

""" Counting operations """
