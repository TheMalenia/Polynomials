# Polynomials

This repository contains a Python script for working with polynomials.

## Polynomial.py

`Polynomial.py` is the primary script in this repository.

### Description

This script is designed to perform operations on polynomials.

- **Polynomial Representation**: The `Polynomial` class represents a polynomial as a list of coefficients. It supports the creation of polynomials from scalars, lists, or arrays of coefficients.

- **Polynomial Operations**: The class overloads standard Python operators to provide intuitive operations between polynomials. This includes addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`**`).

- **Polynomial Evaluation**: The class allows for the evaluation of the polynomial at a given point using the `__call__` method.

- **Polynomial Differentiation**: The `differentiate` method provides symbolic differentiation of the polynomial.

- **Root Finding**: The `zeros` method computes the roots of the polynomial using the companion matrix method.

- **Other Features**: The class also provides other features such as pretty printing of polynomials, comparison between polynomials, and more.
  

### Requirements

- Python 3.x

### Usage

To import the script, use the following command:

```bash
from Polynomial import Polynomial
```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
