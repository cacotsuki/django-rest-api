# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgenciaFomento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'agencia_fomento'


class AreaConhecimento(models.Model):
    nome = models.CharField(max_length=100)
    codigo_cnpq = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_conhecimento'


class Campus(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'campus'


class Coordenador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    link_lattes = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'coordenador'


class Edital(models.Model):
    identificacao = models.CharField(max_length=50)
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edital'


class EntidadesParceiras(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidades_parceiras'


class EntidadesParceirasProjeto(models.Model):
    entidades_parceiras = models.ForeignKey(EntidadesParceiras, models.DO_NOTHING, primary_key=True)
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entidades_parceiras_projeto'
        unique_together = (('entidades_parceiras', 'projeto'),)


class Integrante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    integrante_tipo = models.ForeignKey('IntegranteTipo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'integrante'


class IntegranteProjeto(models.Model):
    integrante = models.ForeignKey(Integrante, models.DO_NOTHING, primary_key=True)
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'integrante_projeto'
        unique_together = (('integrante', 'projeto'),)


class IntegranteTipo(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'integrante_tipo'


class Multimidia(models.Model):
    tipo = models.CharField(max_length=1)
    link = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'multimidia'


class MultimidiaProjeto(models.Model):
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING, primary_key=True)
    multimidia = models.ForeignKey(Multimidia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'multimidia_projeto'
        unique_together = (('projeto', 'multimidia'),)


class PalavraChave(models.Model):
    palavra = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'palavra_chave'


class PalavraChaveProjeto(models.Model):
    palavra_chave = models.ForeignKey(PalavraChave, models.DO_NOTHING, primary_key=True)
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'palavra_chave_projeto'
        unique_together = (('palavra_chave', 'projeto'),)


class Premio(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=2048, blank=True, null=True)
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'premio'


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.TextField()  # This field type is a guess.
    tipo_projeto = models.ForeignKey('TipoProjeto', models.DO_NOTHING)
    agencia_fomento = models.ForeignKey(AgenciaFomento, models.DO_NOTHING)
    edital = models.ForeignKey(Edital, models.DO_NOTHING)
    coordenador = models.ForeignKey(Coordenador, models.DO_NOTHING)
    campus = models.ForeignKey(Campus, models.DO_NOTHING)
    resumo = models.CharField(max_length=3000)
    area_conhecimento = models.ForeignKey(AreaConhecimento, models.DO_NOTHING)
    sub_area_conhecimento = models.ForeignKey('SubAreaConhecimento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projeto'


class SubAreaConhecimento(models.Model):
    nome = models.CharField(max_length=100)
    area_conhecimento = models.ForeignKey(AreaConhecimento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_area_conhecimento'


class TipoProjeto(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tipo_projeto'
