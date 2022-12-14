# Generated by Django 2.2.27 on 2022-05-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pptxlist', '0007_auto_20220421_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pptx2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pptxname_text', models.CharField(max_length=200)),
                ('pptx_file', models.BinaryField(blank=True)),
                ('pptx_size', models.CharField(max_length=100)),
                ('pptx_thumbnail', models.ImageField(upload_to='images/%Y/%m/%d/')),
            ],
        ),
    ]
