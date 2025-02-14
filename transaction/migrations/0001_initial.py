# Generated by Django 5.1.4 on 2025-01-03 14:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('47ff6210-201c-4334-ba4d-f8e53346dd0f'), primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=11, unique=True)),
                ('adress', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('gstn', models.CharField(max_length=15, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
