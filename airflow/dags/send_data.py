import smtplib
import email.message
import email.utils


def send_email(send_from, send_to):
    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "E-mail Subject"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("This is your message.")

    smtp_obj = smtplib.SMTP("localhost")
    smtp_obj.sendmail(msg['From'], [msg['To']], msg.as_string())
    smtp_obj.quit()


send_email("zkan.cs@gmail.com", "zkan.cs@gmail.com")
