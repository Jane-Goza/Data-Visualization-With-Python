import matplotlib.pyplot as plt

years = [1994, 1998, 2002, 2006, 2010, 2014]
pops = [4, 6, 40, 41, 25, 68]

# plot our chart with data above
plt.plot(years, pops, color=(0/255, 100/255, 100/255), linewidth=3.0)

#label on the left hand side
plt.ylabel("Population of sportmans in Russia")
#label on the bottom of the chart
plt.xlabel("Sportsmens Growth by Year")

#add a title to the chart
plt.title("World Population Growth", pad="20")
plt.show() 