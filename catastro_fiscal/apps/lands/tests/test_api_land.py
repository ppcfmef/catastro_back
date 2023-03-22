from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.tests.api_auth_test_mixin import APIAuthTestMixin
from ..models import LandOwner, Land


class ApiLandTest(APIAuthTestMixin, APITestCase):
    """
    Unit tests to validate api land
    """
    fixtures = ["master.json", 'test/land_test.json']

    def setUp(self):
        """
        User Data for test
        """

        self.auth()

    def test_land_records(self):
        """
        test api lands validate not return list of owners
        """
        api_url = reverse('api:api_lands:lands_records-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        lands = Land.objects.all()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'], lands.count())

    def test_land_records_with_cartographic(self):
        """
        test api lands validate not return list of owners
        """
        api_url = reverse('api:api_lands:lands_records-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(f'{api_url}?status=1', format='json')
        response_data = response.json()
        lands = Land.objects.filter(status=1)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'], lands.count())

    def test_land_records_without_cartographic(self):
        """
        test api lands validate not return list of owners
        """
        api_url = reverse('api:api_lands:lands_records-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(f'{api_url}?status=0', format='json')
        response_data = response.json()
        lands = Land.objects.filter(status=0)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'], lands.count())

    def test_land_register(self):
        """
        test api lands validate not return list of owners
        """
        owner = LandOwner.objects.first()
        api_url = reverse('api:api_lands:lands_register-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {
            "idObjectImg": 16401,
            "idCartographicImg": "i1714020435",
            "status": 2,
            "ubigeo": "140204",
            "uuType": "32",
            "habilitacionName": "Mesones muro demo",
            "codStreet": "01",
            "streetType": "02",
            "streetName": "Calle Prueba prueba ",
            "urbanMza": "10",
            "urbanLotNumber": "11",
            "block": "1",
            "indoor": "1",
            "municipalNumber": "150",
            "resolutionDocument": "00001",
            "resolutionType": "1",
            "latitude": -6.643603777904877,
            "longitude": -79.74115407317974,
            "owner": owner.pk
        }
        response = self.client.post(api_url, data=data, format='json')
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Land.objects.filter(id=response_data['id']).exists(), True)

        owner_update = LandOwner.objects.get(pk=owner.pk)
        self.assertEquals(response_data['status'], 2)
        # Update LandOwner.number_lands
        self.assertEquals(owner_update.number_lands, Land.objects.filter(owner=owner_update).count())

    def test_land_update(self):
        """
        test api lands validate not return list of owners
        """
        land = Land.objects.first()
        api_url = reverse('api:api_lands:lands_register-detail', args=(str(land.pk), ))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {
            "status": 1,
            "streetName": "Calle Prueba prueba 2",
            "latitude": -6.6436037779048766,
            "longitude": -79.74115407317977
        }
        response = self.client.patch(api_url, data=data, format='json')
        land_update = Land.objects.get(pk=land.pk)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(land_update.status, data['status'])
        self.assertEquals(land_update.street_name, data['streetName'])
        self.assertEquals(land_update.latitude, data['latitude'])
        self.assertEquals(land_update.longitude, data['longitude'])
