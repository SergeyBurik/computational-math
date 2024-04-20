# data generation
from random import uniform
import matplotlib.pyplot as plt

W = [uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]
print(W)

X = [[uniform(1, 2), uniform(1, 2)] for _ in range(10000)]
Y = [x[0] * W[0] + x[1] * W[1] + W[2] for x in X]


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

weights = [0.1 for _ in range(len(W))]
learning_rate = 0.01
epochs = 1000

predictions = model(X, weights)

learning_history = []

delta = 0.01
for i in range(epochs):
    if i % 100 == 0:
        print("epoch", i)
    # calculate gradient

    # d(W[n])/d(loss_function)
    anti_gradient = []
    for n in range(len(weights)):
        der_weights = weights[::]
        der_weights[n] += delta
        der_predictions = model(X, der_weights)

        delta_loss = loss_function(der_predictions, Y)
        loss = loss_function(predictions, Y)

        learning_history.append(delta_loss)

        derivative = -(delta_loss - loss) / delta
        predictions = der_predictions
        anti_gradient.append(derivative)

    # print(anti_gradient)
    # update weights
    for i in range(len(anti_gradient)):
        weights[i] += learning_rate * anti_gradient[i]


print("MSE", delta_loss)
print(weights)

# plt.scatter(list(range(len(learning_history))), learning_history)

plt.scatter([x[0] for x in X[:100]], [y for y in predictions[:100]], color = 'red')
plt.show()
