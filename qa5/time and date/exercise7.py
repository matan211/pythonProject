#yesterday, today, tommorow
from datetime import datetime, timedelta

yesterday = datetime.today() - timedelta(days=1)
today = datetime.today()
tommorow = datetime.today() + timedelta(days=1)
print(yesterday)
print(today)
print(tommorow)
