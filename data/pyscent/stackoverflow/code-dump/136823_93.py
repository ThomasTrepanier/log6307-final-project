import csv

def get_csv_file_lines(file):
   with open(file, 'r', encoding='utf-8') as csv_file:
      rows = csv.reader(csv_file)
      for row in rows:
         yield row

def compare_csv_files_line_by_line(csv_file_one, csv_file_two):
   csvfile_02 = get_csv_file_lines(csv_file_two)
   for line_one in get_csv_file_lines(csv_file_one):
      line_two = csvfile_02.__next__()
      if line_two != line_one:
        print('File names being compared:')
        print(f'csv_file_one: {csv_file_one}')
        print(f'csv_file_two: {csv_file_two}')
        print(f'The following rows have difference in the files being compared.')
        print('csv_file_one:', line_one)
        print('csv_file_two:', line_two)
        print('\n')
