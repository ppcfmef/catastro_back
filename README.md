## API Catastro Fiscal

API rest para el proyecto MEF Catastro Fiscal

### Requerimientos
* Python 3.9
* Django <4
* Pipenv

#### Instalar requerimientos
```
pipenv install
pipenv install --dev
```

#### Configuracion
`
Nota: Cambiar <django_project> por catastro_fiscal en cada paso de este documento
`

* Crear el archivo .env y configurarlo de acuerdo al ambiente
```
cd <django_project>/
cp -a .env.example .env
```

* Crear el archivo de configuracion de django segun ambiente de despliegue
```
cd <django_project>/settings/
cp -a local_settings.py.example local.py
```

* Generar **_SECRET_KEY_** desde la consola de django y remplazar en .env
```
python manage.py shell --settings=<django_project>.settings.local
```

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

#### Iniciar proyecto

* Ejecutar servidor de prueba
```
python manage.py runserver --settings=<django_project>.settings.local
```
### Fixture
* Generar Fixture para datos maestros
```
python manage.py dumpdata common master_data places -o fixtures/master.json --settings=<django_project>.settings.local
```

### Test
* Cumplimiento de la guía de estilo de python
```
pipenv run flake8 .
```
* Generar fixture para test
```
pipenv run python manage.py \
dumpdata --natural-primary --natural-foreign -e contenttypes -e auth.permission -e admin.logentry -e sessions.session \
-e admin_interface -e colorfield -e rest_captcha --indent 4 -o fixtures/test/db_test.json \
--settings=<django_project>.settings.local
```
* Ejecutar test
```
pipenv run python manage.py test <apps.name> --settings=<django_project>.settings.local
```
Remplazar `<apps.name>`  por nombre de aplicacion ejemplo la aplicaicon de usuarios `apps.users`

* Ejecutar coverage
```
pipenv run coverage run --source='.' manage.py test <apps.name> --settings=catastro_fiscal.settings.local
```
Remplazar `<apps.name>`  por nombre de aplicacion ejemplo la aplicaicon de usuarios `apps.users`

* Ver Reporte en consola
```
pipenv run coverage report
```

* Generar Reporte HTML
```
pipenv run coverage html
```
Abrir la carpeta `htmlcov` y ver el archivo `index.html` en el navegador

### Docker
para facilitar el uso y facilitar cualquier problema de dependencias se implementa el archivo docker/Dockerfile

#### Generar la imagen Docker (build)
```
sudo docker build -t catastro_fiscal -f docker/Dockerfile .
```

#### Ejecutar runserver con Docker
Este comando ejecutara el comando runserver e iniciara el proyecto en el puerto 8000
```
sudo docker run -p 8000:8000 catastro_fiscal python manage.py runserver 0.0.0.0:8000
```

#### Ejecutar usando docker-compose
```
sudo docker-compose -f docker/docker-compose.yml up -d
```