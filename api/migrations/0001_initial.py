# Generated by Django 2.0.3 on 2019-02-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrudItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=256, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]