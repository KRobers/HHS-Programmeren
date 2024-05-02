#H15.1

import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values)
plt.show()

#15.3

import matplotlib.pyplot as plt


rw = RandomWalk(5000)
rw.fill_walk()
plt.figure(figsize=(10, 6))
plt.plot(rw.x_values, rw.y_values, linewidth=1)

plt.plot(0, 0, c='green', marker='o')
plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', marker='o')

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
