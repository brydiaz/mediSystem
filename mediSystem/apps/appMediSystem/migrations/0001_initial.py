# Generated by Django 3.0.5 on 2021-04-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEbais', models.CharField(max_length=100)),
                ('ubicacionEbais', models.CharField(max_length=300)),
                ('capacidadEbais', models.IntegerField()),
            ],
        ),
    ]
