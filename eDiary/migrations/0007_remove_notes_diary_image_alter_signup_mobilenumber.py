# Generated by Django 5.0.6 on 2024-09-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eDiary', '0006_delete_audiotext_notes_diary_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='diary_image',
        ),
        migrations.AlterField(
            model_name='signup',
            name='mobileNumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]