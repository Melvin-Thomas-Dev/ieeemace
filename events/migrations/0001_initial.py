# Generated by Django 3.0.6 on 2020-06-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('event_type', models.CharField(choices=[('Competition', 'competition'), ('workshop', 'workshop'), ('webinar', 'webinar'), ('talk session', 'talk session'), ('peer to peer', 'peer to peer'), ('miscellaneous', 'miscellaneous'), ('other', 'other')], max_length=200)),
                ('slug', models.SlugField(default='slug', max_length=200, unique=True)),
                ('brief', models.CharField(blank=True, max_length=400)),
                ('description', models.TextField(default=' ')),
                ('date', models.CharField(max_length=100)),
                ('fees', models.TextField(blank=True, max_length=50)),
                ('prize', models.TextField(blank=True, max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
