
# Endpoints

#### URL
https://vmd120205.contaboserver.net

[POST]  <hostname>/api/v1/lands/external/guardar-predio-contribuyente

#### request:

###### headers:
    Content-Type: application/json
    Authorization: Bearer Token [token]



###### body: 

```json
/**

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

 ###### headers:
    Content-Type: application/json
    Authorization: Bearer Token [token]


#### request:

###### body: 


```json


{
    "contribuyente": {
    "municipalidadId": 301807,
    "contribuyenteNumero": "1166",
    "ubigeoRegistro": "240104",
    "tipContribuyenteId": 1,
    "docIdentidadId": 1,
    "numDocIdentidad": "40393939",
    "nombres": "EDITH ROXANA",
    "apePaterno": "AQUINO",
    "apeMaterno": "HUAYTA",
    "razonSocial": null
  },
  "domicilios": [
    {
      "tipDomicilioId": 1,
      "ubigeoDomicilio": "240104",
      "desDomicilio": "N° 123, AGRUPACION 123, TUMBES-TUMBES-PAMPAS DE HOSPITAL ",
      "latitud": -3.6953866,
      "longitud": -80.4368245,
      "referencia": null
    }
  ],
  "contactos": [
  
    {
      "tipMedContactoId": 3,
      "descripcion": "CORREG@GMAIL.COM",
      "principal": 1
    }    
  ]
}

```




###### response:

```json
/**
status 201s
**/
{
   "success" : true,
   "message" : "Contribuyente creado",
  
}
```



---

[POST] <hostname>/external/iniciar-sesion

 

#### request:

###### body: 


```json

{
   "username" : "usuario",
   "password" : "password",
  
}
```

###### response:

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxODcsInVzZXJuYW1lIjoiU1JUTSIsImV4cCI6MTcyMDYxOTgzMCwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTcyMDQ0NzAzMH0.z7zz3JNo4YX_2ygMDIceSTqNs0OJ7FGzSmpugdA87qM"

}
```