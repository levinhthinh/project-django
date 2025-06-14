# Generated by Django 5.2 on 2025-06-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_keyboard_unique_keyboard_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='keyboard',
            name='unique keyboard',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='Image',
            field=models.ImageField(default='bad_sign.png', upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='Height',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='Length',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='Width',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AddConstraint(
            model_name='keyboard',
            constraint=models.UniqueConstraint(fields=('Name', 'Image'), name='unique keyboard'),
        ),
    ]
