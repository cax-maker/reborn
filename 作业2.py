import math
v0 = 17
x = 3
y = 4
z = 0.25
m = 3.2 * 10**(-3)
k = 0.038
k1 = k / m
g = 9.8
n = 20
error = 1e-6
angle = math.atan(z / s)
s = math.sqrt(x**2 + y**2)
for i in range(n):
    t = (math.exp(k1 * s) - 1) / (k1 * v0 * math.cos(angle))
    z_actual = v0 * t * math.sin(angle) - 0.5 * g * t ** 2
    dz = z - z_actual
    z += dz
    angle = math.atan(z / s)
    if abs(dz) < error:
        break
angle %= math.pi
print(f"炮台的出射角：{angle:.6f}")
