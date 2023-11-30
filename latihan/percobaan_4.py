import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Menambahkan judul dan label sumbu 
plt.title('Titik') 
plt.xlabel('Nilai x') 
plt.ylabel('Nilai y')

plt.scatter(x, y)
plt.show()