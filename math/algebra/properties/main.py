import sympy as sym
from sympy.abc import x, y, a, b, c, d, w, z


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


# Associative Property
expr1 = x*(4*y)
expr2 = (x*4)*y
associative_result = expr1 - expr2
print("Associative Property Result:", associative_result)

# Commutative Property
e1 = x*4*y
e2 = 4*x*y
e3 = y*x*4
commutative_subs = e3.subs({x:2, y:3})
print("Commutative Property Substitution Result:", commutative_subs)

# Distributive Property
distributive_expr = (a+b)*(c+d)
distributive_expanded = sym.expand(distributive_expr)
print("Distributive Property Expanded Expression:", distributive_expanded)

# Embedding expressions
x = 3*y + z
a = 4*x
print("Embedded Expressions Result:", a)

# Exercises
w, x, y, z = sym.symbols('w, x, y, z')
x = w*(4-w) + 1/w**2 * (1+w)
expr1 = x*(y+z)
expr2 = 3/x + x**2
exercise_result = sym.simplify(expr1*expr2)
exercise_difference = expr2*expr1 - expr1*expr2

# LaTeX output to HTML files
latex_to_html(sym.latex(exercise_result), "./math/algebra/properties/exercise_result.html")
latex_to_html(sym.latex(exercise_difference), "./math/algebra/properties/exercise_difference.html")