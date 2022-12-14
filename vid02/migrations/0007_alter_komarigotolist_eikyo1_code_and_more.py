# Generated by Django 4.0.5 on 2022-06-10 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0006_auto_20220530_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komarigotolist',
            name='eikyo1_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.eikyo1'),
        ),
        migrations.AlterField(
            model_name='komarigotolist',
            name='eikyo2_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.eikyo2'),
        ),
        migrations.AlterField(
            model_name='komarigotolist',
            name='genin1_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.genin1'),
        ),
        migrations.AlterField(
            model_name='komarigotolist',
            name='genin2_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.genin2'),
        ),
    ]
