def sort_string(input_text):
  output = sorted(input_text.split(), key=str.upper)
  return output

print(sort_string("banana ORANGE apple"))