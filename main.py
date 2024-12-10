import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
recipient = os.getenv("RECIPIENT")




f = open("quotes.txt", "r")
content = f.readlines()

random_number = random.randint(0, len(content)) # Picks a random number from the length of the quotes list
random_quote = content[random_number] # Picks the quote on the position of the random number

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = dt.datetime.now()
weekday = now.weekday()

print(weekday)

today = days_of_week[weekday]


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="augustsletto@yahoo.com", 
        msg=f"Subject:{today} motivation\n\n{random_quote}")
