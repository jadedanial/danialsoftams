# Generated by Django 4.0.3 on 2022-09-03 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0002_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(max_length=10, verbose_name='Asset ID'),
        ),
        migrations.CreateModel(
            name='Roadcall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rc_date', models.CharField(max_length=100, verbose_name='Road Call Date')),
                ('rc_exitdate', models.CharField(max_length=100, verbose_name='Finished Date')),
                ('rc_loc', models.CharField(max_length=300, verbose_name='Location')),
                ('rc_reploc', models.CharField(max_length=300, verbose_name='Reported Workshop')),
                ('rc_mobilews', models.CharField(max_length=100, verbose_name='Mobile Workshop')),
                ('rc_deftype', models.CharField(max_length=300, verbose_name='Defect Type')),
                ('rc_failure', models.CharField(max_length=300, verbose_name='Failure')),
                ('rc_actdef', models.TextField(verbose_name='Actual Defect')),
                ('rc_repair', models.TextField(verbose_name='Repair Action')),
                ('rc_parts', models.TextField(verbose_name='Spare Part')),
                ('asset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.asset', verbose_name='Asset ID')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.employee', verbose_name='Technician ID')),
            ],
        ),
    ]
