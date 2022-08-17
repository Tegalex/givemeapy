import datetime

from datetime import date, time
#from datetime import time

now = datetime.datetime.now()
print("Il giorno e l'ora in questo momento: " +str(now))

day=date.today()
#day=time()
print("Oggi è il " +str(day))
