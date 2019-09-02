import numpy as np

def Rx(theta,V):
    """
    Rotation of a 3d vector V
    of an angle theta around
    the x-axis
    """
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.matrix(
        [[1, 0, 0], 
         [0, c, -s], 
         [0, s, c]]
    )
    return R*V


def Ry(theta,V):
    """
    Rotation of a 3d vector V
    of an angle theta around
    the y-axis
    """
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.matrix(
        [[c, 0, s],
         [0, 1, 0],
         [-s, 0, c]]
    )
    return R*V


def Rz(theta,V):
    """
    Rotation of a 3d vector V
    of an angle theta around
    the z-axis
    """
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.matrix(
        [[c, -s, 0], 
         [s, c, 0],
         [0, 0, 1]]
    )
    return R*V


#print("My name is", __name__)


if __name__ == "__main__":
    print("A little demo of how the functions in this module can be used:")
    V = np.matrix([[1],[2],[3]])
    print("Original vector V:\n" + str(V))
    V1 = Rx(np.pi/2.,V)
    print("V rotated of pi/2 araund the x-axis: Rx(np.pi/2.,V)\n" + str(V1))
    V2 = Rz(np.pi/4,V)
    print("V rotated of pi/4 araund the z-axis: Rz(np.pi/4.,V)\n" + str(V2))
    

