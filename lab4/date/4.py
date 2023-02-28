from datetime import date, timedelta



newdate = date.today() - timedelta(5)
x = date.today() - newdate
print("two date difference in seconds:", x.total_seconds(), "s")


