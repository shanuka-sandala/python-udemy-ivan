import matplotlib.pyplot as plt ## This is a external module, it has to install by cmd "pip install matplotlib"

x = [1,2,3,4] ## a list
y = [1500,1200,1100,1800]

plt.plot(x,y)
plt.show()

legend = ["January","February","March","April"]
plt.xticks(x,legend)
plt.plot(x,y)
plt.show()