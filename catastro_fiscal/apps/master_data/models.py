from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.places.models import District

class Institution(models.Model):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'INSTITUCION'
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')

    def __str__(self):
        return self.name


class MasterDomain(models.Model):
    id = models.CharField(_('key id'), max_length=50, primary_key=True)
    name = models.CharField(_('name'), max_length=150)
    description = models.CharField(_('description'), max_length=150)
    short_name = models.CharField(_('short name'), max_length=100)
    estado = models.IntegerField(blank=True, null=True, default=1)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MasterTypeUrbanUnit(MasterDomain):
    class Meta:
        db_table = 'M_TIPO_UU'
        verbose_name = _('urban unit type')
        verbose_name_plural = _('urban unit types')


class MasterSide(MasterDomain):
    class Meta:
        db_table = 'M_LADO'
        verbose_name = _('side')
        verbose_name_plural = _('sides')


class MasterCodeStreet(MasterDomain):
    class Meta:
        db_table = 'M_COD_VIA'
        verbose_name = _('street code')
        verbose_name_plural = _('street codes')





class MasterResolutionType(MasterDomain):
    tipo =  models.IntegerField(blank=True, null=True, default=1)
    estado_registro  =  models.IntegerField(blank=True, null=True, default=1)
    estado_mantenimiento=  models.IntegerField(blank=True, null=True, default=1)


    class Meta:
        db_table = 'M_TDOC_RES'
        verbose_name = _('resolution type')
        verbose_name_plural = _('resolution types')

class ResolutionTypeDistrito(models.Model):
    id  = models.AutoField(primary_key=True,)
    ubigeo = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='distrito',blank=True, null=True)
    resolucion = models.ForeignKey(MasterResolutionType, on_delete=models.DO_NOTHING, related_name='resolucion',blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True, default=1)
    class Meta:
        db_table = 'TDOC_RES_DISTRITO'
        verbose_name = _('tipo de resolucion distrito')
        verbose_name_plural = _('tipos de resolucion distrito')


class MasterTipoDocumentoIdentidad(MasterDomain):
    class Meta:
        db_table = 'M_TDOC_IDENTIDAD'
        verbose_name = _('tipo de documento de identidad')
        verbose_name_plural = _('tipos de documento de identidad')


class MasterType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(_('name'), max_length=150,blank=True, null=True)
    description = models.CharField(_('description'), max_length=150)
    short_name = models.CharField(_('short name'), max_length=100)
    estado = models.IntegerField(blank=True, null=True, default=1)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class MasterTipoContribuyente(MasterType):
    class Meta:
        db_table = 'M_TIPO_CONTRIBUYENTE'
        verbose_name = _('tipo de contribuyente')
        verbose_name_plural = _('tipos de contribuyente')

class MasterTipoPropiedad(MasterType):
    class Meta:
        db_table = 'M_TIPO_PROPIEDAD'
        verbose_name = _('tipo de propiedad')
        verbose_name_plural = _('tipos de propiedad')


class MasterTipoTransferencia(MasterType):
    class Meta:
        db_table = 'M_TIPO_TRANSFERENCIA'
        verbose_name = _('tipo de transferencia')
        verbose_name_plural = _('tipos de transferencia')




class MasterTipoNivel(MasterType):
    class Meta:
        db_table = 'M_TIPO_NIVEL'
        verbose_name = _('tipo de nivel')
        verbose_name_plural = _('tipos de nivel')

class MasterTipoMaterial(MasterType):
    class Meta:
        db_table = 'M_TIPO_MATERIAL'
        verbose_name = _('tipo de material')
        verbose_name_plural = _('tipos de material')

class MasterTipoEstadoConservacion(MasterType):
    class Meta:
        db_table = 'M_TIPO_ESTADO_CONSERVACION'
        verbose_name = _('tipo de estado de conservacion')
        verbose_name_plural = _('tipos de estado de conservacion')

class MasterTipoObraComplementaria(MasterType):
    class Meta:
        db_table = 'M_TIPO_OBRA_COMPLEMENTARIA'
        verbose_name = _('tipo de obra')
        verbose_name_plural = _('tipos de obra')


class MasterClaseUso(MasterType):
    class Meta:
        db_table = 'M_CLASE_USO'
        verbose_name = _('clase de uso')
        verbose_name_plural = _('clases de uso')


class MasterSubClaseUso(MasterType):
    codigo_clase_uso = models.ForeignKey(MasterClaseUso,blank=True, null=True, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'M_SUBCLASE_USO'
        verbose_name = _('subclase de uso')
        verbose_name_plural = _('subclases de uso')

class MasterTipoPredio(MasterType):

    class Meta:
        db_table = 'M_TIPO_PREDIO'
        verbose_name = _('tipo de predio')
        verbose_name_plural = _('tipos de predio')



class MasterTipoUsoPredio(MasterType):
    codigo_subclase_uso = models.ForeignKey(MasterSubClaseUso,blank=True, null=True, on_delete=models.DO_NOTHING)
    codigo_tipo_uso =  models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'M_TIPO_USO_PREDIO'
        verbose_name = _('tipo uso de predio')
        verbose_name_plural = _('tipos uso de predio')

# class MasterEstadoConserva(MasterDomain):
#     class Meta:
#         db_table = 'M_ESTADO_CONSERVA'
#         verbose_name = _('estado conserva')
#         verbose_name_plural = _('estados conserva')




# class MasterMaterial(MasterDomain):
#     class Meta:
#         db_table = 'M_MATERIAL'
#         verbose_name = _('material')
#         verbose_name_plural = _('materiales')