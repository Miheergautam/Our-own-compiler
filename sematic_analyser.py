"""class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, parse_tree):
        for statement in parse_tree.iter_subtrees():
            # Process each statement
            if statement.data == 'Declaration':
                # Assuming 'Declaration' is a rule in your grammar
                variable_name = statement.children[0]
                variable_type = statement.children[1]
                if variable_name in self.symbol_table:
                    print(f"Error: Variable '{variable_name}' already declared")
                else:
                    self.symbol_table[variable_name] = variable_type
                    print(f"Declaration: Variable '{variable_name}' of type '{variable_type}' is valid")"""

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node, scope="global"):
        # Recursive analysis of AST nodes
        if node["type"] == "program":
            for child in node["children"]:
                self.analyze(child, scope)

        elif node["type"] == "declaration":
            var_name = node["name"]
            var_type = node["var_type"]
            if var_name in self.symbol_table and self.symbol_table[var_name]["scope"] == scope:
                raise Exception(f"Variable '{var_name}' already declared in this scope")
            self.symbol_table[var_name] = {"type": var_type, "scope": scope}

        elif node["type"] == "assignment":
            var_name = node["name"]
            if var_name not in self.symbol_table:
                raise Exception(f"Variable '{var_name}' not declared")
            # Simple type check example
            expected_type = self.symbol_table[var_name]["type"]
            if expected_type != node["value_type"]:
                raise Exception(f"Type mismatch: Variable '{var_name}' is of type '{expected_type}', not '{node['value_type']}'")

        elif node["type"] == "binary_operation":
            left_type = self.analyze(node["left"], scope)
            right_type = self.analyze(node["right"], scope)
            if left_type != right_type:
                raise Exception("Type mismatch in binary operation")

            # Return the type for further checking
            return left_type
