def get_prime_factors(num):
  prime_factors = []
  div = 2
  while div <= num:
    if num % div == 0:
      prime_factors.append(div)
      num = num // div
    else:
      div = div + 1
  
  return prime_factors


print(get_prime_factors(630))
print(get_prime_factors(13))