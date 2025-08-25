from django.test import TestCase
from django.contrib.auth import get_user_model
from api.roles.models import Rol

class UsuarioModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear el rol que se requiere para el usuario
        cls.rol = Rol.objects.create(nombre='TestRol', estado='activo')

    def test_crear_usuario(self):
        User = get_user_model()
        user = User.objects.create_user(
            correo_electronico='testuser@example.com',
            password='testpass123',
            nombre='Test User',
            tipo_documento='CC',
            documento='123456789',
            celular='+12345678901',
            rol=self.rol
        )
        self.assertEqual(user.correo_electronico, 'testuser@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_crear_superusuario(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            correo_electronico='admin@example.com',
            password='adminpass123',
            nombre='Admin User',
            tipo_documento='CC',
            documento='987654321',
            celular='+10987654321',
            rol=self.rol
        )
        self.assertEqual(admin_user.correo_electronico, 'admin@example.com')
        self.assertTrue(admin_user.check_password('adminpass123'))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

    def test_generar_y_verificar_contraseña_temporal(self):
        User = get_user_model()
        user = User.objects.create_user(
            correo_electronico='tempuser@example.com',
            password='temp12345',
            nombre='Temp User',
            tipo_documento='CC',
            documento='1122334455',
            celular='+12312312345',
            rol=self.rol
        )
        contra = user.generar_contraseña_temporal()
        self.assertTrue(user.verificar_contraseña_temporal(contra))
        self.assertTrue(user.debe_cambiar_contraseña)

    def test_cambiar_contraseña_actualiza_flag(self):
        User = get_user_model()
        user = User.objects.create_user(
            correo_electronico='changepass@example.com',
            password='oldpassword',
            nombre='Change Password User',
            tipo_documento='CE',
            documento='5544332211',
            celular='+19876543210',
            rol=self.rol
        )
        user.generar_contraseña_temporal()
        user.cambiar_contraseña('newsecurepass123')
        self.assertFalse(user.debe_cambiar_contraseña)
        self.assertTrue(user.check_password('newsecurepass123'))
