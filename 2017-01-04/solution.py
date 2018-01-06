def productExceptI(list):
  if len(list) == 1:
    return [0]

  products_lower = []
  p_lower = 1
  for i in list:
    products_lower.append(p_lower)
    p_lower *= i

  products_higher = []
  p_higher = 1
  for i in list[::-1]:
    products_higher.append(p_higher)
    p_higher *= i

  products_higher = products_higher[::-1]

  products = []
  for i in range(0, len(list)):
    products.append(
      products_lower[i] * products_higher[i]
    )

  return products
