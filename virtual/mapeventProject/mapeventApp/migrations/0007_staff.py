# Generated by Django 4.0.5 on 2022-06-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeventApp', '0006_delete_make_alter_event_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122)),
                ('last_name', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
            ],
        ),
    ]
