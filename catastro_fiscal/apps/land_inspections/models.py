from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class LandInspectionUpload(models.Model):
    """LandInspectionUpload
    Utilizado para el nodo del API tbProperties
    """
    cod_carga = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=150)

    class Meta:
        # TB_PROPERTIES
        db_table = 'TB_INSPECCION_PREDIAL'
        verbose_name = _('Land Inspection')
        verbose_name_plural = _('LandS Inspection')


class TicketType(models.Model):
    cod_tipo_ticket = models.CharField(max_length=2, primary_key=True)
    desc_tipo_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_TICKET'
        verbose_name = _('Ticket Type')
        verbose_name_plural = _('Ticket Types')


class TicketWorkStation(models.Model):
    cod_est_trabajo_ticket = models.CharField(max_length=5, primary_key=True)
    desc_est_trabajo_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_EST_TRABAJO_TICKET'
        verbose_name = _('Ticket WorkStation')
        verbose_name_plural = _('Ticket WorkStation')


class TicketSendStation(models.Model):
    cod_est_envio_ticket = models.CharField(max_length=5, primary_key=True)
    desc_est_envio_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_EST_ENVIO_TICKET'
        verbose_name = _('Ticket SendStation')
        verbose_name_plural = _('Ticket SendStation')


class Ticket(models.Model):
    """Ticket"""
    cod_ticket = models.CharField(max_length=20, primary_key=True)
    cod_carga = models.ForeignKey(
        LandInspectionUpload, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_carga"
    )
    cod_tipo_ticket = models.ForeignKey(
        TicketType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_ticket"
    )
    cod_est_trabajo_ticket = models.ForeignKey(
        TicketWorkStation, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_est_trabajo_ticket"
    )
    cod_est_envio_ticket = models.ForeignKey(
        TicketSendStation, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_est_envio_ticket"
    )
    username = models.CharField(max_length=150, blank=True, null=True)
    cod_usuario = models.CharField(max_length=255, blank=True, null=True)  # Codigo de usuario mobile
    obs_ticket_usuario = models.CharField(max_length=255, blank=True, null=True)
    fec_inicio_trabajo = models.DateTimeField(blank=True, null=True)
    fec_asignacion = models.DateTimeField(blank=True, null=True)
    fec_ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    obs_ticket_gabinete = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'TB_TICKET'
        verbose_name = _('Ticket')
        verbose_name_plural = _('Ticket')


class Location(models.Model):
    """Ubicacion"""
    cod_ubicacion = models.CharField(max_length=20, primary_key=True)
    cod_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, db_column="cod_ticket")
    cod_tip_via = models.CharField(max_length=10, blank=True, null=True)  # ToDo: ver FK
    cod_via = models.CharField(max_length=255, blank=True, null=True)  # ToDo: ver FK
    nom_via = models.CharField(max_length=255, blank=True, null=True)
    num_alt = models.CharField(max_length=255, blank=True, null=True)
    nom_alt = models.CharField(max_length=255, blank=True, null=True)
    cod_tipo_uu = models.CharField(max_length=255, blank=True, null=True)  # ToDo: ver FK
    cod_uu = models.CharField(max_length=255, blank=True, null=True)  # ToDo: ver FK
    nom_uu = models.CharField(max_length=255, blank=True, null=True)
    nom_ref = models.CharField(max_length=255, blank=True, null=True)
    km = models.CharField(max_length=255, blank=True, null=True)
    x = models.FloatField(blank=True, null=True, db_column='coor_x')
    y = models.FloatField(blank=True, null=True, db_column='coor_y')
    lot_urb = models.CharField(max_length=255, blank=True, null=True)
    num_mun = models.CharField(max_length=255, blank=True, null=True)
    mzn_urb = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    cod_usuario = models.CharField(max_length=255, blank=True, null=True)  # Codigo de usuario mobile
    obs_ubicacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'TB_UBICACION'
        verbose_name = _('Location')
        verbose_name_plural = _('Location')


class PhotoType(models.Model):
    cod_tipo_foto = models.AutoField(primary_key=True)
    desc_tipo_foto = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_FOTO'
        verbose_name = _('Photo Type')
        verbose_name_plural = _('Photo Type')


class LocationPhoto(models.Model):
    """Fotos"""

    cod_foto = models.CharField(max_length=20, primary_key=True)
    cod_ubicacion = models.ForeignKey(Location, on_delete=models.CASCADE, db_column="cod_ubicacion")
    cod_tipo_foto = models.ForeignKey(PhotoType, on_delete=models.CASCADE, db_column="cod_tipo_foto")
    foto = models.ImageField(upload_to='land_inspections', blank=True, null=True)  # ToDo: genera url

    class Meta:
        db_table = 'TB_FOTOS'
        verbose_name = _('Photo')
        verbose_name_plural = _('Photo')


class OwnerShipType(models.Model):
    cod_tipo_tit = models.AutoField(primary_key=True)
    desc_tipo_tit = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_TITULARIDAD'
        verbose_name = _('OwnerShip Type')
        verbose_name_plural = _('OwnerShip Type')


class RecordOwnerShip(models.Model):
    """Registro Titularidad"""
    cod_tit = models.CharField(max_length=20, primary_key=True)
    cod_tipo_tit = models.ForeignKey(
        OwnerShipType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_tit"
    )
    cod_ubicacion = models.ForeignKey(Location, on_delete=models.CASCADE, db_column="cod_ubicacion")

    class Meta:
        db_table = 'TB_REGISTRO_TITULARIDAD'
        verbose_name = _('OwnerShip')
        verbose_name_plural = _('OwnerShip')


class LandCharacteristic(models.Model):
    """Caracteristicas"""
    cod_caracteristica = models.AutoField(primary_key=True)
    cod_tit = models.ForeignKey(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit")
    categoria_electrica = models.CharField(max_length=100, blank=True, null=True)
    piso = models.CharField(max_length=100, blank=True, null=True)
    estado_conserva = models.CharField(max_length=100, blank=True, null=True)
    anio_construccion = models.CharField(max_length=100, blank=True, null=True)
    catergoria_techo = models.CharField(max_length=100, blank=True, null=True)
    longitud_frente = models.FloatField(blank=True, null=True)
    categoria_muro_columna = models.CharField(max_length=100, blank=True, null=True)
    catergoria_puerta_ventana = models.CharField(max_length=100, blank=True, null=True)
    arancel = models.FloatField(blank=True, null=True)
    material_pred = models.CharField(max_length=100, blank=True, null=True)
    categoria_revestimiento = models.CharField(max_length=100, blank=True, null=True)
    area_terreno = models.FloatField(blank=True, null=True)
    clasificacion_pred = models.CharField(max_length=100, blank=True, null=True)
    catergoria_piso = models.CharField(max_length=100, blank=True, null=True)
    catergoria_bano = models.CharField(max_length=100, blank=True, null=True)
    area_construida = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'TB_CARACTERISTICAS'
        verbose_name = _('Land Characteristic')
        verbose_name_plural = _('Land Characteristics')


class FacilityType(models.Model):
    """Tipo de instalaciones"""
    cod_tipo_inst = models.AutoField(primary_key=True)
    desc_tipo_inst = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_INSTA'
        verbose_name = _('Facility type')
        verbose_name_plural = _('Facility types')


class LandFacility(models.Model):
    """Instalaciones"""
    cod_inst = models.CharField(max_length=20, primary_key=True)
    cod_tit = models.ForeignKey(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit")
    cod_tipo_inst = models.ForeignKey(
        FacilityType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_inst"
    )
    anio_construccion = models.CharField(max_length=20, blank=True, null=True)
    estado_conserva = models.CharField(max_length=255, blank=True, null=True)
    dimension = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'TB_INSTALACIONES'
        verbose_name = _('Land Facility')
        verbose_name_plural = _('Land Facilities')


class SupplyType(models.Model):
    """Tipo de suministro"""
    cod_tipo_sumi = models.AutoField(primary_key=True)
    desc_tipo_sumi = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_SUMINISTRO'
        verbose_name = _('Facility Type')
        verbose_name_plural = _('Facility Types')


class LandSupply(models.Model):
    """Suministros"""
    cod_suministro = models.AutoField(primary_key=True)
    cod_tit = models.ForeignKey(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit")
    cod_tipo_sumi = models.ForeignKey(
        SupplyType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_sumi"
    )
    num_sumis = models.CharField(max_length=20, blank=True, null=True)
    obs_sumis = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'TB_SUMINISTRO'
        verbose_name = _('Land Supply')
        verbose_name_plural = _('Land Supplies')
