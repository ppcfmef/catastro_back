
# Endpoints

#### URL
https://vmd120205.contaboserver.net

[POST]  <hostname>/api/v1/valorization/offer/photo/guardar-fotos/

#### request:
###### body: 

```json
/**

*1 => codigo de ubicacion
*2 => codigo de foto
*3 => codigo de tipo de foto(1,2,3,4,5,6) 
*3 => url_foto
**/
[
{
    "cod_ubicacion":"1",
    "cod_foto":"2",
    "cod_tipo_foto":"1",
    "url_foto": "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAANHUlEQVR4nOzXDc/W9X3GYe96O6lD0LoabZvOWRl2xqLV6qaVWvABHyhKdEzJJlgT7Trxoa7D1ZKipeBs3WzVdZvGampba1GGgFJhbsjaYhwGO2CQQnGUYeltBSZ1ZSJ7FWey5DyOF3D+kn"

}

]
```

 

###### response:
```json
{
    "status": "success",
    "message": "Los registros se guardaron correctamente"
}
``` 


```json
{
   "success" : "error",
   "message" : "error",
  
}
```


[GET]  <hostname>/api/v1/valorization/offer/photo/

#### request:

#### query params:
?cod_ubicacion=1
?cod_foto=1

###### response:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "codFoto": "1",
            "descTipoFoto": "Frontis",
            "codUbicacion": "1",
            "urlFoto": "http://127.0.0.1:8000/media/valorization/predio.png",
            "codTipoFoto": "1"
        },
        {
            "codFoto": "2",
            "descTipoFoto": "Frontis",
            "codUbicacion": "1",
            "urlFoto": "http://127.0.0.1:8000/media/valorization/1_2.jpg",
            "codTipoFoto": "1"
        }
    ]
}
``` 


