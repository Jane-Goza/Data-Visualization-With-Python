# # of biathlon sportsmens with medals: 57
# # of bobsleigh sportsmens with medals: 15
# # of Ice Hockey sportsmens with medals: 46
# # of Luge sportsmens with medals: 6
# # of Skating sportsmens with medals: 79
# # of Skiing sportsmens with medals: 60

import matplotlib.pyplot as plt
import pandas as pd

run1 = [14,9,7,13,5,31]
run2 = [11,12,4,12,7,14]
run3 = [11,9,6,11,10,10]
run4 = [0,23,23,0, 0,0]
run5 = [0,0,0,4,3,8]
run6 = [0,0,0,1,0]

runs = pd.DataFrame({'Skating': run1, 'Skiing': run2,
 'Biathlon': run3, 'Ice Hockey': run4}, 'Bobsleigh': run5, 'Luge': run6)
runs.plot.bar()
plt.show() 