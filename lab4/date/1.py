from datetime import date, timedelta

print('today:', date.today())

newdate = date.today() - timedelta(5)

print('5 days before:', newdate)
