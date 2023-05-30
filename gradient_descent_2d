from random import choice, randint, random

k = random() * randint(-100, 100)
b = random() * randint(-100, 100)
print(f"read k: {k}, b:{b}")
data = [[x, k * x] for x in range(1, 10000)]
l = len(data)
h = 0.01  # learning rate
lb = 1  # learning memory rate

# weights = [0.01] * len(data)
weights = 0.5
gradient = 0.1
epochs = 100000


def q_(weights):
	q = 0
	for i in range(l):
		q += (data[i][0] * weights - data[i][1]) ** 2
	q /= l
	return q


def loss_(x, y, w):
	return (x * w - y) ** 2


# if gradient is negative -> increase w
# else -> decrease w
import time

start = time.time()
for _ in range(epochs):
	x1 = choice(data)

	gradient = (loss_(x1[0], x1[1], weights-0.01) - loss_(x1[0], x1[1], weights)) / 0.01

	if gradient > 0:
		weights += h
	else:
		weights -= h

end = time.time()
print(f"{round(end - start, 4)}s")

print("MSE:", q_(weights))
print("Weights:", weights)
