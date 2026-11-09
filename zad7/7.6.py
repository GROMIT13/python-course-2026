import itertools
import random


# Stworzyć następujące iteratory nieskończone
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
print("---(a)---")

i_a = iter(itertools.cycle(range(2)))

for _ in range(10):
    print(next(i_a))  

# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
print("---(b)---")
i_b = iter(lambda : random.choice(["N", "W", "S", "E"]), 0)
for _ in range(10):
    print(next(i_b))  

# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
print("---(c)---")
i_c = iter(lambda : random.choice(range(7)), -1)
for _ in range(10):
    print(next(i_c))  

