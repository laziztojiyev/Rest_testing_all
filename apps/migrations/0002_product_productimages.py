# Generated by Django 4.1.3 on 2022-11-19 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=30000, max_digits=9)),
                ('description', models.TextField()),
                ('size', models.CharField(choices=[('S', 'S'), ('L', 'L'), ('XL', 'Xl'), ('XXL', 'Xxl')], default='S', max_length=25)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('RED', 'Red'), ('BLUE', 'Blue'), ('GREEN', 'Green'), ('WHITE', 'White')], default='WHITE', max_length=25)),
                ('expired_date', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='apps.category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='apps.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]