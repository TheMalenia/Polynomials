# Polynomials

This repository contains a Python script for working with polynomials.

## Polynomial.py

`Polynomial.py` is the primary script in this repository.

### Description

This script is designed to perform operations on polynomials.

- **Polynomial Representation**: The `Polynomial` class represents a polynomial as a list of coefficients. It supports the creation of polynomials from scalars, lists, or arrays of coefficients.

- **Polynomial Operations**: The class overloads standard Python operators to provide intuitive operations between polynomials. This includes addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`).

- **Polynomial Evaluation**: The class allows for the evaluation of the polynomial at a given point using the `__call__` method.

- **Polynomial Differentiation and Integration**: The `diff` and `inl` methods provide symbolic differentiation and integration of the polynomial, respectively.

- **Root Finding**: Using Newton Raphson Method to find one root

- **Other Features**: The class also provides other features such as pretty printing of polynomials, fitting a polynomial on data, and more.
  

### Requirements

- Python 3.x

### Usage

To import the script, use the following command:

```bash
git clone https://github.com/TheMalenia/Polynomials.git
cd Polynomials
```
```python
from Polynomial import Polynomial
```
### Samples

```python
# Create a Polynomial object
p1 = Polynomial([1, 2, 3])  # Represents the polynomial 1X^2 + 2X + 3
p2 = Polynomial(2 , 3 , 0)  # Represents the polynomial 2X^2 + 3X

# Evaluate the polynomial at a point
value_at_2 = p1(2)  # Substitute x = 2 -> 11

# Addition
p3 = p1 + p2  # Represents the polynomial 3X^2 + 5X + 3

# Subtraction
p4 = p1 - p2  # Represents the polynomial -1X^2 + -1X + 3

# Multiplication
p5 = p1 * p2  # Represents the polynomial 2X^4 + 7X^3 + 12X^2 + 9X

# Division
quotient, remainder = p1 / p2  # Performs polynomial division -> 0.5 , 0.5X + 3.0

# Derivative
p6 = p1.diff(2) # get derivative for two times -> 2

# Integral
p7 = p1.inl(3) # get integral for three times -> 0.016666666666666666X^5 + 0.08333333333333333X^4 + 0.5X^3

# Print Polynomial
print(p1) # Output -> 1X^2 + 2X + 3
```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
