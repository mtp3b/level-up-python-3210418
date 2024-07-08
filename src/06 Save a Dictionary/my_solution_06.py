import json

def save_dictionary(dict, file_path):
  f = open(file_path, 'w')
  f.write(json.dumps(dict))
  f.close()

def open_dictionary(file_path2):
  o = open(file_path2, 'r')
  contents = o.read()
  retrieved_dict = json.loads(contents)
  return retrieved_dict