def find_index(given_list, value):
  indices = []
  for i, v in enumerate(given_list):
    #print(f'index is: {i} and value is: {v}')
     if v == value:
       indices.append([i])
    
  return indices

print(find_index([1,2,2,3], 2))
