# Generated by Django 3.1.5 on 2021-05-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0013_auto_20210531_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movementpass',
            options={'verbose_name': 'Movement Pass', 'verbose_name_plural': 'Movement Pass'},
        ),
        migrations.AddField(
            model_name='movementpass',
            name='created_at',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]