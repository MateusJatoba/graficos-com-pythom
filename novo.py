import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x = np.linspace(0,7,50)
y1 = np.sin(x)
y2= np.cos(x)

plt.plot(x,y1,"b", label="linha azul")
plt.legend()
plt.plot(x,y2,"r", label="Linha vermelha")
plt.legend()
# plt.plot(x,y1,y2,"g")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.title("Grafico de $ f(x) = e^{-x}\sin(x) $",\
          fontsize=16)
plt.axis("equal")
plt.show()