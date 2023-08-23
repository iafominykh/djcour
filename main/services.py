from django.conf import settings
from django.core.mail import send_mail

from main.models import Customer, Mailing, Message, Attempt


def send_email(*args):
    mail_list = []
    for customer in Customer.objects.all():
        mail_list.append(str(customer.email))

    for mail in Mailing.objects.all():
        if mail.status == Mailing.CREATED and mail.frequency == (str(*args)):
            message_for_filter = mail.message
            message = Message.objects.filter(subject=message_for_filter)
            for i in message:
                send_mail(
                    subject=i.subject,
                    message=i.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*mail_list],
                )
                status_list = []
                server_response = {
                    'mailing': Mailing.objects.get(pk=mail.id),
                    'status': Attempt.DELIVERED,
                    'server_response': [*mail_list]}
                status_list.append(Attempt(**server_response))
                Attempt.objects.bulk_create(status_list)
                if mail.frequency == Mailing.ONCE:
                    mail.status = Mailing.COMPLETED
                    mail.save()
                else:
                    mail.status = Mailing.LAUNCHED
                    mail.save()
