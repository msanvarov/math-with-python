"""Vector operations using numpy."""

import numpy as np


def add(u, v):
    return np.asarray(u) + np.asarray(v)


def scale(c, v):
    return c * np.asarray(v)


def dot(u, v):
    return float(np.dot(u, v))


def cross(u, v):
    """Cross product. Only defined in 3D."""
    return np.cross(u, v)


def norm(v, p=2):
    """Lp norm of v. p=2 is Euclidean length."""
    return float(np.linalg.norm(v, ord=p))


def normalize(v):
    """Unit vector in the direction of v."""
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return v / n


def angle(u, v):
    """Angle between u and v in radians."""
    cos_theta = dot(u, v) / (norm(u) * norm(v))
    cos_theta = max(-1.0, min(1.0, cos_theta))
    return float(np.arccos(cos_theta))


def project(u, onto):
    """Vector projection of u onto the direction of `onto`."""
    onto = np.asarray(onto, dtype=float)
    return (dot(u, onto) / dot(onto, onto)) * onto
