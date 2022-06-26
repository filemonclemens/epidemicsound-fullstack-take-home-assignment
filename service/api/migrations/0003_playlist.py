# Generated by Django 3.2.13 on 2022-06-26 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_fetch_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('tracks', models.ManyToManyField(related_name='track', through='api.Listing', to='api.Track')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.playlist'),
        ),
        migrations.AddField(
            model_name='listing',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.track'),
        ),
    ]
