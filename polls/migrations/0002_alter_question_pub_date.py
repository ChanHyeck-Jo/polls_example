# Generated by Django 4.2.1 on 2023-05-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateField(verbose_name="date published"),
        ),
    ]
