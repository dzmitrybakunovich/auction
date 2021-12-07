# Generated by Django 3.1 on 2021-09-27 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auctions', '0003_auto_20210927_1250'),
        ('items', '0002_auto_20210927_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
        ),
    ]