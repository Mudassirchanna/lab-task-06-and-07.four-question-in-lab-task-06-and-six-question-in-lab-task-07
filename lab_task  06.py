# LAB_TASK 06
"""Q:NO:04 input 
 words=['apple','ant','banana', 'ball', 'cat']
expected output:
{'a':['apple','ant'], 'b':['banana','ball',],
'c':['cat']}."""

words=['apple','ant','banana', 'ball', 'cat']
grouped={} 
for word in words:
    frist = word[0]
    if frist in grouped:
        grouped[frist].append(word)
    else:
        grouped[frist]=[word]
        print(grouped)    