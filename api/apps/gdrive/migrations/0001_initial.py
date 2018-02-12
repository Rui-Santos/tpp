# Generated by Django 2.0 on 2018-02-08 23:34

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(upload_to='maps')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agencies.Agency')),
            ],
        ),
    ]
