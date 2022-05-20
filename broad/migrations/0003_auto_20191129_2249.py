# Generated by Django 2.2.7 on 2019-11-29 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191129_2249'),
        ('broad', '0002_globalgallary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalgallary',
            options={'verbose_name_plural': 'GlobalGallaries'},
        ),
        migrations.AddField(
            model_name='globalgallary',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_img', to='users.UserGallary', to_field='own_image'),
        ),
        migrations.AlterField(
            model_name='globalgallary',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='g_item', to='users.UserGallary'),
        ),
    ]