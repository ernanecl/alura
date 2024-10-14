PI = 3.14159

def area(raio):
  """Calcula a área de um círculo.

  Args:
    raio: O raio do círculo.

  Returns:
    A área do círculo.
  """
  return PI * (raio ** 2)

def comprimento_circunferencia(raio):
  """Calcula o comprimento da circunferência de um círculo.

  Args:
    raio: O raio do círculo.

  Returns:
    O comprimento da circunferência.
  """
  return 2 * PI * raio