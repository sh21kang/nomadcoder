# Generated by Django 2.0.6 on 2018-07-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-create_at']},
        ),
    ]
