# Generated by Django 4.1.2 on 2022-10-27 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifa22_app', '0002_alter_fixture_result_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestions',
            name='point',
            field=models.IntegerField(null=True),
        ),
    ]
