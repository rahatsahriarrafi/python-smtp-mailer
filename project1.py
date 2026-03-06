import smtplib

def send_email(subject, message, from_email, to_email, password):
    server = None
    try:
        # Create email content
        email_message = f"Subject: {subject}\nFrom: {from_email}\nTo: {to_email}\n\n{message}"

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to email
        server.login(from_email, password)

        # Send email
        server.sendmail(from_email, to_email, email_message)

        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        if server:                                                                                                                                                                                                
            server.quit()


# ---- User Input Section ----
subject = input("Enter subject: ")
message = input("Enter message: ")
from_email = input("Enter your email: ")
to_email = input("Enter receiver email: ")
password = input("Enter your app password: ")

send_email(subject, message, from_email, to_email, password)