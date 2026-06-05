# Vectors

Vectors are ordered tuples of numbers that can be added, scaled, and compared geometrically through dot and cross products.

## Concepts

- **Addition and scalar multiplication** — the two operations that define a vector space.
- **Dot product** — `u . v = sum(u_i * v_i)`. Zero when vectors are orthogonal.
- **Cross product** — defined in 3D; produces a vector perpendicular to both inputs.
- **Norm (length)** — `||v||_p = (sum |v_i|^p)^(1/p)`. The 2-norm is the Euclidean length.
- **Unit vector** — `v / ||v||`. Has length 1.
- **Angle between vectors** — `cos(theta) = (u . v) / (||u|| ||v||)`.
- **Projection** — the component of one vector along the direction of another.

## Files

- `vectors.py` — `add`, `scale`, `dot`, `cross`, `norm`, `normalize`, `angle`, `project`.
- `main.py` — examples covering each operation.

## Usage

```bash
python math/linear_algebra/vectors/main.py
```
