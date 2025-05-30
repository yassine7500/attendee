# Generated by Django 5.1.2 on 2025-04-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0024_alter_credentials_credential_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='credential_type',
            field=models.IntegerField(choices=[(1, 'Deepgram'), (2, 'Zoom OAuth'), (3, 'Google Text To Speech'), (4, 'Gladia'), (5, 'OpenAI')]),
        ),
        migrations.AlterField(
            model_name='recording',
            name='transcription_provider',
            field=models.IntegerField(blank=True, choices=[(1, 'Deepgram'), (2, 'Closed Caption From Platform'), (3, 'Gladia'), (4, 'OpenAI')], null=True),
        ),
    ]
