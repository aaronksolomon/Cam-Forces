import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_sympy_expression(expr, x_var, y_var, x_range, y_range, sub_dict, above=None, below=None):
    """
    Plots a SymPy expression with specified values for some variables, while 
    using the remaining variables to represent the x and y axes.

    Parameters:
    -----------
    expr : sympy.Expr
        The SymPy expression to plot.
    x_var : sympy.Symbol
        The variable to be used for the x-axis.
    y_var : sympy.Symbol
        The variable to be used for the y-axis.
    x_range : tuple
        A tuple specifying the range of values for the x-axis in the form (x_min, x_max).
    y_range : tuple
        A tuple specifying the range of values for the y-axis in the form (y_min, y_max).
    sub_dict : dict
        A dictionary where the keys are SymPy Symbols and the values are the numerical values 
        to be substituted for those variables in the expression.
    above : float, optional
        If specified, highlights the region where the expression is greater than or equal to this value.
    below : float, optional
        If specified, highlights the region where the expression is less than or equal to this value.

    Returns:
    --------
    None
    """

    # Substitute the given variable values into the expression
    expr_substituted = expr.subs(sub_dict)

    # Convert the sympy expression to a lambda function for numerical evaluation
    f = sp.lambdify((x_var, y_var), expr_substituted, "numpy")

    # Create a grid of x and y values
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = np.linspace(y_range[0], y_range[1], 400)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Evaluate the function on the grid
    Z = f(X, Y)

    # Plotting the result
    plt.figure(figsize=(8, 6))
    plt.rcParams['font.family'] = 'DejaVu Sans'
    
    if above is not None:
        Z_masked = np.ma.masked_where(Z < above, Z)  # Mask regions where Z < above
        cp = plt.contourf(X, Y, Z_masked, levels=np.linspace(above, Z.max(), 50), cmap='Reds')
        plt.title(rf'${sp.latex(expr)} \geq {above}$ | ${sub_dict}$')
    elif below is not None:
        Z_masked = np.ma.masked_where(Z > below, Z)  # Mask regions where Z > below
        cp = plt.contourf(X, Y, Z_masked, levels=np.linspace(Z.min(), below, 50), cmap='Blues')
        plt.title(rf'${sp.latex(expr)} \leq {below}$ | ${sub_dict}$')
    else:
        cp = plt.contourf(X, Y, Z, levels=50, cmap='viridis')

    plt.colorbar(cp)
    plt.xlabel(rf'${str(x_var)}$')
    plt.ylabel(rf'${str(y_var)}$')
    
    plt.show()

# Example usage:
# x, y, z = sp.symbols('x y z')
# expr = sp.sin(x*y) + z

# plot_sympy_expression(expr, x, y, x_range=(0, 10), y_range=(0, 10), sub_dict={z: 1}, above=0.5)

def draw_triangle(r1, theta1, r2, theta2):
    """
    Draws a triangle with one vertex at the origin, with the first side defined
    by the polar coordinates (r1, theta1) and the second side defined by (r2, theta2).
    The triangle is drawn with a red border and a white-filled interior.

    Parameters:
    r1 (float): Radius of the first side in polar coordinates.
    theta1 (float): Angle of the first side in polar coordinates (in radians).
    r2 (float): Radius of the second side in polar coordinates.
    theta2 (float): Angle of the second side in polar coordinates (in radians).
    """
    
    # Convert polar coordinates to Cartesian coordinates
    x1, y1 = r1 * np.cos(theta1), r1 * np.sin(theta1)
    x2, y2 = r2 * np.cos(theta2), r2 * np.sin(theta2)

    # Define the vertices of the triangle
    vertices = np.array([[0, 0], [x1, y1], [x2, y2]])

    # Create the triangle with red border and white fill
    plt.figure()
    plt.fill(vertices[:, 0], vertices[:, 1], edgecolor='grey', facecolor='grey')

    # Set equal scaling
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title("Triangle")
    plt.show()

# Example usage
# draw_triangle(3, np.pi / 4, 2, np.pi / 3)

def calculate_triangle_angles(r1, theta1, r2, theta2, decimals=3):
    """
    Calculate the angles of the triangle formed by two vectors (r1, theta1) and (r2, theta2)
    with a third side connecting the endpoints of the vectors.
    
    Parameters:
    r1 (float): Magnitude of the first vector.
    theta1 (float): Angle of the first vector in radians.
    r2 (float): Magnitude of the second vector.
    theta2 (float): Angle of the second vector in radians.
    decimals (int): Number of decimal places to round the results to.
    
    Returns:
    tuple: Two numpy arrays containing the angles of the triangle, 
           one in radians and the other in degrees, rounded to the specified decimal places.
    """
    # Convert the vectors from polar to Cartesian coordinates
    x1, y1 = r1 * np.cos(theta1), r1 * np.sin(theta1)
    x2, y2 = r2 * np.cos(theta2), r2 * np.sin(theta2)
    
    # Calculate the angle at the origin
    angle_A = abs(theta2 - theta1)
    
    # Calculate the vector from the endpoint of the first vector to the endpoint of the second vector
    x3, y3 = x2 - x1, y2 - y1
    
    # Calculate the angle of this new vector
    theta3 = np.arctan2(y3, x3)
    
    # Calculate the other two angles
    angle_B = abs(theta1 - theta3)
    angle_C = abs(theta2 - theta3)
    
    # Ensure the angles are within the correct range
    angle_A = angle_A % (2 * np.pi)
    angle_B = angle_B % (2 * np.pi)
    angle_C = angle_C % (2 * np.pi)
    
    # Create numpy arrays for the angles in radians and degrees
    angles_radians = np.array([angle_A, angle_B, angle_C])
    angles_degrees = np.degrees(angles_radians)
    
    # Round the results to the specified number of decimal places
    angles_radians_rounded = np.round(angles_radians, decimals=decimals)
    angles_degrees_rounded = np.round(angles_degrees, decimals=decimals)
    
    return angles_radians_rounded, angles_degrees_rounded

# Example usage
# r1, theta1 = 4, math.radians(10)  # Example values in polar coordinates
# r2, theta2 = 6, math.radians(60)

# angles_radians, angles_degrees = calculate_triangle_angles(r1, theta1, r2, theta2)
# #print("Angles of the triangle (in radians):", angles_radians)
# print("Angles of the triangle (in degrees):", angles_degrees)