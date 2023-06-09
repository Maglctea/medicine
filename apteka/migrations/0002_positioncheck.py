# Generated by Django 4.1.7 on 2023-03-03 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka.medicament', verbose_name='Название')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka.check', verbose_name='Номер заказа')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apteka.salesman', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
            },
        ),
    ]
