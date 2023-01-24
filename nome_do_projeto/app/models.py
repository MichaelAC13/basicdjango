# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fornecedor(models.Model):
    cnpj = models.CharField(primary_key=True, max_length=20)
    fornecedor = models.CharField(max_length=200, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=40, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    logradouro = models.CharField(max_length=960, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=960, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    setor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'

class Mercadorias(models.Model):
    descricao = models.CharField(max_length=450)
    ncm = models.CharField(max_length=200, blank=True, null=True)
    pisecofins = models.CharField(max_length=450, blank=True, null=True)
    setor = models.CharField(max_length=450, blank=True, null=True)
    icms = models.CharField(max_length=450, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    dtupdate = models.DateTimeField(blank=True, null=True)
    fornecedores = models.CharField(max_length=15000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mercadorias'

class Users(models.Model):
    email = models.CharField(unique=True, max_length=450)
    hashcode = models.CharField(max_length=450, blank=True, null=True)
    name = models.CharField(max_length=450, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    master = models.CharField(max_length=1, blank=True, null=True)
    dtupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'