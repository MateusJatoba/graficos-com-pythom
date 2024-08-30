import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20,20,100)



plt.subplot(2,2,1)
y = np.sin(x) / x
plt.plot(x, y, label="valores")
plt.legend()
plt.axis("equal")
plt.ylabel("Valor do sen(x)/x")
plt.xlabel("Valor de X")

plt.suptitle("Gráficos de operações com sen(x)")

plt.subplot(2,2,2)
y2 = x * np.sin(x)
plt.plot(x, y2, "r", label="valores")
plt.legend()
plt.axis('equal')
plt.xlabel("Valor de x")
plt.ylabel("Valor de xsen(x)")

plt.subplot(2,2,3)
y3 = np.sin(x) / pow(x,2)
plt.plot(x,y3, "g", label="valores")
plt.legend()
plt.xlabel("Valor de X")
plt.ylabel("Valor de sen(x) / x^2")

plt.subplot(2,2,4)
y4 = pow(x,2) * np.sin(x)
plt.plot(x,y4, "c", label="valores")
plt.legend()
plt.xlabel("Valor de X")
plt.ylabel("Valor de x^2sen(x)")

plt.show()