import ast

# Assuming this is your Python source code
source_code = """
def my_function():
    \"\"\"This is a docstring.\"\"\"
    pass
"""

# Parse the source code into an AST
module = ast.parse(source_code)

# Traverse the AST
for node in ast.walk(module):
    # Check if the current node is a function definition
    if isinstance(node, ast.FunctionDef):
        # Retrieve the docstring
        docstring = ast.get_docstring(node)
        print(docstring)
