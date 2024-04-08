## Beam Deflection Calculation

A simply supported beam is subjected to a non-uniform load whose intensity increases linearly along its length. Let \(x\) be the distance along the beam axis. The beam has a length \(L\) and is supported at \(x = 0\) and \(x = L\). The deflection that the beam undergoes in the vertical direction is a function of the position \(x\). The point \(x\) at which the deflection is maximum is a solution of the equation:

-(w_max / (360 * E * I * L)) * (15x^4 - 30L^2x^2) = (w_max / (360 * E * I * L)) * 7L^4


where:

- \(x\) is the distance along the beam axis (in centimeters [cm]);
- \(L\) is the length of the beam (in meters [m]);
- \(w_max\) is the intensity of the load in the vertical direction per unit length (in Newton per centimeter [N/cm]);
- \(E\) is the Young's modulus (in Newton per square centimeter [N/cm²]);
- \(I\) is the moment of inertia of the cross-sectional area of the beam (in centimeter to the fourth power [cm⁴]).

Consider a beam with parameters \(L = 450\) cm, \(w_max\) = 1.75 \times 10^3\) N/cm, \(E = 50 \times 10^6\) N/cm², and \(I = 30 \times 10^3\) cm⁴. Calculate the point \(x\) where the deflection is maximum by developing the following steps:

1. Find the function \(H(x)\) for the calculation of \(x\).
2. Write a code that plots \(H(x)\) and use it to obtain an initial approximation \(x_0\) for \(x\).
3. In the same code, implement the Newton's method to find an approximation for \(x\). Use \(x_0\) as the initial estimate and \(|H(x)| < 10^{-9}\) as the stopping criterion.
