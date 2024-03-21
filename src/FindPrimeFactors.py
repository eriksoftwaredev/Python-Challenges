def PrimeFactors(number):
  factor = 2
  result = []
  
  while factor <= number:
    if number % factor == 0:
      result.append(factor)
      number = number / factor
    else:
      factor = factor + 1

  return result


print(PrimeFactors(630))