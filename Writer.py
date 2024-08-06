import csv
import Scraper
import Central_time

data_to_append = [[str(Central_time.getTime()), str(Scraper.getNumber())]]

file = open('ActBlue.csv' , "a", newline = "")
writer = csv.writer(file)

writer.writerows(data_to_append)

file.close()