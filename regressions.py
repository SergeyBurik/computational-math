from random import randint
import matplotlib.pyplot as plt

n = 20
k = randint(-100, 100)
b = randint(-100, 100)
# generate points
points = [[i, k*i+b+randint(-int(abs(b*0.5)), int(abs(b*0.5)))] for i in range(n)]

print("real k value:",k)
avg_k = 0
count = 0
for i in range(len(points)):
	for j in range(i+1, len(points)):
		k = (points[i][1]- points[j][1]) / (points[i][0] - points[j][0])
		avg_k += k
		count += 1

avg_k /= count

avg_b = 0
for point in points:
	b = point[1] - (avg_k * point[0]) 
	avg_b += b

avg_b /= len(points)


print(f"y = {avg_k}x + {avg_b}")	

def f(x):
	global avg_k
	global avg_b
	return avg_k*x+avg_b

mae = 0
for point in points:
	mae = abs(abs(point[1]) - abs(f(point[0])))

mae /= len(points)
print("MAE (avg)", mae)

points_sorted = sorted(points)

x_0, x_1 = points_sorted[0][0], points_sorted[-1][0]
x_reg = list(range(x_0, x_1+1))
y_reg = [f(x) for x in x_reg]

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.scatter(x, y, c ="blue")
plt.plot(x_reg, y_reg, linestyle='-', c="red")  # solid

plt.show()
