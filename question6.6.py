from datetime import date,timedelta
import time
date_sub = int(input("Enter the days you need to subtract:"))
da= date.today() - timedelta(date_sub)
print(f"your's requested date is:{da}")
