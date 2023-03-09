from ..models import User


class UserSetUpTestData:
    NATIONAL_SCOPE = 1
    DEPARTMENT_SCOPE = 2
    PROVINCE_SCOPE = 3
    DISTRICT_SCOPE = 4

    @staticmethod
    def mock():
        User.objects.create_user(
            dni='99999001',
            username='99999001',
            password='prueba',
            first_name='Usuario',
            last_name='Nacional',
        )

        User.objects.create_user(
            dni='99999002',
            username='99999002',
            password='prueba',
            first_name='Usuario',
            last_name='Departamental',
            department_id='15',
        )

        User.objects.create_user(
            dni='99999003',
            username='99999003',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501'
        )

        User.objects.create_user(
            dni='99999004',
            username='99999004',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501',
            district_id='150101'
        )
