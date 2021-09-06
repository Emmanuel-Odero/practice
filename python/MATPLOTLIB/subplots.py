from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("dark_background")

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)


#alternative if we want two figures
#fig1, ax1 = plt.subplots()
#fig2, ax2 = plt.subplots()

print(ax1)
print(ax2)

ax1.legend()

ax1.set_ylabel("Developers")
ax1.set_title("Average Salary")


ax2.legend()
ax2.set_xlabel("Ages")
ax2.set_ylabel("Developers")


plt.show()