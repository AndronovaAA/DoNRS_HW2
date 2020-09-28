import numpy as np

def R_z(q):
    return np.array([[np.math.cos(q), -np.math.sin(q), 0, 0],
                     [np.math.sin(q), np.math.cos(q), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def R_x(q):
    return np.array([[1, 0, 0, 0],
                     [0, np.math.cos(q), -np.math.sin(q), 0],
                     [0, np.math.sin(q), np.math.cos(q), 0],
                     [0, 0, 0, 1]])
def R_y(q):
    return np.array([[np.math.cos(q), 0, np.math.sin(q), 0],
                     [0, 1, 0, 0],
                     [-np.math.sin(q), 0, np.math.cos(q), 0],
                     [0, 0, 0, 1]])
def T_x(a):
    return np.array([[1, 0, 0, a],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def T_y(a):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, a],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def T_z(a):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, a],
                     [0, 0, 0, 1]])

def FK(q, l):
    T = np.dot(R_z(q[0]),
        np.dot(T_z(l[0]), np.dot(R_x(q[1]),
        np.dot(R_y(q[2]), np.dot(T_z(l[1]),
        np.dot(R_y(q[3]), np.dot(T_z(l[2]),
        np.dot(R_x(q[4]), np.dot(R_y(q[5]),
        T_z(l[3]))))))))))

    return T

[q1, q2, q3, q4, q5, q6] = [1.57, 0, 0, 0, 0, 0.5]
print(FK([q1, q2, q3, q4, q5, q6], [1, 1, 1, 1]))