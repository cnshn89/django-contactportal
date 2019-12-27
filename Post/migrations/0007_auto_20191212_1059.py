# Generated by Django 2.1.7 on 2019-12-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20191212_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docnumber',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Belge No'),
        ),
        migrations.AlterField(
            model_name='post',
            name='duedate',
            field=models.DateField(blank=True, null=True, verbose_name='Termin Tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='mail_group',
            field=models.CharField(blank=True, choices=[('Y', 'Üst Yönetim'), ('F', 'Finansman'), ('S', 'Satın Alma'), ('M', 'Muhasebe'), ('IP', 'Yurtiçi Satış'), ('IH', 'İhracat Satış'), ('P', 'Üretim Planlama - ARGE')], max_length=2, null=True, verbose_name='Mail Grupları'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Onay Bekliyor'), (1, 'Onaylandı'), (2, 'Reddedildi')], verbose_name='Mesaj Durumu'),
        ),
    ]
