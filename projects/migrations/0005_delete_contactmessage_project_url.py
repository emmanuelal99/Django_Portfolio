# Generated by Django 5.1.6 on 2025-04-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactMessage',
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
