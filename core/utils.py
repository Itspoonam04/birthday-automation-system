# from datetime import date
# from django.core.mail import send_mail
# from .models import Customer

# def send_birthday_emails():
#     today = date.today()

#     customers = Customer.objects.filter(
#         dob__day=today.day,
#         dob__month=today.month,
#         consent=True
#     )

#     print("Birthday job running...")
#     print("Customers found:", customers.count())

#     for customer in customers:
#         print("Sending birthday email to:", customer.email)

#         send_mail(
#             subject="🎉 Happy Birthday from Bake House!",
#             message=f"""
# Hi {customer.name} 🎂

# Wishing you a very Happy Birthday!
# Celebrate your day with a special cake from us 🍰

# – Bake House
# """,
#             from_email="Bake House <yourshop@gmail.com>",
#             recipient_list=[customer.email],
#             fail_silently=False,
#         )

from datetime import date
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer, EmailTemplate

def send_birthday_emails():
    today = date.today()

    customers = Customer.objects.filter(
        dob__day=today.day,
        dob__month=today.month,
        consent=True
    )

    template = EmailTemplate.objects.filter(active=True).first()
    if not template:
        return

    for customer in customers:
        unsubscribe_link = f"http://127.0.0.1:8000/unsubscribe/{customer.unsubscribe_token}/"

        message = template.body.replace("{{name}}", customer.name)
        message += f"\n\nTo unsubscribe, click here:\n{unsubscribe_link}"

        send_mail(
            subject=template.subject,
            message=message,
            from_email="Bake House <yourshop@gmail.com>",
            recipient_list=[customer.email],
            fail_silently=False,
        )

