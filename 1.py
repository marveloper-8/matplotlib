# import matplotlib
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np

# a = np.array([0, 6])
# b = np.array([0, 250])

# plt.plot(a, b)
# plt.show

# import matplotlib.pyplot as plt
# import numpy as np

# a = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(a)
# plt.show()

# a = np.array([1, 2, 6, 8])
# b = np.array([3, 8, 1, 10])

# plt.plot(a, b, 'o')
# plt.plot(a, b)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# a = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# b = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# c = {'family': 'serif', 'color': 'blue', 'size': 20}
# d = {'family': 'serif', 'color': 'darkred', 'size': 15}


# plt.title("Sports Watch Data", fontdict=c, loc='left')
# plt.xlabel("Average Pulse", fontdict=d)
# plt.ylabel("Calorie Burnage", fontdict=d)

# plt.plot(a, b)
# plt.grid(color='green', linestyle='--', linewidth=0.5)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# a = np.array([0, 1, 2, 3])
# b = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(a, b)
# plt.title('SALES')

# a = np.array([0, 1, 2, 3])
# b = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(a, b)
# plt.title('INCOME')

# plt.suptitle=('MY SHOP')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

a = np.random.randint(100, size=(100))
b = np.random.randint(100, size=(100))
c = np.random.randint(100, size=(100))
plt.scatter(a, b, c=c, cmap='twilight')

plt.colorbar()
plt.show()