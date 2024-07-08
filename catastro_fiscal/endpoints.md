
# Endpoints

#### URL
https://antmna-bluetrace-api-dev.mybluemix.net/

[POST]  <hostname>/api/employees/register

#### request:
###### body: 

```json
/**
*Values of document_type
*1 => DNI
*2 => Carnet de extranjeria
*3 => Pasaporte
**/
{
   "document_number" : "75402332",
   "document_type": 1,
   "phone" : "941923262"    
}
```

 

###### response:
```json
{
   "success"  : true,
   "message" : "all is ok"
}
``` 

```json
{
   "success" : false,
   "message" : "all is bad",
   "errors" : [
        {
            "msg": "the dni is required",
            "param": "dni",
            "location": "body"
        }
   ]
}
```

 
---

[POST] <hostname>/api/employees/confirm

 

#### request:
###### body: 

```json
{
   "code_otp" : "904756",  
   "phone": "992811214",
   "device_id":"b7e0ed91990582de"
}
```


###### response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF9hbm9ueW1vdXMiOiIxMjE3YzY1MC1hYTAyLTQ5ZGEtOWMzMC01ZWY4MTEyMjY1NWQiLCJpYXQiOjE1OTI1OTcxNjgsImV4cCI6MTU5MjYyMzE2OH0.gwzEJN7d7pQq_923frPZYWnmwsZ1NxSDtm1BV7h8jP0",
    "refresh_token": "5aEIrDaqxgLZsf2zTfRD5UX0hPUCatGI54G8tW8oll2TbD0ecAmf2Mdz5F5WYVG5",
    "expires_token": 1593391885059,
    "message": "Codigo valido.",
   "data" : {
     "employee" : {
         "id_anonymous" : "aec237b5-470a-43ee-a924-557fe7a8e156"
     }
   }
}
```
 

```json
{
   "success" : false,
   "message" : "all is bad",
   "errors" : [{
            "msg": "the code_otp is required",
            "param": "code_otp",
            "location": "body"
        }]
}
```
---
[POST] <hostname>/api/employees/token
#### request:
###### body: 

```json
{
   "refresh_token": "28CEN4EwKOTwx8vTkeNw2NSAynU0QS4EATWmgrP9kFXJ6qniOtMnwY72JTtWcTLY",
   "device_id":"b7e0ed91990582dv2",
   "id_anonymous": "1217c650-aa02-49da-9c30-5ef81122655d"
}
```
#### response:
```json
{
    "success": true,
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF9hbm9ueW1vdXMiOiIxMjE3YzY1MC1hYTAyLTQ5ZGEtOWMzMC01ZWY4MTEyMjY1NWQiLCJpYXQiOjE1OTI1OTMyNjYsImV4cCI6MTU5MjYxOTI2Nn0.VYPNu12m_FN0YHdU_uQ9hmZTtIHOX3f3sRhRQ6AHhXU",
    "refresh_token": "GCaufqU1DRzRJhv17YvUxkNtK4JAl5X1PN9UDXBc3P6XOLLQytIaUbUCrddKvVZo",
    "expires_token": 1593391885059,
    "message": "Codigo valido."
}
```
```json
{
    "success": false,
    "message": "token invalido."
}
```

---

[POST] <hostname>/api/tracking/register

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 
```json
{
    "data": [{
            "id_1": "492e138b-181f-4a54-a83c-c4efaa7a81fb",
            "lat_1": -12.110925,
            "lon_1": -77.0268348,
            "model_1": "SM-A307G|-52.84",
            "id_2": "5188d795-6d65-4b92-819e-33c298a73806",
            "model_2": "SM-A307G",
            "ble": -57,
            "role": 0,
            "so": 0,
            "ts": "2020-05-26 17:57:58.163",
            "not_shown": true,
            "ble_fixed": 23.565658,
            "ble_threshold": 23,
            "travel_mode" : false
        },
        {
            "id_1": "492e138b-181f-4a54-a83c-c4efaa7a81fb",
            "lat_1": -12.110925,
            "lon_1": -77.0268348,
            "model_1": "SM-A307G|-52.84",
            "id_2": "5188d795-6d65-4b92-819e-33c298a73806",
            "model_2": "SM-A307G",
            "ble": -57,
            "role": 0,
            "so": 0,
            "ts": "2020-05-26 17:57:58.163",
            "not_shown": true,
            "ble_fixed": 23.565658,
            "ble_threshold": 23,
            "travel_mode" : false
        }
    ]
}
```
 

###### response:

```json
{
    "success": true,
    "message": "Tracking Registered"
}  
```
##### error response: 
```json
{
    "success": false,
    "message": "all is bad",
    "errors": [
        {
            "msg": "Invalid value",
            "param": "data[0].encounter_timestamp",
            "location": "body"
        }
    ]
}
```

```json
{
    "success": false,
    "error":{
        "code":102,
        "message": "Token invalido"
    }
    
}  
```

```json
{
    "success": false,
    "error": {
            "code":107,
            "message": "Token caducado "
            }
}  
```
```json
{
    "success": false,
    "error": {
            "code":101,
            "message": "Falta el token "
            }
}  
```

```json
{
    "success": false,
    "error": {
            "code":104,
            "message": "Sesion terminada"
            }
}  
```

```json
{
    "success": false,
    "error": {
            "code":103,
            "message": "Token expirado"
            }
}  
```

---
[POST] <hostname>/api/encuesta/nueva_encuesta

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 
```json
{
	"id_anonymous": "ee27da69-f877-4661-9b7e-16dcbf015420"
}
```


---

[POST] <hostname>/api/encuesta/fin_encuesta

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 
```json
{
    "id_survey": 225,
    "answers": [
        {
            "id": "answer_1_1_2"
        },
        {
            "id": "answer_1_2_3"
        },
        {
            "id": "answer_1_3_1"
        }
        
    ]
}
```


###### response:
```json
{
   "success" : true,
   "message" : "all is ok"
   }

```

---

[POST] <hostname>/api/employees/end_register

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 



#### response:
```json
{
   "success" : true,
   "message" : "all is ok"
   
}
```


[POST] <hostname>/api/employees/active_state

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 
```json
{
    
    "lat": 1236.2114,
    "lon": 1236.2114
}
```


#### response:
```json
{
   "success" : true,
   "message" : "all is ok"
   }
}
```



[POST] <hostname>/api/employees/update-device-token-fcm

#### request:
###### headers:
    Content-Type: application/json
    Authorization: JWT [token]
###### body: 
```json
{
    "device_token_fcm":"4444"
}
```
 

###### response:

```json
{
    "success": true,
    "message": "all is ok"
}  
```