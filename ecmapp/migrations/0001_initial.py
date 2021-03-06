# Generated by Django 3.2.5 on 2021-08-23 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('home_no', models.CharField(max_length=10)),
                ('landmark', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='admin1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('upload', models.FileField(blank=True, max_length=255, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='buy123',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('upload', models.FileField(blank=True, max_length=255, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('upload', models.FileField(blank=True, max_length=255, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('vendor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('buy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.buy123')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.register')),
                ('vendor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.vendor')),
                ('wallet', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cname', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('count', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='productss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('admin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.vendor')),
                ('cate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.category')),
                ('subcate', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pquantity', models.IntegerField()),
                ('pprice', models.IntegerField()),
                ('pdesc', models.CharField(max_length=100)),
                ('pimage', models.ImageField(null=True, upload_to='media/')),
                ('Aname', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.register')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('count', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.country')),
                ('stat', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.productss')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.register')),
                ('vendor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.vendor')),
            ],
        ),
        migrations.AddField(
            model_name='buy123',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.cart'),
        ),
        migrations.AddField(
            model_name='buy123',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.register'),
        ),
        migrations.AddField(
            model_name='buy123',
            name='vendor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecmapp.vendor'),
        ),
    ]
