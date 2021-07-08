from django.db import models
from django.conf import settings

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

