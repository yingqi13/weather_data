import csv

fields = ['Date', 'Max', 'Min', 'Average', 'HDD_CDD']

filename = "daily_weather_CDDHDD.csv"

with open(filename, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)