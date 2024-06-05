
# Endpoints

#### URL
https://vmd120205.contaboserver.net

[POST]  <hostname>/api/v1/lands/external/guardar-caracteristicas

#### request:
###### body: 

```json
/**

*idPredio => identificador del Predio
*idContribuyente => identificador del Contribuyente
*ubigeo => Ubicación Geográfica
*tipUsoPredioId => Tipo de Uso de Predio
*tipPropiedadId => Tipo de Propiedad
*areaTerreno => Area del Terreno
*areaTotTerrComun => Area total del Terreno comun
*areaConstruida => Area construida
*areaTotConsComun => Area total de construccion comun
*porPropiedad => Porcentaje de propiedad
*tipTransferenciaId => Identificador de tipo de Transferencia
*fecTransferencia => fecha de Transferencia
*longitudFrente => longitud del frente
*cantidadHabitantes => cantidad de habitantes
*preInhabitable => indicador de si la propiedad es habitable
*parRegistral => Partidad registral
*activo => estado del registro
**/
{
   
   "idPredio":1,
   "idContribuyente":2,
   "ubigeo":"010101",
   "tipUsoPredioId": 1,
   "tipPropiedadId": 1,
   "areaTerreno": 200.0,
   "areaTotTerrComun":100.0,
   "areaConstruida":100.0,
   "areaTotConsComun":50.0,
   "porPropiedad":25.0,
   "tipTransferenciaId":1,
   "fecTransferencia":"2024-01-01",
   "longitudFrente":12.0,
   "cantidadHabitantes":10,
   "preInhabitable":0,
   "parRegistral":"10452555",
   "activo":1
}
```

 

###### response:
```json
{
   "success"  : true,
   "message" : "Registro guardado",
   "id":1
}
``` 


```json
{
   "success" : false,
   "message" : "Contribuyente no existe",
  
}
```

```json
{
   "success" : false,
   "message" : "Distrito no existe",
  
}
```

```json
{
   "success" : false,
   "message" : "Predio no existe",
  
}
```




---

[POST] <hostname>/api/v1/lands/external/guardar-niv-construccion


#### request:
###### body: 

```json
/**

*ubigeo => Ubicación Geográfica
*idCaracteristica => identificador de caracteristicas
*tipNivelId => Tipo de nivel
*numPiso => Numero de piso
*tipMaterialId => Tipo de Material
*estConservacionId => Identificador de estado de conservación
*anioConstruccion => Año de construccion
*mesConstruccion => Mes de construccion
*areaConstruccion => Area de construccion
*areaConsComun => Area  de construccion comun
*porAreaConsComun => Porcentaje de area de Construccion Comun
*murosColumnas => Clasificacion de muros y columnas
*techos => clasificacion de material de techo
*piso => clasificacion de material de piso
*puertasVentanas => Clasificacion de material de puertas y ventanas
*revestimientos => Clasificacion de material de revestimientos
*banos =>  Clasificacion de material de baños
*insElectricaSanita => Clasificación de instalación eléctrica y sanitaria
*activo => estado del registro
**/

[
{
    "ubigeo":"040501",
    "idCaracteristica":1,
    "tipNivelId":1,
    "numPiso":2,
    "tipMaterialId":1,
    "estConservacionId":2,
    "anioConstruccion":2024,
    "mesConstruccion":1,
    "areaConstruccion":200.0,
    "areaConsComun":100.0,
    "porAreaConsComun":50.0,
    "murosColumnas":"2",
    "techos":"2",
    "piso":"2",
    "puertasVentanas":"5",
    "revestimientos":"5",
    "banos":"5",
    "insElectricaSanita":"5",
    "activo":1,
}]
```


###### response:
```json
{
   "success" : true,
   "message" : "Niveles registrados",
  
}
```

```json
{
   "success" : false,
   "message" : "Registro de Caracteristica no existe",
  
}
{
   "success" : false,
   "message" : "El distrito no existe ",
  
}

```