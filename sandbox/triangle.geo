// Define points
Point(1) = {0, 0, 0, 1};
Point(2) = {1, 0, 0, 1};
Point(3) = {0, 1, 0, 1};

// Define lines
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 1};

// Define the loop and surface
Line Loop(1) = {1, 2, 3};
Plane Surface(1) = {1};

// Define a mesh size field to control element size globally
Field[1] = MathEval;
Field[1].F = "0.05";  // Set global mesh element size to 0.05

// Apply the field to the whole geometry
Background Field = 1;

Mesh 2;