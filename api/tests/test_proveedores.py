import unittest
from django.core.exceptions import ValidationError
from api.proveedores.models import Proveedor

class ProveedorTestCase(unittest.TestCase):

    def setUp(self):
        self.proveedor_data = {
            'tipo_persona': 'natural',
            'nombre_empresa': 'Empresa XYZ',
            'nit': '1234567890',
            'nombre': 'Juan Pérez',
            'direccion': 'Calle Falsa 123',
            'correo_electronico': 'juan@example.com',
            'celular': '+12345678901',
            'estado': 'activo',
        }

    def test_crear_proveedor(self):
        proveedor = Proveedor(**self.proveedor_data)
        self.assertEqual(proveedor.nombre_empresa, 'Empresa XYZ')
        self.assertEqual(proveedor.tipo_persona, 'natural')

    def test_str_proveedor(self):
        proveedor = Proveedor(**self.proveedor_data)
        self.assertEqual(str(proveedor), 'Empresa XYZ (1234567890)')

    def test_celular_valido(self):
        proveedor = Proveedor(**self.proveedor_data)
        try:
            proveedor.full_clean()  # Ejecuta validaciones incluyendo el celular
        except ValidationError:
            self.fail('ValidationError inesperado para celular válido')

    def test_celular_invalido(self):
        self.proveedor_data['celular'] = '12345'  # formato inválido
        proveedor = Proveedor(**self.proveedor_data)
        with self.assertRaises(ValidationError):
            proveedor.full_clean()

if __name__ == '__main__':
    unittest.main()
