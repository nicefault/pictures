# Generated by Django 4.2.1 on 2023-05-03 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('like', models.IntegerField(default=0)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo')),
            ],
        ),
    ]