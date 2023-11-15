from datetime import datetime
from rest_framework import serializers, exceptions
from apps.users.models import User
from .models import LandInspectionUpload, Ticket


class LandOwnerInspectionSerializer(serializers.Serializer):
    """tb_contribuyente"""
    tip_doc = serializers.CharField()
    doc_iden = serializers.CharField()
    cod_contr = serializers.CharField()
    cond_contr = serializers.CharField(allow_blank=True, allow_null=True)
    dir_fiscal = serializers.CharField()
    nombre = serializers.CharField()
    ap_pat = serializers.CharField()
    ap_mat = serializers.CharField()
    contribuyente = serializers.CharField(allow_blank=True, allow_null=True)
    conyuge = serializers.CharField(allow_blank=True, allow_null=True)


class LandOwnerDetailInspectionSerializer(serializers.Serializer):
    """tb_predio_contribuyente"""
    doc_iden = serializers.CharField()
    cod_tit = serializers.CharField()
    cod_pre = serializers.CharField(allow_blank=True, allow_null=True)
    tb_contribuyente = LandOwnerInspectionSerializer()


class LandInspectionSerializer(serializers.Serializer):
    """tb_predio"""
    cod_tit = serializers.CharField()
    cod_pre = serializers.CharField(allow_blank=True, allow_null=True)
    cod_cpu = serializers.CharField(allow_blank=True, allow_null=True)
    piso = serializers.CharField(allow_blank=True, allow_null=True)
    num_sumi_agua = serializers.CharField(allow_blank=True, allow_null=True)
    cod_tipo_predio = serializers.CharField(allow_blank=True, allow_null=True)
    num_sumi_luz = serializers.CharField(allow_blank=True, allow_null=True)
    uso_especifico = serializers.CharField(allow_blank=True, allow_null=True)
    interior = serializers.CharField(allow_blank=True, allow_null=True)
    obs_predio = serializers.CharField(allow_blank=True, allow_null=True)
    num_dpto = serializers.CharField(allow_blank=True, allow_null=True)
    codigo_uso = serializers.CharField(allow_blank=True, allow_null=True)
    estado = serializers.CharField(allow_blank=True, allow_null=True)
    block = serializers.CharField(allow_blank=True, allow_null=True)
    num_sumi_gas = serializers.CharField(allow_blank=True, allow_null=True)
    tb_predio_contribuyente = LandOwnerDetailInspectionSerializer(many=True)


class LandSupplySerializer(serializers.Serializer):
    """tb_suministro"""
    cod_tit = serializers.CharField()
    cod_tipo_sumi = serializers.CharField()
    num_sumis = serializers.CharField()
    obs_sumis = serializers.CharField(allow_blank=True, allow_null=True)


class LandFacilitySerializer(serializers.Serializer):
    """tb_instalaciones"""
    cod_tit = serializers.CharField()
    cod_inst = serializers.CharField()
    cod_tipo_inst = serializers.CharField(allow_blank=True, allow_null=True)
    anio_construccion = serializers.CharField(allow_blank=True, allow_null=True)
    estado_conserva = serializers.CharField(allow_blank=True, allow_null=True)
    dimension = serializers.CharField(allow_blank=True, allow_null=True)


class LandCharacteristicSerializer(serializers.Serializer):
    """tb_caracteristicas"""
    cod_tit = serializers.CharField()
    categoria_electrica = serializers.CharField(allow_blank=True, allow_null=True)
    piso = serializers.CharField(allow_blank=True, allow_null=True)
    estado_conserva = serializers.CharField(allow_blank=True, allow_null=True)
    anio_construccion = serializers.CharField(allow_blank=True, allow_null=True)
    catergoria_techo = serializers.CharField(allow_blank=True, allow_null=True)
    longitud_frente = serializers.FloatField(allow_null=True)
    categoria_muro_columna = serializers.CharField(allow_blank=True, allow_null=True)
    catergoria_puerta_ventana = serializers.CharField(allow_blank=True, allow_null=True)
    arancel = serializers.FloatField(allow_null=True)
    material_pred = serializers.CharField(allow_blank=True, allow_null=True)
    categoria_revestimiento = serializers.CharField(allow_blank=True, allow_null=True)
    area_terreno = serializers.FloatField(allow_null=True)
    clasificacion_pred = serializers.CharField(allow_blank=True, allow_null=True)
    catergoria_piso = serializers.CharField(allow_blank=True, allow_null=True)
    catergoria_bano = serializers.CharField(allow_blank=True, allow_null=True)
    area_construida = serializers.FloatField(allow_null=True)


class RecordOwnerShipSerializer(serializers.Serializer):
    """tb_registro_titularidad"""
    cod_tit = serializers.CharField()
    cod_tipo_tit = serializers.CharField()
    cod_ubicacion = serializers.CharField()
    tb_predio = LandInspectionSerializer(required=False)
    tb_suministro = LandSupplySerializer(required=False)
    tb_caracteristicas = LandCharacteristicSerializer()
    tb_instalaciones = LandFacilitySerializer(many=True)


class LocationPhotoSerializer(serializers.Serializer):
    """tb_foto"""
    cod_foto = serializers.CharField()
    cod_ubicacion = serializers.CharField()
    cod_tipo_foto = serializers.CharField()
    url_foto = serializers.CharField()


class LocationSerializer(serializers.Serializer):
    """tb_ubicacion"""
    cod_ubicacion = serializers.CharField()
    cod_ticket = serializers.CharField()
    cod_usuario = serializers.CharField()
    cod_tip_via = serializers.CharField(allow_blank=True, allow_null=True)
    cod_via = serializers.CharField(allow_blank=True, allow_null=True)
    nom_via = serializers.CharField(allow_blank=True, allow_null=True)
    cod_tipo_uu = serializers.CharField(allow_blank=True, allow_null=True)
    cod_uu = serializers.CharField(allow_blank=True, allow_null=True)
    nom_uu = serializers.CharField(allow_blank=True, allow_null=True)
    num_alt = serializers.CharField(allow_blank=True, allow_null=True)
    nom_alt = serializers.CharField(allow_blank=True, allow_null=True)
    obs_ubicacion = serializers.CharField(allow_blank=True, allow_null=True)
    nom_ref = serializers.CharField(allow_blank=True, allow_null=True)
    referencia = serializers.CharField(allow_blank=True, allow_null=True)
    km = serializers.CharField(allow_blank=True, allow_null=True)
    y = serializers.FloatField()
    x = serializers.FloatField()
    lot_urb = serializers.CharField(allow_blank=True, allow_null=True)
    num_mun = serializers.CharField(allow_blank=True, allow_null=True)
    mzn_urb = serializers.CharField(allow_blank=True, allow_null=True)
    tb_foto = LocationPhotoSerializer(many=True)
    tb_registro_titularidad = RecordOwnerShipSerializer(many=True)


class TicketSerializer(serializers.Serializer):
    """tb_ticket"""
    cod_ticket = serializers.CharField()
    cod_usuario = serializers.CharField()
    obs_ticket_usuario = serializers.CharField(allow_blank=True, allow_null=True)
    cod_est_trabajo_ticket = serializers.CharField()
    fec_inicio_trabajo = serializers.CharField()
    fec_asignacion = serializers.CharField()
    fec_ultima_actualizacion = serializers.CharField()
    cod_est_envio_ticket = serializers.CharField()
    cod_tipo_ticket = serializers.CharField()
    obs_ticket_gabinete = serializers.CharField(allow_blank=True, allow_null=True)
    tb_ubicacion = LocationSerializer(many=True)


class LandInspectionUploadSerializer(serializers.Serializer):
    """tb_properties"""
    cod_carga = serializers.CharField()
    cod_usuario = serializers.CharField()
    tb_ticket = TicketSerializer()


class MobileLandInspectionSerializer(serializers.Serializer):
    """nodo principal"""
    tb_properties = LandInspectionUploadSerializer()

    def save(self, **kwargs):
        validated_data = dict(self.validated_data)
        tb_properties = dict(validated_data.get('tb_properties', {}))
        tb_ticket = dict(tb_properties.get('tb_ticket', {}))
        tb_ubicacion = dict(tb_properties.get('tb_ubicacion', {}))

        # Validar si el registro existe en la tb_properties
        cod_upload = tb_properties.get('cod_carga', None)
        cod_usuario = tb_properties.get('cod_usuario', None)
        self.instance = LandInspectionUpload.objects.filter(cod_carga=cod_upload, user_id=cod_usuario).first()
        if self.instance is None:
            self.instance = self.create_inspection_upload(tb_properties, cod_upload)

        self.create_ticket(tb_ticket, inspection_upload=self.instance)

        return self.instance

    def create_inspection_upload(self, tb_properties, cod_upload):
        cod_uer = int(tb_properties.get('cod_usuario', None))
        user = User.objects.filter(id=cod_uer).first()
        instance = LandInspectionUpload.objects.create(
            cod_carga=cod_upload,
            user=user,
            username=user.username
        )
        return instance

    def create_ticket(self, tb_ticket, inspection_upload):
        cod_ticket = tb_ticket.get('cod_ticket', None)
        ticket = Ticket.objects.filter(cod_ticket=cod_ticket).first()
        if cod_ticket is not None and ticket is not None:
            raise exceptions.ValidationError('El ticket ya existe')
        date_format = '%d%m%y%H%M'
        fec_inicio_trabajo = tb_ticket.get('fec_inicio_trabajo', None)
        fec_ultima_actualizacion = tb_ticket.get('fec_ultima_actualizacion', None)
        fec_asignacion = tb_ticket.get('fec_asignacion', None)

        if fec_inicio_trabajo:
            fec_inicio_trabajo = datetime.strptime(fec_inicio_trabajo, date_format)

        if fec_ultima_actualizacion:
            fec_ultima_actualizacion = datetime.strptime(fec_ultima_actualizacion, date_format)

        if fec_asignacion:
            fec_asignacion = datetime.strptime(fec_asignacion, date_format)

        Ticket.objects.create(
            inspection_upload=inspection_upload,
            cod_ticket=tb_ticket.get('cod_ticket', None),
            cod_tipo_ticket_id=tb_ticket.get('cod_tipo_ticket', None),
            cod_est_trabajo_ticket_id=tb_ticket.get('cod_est_trabajo_ticket', None),
            cod_est_envio_ticket_id=tb_ticket.get('cod_est_envio_ticket', None),
            cod_usuario=tb_ticket.get('cod_usuario', None),
            obs_ticket_usuario=tb_ticket.get('obs_ticket_usuario', None),
            fec_inicio_trabajo=fec_inicio_trabajo,
            fec_ultima_actualizacion=fec_ultima_actualizacion,
            fec_asignacion=fec_asignacion,
            obs_ticket_gabinete=tb_ticket.get('obs_ticket_gabinete', None)
        )
