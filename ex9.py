import numpy as np
import matplotlib.pyplot as plt

# Exercise 9.1

x_val = np.linspace(0, 10, 400)
plt.plot(x_val, np.sin(x_val), color="red", linestyle="-", label="sin(x)")
plt.plot(x_val, np.cos(x_val), color="green", linestyle="--", label="cos(x)")
plt.plot(x_val, np.exp(-x_val), color="blue", linestyle=":", label="exp(-x)")

plt.legend()

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.grid(True)
plt.tight_layout()
plt.savefig("notebook9ex1.png")
plt.close()

# Exercise 9.2

n = 100
pts = (np.random.rand(n), np.random.rand(n))

x_pts, y_pts = pts
dist = np.sqrt(x_pts**2 + y_pts**2)

colors = ["green" if d < 1 else "red" for d in dist]
sizes = (np.abs(x_pts) + np.abs(y_pts)) * 100

plt.scatter(x_pts, y_pts, c=colors, s=sizes, alpha=0.6)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title("100 random Points from unit square")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect("equal", adjustable="box")
plt.tight_layout()
plt.savefig("notebook9ex2.png")
plt.close()

# Exercise 9.3

def sum_distances(x, y):
    d1 = np.sqrt((x + 1)**2 + y**2)
    d2 = np.sqrt((x - 1)**2 + y**2)
    return d1 + d2


x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)

X, Y = np.meshgrid(x, y)
Z = sum_distances(X, Y)

plt.imshow(
    Z,
    extent=[-2, 2, -2, 2],
    origin="lower",
    cmap="viridis"
)

plt.colorbar(label="Sum of distances")
plt.scatter([-1, 1], [0, 0], color="red", label="Fixed points")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sum of distances from (-1,0) and (1,0)")
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")

plt.tight_layout()
plt.savefig("notebook9ex3.png")
plt.close()
