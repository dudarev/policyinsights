# Generated by Django 2.0.2 on 2018-03-03 18:50

import annoying.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramImportance',
            fields=[
                ('program', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='importance', serialize=False, to='programs.Program')),
            ],
        ),
    ]
