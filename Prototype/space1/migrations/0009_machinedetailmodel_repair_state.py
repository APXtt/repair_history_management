# Generated by Django 4.2 on 2023-05-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space1', '0008_alter_machinedetailmodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetailmodel',
            name='repair_state',
            field=models.CharField(choices=[('B', '수리전'), ('A', '수리후')], default='B', max_length=1),
        ),
    ]
