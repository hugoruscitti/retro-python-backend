import json
from django.test import TestCase
from app.models import Proyecto
from django.contrib.auth.models import User

class TestApi(TestCase):

    def test_se_creo_el_usuario_admin(self):
        self.assertEqual(User.objects.count(), 1)

    def test_puede_crear_y_obtener_un_proyecto(self):
        data = {
            "screenshot": "base64...",
            "version": "0.0.1",
            "codigo": "circulo(0, 0, 10, 10, 3, True)",
            "textura": "base64...",
        }

        response = self.client.post("/subir", json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Proyecto.objects.count(), 1)
        hash = response.json()["hash"]

        response = self.client.get(f"/obtener/{hash}")

        self.assertEqual(response.status_code, 200)
        resultado = response.json()
        self.assertEqual(resultado['codigo'], 'circulo(0, 0, 10, 10, 3, True)')

    def test_puede_solicitar_la_lista_de_ejemplos(self):
        data = {
            "screenshot": "base64...",
            "version": "0.0.1",
            "codigo": "circulo(0, 0, 10, 10, 3, True)",
            "textura": "base64...",
        }

        response = self.client.post("/subir", json.dumps(data), content_type='application/json')

        response = self.client.get(f"/ejemplos")

        self.assertEqual(response.status_code, 200)
        resultado = response.json()
        self.assertEqual(len(resultado['ejemplos']), 1)

