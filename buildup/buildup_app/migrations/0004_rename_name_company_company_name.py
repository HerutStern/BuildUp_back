# Generated by Django 4.1.7 on 2023-07-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildup_app', '0003_alter_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
    ]