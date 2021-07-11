
from django.db import models

class Tipo_cliente(models.Model):
    id_tipo_cliente = models.AutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=45)

    def __str__(self):
        return f'id: {self.id_tipo_cliente} tipo cliente: {self.tipo_cliente}'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    fotografia = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    fk_tipo_cliente = models.ForeignKey(Tipo_cliente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id_cliente} nombre: {self.nombre} codigo: {self.codigo} fk_tipo_cliente: {self.fk_tipo_cliente}'


class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField()

    def __str__(self):
        return f'id: {self.id_articulo} tipo codigo: {self.codigo}'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)

    def __str__(self):
        return f'id: {self.id_proveedor} nombre: {self.nombre}'


class Empresa_asociada(models.Model):
    id_empresa_asociada = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=45)
    codigo_socio = models.IntegerField()

    def __str__(self):
        return f'id: {self.id_empresa_asociada} referencia: {self.referencia}'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=45)
    codigo_sucursal = models.IntegerField()

    def __str__(self):
        return f'id: {self.id_sucursal} referencia: {self.referencia}'


class Centro_distribucion(models.Model):
    id_centro_distribucion = models.AutoField(primary_key=True)
    almacen = models.CharField(max_length=45)

    def __str__(self):
        return f'id: {self.id_centro_distribucion} referencia: {self.referencia}'


class Pedido(models.Model):

    id_pedido = models.AutoField(primary_key=True)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fecha_gen_pedido = models.DateField()
    hora_gen_pedido = models.CharField(max_length=45)
    fecha_surte_pedido = models.DateField(null=True)
    hora_surte_pedido = models.CharField(max_length=45, null=True)
    es_urgente = models.BooleanField()
    fk_sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)
    fk_centro_distribucion = models.ForeignKey(Centro_distribucion, on_delete=models.SET_NULL, null=True)
    fk_empresa_asociada = models.ManyToManyField(Empresa_asociada, blank=True)


class Detalle_pedido(models.Model):

    id_detalle_pedido = models.AutoField(primary_key=True)
    fk_proveedor = models.ManyToManyField(Proveedor, blank=True)
    fk_articulo = models.ManyToManyField(Articulo, blank=True)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fk_pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
