from django.db import models
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.lands.models import LandOwner
# Create your models here.


class LandInspectionUpload(models.Model):
    """LandInspectionUpload
    Utilizado para el nodo del API tbProperties
    """
    id = models.AutoField(primary_key=True)
    cod_carga = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, db_column='cod_usuario')
    username = models.CharField(max_length=150)

    class Meta:
        # TB_PROPERTIES
        db_table = 'TB_INSPECCION_PREDIAL'
        verbose_name = _('Land Inspection')
        verbose_name_plural = _('Lands Inspection Upload')

    def __str__(self):
        return self.cod_carga


class TicketType(models.Model):
    cod_tipo_ticket = models.CharField(max_length=2, primary_key=True)
    desc_tipo_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_TICKET'
        verbose_name = _('Ticket Type')
        verbose_name_plural = _('Ticket Types')

    def __str__(self):
        return self.desc_tipo_ticket


# ToDo: Cambiar de station a state
class TicketWorkStation(models.Model):
    """Estado de la estacion de trabajo"""
    cod_est_trabajo_ticket = models.CharField(max_length=5, primary_key=True)
    desc_est_trabajo_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_EST_TRABAJO_TICKET'
        verbose_name = _('Ticket Work state')
        verbose_name_plural = _('Ticket Work state')

    def __str__(self):
        return self.desc_est_trabajo_ticket


# ToDo: Cambiar de station a state
class TicketSendStation(models.Model):
    """Estado de envio"""
    cod_est_envio_ticket = models.CharField(max_length=5, primary_key=True)
    desc_est_envio_ticket = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_EST_ENVIO_TICKET'
        verbose_name = _('Ticket Send state')
        verbose_name_plural = _('Ticket Send state')

    def __str__(self):
        return self.desc_est_envio_ticket


class Ticket(models.Model):
    """Ticket"""
    cod_ticket = models.CharField(max_length=20, primary_key=True)
    inspection_upload = models.ForeignKey(
        LandInspectionUpload, blank=True, null=True, on_delete=models.SET_NULL
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

    def __str__(self):
        return self.cod_ticket


class Location(models.Model):
    STATUS_CHOICE = (
        (0, 'pendiente'),
        (6, 'resuelto'),
        (98, 'observado'),
        
    )
    """Ubicacion"""
    cod_ubicacion = models.CharField(max_length=20, primary_key=True)
    cod_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, db_column="cod_ticket", related_name='ubicaciones')
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
    referencia = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado')
    file_obs =models.FileField(blank=True, null=True)  # ToDo: genera url
    
    class Meta:
        db_table = 'TB_UBICACION'
        verbose_name = _('Location')
        verbose_name_plural = _('Location')

    def __str__(self):
        return self.cod_ubicacion


class PhotoType(models.Model):
    cod_tipo_foto = models.AutoField(primary_key=True)
    desc_tipo_foto = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_FOTO'
        verbose_name = _('Photo Type')
        verbose_name_plural = _('Photo Type')

    def __str__(self):
        return self.desc_tipo_foto


class LocationPhoto(models.Model):
    """Fotos"""

    cod_foto = models.CharField(max_length=20, primary_key=True)
    cod_ubicacion = models.ForeignKey(Location, on_delete=models.CASCADE, db_column="cod_ubicacion", related_name='fotos')
    cod_tipo_foto = models.ForeignKey(PhotoType, on_delete=models.CASCADE, db_column="cod_tipo_foto")
    foto = models.ImageField(upload_to='land_inspections', blank=True, null=True)  # ToDo: genera url

    class Meta:
        db_table = 'TB_FOTOS'
        verbose_name = _('Photo')
        verbose_name_plural = _('Photo')

    def __str__(self):
        return self.cod_foto


class OwnerShipType(models.Model):
    cod_tipo_tit = models.AutoField(primary_key=True)
    desc_tipo_tit = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_TITULARIDAD'
        verbose_name = _('OwnerShip Type')
        verbose_name_plural = _('OwnerShip Type')

    def __str__(self):
        return self.desc_tipo_tit


class RecordOwnerShip(models.Model):
    STATUS_CHOICE = (
        (0, 'pendiente'),
        (6, 'resuelto'),
        (98, 'observado'),
    )
    """Registro Titularidad"""
    cod_tit = models.CharField(max_length=20, primary_key=True)
    cod_tipo_tit = models.ForeignKey(
        OwnerShipType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_tit"
    )
    cod_ubicacion = models.ForeignKey(Location, on_delete=models.CASCADE, db_column="cod_ubicacion", related_name='registros_titularidad')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, blank=True, null=True, default=0,
                                              db_column='estado')
    file_notificacion =models.FileField(blank=True, null=True)  # ToDo: genera url
    class Meta:
        db_table = 'TB_REGISTRO_TITULARIDAD'
        verbose_name = _('OwnerShip')
        verbose_name_plural = _('OwnerShip')

    def __str__(self):
        return self.cod_tit


class LandCharacteristic(models.Model):
    """Caracteristicas"""
    cod_caracteristica = models.AutoField(primary_key=True)
    cod_tit = models.OneToOneField(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit", related_name='caracteristicas')
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

    def __str__(self):
        return str(self.cod_caracteristica)


class FacilityType(models.Model):
    """Tipo de instalaciones"""
    cod_tipo_inst = models.AutoField(primary_key=True)
    desc_tipo_inst = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_INSTA'
        verbose_name = _('Facility type')
        verbose_name_plural = _('Facility types')

    def __str__(self):
        return self.desc_tipo_inst


class LandFacility(models.Model):
    """Instalaciones"""
    cod_inst = models.CharField(max_length=20, primary_key=True)
    cod_tit = models.ForeignKey(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit",related_name='instalaciones')
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

    def __str__(self):
        return self.cod_inst


class SupplyType(models.Model):
    """Tipo de suministro"""
    cod_tipo_sumi = models.AutoField(primary_key=True)
    desc_tipo_sumi = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIPO_SUMINISTRO'
        verbose_name = _('Facility Type')
        verbose_name_plural = _('Supply Types')

    def __str__(self):
        return self.desc_tipo_sumi


class LandSupply(models.Model):
    """Suministros"""
    cod_suministro = models.AutoField(primary_key=True)
    cod_tit = models.OneToOneField(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit", related_name='suministro')
    cod_tipo_sumi = models.ForeignKey(
        SupplyType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_sumi"
    )
    num_sumis = models.CharField(max_length=20, blank=True, null=True)
    obs_sumis = models.CharField(max_length=100, blank=True, null=True)
    #cod_contr_inspec = models.ForeignKey(LandOwnerInspection, on_delete=models.CASCADE, db_column="cod_contr_inspec",related_name='contribuyentes')
    cod_contr = models.ForeignKey(
        LandOwner, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_contr",related_name='suministro'
    )
    class Meta:
        db_table = 'TB_SUMINISTRO'
        verbose_name = _('Land Supply')
        verbose_name_plural = _('Land Supplies')

    def __str__(self):
        return str(self.cod_suministro)


class LandInspectionType(models.Model):
    """Tipo de predio"""
    cod_tipo_predio = models.AutoField(primary_key=True)
    desc_tipo_predio = models.CharField(max_length=100)

    class Meta:
        db_table = 'TB_TIP_PREDIO_INSPEC'
        verbose_name = _('Facility Type')
        verbose_name_plural = _('Land Inspection Types')

    def __str__(self):
        return self.desc_tipo_predio


class LandInspection(models.Model):
    """Predios
    Tabla de almacenamiento de mobile una vez aceptado los datos pasan a la `lands.Land` bd `TB_PREDIO`
    """
    id = models.AutoField(primary_key=True)
    cod_tit = models.OneToOneField(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit", related_name='predio_inspeccion')
    ubigeo = models.CharField(max_length=6)
    cod_cpu = models.CharField(max_length=50, blank=True, null=True)
    cod_pre = models.CharField(max_length=50, blank=True, null=True)
    cod_tipo_predio = models.ForeignKey(
        LandInspectionType, blank=True, null=True, on_delete=models.SET_NULL, db_column="cod_tipo_predio"
    )
    piso = models.CharField(max_length=100, blank=True, null=True)
    num_sumi_agua = models.CharField(max_length=100, blank=True, null=True)
    num_sumi_luz = models.CharField(max_length=100, blank=True, null=True)
    uso_especifico = models.CharField(max_length=100, blank=True, null=True)
    interior = models.CharField(max_length=100, blank=True, null=True)
    obs_predio = models.CharField(max_length=100, blank=True, null=True)
    num_dpto = models.CharField(max_length=100, blank=True, null=True)
    codigo_uso = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    num_sumi_gas = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'TB_PREDIO_INSPEC'
        verbose_name = _('Land Inspection')
        verbose_name_plural = _('Lands Inspection')

    def __str__(self):
        return str(self.id)


class LandOwnerInspection(models.Model):
    """Contribuyente
    Tabla de almacenamiento de mobile una vez aceptado los datos pasan a la `lands.LandOwner` bd `PROPIETARIO`
    """
    id = models.AutoField(primary_key=True)
    cod_contr = models.CharField(max_length=50)
    tip_doc = models.CharField(max_length=2, blank=True, null=True)  # ToDo: validar si debe ser FK
    doc_iden = models.CharField(max_length=20, blank=True, null=True)
    dir_fiscal = models.CharField(max_length=255, blank=True, null=True)
    ap_mat = models.CharField(max_length=100, blank=True, null=True)
    ap_pat = models.CharField(max_length=150, blank=True, null=True)
    cond_contr = models.CharField(max_length=150, blank=True, null=True)  # ToDo: Validar su valor
    contribuyente = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    conyuge = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'TB_CONTRIBUYENTE_INSPEC'
        verbose_name = _('Land Owner Inspection')
        verbose_name_plural = _('Land Owner Inspection')

    def __str__(self):
        return str(self.id)


class LandOwnerDetailInspection(models.Model):
    """Predios
    Tabla de almacenamiento de mobile una vez aceptado los datos pasan a la `lands.LandOwner` bd ``
    """
    cod_tit = models.ForeignKey(RecordOwnerShip, on_delete=models.CASCADE, db_column="cod_tit")
    ubigeo = models.CharField(max_length=6)
    cod_pred_inspec = models.ForeignKey(LandInspection, on_delete=models.CASCADE, db_column="cod_pred_inspec",related_name='predio_contribuyente')
    cod_contr_inspec = models.ForeignKey(LandOwnerInspection, on_delete=models.CASCADE, db_column="cod_contr_inspec",related_name='contribuyentes')
    doc_iden = models.CharField(max_length=20, blank=True, null=True)
    cod_pre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'TB_PREDIO_CONTRIBUYENTE_INSPEC'
        verbose_name = _('Land Inspection')
        verbose_name_plural = _('Lands Owner Detail Inspection')

    def __str__(self):
        return str(self.id)
