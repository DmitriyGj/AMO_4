import os

from constants import files_dir, results_dir

def count_a_in_file(file_path):
  with open(file_path, 'r') as f:
    count = sum(1 for line in f for char in line if char == 'a')
  result_file = os.path.join(results_dir, os.path.basename(file_path).replace('.txt', '.res'))
  with open(result_file, 'w') as f:
    f.write(str(count))

def count_every_file():
  os.makedirs(results_dir, exist_ok=True)
  for file in os.listdir(files_dir):
    if file.endswith('.txt'):
      count_a_in_file(os.path.join(files_dir, file))

count_every_file()