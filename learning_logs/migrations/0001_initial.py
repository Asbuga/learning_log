# Generated by Django 5.1.4 on 2025-01-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_created=True)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
