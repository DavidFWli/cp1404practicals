import random
randInt =random.getrandbits(1)
randBool = bool(randInt)
print(randBool)

randBool = random.choice([True, False])
print(randBool)

randInt = random.choice([0,1])
randBool = bool(randInt)
print(randBool)

randBool = random.random()>0.5
print(randBool)