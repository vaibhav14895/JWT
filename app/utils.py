
from django.core.mail import send_mail
from django.conf import settings
def send_email_to_user(useremail,parameter):
    subject="Reset password"
    message=f"http://127.0.0.1:8000/change_password/{parameter}"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[f"{useremail}"]
    send_mail(subject,message,from_email,recipient_list)