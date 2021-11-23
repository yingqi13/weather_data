import datetime

#Create a list of dates that correspond to the data you would like to obtain

start_date = datetime.date(2016, 1, 1)
#No. of days from start date
number_of_days = 365

date_list = []

for day in range(number_of_days):
    date = (start_date + datetime.timedelta(days=day)).isoformat()
    date_list.append(date)

full_dates = date_list

