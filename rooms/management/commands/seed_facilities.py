from django.core.management.base import BaseCommand, CommandError
from rooms.models import Facility
class Command(BaseCommand):
    print("hello")

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many time do you wnat me to tell you that i love you?"
        )

    def handle(self, *args, **options):
        facilites = [
            "건물 내 무료 주차",
            "헬스장",
            "자쿠지",
            "수영장",
        ]
        for f in facilites:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilites)} facilites created"))
