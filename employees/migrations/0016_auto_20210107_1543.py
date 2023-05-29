# Generated by Django 3.1.4 on 2021-01-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20210107_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='counseling',
            name='uploaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='email_settlement_doc_day10',
            field=models.BooleanField(default=True, help_text='Receive an email when it has been 10 or more days sincea settlement was created but a signed documenthas not been uploaded', verbose_name='10 Days Past Due Settlement'),
        ),
        migrations.AddField(
            model_name='employee',
            name='email_settlement_doc_day3',
            field=models.BooleanField(default=True, help_text='Receive an email when it has been 3 or more days sincea settlement was created but a signed documenthas not been uploaded', verbose_name='3 Days Past Due Settlement'),
        ),
        migrations.AddField(
            model_name='settlement',
            name='uploaded',
            field=models.BooleanField(default=False),
        ),
    ]