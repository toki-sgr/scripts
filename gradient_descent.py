# theta_i x + theta_j y = J(theta)
theta_i = 1.0
theta_j = 1.0
i = 0
lr = 0.001

data = [[1, 5, 29], [5, 2, 45], [4.3, 6.4, 60], [7, 1, 56], [8, 6.6, 87]]
def data_provider():
    while (True):
        for i in data:
            yield i[0], i[1], i[2]
batch = len(data)
dp = data_provider()
predict_history = []
history_dict = dict()
while i < 100 * batch:
    print("step: {}".format(i))
    x_i, x_j, res = next(dp)
    predict = theta_i * x_i + theta_j * x_j
    print("data slice: x_i: {}, x_j: {}, res: {}".format(x_i, x_j, res))
    print("old_theta_i: {}, old_theta_j: {}, predict: {}".format(theta_i, theta_j, predict))
    new_theta_i = theta_i - lr * x_i * (predict - res)
    new_theta_j = theta_j - lr * x_j * (predict - res)
    theta_i = new_theta_i
    theta_j = new_theta_j
    print("new_theta_i: {}, new_theta_j: {}, new predict: {}".format(theta_i, theta_j, theta_i * x_i + theta_j * x_j))
    i += 1
    predict_history.append(predict)

for i, h in enumerate(predict_history):
    if not history_dict.get(i % batch, ""):
        history_dict[i % batch] = list()
    history_dict[i % batch].append(format(h, '.3f'))

print(history_dict)