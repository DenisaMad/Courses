# Generated by Django 5.1.7 on 2025-04-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ProfesoriApp", "0002_profesori_an_universitae"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesori",
            name="salary",
            field=models.FloatField(default=4000, max_length=10),
        ),
    ]
