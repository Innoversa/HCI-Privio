import smtplib
import ssl

port = 465  # For SSL
# password = input("Type your password and press enter: ")
password = 'cdy1314.'
# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "privio.315@gmail.com"
receiver_email = "lidazhang@tamu.edu"
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("privio.315@gmail.com", password)
    # TODO: Send email here

    server.sendmail(sender_email, receiver_email, message)
