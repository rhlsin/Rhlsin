import  smtplib

def send_emails(emails, schedule, forecast):
    # connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com','587')

    #start TLS encryption
    server.starttls()

    # Login
    password = 'python?12'
    from_email = 'jspaow112@gmail.com'
    server.login(from_email, password)

    # send msg to entire email list
    for to_email,name in emails.items():
         message = "Subject: Schedule for today:\n\n"
         message += 'Hi ' + name + ':\n\n'
         message += "=========== Current Weather Statistics ========="+'\n\n'
         message += forecast + '\n\n'
         message+= "=========== Today's Schedule ========="+'\n\n'
         message += schedule + '\n\n'
         server.sendmail(from_email, to_email, message)

    server.quit()