# Generated by Django 2.2.8 on 2020-01-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_seg', '0003_auto_20191231_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waste_dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='waste/')),
                ('predicted_category', models.CharField(max_length=50)),
                ('actual_category', models.CharField(max_length=50)),
            ],
        ),
    ]
