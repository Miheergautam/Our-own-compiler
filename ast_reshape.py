from lark import Transformer
from ast_classes import *

class ASTTransformer(Transformer):
  
  def statement_list(self, children):
    return [self.transform(child) for child in children]

  def declaration_statement(self, children):
    type_name = None
    identifier = None
    for child in children:
        if child.type == "IDENTIFIER":  # Assuming IDENTIFIER type for identifier
            identifier = IdentifierNode(child.value)
        elif child.type == "NUM":  # Assuming a custom type for type name
            type_name = TypeNode(child.value)  # Access type name from custom type class
        elif child.type == "STR":
            type_name = TypeNode(child.value)
        elif child.type == "BOOL":
            type_name = TypeNode(child.value)
    return VariableDeclarationNode(type_name, identifier)
  
  def assignment_statement(self, children):
    # Assuming children are ["identifier", "=", expression, ";"]
    identifier = None
    expression = None
    for child in children:
      if child.type == "IDENTIFIER":
        identifier = IdentifierNode(child.value)
      elif child.type == "expression":
        expression = self.transform(child)
    return AssignmentNode(identifier, expression)

  def expression(self, children):
    """
    This method handles basic expressions (consider extending for more complex cases)
    """
    operator = None
    operands = []
    for child in children:
      if child.type in ("NUM", "IDENTIFIER", "expression"):  # Assuming operand types
        operands.append(self.transform(child))
      elif child.type == "OPERATOR":  # Assuming operator type
        operator = child.value
    return ExpressionNode(operands, operator)