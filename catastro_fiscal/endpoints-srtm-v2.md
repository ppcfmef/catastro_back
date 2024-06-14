
# Endpoints

#### URL
https://vmd120205.contaboserver.net

[POST]  <hostname>/api/v1/lands/external/guardar-predio-contribuyente

#### request:
###### body: 
/**

*1 => ubigeo
*2 => codigo de contribuyente
*3 => codigo de predio municipal(cpu)
*4 => area del terreno
*5 => area total del terreno comun
*6 => area construida
*7 => area total construida comun
*8 => porcentaje de propiedad
*9 => tipo de Uso del Predio
*10 => tipo de Propiedad
*11 => fecha de transferencia
*12 => longitud de Frente
*13 => cantidad de habitantes
*14 => predio inhabitable(0 falso, 1  verdadero)
*14 => partida registral
*15 => numero de declaracion jurada
*16 => fecha de declaracion jurada
*17 => usuario de creacion
*18 => estado
**/
```json

{ 
"ubigeo":"040501", 
"codigoContribuyente":"100000011", 
"codigoPredioUnico":"30151040-0001-9",
"area_terreno":100.00,
"areaTotTerrComun": 50.00,
"areaConstruida": 50.00,
"areaTotConsComun": 50.00,
"porPropiedad": 50.00,
"tipTransferencia": 1,
"tipUsoPredio": 1,
"tipPropiedad": 1,
"fec_transferencia": "2024-06-14",
"longitudFrente": 100.00,
"cantidad_habitantes": 10,
"preInhabitable": 0,
"parRegistral": "2000-59-6",
"numero_dj": "200000",
"fecha_dj": "2024-06-14",
"usuarioCreacion": "TEST",
"estado": 1
}
```

 

###### response:
/**
status 201
**/
```json
{
   "success"  : true,
   "message" : "Registro guardado"
}
``` 

##### response:
/**
status 400
**/
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

[POST] <hostname>/api/v1/lands/external/crear-contribuyente

 

#### request:

###### body: 

/**

*1 => ubigeo
*2 => codigo de contribuyente
*3 => tipo de documento
*4 => numero de documento(dni o ruc)
*5 => nombre 
*6 => apellido paterno 
*7 => apellido materno
*8 => domicilios
*9 => contactos


domicilios=>array 
   *1 => ubigeo del domicilio 
   *2 => decripcion de domicilio
   *3 => latitud
   *4 => longitud
   *5  => referencia adicional
   *6  => piso
   *7  => manzana
   *8  => lote
   *9  => kilometro


contactos=>array 
   *1 => descripcion 
   *2 => es principal (1 si es principal , 0 si no lo es)
   *3 => tipo de medio de contacto
**/
```json
{
"ubigeo":"040501", 
"codigoContribuyente":"100000011", 
"docIdentidadId":1, 
"numDocIdentidad":"45257503", 
"nombres":"frank", 
"apePaterno":"soto", 
"apeMaterno":"peña", 
"domicilios":[
{
"ubigeo":"040501",
"desDomicilio":"ejemplo 1",
"latitud":0,
"longitud":0,
"referencia":"ejemplo referencia"
}

], 
"contactos":[
    {
        "descripcion":"965193248",
        "principal":1,
        "tipoMedContacto":2
    },
       {
        "descripcion":"frank@gmail.com",
        "principal":0,
        "tipoMedContacto":3
    }

]
}
```




###### response:
/**
status 201
**/
```json
{
   "success" : true,
   "message" : "Contribuyente creado",
  
}
```



###### response:
/**
status 400
**/
```json
{
   "success" : false,
   "message" : "Contribuyente ya existe",
  
}
```





---

[POST] <hostname>/api/v1/lands/external/guardar-nivel-construccion



#### request:

###### body: 


```json

{ 
"ubigeo":"040501", 
"codigoContribuyente":"100000011", 
"codigoPredioUnico":"30151040-0001-9",
"tipNivel": 1,
"num_piso":2, 
"tipMaterial":1,
"estConservacion":1, 
"anioConstruccion":2024, 
"mesConstruccion":5 ,
"areaConstruida":100.00 ,
"areaConstruidaComun":5.0 ,
"porAreaConstruidaComun":100, 
"categoriaMuroColumna":"A" ,
"categoriaPuertaVentana":"B", 
"categoriaRevestimiento":"A", 
"categoriaBano":"A",
"categoriaInstElectricaSanita ":"A",
"estado":1 
           
}
```


###### response:
/**
status 201
**/
```json
{
   "success" : true,
   "message" : "Registro guardado",
  
}
```



###### response:
/**
status 400
**/
```json
{
    "message": "Ya existe este nivel para el predio"
}
```

---

[POST] <hostname>/api/v1/lands/external/guardar-deuda-contribuyente

#### request:

###### body: 
```json
{ 
"ubigeo":"040501", 
"codigoContribuyente":"100000011", 
"tieneDeuda":1,
"anio":2024
}

```


###### response:
/**
status 201
**/
```json
{
   "success" : true,
   "message" : "Registro guardado",
  
}
```



###### response:
/**
status 400
**/
```json
{
    "message": "Ya existe esta deuda para este contribuyente y con este año"
}
```