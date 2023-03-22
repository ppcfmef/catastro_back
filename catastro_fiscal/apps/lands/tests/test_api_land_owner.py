from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.tests.api_auth_test_mixin import APIAuthTestMixin
from ..models import LandOwner, Land


class ApiLandOwnerTest(APIAuthTestMixin, APITestCase):
    """
    Unit tests to validate api landOwner
    """
    fixtures = ["master.json", 'test/land_test.json']

    def setUp(self):
        """
        User Data for test
        """

        self.auth()

    def test_landowner_records(self):
        """
        test api land owner validate not return list of owners
        """
        api_url = reverse('api:api_lands:owners_records-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        owners = LandOwner.objects.all()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'], owners.count())

    def test_landowner_detail(self):
        """
        test api land owner validate not return detail by owner id
        """
        owner = LandOwner.objects.first()
        api_url = reverse('api:api_lands:owners-detail', args=(str(owner.pk), ))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['id'], owner.pk)

    def test_landowner_search(self):
        """
        test api search land owner validate return land owner
        """
        owner = LandOwner.objects.filter(dni__isnull=False).first()
        api_url = reverse('api:api_lands:owners_search-detail', args=(owner.dni,))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['id'], owner.pk)

    def test_landowner_search_not_owner(self):
        """
        test api search land owner validate not return if owner not exists
        """
        api_url = reverse('api:api_lands:owners_search-detail', args=('xxxxxx',))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_landowner_lands(self):
        """
        test api get land by owner validate return listo of land by owner id in query parameter
        """
        owner = LandOwner.objects.filter(number_lands__gt=0).first()
        api_url = reverse('api:api_lands:lands_records-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(f'{api_url}?owner={owner.pk}', format='json')
        response_data = response.json()
        lands_by_owner = Land.objects.filter(owner=owner)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'], lands_by_owner.count())

    def test_landowner_register(self):
        """
        test api land owner register validate create new record
        """
        api_url = reverse('api:api_lands:owners_register-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {
            "documentType": "01",
            "dni": "1B345679",
            "name": "Jose ",
            "paternalSurname": "Ramirez",
            "maternalSurname": "Tello",
            "descriptionOwner": None,
            "phone": "926326525",
            "email": "jcramireztello@gmail.com",
            "address": {}
        }
        response = self.client.post(api_url, data=data, format='json')
        response_data = response.json()
        owner = LandOwner.objects.get(pk=response_data['id'])
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response_data['id'], owner.pk)

    def test_landowner_update(self):
        """
        test api land owner update validate update fields
        """
        owner = LandOwner.objects.first()
        api_url = reverse('api:api_lands:owners_register-detail', args=(str(owner.pk), ))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {
            "name": "Juan"
        }
        response = self.client.patch(api_url, data=data, format='json')
        response_data = response.json()
        owner_update = LandOwner.objects.get(pk=owner.pk)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['name'], owner_update.name)

    def test_landowner_not_update_fields(self):
        """
        test api land owner update validate not change document and documentType
        """
        owner = LandOwner.objects.first()
        api_url = reverse('api:api_lands:owners_register-detail', args=(str(owner.pk), ))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {
            "documentType": "00",
            "dni": "123456"
        }
        response = self.client.patch(api_url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
