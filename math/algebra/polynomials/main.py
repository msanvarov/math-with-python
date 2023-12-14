import sympy as sym
from sympy.abc import x

def latex_to_html(latex_str, filename):
    html_content = f"""
    <html>
    <head><title>LaTeX Output</title></head>
    <body>
    <p>Rendered LaTeX:</p>
    <script type="text/javascript" async
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml.js">
    </script>
    <div style="font-size:20px" id="math-content">
    \\({latex_str}\\)
    </div>
    </body>
    </html>
    """
    with open(filename, "w") as file:
        file.write(html_content)
    print(f"LaTeX output saved to {filename}")

# Example of adding polynomials
p1 = 2*x**3 + x**2 - x
p2 = x**3 - x**4 - 4*x**2
print("Sum of polynomials (p1 + p2):", p1 + p2)

# LaTeX output to HTML file
latex_str = '(%s) + (%s) \\quad=\\quad (%s)' % (sym.latex(p1), sym.latex(p2), sym.latex(p1 + p2))
latex_to_html(latex_str, "./math/algebra/polynomials/polynomial_addition.html")

# Using the Poly class
p1 = sym.Poly(2*x**6 + x**2 - x)
print("Polynomial p1 (using Poly class):", p1)

# Methods on the polynomial object
print("p1 evaluated at 10:", p1.eval(10))
print("Degree of p1:", p1.degree())

# Creating and manipulating another polynomial
p2 = sym.Poly(x**3 - x**4 - .4*x**2)
print("Difference of polynomials (p1 - p2):", p1 - p2)
print("Subtraction using sub method:", p1.sub(p2))

# Exercise
polys = [sym.Poly(2*x + x**2), sym.Poly(-x**3 + 4*x), sym.Poly(x**5 - x**4 + 1/4*x + 4)]
for poli in polys:
    if poli.degree() % 2 == 0:
        print('The degree of %s is even, and the coefficients sum to %s.' % (poli.as_expr(), sum(poli.coeffs())))
    else:
        print('The degree of %s is odd, and there are %s coefficients.' % (poli.as_expr(), len(poli.coeffs())))
        
     
##### Multiplying polynomials #####
# Simple polynomial multiplication
simple_poly = x**2 * x**3
print("Simple polynomial multiplication:", simple_poly)

# More complex polynomial multiplication
p1 = 4*x**2 - 2*x
p2 = x**3 + 1
complex_poly = p1 * p2
expanded_complex_poly = sym.expand(complex_poly)
print("Complex polynomial multiplication:", complex_poly)
print("Expanded complex polynomial:", expanded_complex_poly)

# Polynomial multiplication with different variables
poly1 = x**5 + 2*x*y + y**2
poly2 = x - 3*x*y
multi_var_poly = poly1 * poly2
expanded_multi_var_poly = sym.expand(multi_var_poly)
print("Polynomial multiplication with different variables:", multi_var_poly)
print("Expanded polynomial with different variables:", expanded_multi_var_poly)

# Exercise: Multiplication with substitution
fxy = 4*x**4 - 9*y**3 - 3*x**2 + x*y**2
gxy = 4/5*y**3 - x**3 + 6*x**2*y
product_fxy_gxy = sym.expand(fxy * gxy)

xval = 5
yval = -2

# First substitute and then multiply
fxy_subs = fxy.subs({x: xval, y: yval})
gxy_subs = gxy.subs({x: xval, y: yval})
separate_substitution = fxy_subs * gxy_subs

# Multiply then substitute
multiplied_substitution = product_fxy_gxy.subs({x: xval, y: yval})

print("Product of fxy and gxy:", product_fxy_gxy)
print("Separate substitution result:", separate_substitution)
print("Multiplied substitution result:", multiplied_substitution)
   
##### Dividing polynomials #####
# Dividing polynomials with one variable
p1 = 4*x**5 - x
p2 = 2*x**3 - x
latex_str_div_one_var = '\\\\frac{%s}{%s} = %s' % (sym.latex(p1), sym.latex(p2), sym.latex(sym.simplify(p1/p2)))
latex_to_html(latex_str_div_one_var, "./math/algebra/polynomials/division_one_variable.html")

# Dividing polynomials with two variables
pNum = x**3 + y**2 - 4*x**2*y + x*y + 4*y
pDen = x + y
latex_str_div_two_vars = '\\\\frac{%s}{%s} = %s' % (sym.latex(pNum), sym.latex(pDen), sym.latex(sym.simplify(pNum/pDen)))
latex_to_html(latex_str_div_two_vars, "./math/algebra/polynomials/division_two_variables.html")

# Exercise
# Loop to find the integer value of y that simplifies the equation
pNum = x**6 + 2*x**4 + 6*x - y
pDen = x**3 + 3
rightnumber = None

for i in range(5, 16):
    pnum = pNum.subs({y: i})
    simplified = sym.simplify(pnum/pDen)

    if sym.fraction(simplified)[1] == 1:
        rightnumber = i
        break

print(f'When y={rightnumber}, there is no denominator!')


#### Factoring polynomials ####
# Factoring a polynomial
po = x**2 + 4*x + 3
factored_po = sym.factor(po)
print("Factored polynomial:", factored_po)

# Example where the polynomial cannot be factored
po_unfactorable = x**2 + 4*x - 3
factored_po_unfactorable = sym.factor(po_unfactorable)
print("Attempted factoring of an unfactorable polynomial:", factored_po_unfactorable)

# Factoring with multiple terms
expr = 2*y**3 - 2*y**2 - 18*y + 18
factored_expr = sym.factor(expr)
print("Factored expression with multiple terms:", factored_expr)

# Factoring with multiple variables
expr_multi_var = 2*x**3*y - 2*x**2*y**2 + 2*x**2*y + 6*x**2 - 6*x*y + 6*x
factored_expr_multi_var = sym.factor(expr_multi_var)
print("Factored expression with multiple variables:", factored_expr_multi_var)

# Exercise: Test whether expressions are factorable
exprs = [x**2 + 4*x + 3, 2*y**2 - 1, 3*y**2 + 12*y]
for expri in exprs:
    tmp = str(sym.factor(expri))
    if tmp.find('(') != -1:
        print(f'{expri} => {tmp}')
    else:
        print(f'{expri} is not factorable!')
        