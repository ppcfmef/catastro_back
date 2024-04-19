from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractAudit
from apps.places.models import District
from apps.lands.models import Land
from django.contrib.auth import get_user_model



User = get_user_model()

# class AplicationType(models.Model):
#     id = models.AutoField(primary_key=True)
#     description =  models.CharField(max_length=50, blank=True, null=True, db_column='descripcion')
#     class Meta:
#         db_table = 'TIPO_SOLICITUD'


class Application(models.Model):
    STATUS_CHOICE = (
        (1, 'Por atender'),
        (2, 'Atendido'),
        (3, 'Observado'),
        (4,'De baja')
    )
    TYPE_CHOICE =(
        (1,'Reasignar ubicación'),
        (2,'Acumular'),
        (3,'Dividir'),
        (4,'Inactivar'),
        (5,'Independizar')
    )
          
    
    id = models.AutoField(primary_key=True)
    id_type = models.PositiveSmallIntegerField(blank=True, null=True, db_column='tipo',choices=TYPE_CHOICE)
    
    #id_type =models.ForeignKey(AplicationType, on_delete=models.SET_NULL, blank=True, null=True, db_column='tipo')
    usermane = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,db_column='username') 
    date = models.DateTimeField(null=True, db_column='fecha',auto_now=True)
    id_status = models.PositiveSmallIntegerField(blank=True, null=True, db_column='estado',choices=STATUS_CHOICE)
    ubigeo = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, db_column='ubigeo')
    support = models.FileField(upload_to='sustento/',db_column='sustento', blank=True, null=True)
    class Meta:
        db_table = 'SOLICITUD'
    
class Result(models.Model):
    SOURCE_CHOICES = (
        ('carga_masiva', 'Carga Masiva'),
        ('asignar_lote', 'Asignar Lote'),
        ('asignar_img', 'Asignar Imagen'),
    )
    STATUS_CHOICE = (
        (0, 'Sin Cartografia'),
        (1, 'Con cartografia (Lote)'),
        (2, 'Con cartografia (Imagen)'),
        (3, 'Inactivo'),
    )
    id = models.AutoField(primary_key=True)
    ubigeo = models.ForeignKey(District, on_delete=models.CASCADE, db_column='ubigeo')
    cpm = models.CharField(max_length=50, db_column='cod_pre', blank=True, null=True)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, blank=True, null=True, db_column='origen')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado')
    id_land_cartographic = models.CharField(max_length=18, blank=True, null=True, help_text=_('id land cartographic'),
                                            db_column='id_predio_cartografico')
    id_plot = models.CharField(max_length=25, blank=True, null=True, help_text=_('id plot'), db_column='id_lote')
    id_cartographic_img = models.CharField(max_length=26, blank=True, null=True, help_text=_('id cartographic image'),
                                           db_column='id_imagen_cartografica')
    id_object_img = models.IntegerField(blank=True, null=True, help_text=_('id object image'),
                                        db_column='id_imagen_objeto')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, db_column='sec_ejec')
    cup = models.CharField(max_length=20, blank=True, null=True, db_column='cod_cpu')
    cod_sect = models.CharField(max_length=2, blank=True, null=True, db_column='cod_sect')
    cod_uu = models.CharField(max_length=4, blank=True, null=True, db_column='cod_uu')
    cod_mzn = models.CharField(max_length=3, blank=True, null=True, db_column='cod_mzn')
    cod_land = models.CharField(max_length=5, blank=True, null=True, db_column='cod_lote')
    cod_cuc = models.CharField(max_length=18, blank=True, null=True, db_column='cod_cuc')
    uu_type = models.CharField(max_length=2, blank=True, null=True, db_column='tipo_uu')
    habilitacion_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_uu')
    reference_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_ref')
    urban_mza = models.CharField(max_length=10, blank=True, null=True, db_column='mzn_urb')
    urban_lot_number = models.CharField(max_length=10, blank=True, null=True, db_column='lot_urb')
    cod_street = models.CharField(max_length=20, blank=True, null=True, db_column='cod_via')
    street_type = models.CharField(max_length=20, blank=True, null=True, db_column='tip_via')
    street_name = models.CharField(max_length=255, blank=True, null=True, db_column='nom_via')
    street_name_alt = models.CharField(max_length=255, blank=True, null=True, db_column='nom_alt')
    municipal_number = models.CharField(max_length=6, blank=True, null=True, db_column='num_mun')  # numero de puerta
    block = models.CharField(max_length=6, blank=True, null=True, db_column='block')
    indoor = models.CharField(max_length=5, blank=True, null=True, db_column='interior')
    floor = models.CharField(max_length=2, blank=True, null=True, db_column='piso')
    km = models.CharField(max_length=4, blank=True, null=True, db_column='km')
    landmark = models.CharField(max_length=250, blank=True, null=True, db_column='referencia')
    municipal_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_mun')
    urban_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_urb')
    assigned_address = models.CharField(max_length=255, blank=True, null=True, db_column='dir_asig')
    longitude = models.FloatField(blank=True, null=True, db_column='coor_x')
    latitude = models.FloatField(blank=True, null=True, db_column='coor_y')
    id_aranc = models.IntegerField(blank=True, null=True, db_column='id_aranc')
    status_img = models.PositiveSmallIntegerField(blank=True, null=True, db_column='estado_imagen')
    land_area = models.FloatField(blank=True, null=True, db_column='area_terreno')
    front_length = models.FloatField(blank=True, null=True, db_column='longitud_frente')
    location_park = models.CharField(max_length=250, blank=True, null=True, db_column='ubicacion_parque')
    group_use_desc = models.CharField(max_length=50, blank=True, null=True, db_column='grupo_uso_desc')
    number_inhabitants = models.IntegerField(blank=True, null=True, db_column='cantidad_habitantes')
    classification_land_desc = models.CharField(max_length=90, blank=True, null=True,
                                                db_column='clasificacion_predio_desc')
    build_status_desc = models.CharField(max_length=120, blank=True, null=True, db_column='estado_construccion_desc')
    property_type = models.CharField(max_length=20, blank=True, null=True, db_column='tipo_predio')
    self_assessment_total = models.FloatField(blank=True, null=True, db_column='autoavaluo_total')
    condominium = models.FloatField(blank=True, null=True, db_column='condominio')
    deduction = models.FloatField(blank=True, null=True, db_column='deduccion')
    self_assessment_affection = models.FloatField(blank=True, null=True, db_column='autoavaluo_afecto')
    source_information = models.CharField(max_length=255, blank=True, null=True, db_column='fuente')
    resolution_date = models.DateField( blank=True, null=True, db_column='date_res')
    resolution_type = models.CharField(max_length=2, blank=True, null=True, db_column='tdoc_res')
    resolution_document = models.CharField(max_length=255, blank=True, null=True, db_column='ndoc_res')
    apartment_number = models.CharField(max_length=20, blank=True, null=True, db_column='numero_departamento')
    site = models.IntegerField(blank=True, null=True, db_column='lugar')
    built_area = models.FloatField(blank=True, null=True, db_column='area_construida')

    class Meta:
        db_table = 'RESULTADO'
        #unique_together = ["ubigeo", "cpm"]
        verbose_name = _('Result Detail')
        verbose_name_plural = _('Results Detail')

class ApplicationResultDetail(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='id_solicitud')
    result = models.ForeignKey(Result, on_delete=models.CASCADE, db_column='id_resultado')
    
    class Meta:
        db_table = 'SOLICITUD_RESULTADO'
        verbose_name = _('Application Result Detail')
        verbose_name_plural = _('Applications Result Detail')
        
class ApplicationLandDetail(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='id_solicitud',related_name='toapplication')
    land = models.ForeignKey(Land, on_delete=models.CASCADE, db_column='id_predio',related_name='toland')
    class Meta:
        db_table = 'SOLICITUD_PREDIO'
        verbose_name = _('Application Land Detail')
        verbose_name_plural = _('Applications Land Detail')


class ApplicationObservationDetail(models.Model):
    id = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='id_solicitud')
    description = models.CharField(max_length=250,blank=True, null=True, db_column='descripcion')
    img = models.ImageField(upload_to='observacion/',db_column='img')
    class Meta:
        db_table = 'SOLICITUD_OBSERVACION'
        verbose_name = _('Application Observation Detail')
        verbose_name_plural = _('Applications Observation Detail')