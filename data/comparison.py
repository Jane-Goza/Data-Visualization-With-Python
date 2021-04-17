import matplotlib.pyplot as plt

heights = [157, 106]
bars = ['Men', 'Women' ]
y_pos = range(len(bars))
plt.bar(y_pos, heights)
# Rotation of the bars names
plt.xticks(y_pos, bars, rotation=90)
plt.show()