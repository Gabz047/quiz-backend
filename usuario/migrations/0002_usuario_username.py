# Generated by Django 5.0.7 on 2024-07-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]