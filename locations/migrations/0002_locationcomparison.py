# Generated by Django 2.0.2 on 2018-04-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationComparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparison_1', to='locations.Location')),
                ('object_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparison_2', to='locations.Location')),
            ],
        ),
    ]
