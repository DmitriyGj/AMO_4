import string as str

files_dir = 'files'
file_template = str.Template(f'{files_dir}/file_$i.txt')
characters_count = 1000
files_amount = 100
results_dir = 'results'
ascii_case = str.ascii_lowercase