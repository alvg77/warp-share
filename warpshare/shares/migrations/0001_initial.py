# Generated by Django 4.2 on 2023-04-16 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=1000)),
                ('shared_at', models.DateTimeField(auto_now=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
