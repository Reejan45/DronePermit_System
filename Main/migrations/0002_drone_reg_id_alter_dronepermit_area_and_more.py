# Generated by Django 4.1.7 on 2023-07-14 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='reg_id',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Drone Registration No.'),
        ),
        migrations.AlterField(
            model_name='dronepermit',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.area'),
        ),
        migrations.AlterField(
            model_name='dronepermit',
            name='drone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.drone'),
        ),
        migrations.AlterField(
            model_name='dronepermit',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.owner'),
        ),
    ]
