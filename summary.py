import os

from constants import results_dir

def summuary_results():
    total_count = 0
    result_files = os.listdir(results_dir)
    for file in result_files:
        with open(os.path.join(results_dir, file), 'r') as f:
            total_count += int(f.read())
    print(f'Total count of "a": {total_count}')

summuary_results()