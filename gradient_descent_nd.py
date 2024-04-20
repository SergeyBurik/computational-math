# data generation
from random import uniform, randint
import matplotlib.pyplot as plt
import json

weights_num = 20

W = [uniform(-1, 1) for _ in range(weights_num)]
print(W)

X = [[uniform(0, 2) for _ in range(weights_num - 1)] for _ in range(100000)]
Y = []
for x in X:
    res = W[-1]
    for i in range(len(x) - 1):
        res += x[i] * W[i]
    res += uniform(-0.3, 0.3) # add noise
    Y.append(res)

with open("X.txt", "w") as X_file:
    X_file.write(json.dumps(X))

with open("Y.txt", "w") as X_file:
    X_file.write(json.dumps(Y))

plt.scatter([x[0] for x in X[:100]], [y for y in Y[:100]], color = '#88c999')


# linear regression
def loss_function(predicted, real):
    res = 0
    if len(predicted) != len(real):
        raise Exception("lengths are not the same")
    
    for i in range(len(predicted)):
        res += (real[i] - predicted[i]) ** 2
    
    return res / (2 * len(predicted))

def model(X, weights):
    predictions = []
    for x in X:
        prediction = 0
        for i in range(len(x)):
            prediction += x[i] * weights[i]
        prediction += weights[-1]
        predictions.append(prediction)

    return predictions

X_train = X[:int(0.8 * len(X))]
Y_train = Y[:int(0.8 * len(Y))]

X_test = X[int(0.8 * len(X)):]
Y_test = Y[int(0.8 * len(Y)):]

weights = [0 for _ in range(len(W))]
learning_rate = 0.01
epochs = 5000
learning_history = []
delta = 0.01

for i in range(epochs):
    if i % 1000 == 0:
        print("epoch", i)
    
    random_index = randint(0, len(X_train) - 1)

    # calculate gradient
    # d(W[n])/d(loss_function)
    anti_gradient = []
    for n in range(len(weights)):
        der_weights = weights[::]
        der_weights[n] += delta
        der_predictions = model([X_train[random_index]], der_weights)
        predictions = model([X_train[random_index]], weights)

        delta_loss = loss_function(der_predictions, [Y_train[random_index]])
        loss = loss_function(predictions, [Y_train[random_index]])

        learning_history.append(delta_loss)
        derivative = -(delta_loss - loss) / delta
        anti_gradient.append(derivative)

    # update weights
    for i in range(len(anti_gradient)):
        weights[i] += learning_rate * anti_gradient[i]

print(weights)
predictions = model(X_test, weights)
print("MSE:", loss_function(predictions, Y_test))

plt.scatter([x[0] for x in X_test[:100]], [y for y in predictions[:100]], color = 'red')
plt.figure()

plt.plot(list(range(len(learning_history))), learning_history)

plt.show()
