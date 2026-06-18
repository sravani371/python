#call
def send_email(to, subject, body):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

# Keyword arguments in a different order
send_email(
    subject="Meeting Reminder",
    body="Please attend the meeting at 10 AM.",
    to="alice@example.com"
)

#2
def create_profile(username, email, age):
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")

create_profile(
    email="john@example.com",
    age=21,
    username="john123"
)