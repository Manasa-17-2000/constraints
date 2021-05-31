word = "FIRSTCHARSTRING"
commands = [
    ('L',2),
    ('R',2),
    ('L',3),
]
from collections import deque

q = deque(word)
for direction, magnitude in commands:
    if direction == "L" :
        q. rotate(-magnitude)
    else:
        q.rotate(magnitude)

if '' . join(q) == word:
    print("yes")
else:
    print("no")
