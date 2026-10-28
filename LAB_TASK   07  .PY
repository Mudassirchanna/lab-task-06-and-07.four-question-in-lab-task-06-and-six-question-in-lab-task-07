# LAB_TASK 07
"""Q:NO:06 practice the four important operations: union(|),
intersection(&),difference(-), and symmetric difference (^). 
A={1,2,3,4}  , B={3,4,5,6}  find all unique element in A and B .
using the same sets , find element common to both sets.
find A-B, AND B-A .explain why their result difer .find elements that
 are in either A or B, but not in both."""

A={1,2,3,4}

B={3,4,5,6}
 # Union: all unique elements
print("Union:", A | B)

# Intersection: common elements
print("Intersection:", A & B)

# Difference: elements in A but not in B
print("A - B:", A - B)

# Difference: elements in B but not in A
print("B - A:", B - A)

# Symmetric difference: elements in either set, but not both
print("Symmetric Difference:", A ^ B)

