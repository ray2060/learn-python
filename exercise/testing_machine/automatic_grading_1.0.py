FILENAME = 'abc.txt'
RIGHT_ANSWERS = ['A', 'A', 'D', 'C', 'B', 'D', 'B', 'C']

f = open(FILENAME, 'r')

s = f.read()
index = -1
score = 0
for i in s:
    index += 1
    if i == RIGHT_ANSWERS:
        score += 12.5
    else:
        score -= 4.1
print(score)
        
