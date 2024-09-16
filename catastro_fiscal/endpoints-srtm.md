
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
{
  "predios": [
    {
      "ubigeoPredio": "220901",
      "municipalidadId": 301759,
      "contribuyenteNumero": 263,
      "codigoPredioUnico": "78070817-0001-6",
      "predioCodigo": 1,
      "areaTerreno": 279,
      "areaTotTerrComun": 0,
      "areaConstruida": 0,
      "areaTotConsComun": 0,
      "porPropiedad": 100,
      "tipTransferenciaId": null,
      "tipUsoPredioId": 299,
      "tipPropiedadId": 1,
      "fechaAdquisicion": "2024-08-27",
      "fecTransferencia": null,
      "cantidadHabitantes": 1,
      "preInhabitable": 0,
      "parRegistral": "P09089068",
      "predialNumero": 1,
      "numeroDj": "1609",
      "fechaDj": "2024-08-02",
      "usuarioAuditoria": "USU",
      "estadoDjId": 1,
      "motivoDjId": 1,
      "anioDeterminacion": 2024,
      "longitudFrente": 12.15,
      "nivelesConstruccion":[
          {
            "tipNivelId": 1,
            "numPiso": 1,
            "tipMaterialId": 1,
            "estConservacionId": 1,
            "anioConstruccion": 2024,
            "mesConstruccion": 1,
            "areaConstruida": 100,
            "areaConstruidaComun": 10,
            "porAreaConstruidaComun": 10,
            "categoriaMuroColumna": "A",
            "categoriaBano": "A",
            "categoriaPuertaVentana": "A",
            "categoriaRevestimiento": "A",
            "categoriaInstElectricaSanita": "A",
            "categoriaTecho":"A",
            "categoriaPiso":"A"
        
        },
        {
            "tipNivelId": 1,
            "numPiso": 2,
            "tipMaterialId": 1,
            "estConservacionId": 1,
            "anioConstruccion": 2024,
            "mesConstruccion": 1,
            "areaConstruida": 100,
            "areaConstruidaComun": 10,
            "porAreaConstruidaComun": 10,
            "categoriaMuroColumna": "B",
            "categoriaBano": "A",
            "categoriaPuertaVentana": "B",
            "categoriaRevestimiento": "B",
            "categoriaInstElectricaSanita": "B",
            "categoriaTecho":"B",
            "categoriaPiso":"B"
        }
      ],
      "obrasComplementarias":[
        {
            "numPiso": 1,
            "tipObraComplementariaId":3,
            "tipMaterialId": 2,
            "estConservacionId": 1,
            "anioConstruccion": 2024,
            "mesConstruccion": 1,
            "categoria": "1",
            "cantidad":1,
            "metroRedondeado":50.0,
            "totalMetrado":50.0
        }]
      
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
   "success"  : true,
   "mensaje" : "Registro guardado"
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
   "mensaje" : "Contribuyente creado",
  
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