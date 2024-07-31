import base64
from datetime import datetime

from django.core.files import File
from django.conf import settings
from django.db import transaction
from rest_framework import serializers, exceptions
from apps.users.models import User
from .models import (
    LandInspectionUpload, Ticket, Location, RecordOwnerShip, LandCharacteristic, LandFacility, LandSupply,
    LandInspection, LandOwnerInspection, LandOwnerDetailInspection, LocationPhoto
)

from apps.master_data.models import MasterTypeUrbanUnit
class LandOwnerInspectionSerializer(serializers.Serializer):
    """tb_contribuyente"""
    tip_doc = serializers.CharField()
    doc_iden = serializers.CharField()
    cod_contr = serializers.CharField(allow_blank=True, allow_null=True)
    cond_contr = serializers.CharField(allow_blank=True, allow_null=True)
    dir_fiscal = serializers.CharField(allow_blank=True, allow_null=True)
    nombre = serializers.CharField()
    ap_pat = serializers.CharField()
    ap_mat = serializers.CharField()
    contribuyente = serializers.CharField(allow_blank=True, allow_null=True)
    conyuge = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        ref_name = 'mobile_owner_serializer'


class LandOwnerDetailInspectionSerializer(serializers.Serializer):
    """tb_predio_contribuyente"""
    doc_iden = serializers.CharField()
    cod_tit = serializers.CharField()
    cod_pre = serializers.CharField(allow_blank=True, allow_null=True)
    tb_contribuyente = LandOwnerInspectionSerializer()

    class Meta:
        ref_name = 'mobile_owner_datail_serializer'


class LandInspectionSerializer(serializers.Serializer):
    """tb_predio"""
    cod_tit = serializers.CharField()
    cod_pre = serializers.CharField(allow_blank=True, allow_null=True)
    cod_cpu = serializers.CharField(allow_blank=True, allow_null=True)
    piso = serializers.CharField(allow_blank=True, allow_null=True)
    num_sumi_agua = serializers.CharField(allow_blank=True, allow_null=True)
    cod_tipo_predio = serializers.IntegerField(allow_blank=True, allow_null=True)
    num_sumi_luz = serializers.CharField(allow_blank=True, allow_null=True)
    #uso_especifico = serializers.CharField(allow_blank=True, allow_null=True)
    interior = serializers.CharField(allow_blank=True, allow_null=True)
    obs_predio = serializers.CharField(allow_blank=True, allow_null=True)
    num_dpto = serializers.CharField(allow_blank=True, allow_null=True)
    codigo_uso = serializers.CharField(allow_blank=True, allow_null=True)
    codigo_clase_uso  = serializers.CharField(allow_blank=True, allow_null=True)
    codigo_subclase_uso = serializers.CharField(allow_blank=True, allow_null=True)
    #estado = serializers.CharField(allow_blank=True, allow_null=True)
    block = serializers.CharField(allow_blank=True, allow_null=True)
    num_sumi_gas = serializers.CharField(allow_blank=True, allow_null=True)
    tb_predio_contribuyente = LandOwnerDetailInspectionSerializer(many=True)

    class Meta:
        ref_name = 'mobile_land_serializer'


class LandSupplySerializer(serializers.Serializer):
    """tb_suministro"""
    cod_tit = serializers.CharField()
    cod_tipo_sumi = serializers.CharField()
    num_sumis = serializers.CharField()
    obs_sumis = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        ref_name = 'mobile_supply_serializer'


class LandFacilitySerializer(serializers.Serializer):
    """tb_instalaciones"""
    cod_tit = serializers.CharField()
    cod_inst = serializers.CharField()
    cod_tipo_inst = serializers.CharField(allow_blank=True, allow_null=True)
    anio_construccion = serializers.CharField(allow_blank=True, allow_null=True)
    estado_conserva = serializers.CharField(allow_blank=True, allow_null=True)
    dimension = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        ref_name = 'mobile_facility_serializer'


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

    class Meta:
        ref_name = 'mobile_characteristic_serializer'


class RecordOwnerShipSerializer(serializers.Serializer):
    """tb_registro_titularidad"""
    cod_tit = serializers.CharField()
    cod_tipo_tit = serializers.CharField()
    cod_ubicacion = serializers.CharField()
    tb_predio = LandInspectionSerializer(required=False)
    tb_suministro = LandSupplySerializer(required=False)
    tb_caracteristicas = LandCharacteristicSerializer()
    tb_instalaciones = LandFacilitySerializer(many=True)

    class Meta:
        ref_name = 'mobile_record_owner_serializer'


class LocationPhotoSerializer(serializers.Serializer):
    """tb_foto"""
    cod_foto = serializers.CharField()
    cod_ubicacion = serializers.CharField()
    cod_tipo_foto = serializers.CharField()
    url_foto = serializers.CharField()

    class Meta:
        ref_name = 'mobile_location_photo_serializer'


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
    num_alt = serializers.CharField(allow_blank=True, allow_null=True, required=False)
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

    class Meta:
        ref_name = 'mobile_location_serializer'


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

    class Meta:
        ref_name = 'mobile_tiket_serializer'


class LandInspectionUploadSerializer(serializers.Serializer):
    """tb_properties"""
    cod_carga = serializers.CharField()
    cod_usuario = serializers.CharField()
    tb_ticket = TicketSerializer()


class MobileLandInspectionSerializer(serializers.Serializer):
    """nodo principal"""
    tb_properties = LandInspectionUploadSerializer()

    @transaction.atomic
    def save(self, **kwargs):
        validated_data = dict(self.validated_data)
        tb_properties = dict(validated_data.get('tb_properties', {}))
        tb_ticket = dict(tb_properties.get('tb_ticket', {}))
        locations = list(tb_ticket.get('tb_ubicacion', []))

        # Validar si el registro existe en la tb_properties
        cod_upload = tb_properties.get('cod_carga', None)
        cod_usuario = tb_properties.get('cod_usuario', None)
        self.instance = LandInspectionUpload.objects.filter(cod_carga=cod_upload, user_id=cod_usuario).first()
        if self.instance is None:
            self.instance = self.create_inspection_upload(tb_properties, cod_upload)

        ticket = self.create_ticket(tb_ticket, inspection_upload=self.instance)

        for location in locations:
            tb_location = dict(location)
            self.create_location(tb_location, ticket,tb_ticket)

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

        return Ticket.objects.create(
            inspection_upload=inspection_upload,
            cod_ticket=tb_ticket.get('cod_ticket', None),
            cod_tipo_ticket_id=self.blank_to_null(tb_ticket.get('cod_tipo_ticket', None)),
            cod_est_trabajo_ticket_id=self.blank_to_null(tb_ticket.get('cod_est_trabajo_ticket', None)),
            cod_est_envio_ticket_id=self.blank_to_null(tb_ticket.get('cod_est_envio_ticket', None)),
            cod_usuario=tb_ticket.get('cod_usuario', None),
            obs_ticket_usuario=tb_ticket.get('obs_ticket_usuario', None),
            fec_inicio_trabajo=fec_inicio_trabajo,
            fec_ultima_actualizacion=fec_ultima_actualizacion,
            fec_asignacion=fec_asignacion,
            obs_ticket_gabinete=tb_ticket.get('obs_ticket_gabinete', None)
        )

    def create_location(self, tb_location, ticket,tb_ticket):
        cod_tipo_uu =tb_location.get('cod_tipo_uu', None)
        uu = None
        if cod_tipo_uu is not None:
            uu=MasterTypeUrbanUnit.objects.get(id=cod_tipo_uu)
            
        location = Location.objects.create(
            cod_ticket=ticket,
            cod_ubicacion=tb_location.get('cod_ubicacion', None),
            cod_tip_via=tb_location.get('cod_tip_via', None),
            cod_via=tb_location.get('cod_via', None),
            nom_via=tb_location.get('nom_via', None),
            num_alt=tb_location.get('num_alt', None),
            nom_alt=tb_location.get('nom_alt', None),
            cod_tipo_uu=uu,
            cod_uu=tb_location.get('cod_uu', None),
            nom_uu=tb_location.get('nom_uu', None),
            nom_ref=tb_location.get('nom_ref', None),
            km=tb_location.get('km', None),
            x=tb_location.get('x', None),
            y=tb_location.get('y', None),
            lot_urb=tb_location.get('lot_urb', None),
            num_mun=tb_location.get('num_mun', None),
            mzn_urb=tb_location.get('mzn_urb', None),
            cod_usuario=tb_location.get('cod_usuario', None),
            obs_ubicacion=tb_location.get('obs_ubicacion', None),
            referencia=tb_location.get('referencia', None),
        )

        records = list(tb_location.get('tb_registro_titularidad', []))
        for record in records:
            tb_registro = dict(record)
            self.create_record_owner(tb_registro, location,tb_ticket)

        photos = list(tb_location.get('tb_foto', []))
        for photo in photos:
            tb_photo = dict(photo)
            self.create_photo(tb_photo, location)

    def create_photo(self, tb_photo, location):
        photo = LocationPhoto.objects.create(
            cod_ubicacion=location,
            cod_foto=tb_photo.get('cod_foto'),
            cod_tipo_foto_id=self.blank_to_null(tb_photo.get('cod_tipo_foto', None)),
            foto=None
        )

        self.photo_base64_to_jpg(tb_photo, photo)

    def photo_base64_to_jpg(self, tb_photo, photo):
        tmp_upload = settings.MEDIA_ROOT / 'tmp_uploads'
        tmp_upload.mkdir(parents=True, exist_ok=True)

        cod_location = tb_photo.get('cod_ubicacion')
        cod_photo = tb_photo.get('cod_foto')
        photo_base64 = tb_photo.get('url_foto')
        file_name = f'{cod_location}_{cod_photo}.jpg'
        file_path = tmp_upload / file_name

        try:
            image = base64.b64decode(photo_base64)
            with open(file_path, "wb") as f:
                f.write(image)

            photo.foto.save(file_name, File(open(file_path, 'rb')))

        except Exception as e:
            print(f'error al cargar imagen imagen {cod_photo}')

    def create_record_owner(self, tb_registro, location,tb_ticket):

        if len(tb_registro) == 0:
            return None

        cod_tit = tb_registro.get('cod_tit', '')
        
        cod_ticket=tb_ticket.get('cod_ticket', None)
        ubigeo = cod_ticket[1:7]
        record = RecordOwnerShip.objects.create(
            cod_ubicacion=location,
            cod_tit=cod_tit,
            ubigeo=ubigeo,
            cod_tipo_tit_id=self.blank_to_null(tb_registro.get('cod_tipo_tit', None)),
        )

        tb_characteristic = dict(tb_registro.get('tb_caracteristicas', {}))
        tb_supply = dict(tb_registro.get('tb_supply', {}))
        tb_land_inspection = dict(tb_registro.get('tb_predio', {}))
        facilities = list(tb_registro.get('tb_instalaciones', []))

        self.create_characteristic(tb_characteristic, record)
        self.create_supply(tb_supply, record)
        self.create_land_inspection(tb_land_inspection, record)

        for facility in facilities:
            tb_facility = dict(facility)
            self.create_facility(tb_facility, record)

    def create_characteristic(self, tb_characteristic, record):

        if len(tb_characteristic) == 0:
            return None

        LandCharacteristic.objects.create(
            cod_tit=record,
            categoria_electrica=tb_characteristic.get('categoria_electrica', None),
            piso=tb_characteristic.get('piso', None),
            estado_conserva=tb_characteristic.get('estado_conserva', None),
            anio_construccion=tb_characteristic.get('anio_construccion', None),
            catergoria_techo=tb_characteristic.get('catergoria_techo', None),
            longitud_frente=tb_characteristic.get('longitud_frente', None),
            categoria_muro_columna=tb_characteristic.get('categoria_muro_columna', None),
            catergoria_puerta_ventana=tb_characteristic.get('catergoria_puerta_ventana', None),
            arancel=tb_characteristic.get('arancel', None),
            material_pred=tb_characteristic.get('material_pred', None),
            categoria_revestimiento=tb_characteristic.get('categoria_revestimiento', None),
            area_terreno=tb_characteristic.get('area_terreno', None),
            clasificacion_pred=tb_characteristic.get('clasificacion_pred', None),
            catergoria_piso=tb_characteristic.get('catergoria_piso', None),
            catergoria_bano=tb_characteristic.get('catergoria_bano', None),
            area_construida=tb_characteristic.get('area_construida', None),
        )

    def create_facility(self, tb_facility, record):
        if len(tb_facility) == 0:
            return None

        LandFacility.objects.create(
            cod_tit=record,
            cod_inst=tb_facility.get('cod_inst', None),
            cod_tipo_inst_id=self.blank_to_null(tb_facility.get('cod_tipo_inst', None)),
            anio_construccion=tb_facility.get('anio_construccion', None),
            estado_conserva=tb_facility.get('estado_conserva', None),
            dimension=tb_facility.get('dimension', None),
        )

    def create_supply(self, tb_supply, record):
        if len(tb_supply) == 0:
            return None

        LandSupply.objects.create(
            cod_tit=record,
            cod_tipo_sumi_id=self.blank_to_null(tb_supply.get('cod_tipo_sumi', None)),
            num_sumis=tb_supply.get('num_sumis', None),
            obs_sumis=tb_supply.get('obs_sumis', None),
        )

    def create_land_inspection(self, tb_land_inspection, record):
        if len(tb_land_inspection) == 0:
            return None

        land_inspection = LandInspection.objects.create(
            cod_tit=record,
            ubigeo=record.ubigeo,
            cod_cpu=tb_land_inspection.get('cod_cpu', None),
            cod_pre=tb_land_inspection.get('cod_pre', None),
            cod_tipo_predio_id=self.blank_to_null(tb_land_inspection.get('cod_tipo_predio', None)),
            piso=tb_land_inspection.get('piso', None),
            num_sumi_agua=tb_land_inspection.get('num_sumi_agua', None),
            num_sumi_luz=tb_land_inspection.get('num_sumi_luz', None),
            #uso_especifico=tb_land_inspection.get('uso_especifico', None),
            interior=tb_land_inspection.get('interior', None),
            obs_predio=tb_land_inspection.get('obs_predio', None),
            num_dpto=tb_land_inspection.get('num_dpto', None),
            codigo_uso=tb_land_inspection.get('codigo_uso', None),
            codigo_clase_uso =tb_land_inspection.get('codigo_clase_uso',  None),
            codigo_subclase_uso=tb_land_inspection.get('codigo_subclase_uso',  None),
            #estado=tb_land_inspection.get('estado', None),
            block=tb_land_inspection.get('block', None),
            num_sumi_gas=tb_land_inspection.get('num_sumi_gas', None),
        )

        land_owner_detail_inspections = list(tb_land_inspection.get('tb_predio_contribuyente', []))
        for tb_land_owner_detail_inspection in land_owner_detail_inspections:
            self.create_land_owner_detail_inspection(tb_land_owner_detail_inspection, land_inspection, record)

    def create_land_owner_detail_inspection(self, tb_land_owner_detail_inspection, land_inspection, record):
        tb_land_owner_inspection = dict(tb_land_owner_detail_inspection.get('tb_contribuyente', {}))

        if not (len(tb_land_owner_detail_inspection) > 0 and len(tb_land_owner_inspection) > 0):
            return None

        land_owner_inspection = self.create_land_owner_inspection(tb_land_owner_inspection, record)
        LandOwnerDetailInspection.objects.create(
            cod_tit=record,
            ubigeo=record.ubigeo,
            cod_pred_inspec=land_inspection,
            cod_contr_inspec=land_owner_inspection,
            doc_iden=tb_land_owner_detail_inspection.get('doc_iden', None),
            cod_pre=tb_land_owner_detail_inspection.get('cod_pre', None),
        )

    def create_land_owner_inspection(self, tb_land_owner_inspection, record):
        return LandOwnerInspection.objects.create(
            cod_tit=record,
            cod_contr=tb_land_owner_inspection.get('cod_contr', None),
            tip_doc=tb_land_owner_inspection.get('tip_doc', None),
            doc_iden=tb_land_owner_inspection.get('doc_iden', None),
            dir_fiscal=tb_land_owner_inspection.get('dir_fiscal', None),
            ap_mat=tb_land_owner_inspection.get('ap_mat', None),
            ap_pat=tb_land_owner_inspection.get('ap_pat', None),
            cond_contr=tb_land_owner_inspection.get('cond_contr', None),
            contribuyente=tb_land_owner_inspection.get('contribuyente', None),
            nombre=tb_land_owner_inspection.get('nombre', None),
            conyuge=tb_land_owner_inspection.get('conyuge', None),
        )

    def blank_to_null(self, value):
        if value == "":
            return None
        return value
