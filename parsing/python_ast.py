import ast


def parse_python_code(code: str):

    tree = ast.parse(code)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        # functions
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        # classes
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        # imports
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ""
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports
    }
