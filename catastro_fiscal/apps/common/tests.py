from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.tests.api_auth_test_mixin import APIAuthTestMixin
from apps.users.models import User, Role, Permission, PermissionType, PermissionNavigation
from .models import Navigation


class ApiNavigationTest(APIAuthTestMixin, APITestCase):
    """
    Unit tests to validate api auth
    """
    fixtures = ["master.json"]

    def setUp(self):
        """
        Auth setup for test
        """

        pass

    def test_api_navigation_superadmin(self):
        """
        test api navigation method api list `api:api_common:navigation-list` validate api exists and valid navigation
        to superadmin user show all navigation items
        """
        self.auth()

        api_url = reverse('api:api_common:navigation-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        number_navigation_parent = Navigation.objects.filter(parent__isnull=True).count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), number_navigation_parent)

    def test_api_navigation_custom_role(self):
        """
        test api navigation method api list `api:api_common:navigation-list` validate api exists and valid navigation
        custom role. Navigation return home, and custom
        """

        permission = Permission.objects.create(description="Demo Show Only User")
        navigation = Navigation.objects.get(id='gesuser')
        permission_type = PermissionType.objects.create(code='read_all', description='Ver todo', order=3)  # ToDo: add to master
        PermissionNavigation.objects.create(
            permission=permission,
            type=permission_type,
            navigation_view=navigation
        )
        role = Role.objects.create(name='Demo', description="Demo Show Only User")
        role.permissions.add(permission)

        test_user = User.objects.create_user(
            dni='99999000',
            username='99999000',
            password='password',
            first_name='Admin',
            last_name='Nacional',
            is_superuser=False,
            role=role
        )
        self.auth_login(login={'username': '99999000', 'password': 'password'})
        api_url = reverse('api:api_common:navigation-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 2)
