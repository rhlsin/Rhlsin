import newww
import mailer
import forecast

def get_emails():
    emails = {}

    try:
        email_file = open('emails.txt','r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)
    return emails


def get_schedule():
    try:
        schedule_file = open('schedule.txt','r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return(schedule)








def mainio():
    emails = get_emails()


    schedule = get_schedule()

    forecast = newww.get_weather_forecast()

    mailer.send_emails(emails,schedule,forecast)

mainio()




