# Generated by Django 3.2.5 on 2021-07-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id_articulo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Centro_distribucion',
            fields=[
                ('id_centro_distribucion', models.AutoField(primary_key=True, serialize=False)),
                ('almacen', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa_asociada',
            fields=[
                ('id_empresa_asociada', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=45)),
                ('codigo_socio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=45)),
                ('codigo_sucursal', models.IntegerField()),
            ],
        ),
    ]