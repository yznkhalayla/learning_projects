import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "smtpjustforexample@gmail.com"
MY_PASSWORD = "Coke_123"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(value.month, value.day): value for (index, value) in df.iterrows()}

number = random.randint(1, 3)
letter_file = f"letter_templates/letter_{number}.txt"

for birthday in birthdays_dict:
    if today == birthday:
        with open(letter_file) as doc:
            message = doc.read()
            message = message.replace("[NAME]", f"{birthdays_dict[birthday]['name']}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthdays_dict[birthday]['email'],
                                msg=message
                                )
