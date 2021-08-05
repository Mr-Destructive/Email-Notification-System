from datetime import date

from django.core.management import BaseCommand

from api.models import ScheduledMail

class Command(BaseCommand):

	def handle(self, *args, **options):
            today_mail = ScheduledMail.get_today_mail()
            for mail_message in today_mail:
                    mail_message.send_scheduled_mail()
