import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email)

# Test the function:
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'recipient_email@example.com'
subject = 'Subject of the email'
message = 'This is the message content.'

send_email(sender_email, sender_password, receiver_email, subject, message)
