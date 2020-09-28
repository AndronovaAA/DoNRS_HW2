import numpy as np

[l0, l1, l2, l3]=[1, 1, 1, 1]

def T_z(a):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, a],
                     [0, 0, 0, 1]])

def IK(T):
    R = np.array(
        [[T[0, 0], T[0, 1], T[0, 2]],
        [T[1, 0], T[1, 1], T[1, 2]],
        [T[2, 0], T[2, 1], T[2, 2]]])

    coord_ankle = np.array([T[0, 3], T[1, 3], T[2, 3]])

    x = coord_ankle[0]
    y = coord_ankle[1]
    z = coord_ankle[2]

    z = z - l0

    q6 = np.arccos((x ** 2 + z ** 2 - (l1+l2)**2 - l3**2)/(2*(l1+l2)*l3))
    print("q6", q6)

    l05 = np.sqrt((x+l3*R[0,2])**2 + (y+l3*R[1,2])**2 + (z+l3*R[2,2])**2)
    print("l05", l05)
    #q4 = np.arccos((l05 **2 - l1**2 -l2**2)/(2*l1*l2))
    #print(((l05 **2 - l1**2 -l2**2)/(2*l1*l2)))
    #print("q4", q4)

    phi1 = np.arccos((-np.sqrt(x ** 2 + z ** 2) - (l1+l2)**2 + l3**2)/(-2*(l1+l2)*np.sqrt(x**2 + z**2)))
    phi2 = np.arctan(-z/x)

    phi3 = np.arctan((2*np.sin(q6)*l3*(l1+l2))/(x**2 + z**2 +(l1+l2)**2-l3**2))

    q3 = phi3+phi2
    return(q6, q3)

H = np.array([[ 6.98842435e-04, -9.99999683e-01,  3.81779362e-04,  3.81779362e-04],
               [ 8.77582284e-01,  7.96326711e-04,  4.79425387e-01,  4.79425387e-01],
               [-4.79425539e-01,  0.00000000e+00,  8.77582562e-01,  3.87758256e+00],
               [0,  0,  0,  1]])

print(IK(H))