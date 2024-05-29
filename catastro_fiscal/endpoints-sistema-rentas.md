
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
*3 => codigo de predio municipal(cpm)
*4 => fecha de registro del predio
**/
{ 
"ubigeo":"040501", 
"codigoContribuyente":"100000", 
"codigoPredioMunicipal":"30151040",
"fechaRegistro":"2024-01-01"
}
```

 

###### response:
```json
{
   "success"  : true,
   "message" : "Registro guardado"
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

[POST] <hostname>/api/v1/lands/external/crear-contribuyente/

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

#### request:
###### body: 

```json

{
"ubigeo":"040501", 
"contribuyenteNumero":"100000009", 
"docIdentidadId":1, 
"numDocIdentidad":"45257502", 
"nombres":"frank2", 
"apePaterno":"soto", 
"apeMaterno":"peña", 
"domicilios":[
{
"ubigeo":"040501",
"desDomicilio":"ejemplo 1",
"latitud":0,
"longitud":0,
"referencia":"ejemplo referencia",
"piso":"2",
"manzana":"E",
"lote": "4",
"kilometro":"3",

}

], 
"contactos":[
    {
        "descripcion":"999999",
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
{
   "success" : true,
   "message" : "Contribuyente creado",
  
}
```



###### response:
```json
{
   "success" : false,
   "message" : "Contribuyente ya existe",
  
}
```