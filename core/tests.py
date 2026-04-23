from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Device, Rack, Sala


class ApiAuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='daniel', password='12345678')
        self.sala = Sala.objects.create(nome='Sala 1304', professor='Professor A')
        self.rack = Rack.objects.create(nome='Rack 1', sala=self.sala)
        self.device = Device.objects.create(
            nome='Notebook 01',
            rack=self.rack,
            processador='Intel Core i5',
            memoria_ram='8 GB DDR4',
            placa_video='Intel UHD',
            bateria_percentual=90,
            duracao_media_bateria='6 horas',
            status_descricao='No lugar certo e carregando',
            armazenamento_total=256,
            armazenamento_usado=120,
            carregando=True,
            presente=True,
        )

    def test_api_requires_authentication(self):
        response = self.client.get('/api/devices/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_list_salas(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/salas/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Sala 1304')

    def test_authenticated_user_can_create_rack(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/racks/', {
            'nome': 'Rack 2',
            'sala': self.sala.id,
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Rack.objects.filter(nome='Rack 2', sala=self.sala).exists())

    def test_authenticated_user_can_get_device_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/devices/{self.device.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Notebook 01')
        self.assertEqual(response.data['rack_nome'], 'Rack 1')

    def test_api_returns_404_for_missing_device(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/devices/9999/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_user_can_delete_device(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/devices/{self.device.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Device.objects.filter(id=self.device.id).exists())
