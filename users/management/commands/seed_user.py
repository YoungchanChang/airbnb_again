from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User
from faker import Faker

class Command(BaseCommand):
    print("hello")

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )




    def handle(self, *args, **options):
        number = options.get("number")

        seeder = Seed.seeder(locale='ko_KR')
        faker = Faker('ko_KR')

        seeder.add_entity(User, number, {
            "first_name": lambda x: faker.name()[0:1],
            "last_name": lambda x: faker.name()[1:4],
            "is_staff": False,
            "is_superuser": False
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))