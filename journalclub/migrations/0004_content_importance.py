# Generated by Django 4.1.2 on 2022-10-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalclub', '0003_content_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='importance',
            field=models.IntegerField(default=0),
        ),
    ]