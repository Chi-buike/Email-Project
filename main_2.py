import smtplib

my_email = "egeonuchibuike2@gmail.com"
password = "yourpassword"
server = smtplib.SMTP("smtp.gmail.com", 587)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
    to_addrs="chibyecce@gmail.com",
    msg="Subject:\n\nThis is the body of the email"
    )