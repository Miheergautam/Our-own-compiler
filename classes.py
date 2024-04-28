from lark import Transformer

class ExtractAST(Transformer):
    def declaration_statement(self, elements):
        return {"Statement": "Declaration", "name": elements[0].value, "type": elements[1].value}

    def assignment_statement(self, elements):
        return {"Statement": "Assignment", "name": elements[0].value, "expression":elements[2]}

    def expression(self, elements):
        # Assuming a simple binary expression
        if len(elements) == 3:
            left, operator, right = elements
            return {"Statement": "BinaryOp", "operator": operator.value, "left": left.value, "right": right.value}
        else:
            return elements[0]
            
        
    def output_statement(self, elements):
        return {"Statement": "Output", "argument": elements[0].value}
    
    def conditional_statement(self, elements):
        condition, if_body, else_body = elements
        return {
            "Statement": "Conditional",
            "if_condition": condition,
            "if_branch": self.transform(if_body),  # Transform nested statements
            "else_branch": self.transform(else_body) if else_body else None
        }