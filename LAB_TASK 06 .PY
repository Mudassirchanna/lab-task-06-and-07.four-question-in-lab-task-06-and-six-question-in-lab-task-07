# LAB_TASK 06
"""Q:no:2 marks={'ali':85, 'sara': 95, 'ahmed': 95, 'noor': 78}
print every student who achieved the highest marks and their marks.
expected toppers: sara and ahmed ."""

marks={'ali':85, 'sara': 95, 'ahmed': 95, 'noor': 78}

for name in marks:
    if name =='sara' or name == 'ahmed':
        print(name, marks[name])
