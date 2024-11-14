import random
import os

from constants import files_dir, files_amount, file_template, characters_count, ascii_case


def generate_files():
  os.makedirs(files_dir, exist_ok=True)
  for i in range(files_amount):
    with open(file_template.substitute(i=i), 'w') as f:
      characters = ''.join(random.choices(ascii_case, k=characters_count)) 
      f.write(characters)

generate_files()