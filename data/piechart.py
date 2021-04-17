# # of men with medals: 157
# # of women with medals: 106
import matplotlib.pyplot as plt

values = [157, 106]
labels = ["Men", "Women"]
colors = ["lightskyblue", "violet"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()