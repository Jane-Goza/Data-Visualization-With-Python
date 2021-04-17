# # of biathlon sportsmens with medals: 57
# # of bobsleigh sportsmens with medals: 15
# # of Ice Hockey sportsmens with medals: 46
# # of Luge sportsmens with medals: 6
# # of Skating sportsmens with medals: 79
# # of Skiing sportsmens with medals: 60

import matplotlib.pyplot as plt

values = [57, 15, 46, 6, 79, 60]
labels = ["Biathlon", "Bobsleigh", "Ice Hockey", "Luge", "Skating", "Skiing"]
colors = ["lightskyblue", "violet", "gold", "brown", "silver", "orange"]
explode = (0, 0, 0, 0, 0.1, 0)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()