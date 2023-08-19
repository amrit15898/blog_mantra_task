from django.core.mail import send_mail

def send_mail_to_user(subject, message, from_email, recipient_email):
    print("running email function")
    send_mail(subject, message, from_email, [recipient_email])
