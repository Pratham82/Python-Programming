def greeting():
  print("Hi there")


def calculate_pi(digits=5):
  """
  Calculate pi to the specified number of decimal digits using the Leibniz formula.
  For better accuracy, we'll use the Chudnovsky algorithm approximation.
  
  Args:
    digits: Number of decimal places (default is 5)
  
  Returns:
    float: Value of pi rounded to the specified digits
  """
  # Using a simple but effective series: Machin's formula
  # pi/4 = 4*arctan(1/5) - arctan(1/239)
  
  def arctan(x, num_terms=100):
    """Calculate arctan using Taylor series"""
    result = 0
    for n in range(num_terms):
      sign = (-1) ** n
      result += sign * (x ** (2 * n + 1)) / (2 * n + 1)
    return result
  
  # Machin's formula
  pi_estimate = 4 * (4 * arctan(1/5, 500) - arctan(1/239, 500))
  
  # Round to the specified number of digits
  return round(pi_estimate, digits)