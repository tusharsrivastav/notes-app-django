# Generated by Django 2.2.2 on 2019-06-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
