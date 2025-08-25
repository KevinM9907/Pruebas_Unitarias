import unittest
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from api.clientes.models import Cliente
from api.roles.models import Rol
from api.usuarios.models import Usuario

class ClienteTestCase(unittest.TestCase):

    def setUp(self):
        self.cliente_data = {
            'tipo_documento': 'CC',
            'documento': '1234567890',
            'nombre': 'Ana Gómez',
            'celular': '+12345678901',
            'correo_electronico': 'ana@example.com',
            'direccion': 'Av Siempre Viva 742',
            'genero': 'F',
            'estado': True,
        }

    def test_crear_cliente(self):
        cliente = Cliente(**self.cliente_data)
        self.assertEqual(cliente.nombre, 'Ana Gómez')
        self.assertEqual(cliente.tipo_documento, 'CC')

    def test_str_cliente(self):
        cliente = Cliente(**self.cliente_data)
        self.assertEqual(str(cliente), 'Ana Gómez (1234567890)')

    def test_celular_valido(self):
        cliente = Cliente(**self.cliente_data)
        try:
            cliente.full_clean()
        except ValidationError:
            self.fail('ValidationError inesperado para celular válido')

    def test_celular_invalido(self):
        self.cliente_data['celular'] = '12345'
        cliente = Cliente(**self.cliente_data)
        with self.assertRaises(ValidationError):
            cliente.full_clean()

    def test_generar_verificar_contrasena_temporal(self):
        cliente = Cliente(**self.cliente_data)
        contra = cliente.generar_contraseña_temporal()
        self.assertTrue(cliente.verificar_contraseña_temporal(contra))
        self.assertTrue(cliente.debe_cambiar_contraseña)

    def test_cambiar_contrasena_actualiza_flag(self):
        cliente = Cliente(**self.cliente_data)
        cliente.generar_contraseña_temporal()
        cliente.cambiar_contraseña('nuevaContra123')
        self.assertFalse(cliente.debe_cambiar_contraseña)

if __name__ == '__main__':
    unittest.main()
