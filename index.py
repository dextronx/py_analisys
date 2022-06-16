import csv
from datetime import date

current_date = date.today().strftime("%Y-%m-%d")

with open('TWITTER.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('analisis_archivo.csv', 'a') as analisis_file:
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                
                current_concept = 'SUBE' if (float(row[4]) - float(row[1]) > 0) else 'BAJA'
                current_open_hight = str(abs(float(row[1]) - float(row[2])))
                analisis_file.writelines(  current_date + ' ' + current_concept + ' ' + current_open_hight + "\n")
                line_count += 1
    
    print(f'Processed {line_count} lines.')