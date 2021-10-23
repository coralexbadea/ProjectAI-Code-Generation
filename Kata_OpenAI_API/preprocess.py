
			
			
import csv
with open('./kata_dataset_csv', 'r') as inp, open('./kata_dataset_csv_edit', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if len(row[2]) > 10:
        	
            writer.writerow(row)
