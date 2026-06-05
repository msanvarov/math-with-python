import math

import numpy as np

from vectors import add, scale, dot, cross, norm, normalize, angle, project

u = np.array([1, 2, 3])
v = np.array([4, -5, 6])

print("u + v =", add(u, v))
print("3 * u =", scale(3, u))
print("u . v =", dot(u, v))
print("u x v =", cross(u, v))
print("||u|| =", norm(u))
print("||u||_1 =", norm(u, p=1))
print("unit u =", normalize(u))

# Angle between orthogonal vectors is pi/2.
e1 = [1, 0, 0]
e2 = [0, 1, 0]
print(f"angle(e1, e2) = {angle(e1, e2):.4f} rad ({math.degrees(angle(e1, e2)):.1f} deg)")

# Projection of [3, 4] onto the x-axis is [3, 0].
print("proj([3, 4] onto [1, 0]) =", project([3, 4], [1, 0]))
