from datetime import datetime, timedelta
import time
given_date = datetime(2023,1,22,12,50,0)
date_add = int(input("ENTER THE DAYS YOU NEED TO ADD:"))
da = given_date + timedelta(date_add,hours=12)
print(f"your's requested date is:{da}")
