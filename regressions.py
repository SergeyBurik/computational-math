points = [[5, 13], [4, 11], [7, 14], [9, 24], [10, 25]]

cur = 10**10
res = 10**10

mnk = 0
mnb = 0

for k in range(-100, 100):
	for b in range(-1000, 1000):
		avg = 0
		for point in points:
			cur = abs(point[1] - (k*point[0] + b))
			avg += cur
		avg /= len(points)
		if avg < res:
			mnk = k
			mnb = b
			res = avg
print(f"y = {mnk}x + {mnb}")	


def f(x):
	global mnk
	global mnb
	return mnk*x+mnb

import matplotlib.pyplot as plt


points_sorted = sorted(points)

x_0, x_1 = points_sorted[0][0], points_sorted[-1][0]
print(x_0, x_1)
x_reg = list(range(x_0, x_1+1))
y_reg = [f(x) for x in x_reg]

x = [point[0] for point in points]
y = [point[1] for point in points]


plt.scatter(x, y, c ="blue")
plt.plot(x_reg, y_reg, linestyle='-')  # solid

# To show the plot
plt.show()



# import math

# points = [[9, 2.95], [27, 4.2], [81, 5.1], [100, 5.4]]

# cur = 10**10
# res = 10**10

# mnk = 0
# mnb = 0
# mnw = 0

# for w in range(1, 2):
# 	for k in range(2, 100):
# 		for b in range(-100, 100):
# 			avg = 0
# 			for point in points:
# 				cur = abs(abs(point[1]) - abs(w*math.log(point[0], k) + b))
# 				avg += cur
# 			avg /= len(points)
# 			if avg < res:
# 				mnk = k
# 				mnb = b
# 				mnw = w
# 				res = avg
# print(f"y = {mnw}*log{mnk}(x) + {mnb}")	
# print(res)

# def f(x):
# 	global mnk
# 	global mnb
# 	return math.log(x, mnk) + mnb

# import matplotlib.pyplot as plt


# points_sorted = sorted(points)

# x_0, x_1 = points_sorted[0][0], points_sorted[-1][0]
# print(x_0, x_1)
# x_reg = list(range(x_0, x_1+1))
# y_reg = [f(x) for x in x_reg]

# x = [point[0] for point in points]
# y = [point[1] for point in points]


# plt.scatter(x, y, c ="blue")
# plt.plot(x_reg, y_reg, linestyle='-')  # solid

# # To show the plot
# plt.show()
