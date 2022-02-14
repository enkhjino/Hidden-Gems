# Generated by Django 4.0.2 on 2022-02-14 21:51

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
            name='Gem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('picture', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('B', 'Business'), ('T', 'Trail'), ('R', 'Ruins'), ('L', 'Landmark')], default='Trail', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
