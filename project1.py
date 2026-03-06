import smtplib

def send_email(subject, message, sender, receiver, password):
    server = None

    try:
        email = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)

        server.sendmail(sender, receiver, email)

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Error sending email:", e)

    finally:
        if server:
            server.quit()


# -------- User Input --------
sender = input("Enter sender email: ")
receiver = input("Enter receiver email: ")
password = input("Enter app password: ")

subject = input("Enter subject: ")

print("Enter your message:")
message = input()

send_email(subject, message, sender, receiver, password)