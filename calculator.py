def addition(a,b):
  if(isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float)):
    return a + b
  else:
    print("Input is invalid")
    return None

def subtraction(a,b):
  if(isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float)):
    return a - b
  else:
    print("Input is invalid")
    return None

def multiplication(a,b):
  if(isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float)):
    return a * b
  else:
    print("Input is invalid")
    return None
  
def division(a,b):
  if(isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float)):
    if(b == 0):
      print("Cannot divide by 0")
      return None
    return a / b
  else:
    print("Input is invalid")
    return None
