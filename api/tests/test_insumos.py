import unittest
from django.core.exceptions import ValidationError
from api.categoriainsumos.models import CategoriaInsumo
from api.insumos.models import Insumo

class InsumoTestCase(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.categoria = CategoriaInsumo.objects.create(nombre='Papelería')

    def setUp(self):
        self.insumo_data = {
            'nombre': 'Cuaderno',
            'cantidad': 10,
            'estado': 'activo',
            'categoria_insumo': self.categoria,
        }

    def test_crear_insumo(self):
        insumo = Insumo.objects.create(**self.insumo_data)
        self.assertEqual(insumo.nombre, 'Cuaderno')
        self.assertEqual(insumo.cantidad, 10)
        self.assertEqual(insumo.estado, 'activo')
        self.assertEqual(insumo.categoria_insumo.nombre, 'Papelería')

    def test_str_insumo(self):
        insumo = Insumo.objects.create(**self.insumo_data)
        self.assertEqual(str(insumo), 'Cuaderno')

    def test_cantidad_no_negativa(self):
        self.insumo_data['cantidad'] = -5
        insumo = Insumo(**self.insumo_data)
        with self.assertRaises(ValidationError):
            insumo.full_clean()

    def test_estado_valido(self):
        self.insumo_data['estado'] = 'invalido'
        insumo = Insumo(**self.insumo_data)
        with self.assertRaises(ValidationError):
            insumo.full_clean()

if __name__ == '__main__':
    unittest.main()
