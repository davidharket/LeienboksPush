import smtplib
import os


class Message:
    def __init__(self):
        self.my_email = "leienboks@gmail.com"
        self.my_password = os.environ.get("APP_PASSWORD")
        print(self.my_password)
    def send_self(self, email, days, date, address, message):
        print(f"your password is :{self.my_password}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                 from_addr=self.my_email,
                 to_addrs=self.my_email,
                 msg=f"Subject: Melding Fra:\n\n"
                     f" E-post: {email}\n\n"
                     f" Antall dager: {days}\n"
                     f" Fra denne datoen: {date}\n"
                     f" Til denne addressen: {address}\n"
                     f" Ekstra beskjed: {message}"
            )

    def send_cus(self, email, days, date, address, message):
        print(email, days, date, address, message)
        print(email, days, date, address, message)
        print(self.my_password)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            print(email, days, date, address, message)
            connection.login(user=self.my_email, password=self.my_password)
            content = f"Subject: Takk for din bestilling!:\n\n"\
                      f"En kundebehandler kontakter deg straks.\n\n"\
                      f"Informasjon om bestillingen\n"\
                      f"Antall dager: {days}\n"\
                      f"Fra denne datoen: {date}\n"\
                      f"Til denne addressen: {address}\n"\
                      f"Ekstra beskjed:{message}\n"
            connection.sendmail(
                 from_addr=self.my_email,
                 to_addrs=f"{email}",
                 msg=content
            )
