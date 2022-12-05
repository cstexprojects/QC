# Generated by Django 4.0.5 on 2022-07-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vid02', '0007_alter_komarigotolist_eikyo1_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KomarigotoInput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('komarigoto', models.CharField(blank=True, max_length=10, null=True)),
                ('eikyo1_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.eikyo1')),
                ('eikyo2_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.eikyo2')),
                ('genin1_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.genin1')),
                ('genin2_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vid02.genin2')),
            ],
        ),
    ]