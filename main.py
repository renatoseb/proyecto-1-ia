import numpy as np
# CodeSet A
np.random.seed(1)
s=np.random.randint(5,10,12)
print("Seed 1")
print(s)
print()
# CodeSet B
np.random.seed(2)
s=np.random.randint(5,10,12)
print("Seed 2")
print(s)
print()
# CodeSet C
np.random.seed()
s=np.random.randint(5,10,12)
print("Seed")
print(s)
print()
# CodeSet D
for i in range(7):
    np.random.seed(1)
    s=np.random.randint(5,10,12)
    print("Seed")
    print(s) 