from django.db import models


class Contribuyente(models.Model):
    """Renta Contribuyente"""
    ubigeo = models.CharField(max_length=6, blank=True, null=True, help_text='Ubigeo de la municipalidad')
    sec_ejec = models.CharField(max_length=6, blank=True, null=True, help_text='Secuencia de ejecutora')
    cod_contr = models.CharField(max_length=50, blank=True, null=True, help_text='Código de contribuyente')
    fecha_inscripcion = models.CharField(max_length=10, blank=True, null=True, help_text='Fecha de inscripción')
    tipo_doc = models.CharField(max_length=10, blank=True, null=True, help_text='Código del tipo de documento')
    documento_desc = models.CharField(max_length=30, blank=True, null=True, help_text='Descripción tipo de documento')
    num_doc = models.CharField(max_length=20, blank=True, null=True, help_text='Número de documento')
    apellido_paterno = models.CharField(max_length=90, blank=True, null=True, help_text='Apellido paterno')
    apellido_materno = models.CharField(max_length=90, blank=True, null=True, help_text='Apellido materno')
    nombre = models.CharField(max_length=90, blank=True, null=True, help_text='Nombre')
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
