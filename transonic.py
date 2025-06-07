import numpy as np
import matplotlib.pyplot as plt

# Define a grid for x and y
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Elliptic (아음속): u_xx + u_yy = 0 -> 라플라스 방정식
Z_elliptic = np.sin(np.pi*X)*np.sinh(np.pi*Y)

# Hyperbolic (초음속): u_xx - u_yy = 0 -> 파동방정식
Z_hyperbolic = np.sin(np.pi*X)*np.sin(np.pi*Y)

# Parabolic (천음속, 전이): u_xx = u_y
Z_parabolic = np.sin(np.pi*X)*np.exp(-np.pi*Y)

fig, axs = plt.subplots(1, 3, figsize=(15,5))

# 아음속
cs1 = axs[0].contourf(X, Y, Z_elliptic, levels=50, cmap='viridis')
axs[0].set_title('Elliptic PDE (M<1)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
fig.colorbar(cs1, ax=axs[0])

# 초음속
cs2 = axs[1].contourf(X, Y, Z_hyperbolic, levels=50, cmap='plasma')
axs[1].set_title('Hyperbolic PDE (M>1)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
fig.colorbar(cs2, ax=axs[1])

# 천음속
cs3 = axs[2].contourf(X, Y, Z_parabolic, levels=50, cmap='inferno')
axs[2].set_title('Parabolic PDE (M=1, transitional)')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
fig.colorbar(cs3, ax=axs[2])

plt.tight_layout()
plt.show()
