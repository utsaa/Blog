# Generated by Django 4.0 on 2021-12-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=13)),
                ('content', models.TextField(default='')),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]