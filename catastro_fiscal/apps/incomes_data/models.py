from django.db import models


class Contribuyente(models.Model):
    """Renta Contribuyente"""
    ubigeo = models.CharField(max_length=6, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(max_length=50, blank=True, null=True, help_text='Código de contribuyente')
    fecha_inscripcion = models.CharField(max_length=10, blank=True, null=True, help_text='Fecha de inscripción')
    tipo_doc = models.CharField(max_length=10, blank=True, null=True, help_text='Código del tipo de documento')
    documento_desc = models.CharField(max_length=30, blank=True, null=True, help_text='Descripción tipo de documento')
    num_doc = models.CharField(max_length=20, blank=True, null=True, help_text='Número de documento')
    apellido_paterno = models.CharField(max_length=90, help_text='Apellido paterno')
    apellido_materno = models.CharField(max_length=90, blank=True, null=True, help_text='Apellido materno')
    nombre = models.CharField(max_length=90, help_text='Nombre')
    tipo_contribuyente_desc = models.CharField(
        max_length=30, blank=True, null=True,
        help_text='Tipo contribuyente (Persona natural o jurídica, Sucesión indivisa)'
    )
    condicion_contribuyente_desc = models.CharField(
        max_length=90, blank=True, null=True,
        help_text='Condición de contribuyente (indicar: Centro Educativo, Centro religioso, Universidades)'
    )
    estado = models.CharField(max_length=20, blank=True, null=True, help_text='Estado (Activo/Inactivo)')
    es_foraneo = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Es foráneo (Si, No) Si el titular vive en el mismo distrito.'
    )
    distrito_desc = models.CharField(max_length=90, blank=True, null=True, help_text='Distrito')
    provincia_desc = models.CharField(max_length=90, blank=True, null=True, help_text='Provincia')
    departamento_desc = models.CharField(max_length=90, blank=True, null=True, help_text='Departamento')
    tipo_habilitacion_desc = models.CharField(
        max_length=30, blank=True, null=True,
        help_text='Tipo de habilitación urbana'
    )
    nombre_habilitacion = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Nombre de la habilitación urbana'
    )
    tipo_via_desc = models.CharField(max_length=30, blank=True, null=True, help_text='Tipo vía')
    nombre_via = models.CharField(max_length=250, blank=True, null=True, help_text='Nombre vía')
    manzana_urbana = models.CharField(max_length=10, blank=True, null=True, help_text='Manzana urbana')
    cuadra = models.CharField(max_length=2, blank=True, null=True, help_text='Cuadra (opcional)')
    lado = models.CharField(max_length=2, blank=True, null=True, help_text='Lado (opcional)')
    numero_direccion = models.CharField(max_length=10, blank=True, null=True, help_text='Número de la dirección')
    numero_alterno = models.CharField(max_length=10, blank=True, null=True, help_text='Numero alterno')
    numero_departamento = models.CharField(max_length=10, blank=True, null=True, help_text='Número del departamento')
    lote = models.CharField(max_length=10, blank=True, null=True, help_text='Lote')
    interior = models.CharField(max_length=10, blank=True, null=True, help_text='Interior')
    block = models.CharField(max_length=10, blank=True, null=True, help_text='Block')
    es_pensionista = models.CharField(max_length=10, blank=True, null=True, help_text='Es pensionista (Si, No)')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_CONTRIBUYENTE'


class MarcoPredio(models.Model):
    """Rentas Marco Predio"""
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_pre = models.CharField(max_length=100, blank=True, null=True, help_text='Código de predio de la municipal')
    codigo_cpu = models.CharField(max_length=15, blank=True, null=True, help_text='Código de CPU (va vacío)')
    nombre_predio = models.CharField(max_length=250, blank=True, null=True, help_text='Descripción de predio')
    habilitacion = models.CharField(max_length=4, blank=True, null=True, help_text='Código de habilitación')
    nombre_habilitacion = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Nombre de la habilitación'
    )
    nombre_tipo_habilitacion = models.CharField(max_length=30, blank=True, null=True, help_text='Tipo de habilitación')
    via = models.CharField(max_length=4, blank=True, null=True, help_text='Código de vía')
    nombre_tipo_via = models.CharField(
        max_length=30, blank=True, null=True,
        help_text='Descripción de tipo de vía (Av/Jr/Pje)'
    )
    nombre_via = models.CharField(max_length=250, blank=True, null=True, help_text='Nombre vía')
    manzana_urbana = models.CharField(max_length=10, blank=True, null=True, help_text='Manzana urbana')
    cuadra = models.CharField(max_length=2, blank=True, null=True, help_text='Cuadra (opcional)')
    lado = models.CharField(max_length=2, blank=True, null=True, help_text='Lado (opcional)')
    numero_direccion = models.CharField(max_length=10, blank=True, null=True, help_text='Número de la dirección')
    numero_alterno = models.CharField(max_length=10, blank=True, null=True, help_text='Numero alterno')
    block = models.CharField(max_length=10, blank=True, null=True, help_text='Block')
    numero_departamento = models.CharField(max_length=10, blank=True, null=True, help_text='Número del departamento')
    interior = models.CharField(max_length=10, blank=True, null=True, help_text='Interior')
    lote = models.CharField(max_length=10, blank=True, null=True, help_text='Lote')
    km = models.CharField(max_length=20, blank=True, null=True, help_text='N° Km ubicación predio rural')
    estado = models.CharField(max_length=20, blank=True, null=True, help_text='Si esta activo, inactivo: A/I')
    es_independizado = models.CharField(max_length=10, blank=True, null=True, help_text='Es independizado (S, N)')
    tipo_titulacion = models.CharField(max_length=10, blank=True, null=True, help_text='Código de tipo de titulación')
    desc_titulo = models.CharField(
        max_length=120, blank=True, null=True,
        help_text='Descripción del título de predio rural'
    )
    codigo_predio_titulo = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Código de predio del título (predio rural)'
    )
    numero_unidad_catastral = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Numero unidad catastral predio rural'
    )
    codigo_referencia_catastral = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Código de referencia catastral predio rural'
    )
    numero_parcela_agricola = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Número de parcela agricola'
    )
    numero_partida_registral = models.CharField(
        max_length=100, blank=True, null=True,
        help_text='Número partida registral'
    )
    perimetro = models.CharField(max_length=100, blank=True, null=True, help_text='Perímetro')
    referencia = models.CharField(max_length=250, blank=True, null=True, help_text='Referencia de dirección')
    id_cl = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Llave de la tabla de aranceles de la municipalidad (id cuadra lado)'
    )
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_MARCO_PREDIO'


class Arancel(models.Model):
    """Renta Arancel"""
    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    id_cl = models.CharField(
        max_length=20, blank=True, null=True,
        help_text='Llave de la tabla de aranceles de la municipalidad (id cuadra lado)'
    )
    sector_catastral = models.CharField(max_length=2, blank=True, null=True, help_text='Sector catastral (opcional)')
    manzana_catastral = models.CharField(max_length=2, blank=True, null=True, help_text='Manzana catastral (opcional)')
    codigo_via = models.CharField(max_length=4, blank=True, null=True, help_text='Código via (opcional)')
    denominacion_de_via = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Denominación de vía (opcional)'
    )
    lado_imp_par = models.CharField(max_length=1, blank=True, null=True, help_text='Lado (impar o par) (opcional)')
    cuadra_de_via = models.CharField(max_length=5, blank=True, null=True, help_text='Cuadra de vía (opcional)')
    cod_hab_urbana = models.CharField(
        max_length=4, blank=True, null=True,
        help_text='Código de habilitación urbana (opcional)'
    )
    habilit_urbana = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Habilitación urbana (opcional)'
    )
    mza_urbana = models.CharField(max_length=10, blank=True, null=True, help_text='Manzana urbana (opcional)')
    ubica_parque_jardin_id = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Id  de ubicación a parque/jardin (opcional)'
    )
    ano_arancelario = models.CharField(max_length=4, blank=True, null=True, help_text='Año arancelario')
    arancel = models.CharField(max_length=6, blank=True, null=True, help_text='Arancel')
    ano_x_procesar = models.CharField(max_length=4, blank=True, null=True, help_text='Año por procesar')
    arancel_actual = models.CharField(max_length=6, blank=True, null=True, help_text='Arancel actual')
    fila = models.CharField(max_length=10, blank=True, null=True, help_text='Fila')
    id_arancel = models.CharField(
        max_length=20, blank=True, null=True,
        help_text='Opcional información del catastro fiscal'
    )
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_ARANCEL'


class PredioDato(models.Model):
    """Renta Predio Dato"""
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    ano_aplicacion = models.CharField(max_length=4, blank=True, null=True, help_text='Año de Aplicación')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Código de contribuyente')
    cod_pre = models.CharField(max_length=100, blank=True, null=True, help_text='Código de predio')
    cond_predio = models.CharField(max_length=20, blank=True, null=True, help_text='Condición del predio')
    fecha_recepcion = models.CharField(max_length=10, blank=True, null=True, help_text='Fecha de recepción')
    codigo_uso = models.CharField(max_length=6, blank=True, null=True, help_text='Código de uso')
    uso_especifico = models.CharField(max_length=150, blank=True, null=True, help_text='Uso específico')
    tipo_predio = models.CharField(max_length=50, blank=True, null=True, help_text='Tipo de predio')
    estado_const = models.CharField(max_length=50, blank=True, null=True, help_text='Estado de construcción')
    condicion_prop = models.CharField(max_length=50, blank=True, null=True, help_text='Condición de propiedad')
    porcentaje_copropiedad = models.CharField(
        max_length=255, blank=True, null=True,
        help_text='Porcentaje de copropiedad'
    )
    area_terreno = models.CharField(max_length=255, blank=True, null=True, help_text='Área de terreno')
    area_terreno_comun = models.CharField(max_length=255, blank=True, null=True, help_text='Área de terreno común')
    arancel = models.CharField(max_length=255, blank=True, null=True, help_text='Arancel')
    valor_terreno_urbano = models.CharField(max_length=255, blank=True, null=True, help_text='Valor terreno urbano')
    area_construida = models.CharField(max_length=255, blank=True, null=True, help_text='Área construida')
    valor_total_construccion = models.CharField(
        max_length=255, blank=True, null=True,
        help_text='Valor total de construccion'
    )
    valor_otras_instalaciones = models.CharField(
        max_length=255, blank=True, null=True,
        help_text='Valor otras instalaciones'
    )
    valor_predio = models.CharField(max_length=255, blank=True, null=True, help_text='Valor de predio')
    imp_predial = models.CharField(max_length=255, blank=True, null=True, help_text='Impuesto predial')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_PREDIO_DATO'


class PredioCaracteristica(models.Model):
    """Contiene los datos de cálculo de las características del predio de la masiva."""
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    ano_aplicacion = models.CharField(max_length=4, blank=True, null=True, help_text='Año de Aplicación')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Código de contribuyente')
    cod_pre = models.CharField(max_length=10, blank=True, null=True, help_text='Código de predio')
    tipo_piso = models.CharField(max_length=9, blank=True, null=True, help_text='Tipo_piso')
    nivel = models.CharField(max_length=4, blank=True, null=True, help_text='Nivel')
    ano_construccion = models.CharField(max_length=4, blank=True, null=True, help_text='Año de construccion')
    clasificacion_pred = models.CharField(max_length=150, blank=True, null=True, help_text='Clasificación del predio')
    material_pred = models.CharField(max_length=50, blank=True, null=True, help_text='Material de predio')
    estado_conserva = models.CharField(max_length=50, blank=True, null=True, help_text='Estado de conservación')
    categoria_muro_columna = models.CharField(
        max_length=1, blank=True, null=True,
        help_text='Categoria de muro y columna'
    )
    categoria_techo = models.CharField(max_length=1, blank=True, null=True, help_text='Categoria de techo')
    categoria_piso = models.CharField(max_length=1, blank=True, null=True, help_text='Categoria de piso')
    categoria_puerta_ventana = models.CharField(
        max_length=1, blank=True, null=True,
        help_text='Categoria de puerta y ventana'
    )
    categoria_revestimiento = models.CharField(
        max_length=1, blank=True, null=True,
        help_text='Categoria de revestimiento'
    )
    categoria_bano = models.CharField(max_length=1, blank=True, null=True, help_text='Categoria de bano')
    categoria_electrica = models.CharField(max_length=1, blank=True, null=True, help_text='Categoria de electricidad')
    area_construida = models.FloatField(blank=True, null=True, help_text='Área construida')
    valor_unitario = models.FloatField(blank=True, null=True, help_text='Valor unitario')
    incremento = models.FloatField(blank=True, null=True, help_text='Incrementos')
    porcentaje_depreciacion = models.FloatField(blank=True, null=True, help_text='Porcentaje de depreciacion')
    valor_unitario_depreciado = models.FloatField(blank=True, null=True, help_text='Valor unitario de depreciado')
    valor_nivel = models.FloatField(blank=True, null=True, help_text='Valor nivel de piso')
    porcentaje_comun = models.FloatField(blank=True, null=True, help_text='Porcentaje comun')
    total_area_bien_comun = models.FloatField(blank=True, null=True, help_text='Total área de bien común')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_PREDIO_CARACT'


class Recaudacion(models.Model):
    """Datos de Recaudación a nivel de contribuyente."""
    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Código de contribuyente')
    rec_imp_pred = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de Impuesto Predial (IP) recaudado corriente'
    )
    rec_arb = models.FloatField(blank=True, null=True, help_text='Recaudación de arbitrios corriente')
    rec_imp_veh = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de impuesto vehicular corriente'
    )
    rec_imp_pred_nc = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de Impuesto Predial (IP) recaudado no corriente'
    )
    rec_arb_nc = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de arbitrios muncipales no corriente'
    )
    rec_imp_veh_nc = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de impuesto vehicular no corriente'
    )
    rec_op_p_c = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por orden de pago predial corriente'
    )
    rec_op_p_nc = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por orden de pago predial no corriente'
    )
    rec_rd_p_c = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por resoluciones de determinación de predial corriente'
    )
    rec_rd_p_nc = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por resoluciones de determinación de predial no corriente'
    )
    rec_res_determ_arb = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por resoluciones de determinación de arbitrios '
    )
    rec_res_ejec_coactiva_predial = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por resoluciones de ejecución coactiva predial'
    )
    rec_res_ejec_coactiva_arbitrios = models.FloatField(
        blank=True, null=True,
        help_text='Recaudado por resoluciones de ejecución coactiva arbitrios municipales'
    )
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_RECAUDACION'


class Deuda(models.Model):
    """Detalle de duda de contribuyentes"""
    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Código de contribuyente')
    deuda_arb = models.FloatField(
        blank=True, null=True,
        help_text='Determinación de arbitrios de la deuda total del año corriente'
    )
    saldo_t_p = models.FloatField(blank=True, null=True, help_text='Saldos por cobrar t predial')
    saldo_t_1_p = models.FloatField(blank=True, null=True, help_text='Saldos por cobrar t-1 predial')
    saldo_t_v = models.FloatField(blank=True, null=True, help_text='Saldos por cobrar t vehicular')
    saldo_t_a = models.FloatField(blank=True, null=True, help_text='Saldos por cobrar t arbitrios')
    saldo_t_1_a = models.FloatField(blank=True, null=True, help_text='Saldos por cobrar t-1 arbitrios')
    ano_deuda_t = models.IntegerField(blank=True, null=True, help_text='Número de años de deuda de arbitrios')
    ano_deuda_p = models.IntegerField(blank=True, null=True, help_text='Número de años de deuda de predial')
    ano_deuda_v = models.IntegerField(blank=True, null=True, help_text='Número de años de deuda del vehícular')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_DEUDA'


class Emision(models.Model):
    """Datos de Emision"""
    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Código de contribuyente')
    emision_ord_pago = models.FloatField(
        blank=True, null=True,
        help_text='Emisión de órdenes de pago deuda no corriente predial'
    )
    emision_res_det = models.FloatField(
        blank=True, null=True,
        help_text='Emisión de resoluciones de determinación'
    )
    emision_iv_corriente = models.FloatField(
        blank=True, null=True,
        help_text='Emisión de Impuesto Vehícular del año corriente'
    )
    emi_res_det_c = models.FloatField(
        blank=True, null=True,
        help_text='Emisión por resoluciones de determinación predial deuda corriente'
    )
    emi_res_det_nc = models.FloatField(
        blank=True, null=True,
        help_text='Emisión por resoluciones de determinación predial deuda no corriente'
    )
    emi_res_cp = models.FloatField(
        blank=True, null=True,
        help_text='Emisión por resoluciones de Ejecución Coactiva predial'
    )
    emi_res_ca = models.FloatField(
        blank=True, null=True,
        help_text='Emisión por resoluciones de Ejecución Coactiva arbitrios'
    )
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_EMISION'


class BaseImponible(models.Model):
    """Datos de Base imponible por contribuyente"""
    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(
        max_length=30, blank=True, null=True,
        help_text='Llave identificador del contribuyente'
    )
    base_imponible_t = models.FloatField(blank=True, null=True, help_text='Base imponible t')
    base_imponible_t_1 = models.FloatField(blank=True, null=True, help_text='base imponible t.1')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_BIMPONIBLE'


class Alicuota(models.Model):
    """Lista de alicuotas por contribuyentes"""

    ano_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(
        max_length=30, blank=True, null=True,
        help_text='Llave identificador del contribuyente'
    )
    rec_pred_alicuota = models.FloatField(
        blank=True, null=True,
        help_text='Recaudación de predial corriente de contribuyentes afectos a la alícuota 1%. '
                  'Recaudación corriente del impuesto predial de contribuyentes cuyo cálculo del '
                  'impuesto predial alcanza la alicuota del 1%')
    emision_pred_alicuota = models.FloatField(
        blank=True, null=True,
        help_text='emisión predial alícuota 1%. Emisión corriente del impuesto predial de contribuyentes'
                  ' cuyo cálculo del impuesto predial alcanza la alicuota del 1%'
    )
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_ALICUOTA'


class AmnistiaContribuyente(models.Model):
    """Contiene el detalle de las amnistías por municipalidades."""

    anio_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de Aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_tipo_amn = models.CharField(max_length=10, blank=True, null=True, help_text='Código del tipo de amnisitia')
    cod_contr = models.CharField(max_length=30, blank=True, null=True, help_text='Descripción del tipo de amnistía')
    tributo_afecto = models.CharField(max_length=120, blank=True, null=True, help_text='Tributo afecto')
    tipo_periodo = models.CharField(max_length=120, blank=True, null=True, help_text='Tipo periodo')
    periodo = models.CharField(max_length=120, blank=True, null=True, help_text='Periodos')
    tipo_int_ins = models.CharField(max_length=120, blank=True, null=True, help_text='Tipo interes o insoluto')
    porc_desc = models.FloatField(blank=True, null=True, help_text='% Descuento')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_AMNCONTRIBUYENTE'


class AmnistiaMunicipal(models.Model):
    """Contiene el resumen de las amnistías de las municipalidades."""

    anio_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de Aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    tipo_amn_benef = models.CharField(max_length=30, blank=True, null=True, help_text='Tipo')
    nomb_amn_benef = models.CharField(
        max_length=250, blank=True, null=True,
        help_text='Nombre de la amnistía o beneficio'
    )
    nro_ordenanza = models.CharField(max_length=120, blank=True, null=True, help_text='N° Ordenanza')
    fecha_ini = models.CharField(max_length=20, blank=True, null=True, help_text='Fecha de inicio')
    fecha_fin = models.CharField(max_length=20, blank=True, null=True, help_text='Fecha de fin')
    tributo_afecto = models.CharField(max_length=120, blank=True, null=True, help_text='Tributo afecto')
    tipo_periodo = models.CharField(max_length=120, blank=True, null=True, help_text='Tipo periodo')
    periodo = models.CharField(max_length=120, blank=True, null=True, help_text='Periodos')
    tipo_int_ins = models.CharField(max_length=120, blank=True, null=True, help_text='Tipo interes o insoluto')
    porc_desc = models.FloatField(blank=True, null=True, help_text='% Descuento')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_AMNMUNICIPAL'


class VaremMunicipal(models.Model):
    """Contiene la fecha de emisión masiva predial para el cálculo de los indicadores."""

    anio_ejec = models.CharField(max_length=4, blank=True, null=True, help_text='Año de Aplicación')
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    muni_2802 = models.PositiveSmallIntegerField(blank=True, null=True, help_text='1= si, 0=no')
    muni_3103 = models.PositiveSmallIntegerField(blank=True, null=True, help_text='1= si, 0=no')
    muni_xx = models.PositiveSmallIntegerField(blank=True, null=True, help_text='1= si, 0=no')
    nro_contrib_t = models.FloatField(blank=True, null=True, help_text='Nro de contribuyentes registrados t')
    nro_contrib_t_1 = models.FloatField(blank=True, null=True, help_text='Nro de contribuyentes registrados t-1')
    nro_ord_x_amnistia = models.FloatField(blank=True, null=True, help_text='Nro ordenanzas de amnistía')
    nro_pred_inafecto = models.FloatField(blank=True, null=True, help_text='Nro de predios inafectos por distrito')
    base_imponible_exento = models.FloatField(
        blank=True, null=True,
        help_text='Base imponible exenta (monto de IP exento). Se encuentra en reporte de '
                  'resumen de predio por tributo en el campo deducción'
    )
    nro_pred_am = models.FloatField(blank=True, null=True, help_text='Nro de predios con deducción por adulto mayor')
    monto_ip_am = models.FloatField(blank=True, null=True, help_text='Monto de IP con deducción por adulto mayor')
    fecha_data = models.CharField(
        max_length=10, blank=True, null=True,
        help_text='Fecha de generación de información a exporta AAAAMMDD (AAAA= año, MM=mes, DD=día)'
    )

    class Meta:
        db_table = 'RT_VAREM_MUNI'
