# Generated by Django 4.0.3 on 2022-10-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_attendance_attend_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('req_code', models.CharField(max_length=500, verbose_name='Request Code')),
                ('req_date', models.CharField(max_length=100, verbose_name='Request Date')),
                ('req_startat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Started At')),
                ('req_completeat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Completed At')),
                ('req_status', models.CharField(max_length=300, verbose_name='Request Status')),
                ('req_type', models.CharField(max_length=300, verbose_name='Order Type')),
                ('req_asset', models.CharField(max_length=100, verbose_name='Asset ID')),
                ('req_createshop', models.CharField(max_length=300, verbose_name='Created Workshop')),
                ('req_workshop', models.CharField(max_length=300, verbose_name='Workshop')),
                ('req_physloc', models.CharField(max_length=500, verbose_name='Physically Location')),
                ('req_desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('req_checkby', models.CharField(max_length=500, verbose_name='Checked By')),
                ('req_createby', models.CharField(max_length=500, verbose_name='Created By')),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_area',
            field=models.CharField(max_length=100, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_model',
            field=models.CharField(max_length=100, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_sector',
            field=models.CharField(max_length=100, verbose_name='Sector'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='object_id',
            field=models.CharField(max_length=100, verbose_name='Asset ID'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attend_timein',
            field=models.CharField(max_length=100, verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attend_timeout',
            field=models.CharField(max_length=100, verbose_name='Time Out'),
        ),
        migrations.AlterField(
            model_name='module',
            name='mod_name',
            field=models.CharField(max_length=300, verbose_name='Module Name'),
        ),
        migrations.AlterField(
            model_name='module',
            name='mod_url',
            field=models.CharField(max_length=300, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='param_name',
            field=models.CharField(max_length=300, verbose_name='Parameter Name'),
        ),
        migrations.AlterField(
            model_name='section',
            name='sec_icon',
            field=models.CharField(max_length=300, verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='section',
            name='sec_name',
            field=models.CharField(max_length=300, verbose_name='Section Name'),
        ),
    ]
