import unittest
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from api.manicuristas.models import Manicurista

class ManicuristaTestCase(unittest.TestCase):

    def setUp(self):
        self.manicurista_data = {
            'nombre': 'Lucía Gómez',
            'tipo_documento': 'CC',
            'numero_documento': '1234567890',
            'especialidad': 'Manicure Gel',
            'celular': '+12345678901',
            'correo': 'lucia@example.com',
            'direccion': 'Av Central 123',
            'estado': 'activo',
            'disponible': True,
        }

    def test_crear_manicurista(self):
        manicurista = Manicurista(**self.manicurista_data)
        self.assertEqual(manicurista.nombre, 'Lucía Gómez')
        self.assertEqual(manicurista.tipo_documento, 'CC')
        self.assertEqual(manicurista.especialidad, 'Manicure Gel')

    def test_propiedades_nombres_apellidos(self):
        manicurista = Manicurista(nombre='Ana María Pérez')
        self.assertEqual(manicurista.nombres, 'Ana')
        self.assertEqual(manicurista.apellidos, 'María Pérez')
        manicurista_short = Manicurista(nombre='Sofía')
        self.assertEqual(manicurista_short.nombres, 'Sofía')
        self.assertEqual(manicurista_short.apellidos, '')

    def test_str_manicurista(self):
        manicurista = Manicurista(**self.manicurista_data)
        self.assertEqual(str(manicurista), 'Lucía Gómez - 1234567890 (Manicure Gel)')
        manicurista_no_doc = Manicurista(nombre='Lucía Gómez', especialidad='Manicure Gel')
        self.assertEqual(str(manicurista_no_doc), 'Lucía Gómez (Manicure Gel)')

    def test_celular_valido(self):
        manicurista = Manicurista(**self.manicurista_data)
        try:
            manicurista.full_clean()
        except ValidationError:
            self.fail('ValidationError inesperado para celular válido')

    def test_celular_invalido(self):
        self.manicurista_data['celular'] = '12345'
        manicurista = Manicurista(**self.manicurista_data)
        with self.assertRaises(ValidationError):
            manicurista.full_clean()

    def test_generar_y_verificar_contraseña_temporal(self):
        manicurista = Manicurista(**self.manicurista_data)
        contra = manicurista.generar_contraseña_temporal()
        self.assertTrue(manicurista.verificar_contraseña_temporal(contra))
        self.assertTrue(manicurista.debe_cambiar_contraseña)

    def test_cambiar_contraseña_actualiza_flag(self):
        manicurista = Manicurista(**self.manicurista_data)
        manicurista.generar_contraseña_temporal()
        manicurista.cambiar_contraseña('nuevaContra123')
        self.assertFalse(manicurista.debe_cambiar_contraseña)

if __name__ == '__main__':
    unittest.main()
