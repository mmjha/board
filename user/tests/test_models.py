from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # class 내에서 초기에 한번 실행
        User.objects.create( 
           username='test_user',
           email='test@test.com',
           password='test123')

    def setUp(self):
        # 테스트 메소드 마다 실행
        print('TEST!!')
        pass

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 150)
        