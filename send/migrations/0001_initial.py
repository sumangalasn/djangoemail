# Generated by Django 4.1.7 on 2023-02-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sentmail',
            fields=[
                ('sent_email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('subject', models.TextField(max_length=100)),
                ('text', models.CharField(max_length=40)),
                ('from_email', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'send',
            },
        ),
    ]
