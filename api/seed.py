from faker import Faker
from faker.providers import date_time

import random

from .models import User, Card, Transaction

fake = Faker()


def seed_data():
    users = []
    for _ in range(1,10):
        user = User(first=fake.first_name(),
                    last=fake.last_name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    approved_seller=True,
                    business_name=fake.company(),
                    business_address=fake.address(),
                    business_city=fake.city(),
                    business_state=fake.state(),
                    business_phone=fake.phone_number(),
                    business_zip='97229'
                    )
        user.save()
        users.append(user)

    for _ in range(1,10):
        card = Card(business=random.choice(users),
                    creation_date=fake.date_between(start_date='-100d', end_date='now'),
                    website=fake.url(),
                    phone=fake.phone_number(),
                    address=fake.address(),
                    city=fake.city(),
                    state=fake.state(),
                    zip='97229',
                    )
        card.save()
    