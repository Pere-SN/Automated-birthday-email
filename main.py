import pandas
import datetime as dt
import smtplib
from random import randint

my_email = "mail@gmail.com"
my_password = "password"
my_name = "My Name"

# csv to dict
birth_data = pandas.read_csv("birthdays.csv")
birth_dict = birth_data.to_dict(orient="records")

# using datetime to get present time
time = dt.datetime.now()
for birthday in birth_dict:
    # checking if there is a birthday today
    if time.month == birthday["month"] and time.day == birthday["day"]:
        # selecting a letter template and replacing names
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
            custom_letter = letter.read()
            custom_letter = custom_letter.replace("[MY_NAME]", my_name)
            custom_letter = custom_letter.replace("[NAME]", birthday["name"])
        # sending the letter with smtplib
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday["email"],
                                msg=f"Subject:Happy birthday!\n\n{custom_letter}")

