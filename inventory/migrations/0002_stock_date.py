# Generated by Django 5.1.4 on 2025-01-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]