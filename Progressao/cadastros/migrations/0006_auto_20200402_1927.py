# Generated by Django 2.2.10 on 2020-04-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_servidor_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='descricao',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='descrição'),
        ),
    ]
