#subtract five days from current date
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=5)
print(d)
