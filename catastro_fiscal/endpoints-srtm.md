
# Endpoints

#### URL
https://vmd120205.contaboserver.net

[POST]  <hostname>/api/v1/lands/external/guardar-predio-contribuyente

#### request:
###### body: 

```json
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
[{ 
"ubigeoPredio":"100105", 
"municipalidadId":1,
"contribuyenteNumero":"1000000002", 
"codigoPredioUnico":"43465339-0001-1",
"areaTerreno":100.00,
"areaTotTerrComun": 50.00,
"areaConstruida": 50.00,
"areaTotConsComun": 50.00,
"porPropiedad": 50.00,
"tipTransferenciaId": 1,
"tipUsoPredioId": 1,
"tipPropiedadId": 1,
"fecTransferencia": "2024-06-14",
"longitudFrente": 100.00,
"cantidad_habitantes": 10,
"preInhabitable": 0,
"parRegistral": "2000-59-6",
"numeroDj": "200000",
"fechaDj": "2024-06-14",
"usuarioAuditoria": "TEST",
"estadoDjId": 1,
"motivoDjId": 1
           
}]
```

 

###### response:

```json
/**
status 201
**/
{
   "success"  : true,
   "message" : "Registro guardado"
}
``` 





---

[POST] <hostname>/api/v1/lands/external/crear-contribuyente

 

#### request:

###### body: 


```json

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

{
"ubigeoRegistro":"100105", 
"municipalidadId":3,
"contribuyenteNumero":"1000000002", 
"docIdentidadId":1, 
"tipContribuyenteId":1, 
"numDocIdentidad":"45257503", 
"nombres":"frank", 
"apePaterno":"soto", 
"apeMaterno":"peña",
"razonSocial":"", 
"domicilios":[
{
"ubigeoDomicilio":"040501",
"tipoDomicilio":1, 
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

```json
/**
status 201
**/
{
   "success" : true,
   "message" : "Contribuyente creado",
  
}
```

