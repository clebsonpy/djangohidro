from django.db import models

class Discretizacao(models.Model):
    Discretizacao_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=10, null=False)

class Fonte(models.Model):
    Fonte_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=10, null=False)

class Nivel_de_Consistencia(models.Model):
    Tipo_Dados_ID = models.AutoField(primary_key=True, null=False)
    Nivel = models.CharField(max_length=20, null=False)

class Tipo_Posto(models.Model):
    Tipo_Posto_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=20, null=False)

class Posto(models.Model):
    Posto_ID = models.AutoField(primary_key=True,null=False)
    Tipo_Posto_ID = models.ForeignKey(Tipo_Posto, null=False)
    Fonte_ID = models.ForeignKey(Fonte, null=False)
    Codigo_ANA = models.CharField(max_length=15, null=True)

class Reducao(models.Model):
    Reducao_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=15, null=False)

class Unidade(models.Model):
    Unidade_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=10, null=False)

class Variavel(models.Model):
    Variavel_ID = models.AutoField(primary_key=True, null=False)
    Variavel = models.CharField(max_length=20, null=False)

class Serie_Temporal(models.Model):
    Serie_Temporal_ID = models.IntegerField(primary_key=True, null=False)
    Data_Hora = models.DateTimeField(primary_key=True, null=False)
    Dado = models.CharField(max_length=10, null=False)