from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from main.models import Customer, Mailing, Attempt


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        mail_list = []
        for customer in Customer.objects.all():
            mail_list.append(str(customer.email))

        for mail in Mailing.objects.all():
            message1 = mail.message
            message = Mailing.objects.filter(subject=message1)
            for i in message:
                send_mail(
                    subject=i.subject,
                    message=i.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*mail_list],
                )
                status_list = []
                server_response = {
                    'sending': Mailing.objects.get(pk=mail.id),
                    'status': Attempt.DELIVERED,
                    'response': [*mail_list]}
                status_list.append(Attempt(**server_response))
                Attempt.objects.bulk_create(status_list)
                if mail.frequency == Mailing.ONCE:
                    mail.status = Mailing.COMPLETED
                    mail.save()
                else:
                    mail.status = Mailing.LAUNCHED
                    mail.save()
