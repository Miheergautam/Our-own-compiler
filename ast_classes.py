class ProgramNode:
  """
  Represents the entire program structure, containing a list of statements.
  """
  def __init__(self, statement_list):
    self.statement_list = statement_list

class StatementNode:
  """
  Base class for all statement nodes in the AST.
  """
  pass

class VariableDeclarationNode(StatementNode):
  """
  Represents variable declaration statements, including type and identifier.
  """
  def __init__(self, variable_type, identifier):
    self.variable_type = variable_type
    self.identifier = identifier

  def __str__(self):
    return f"VariableDeclarationNode({self.variable_type}, {self.identifier})"
  
class AssignmentNode(StatementNode):
  """
  Represents variable or array element assignment statements.
  """
  def __init__(self, identifier, expression):
    self.identifier = identifier
    self.expression = expression

  def __str__(self):
    return f"Assignment(identifier: {self.identifier}, expression: {self.expression})"
  
class ExpressionNode:
  """
  Represents an expression in the AST, potentially containing operators and operands.
  """
  def __init__(self, operands, operator=None):
    self.operands = operands
    self.operator = operator

  def __str__(self):
    if self.operator:
      operand_str = ", ".join(str(operand) for operand in self.operands)
      return f"{operand_str} {self.operator}"
    else:
      # Handle single operand case (e.g., a literal value)
      return str(self.operands[0])


  
class TypeNode:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name  # Return only the type name

class IdentifierNode:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name  # Return only the identifier value
