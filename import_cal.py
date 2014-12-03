import os, django, csv
os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
import datetime as D
from datetime import datetime
from calender.models import Events

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
csvfile = os.path.join(ROOT_DIR,'AH_calendar_web.csv')

def main():
	migrate_events(csvfile)
	
def migrate_events(csvfile):
	with open(csvfile,'rd') as f:
		reader = csv.reader(f)
		reader.next()
		for row in reader:
			council = row[0][0].lower()
			group = row[1]
			color = get_color(row[2])
			school = row[3]
			location = row[4]
			eventdate = convert_date(str(row[5]))
			start = str(datetime.strptime(row[6],"%I:%M:%S %p")).replace('1900-01-01 ',"")
			end = str(datetime.strptime(row[7], "%I:%M:%S %p")).replace("1900-01-01 ",'')
			event, created = Events.objects.get_or_create(council=council, group=group, color=color, school=school, location=location, eventdate=eventdate, start=start, end=end)

def get_color(item):
	colors = {}
	colors['red'] = '#ef4a2d'
	colors['blue'] = '#1ca6bc'
	colors['orange'] = '#f99e35'
	colors['green'] = '#87be62'
	return colors[item]

def convert_date(dateString):
	splits = dateString.split('/')
	return D.date(int(splits[2]), int(splits[0]), int(splits[1]))

if __name__ == "__main__":
	main()
