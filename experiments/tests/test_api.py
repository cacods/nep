from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
import json

from experiments.models import Experiment, Researcher, Study


class ExperimentAPITest(APITestCase):
    base_url = reverse('api_experiments')

    # This test is following tutorial. Not necessary because is
    # django-rest-framework. By default object returned is json.
    def test_get_returns_json_200(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['content-type'], 'application/json')

    def test_get_returns_all_experiments(self):
        researcher = Researcher.objects.create()
        # TODO: What a strange behavior. Maybe post question in Stackoverflow.
        # When trying to create our_user User instance without user name, test
        # doesn't pass. But in the first User instance created (other_user
        # above), without user name, test pass.
        user = User.objects.create(username='João')
        study = Study.objects.create(
            start_date=datetime.utcnow(), researcher=researcher
        )
        experiment1 = Experiment.objects.create(
            title='Our title', description='Our description',
            study=study, user=user
        )
        experiment2 = Experiment.objects.create(
            title='Our second title', description='Our second description',
            study=study, user=user
        )
        response = self.client.get(self.base_url)
        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            [
                {
                    'id': experiment1.id,
                    'title': experiment1.title,
                    'description': experiment1.description,
                    'data_acquisition_done':
                        experiment1.data_acquisition_done,
                    'study': experiment1.study.id,
                    'user': experiment1.user.id
                },
                {
                    'id': experiment2.id,
                    'title': experiment2.title,
                    'description': experiment2.description,
                    'data_acquisition_done':
                        experiment2.data_acquisition_done,
                    'study': experiment2.study.id,
                    'user': experiment2.user.id
                }
            ]
        )

    def test_POSTing_a_new_experiment(self):
            researcher = Researcher.objects.create()
            study = Study.objects.create(
                start_date=datetime.utcnow(), researcher=researcher
            )
            user = User.objects.create(username='Pedro')
            response = self.client.post(
                self.base_url,
                {
                    'title': 'New experiment',
                    'description': 'Some description',
                    'study': study.id,
                    'user': user.id,
                }
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            new_experiment = Experiment.objects.first()
            self.assertEqual(new_experiment.title, 'New experiment')

    # TODO: os testes de validações ainda não foram implementados.
    # Ver:
    # http://www.obeythetestinggoat.com/book/appendix_rest_api.html#_data_validation_an_exercise_for_the_reader


class ResearcherAPITest(APITestCase):
    base_url = reverse('api_researchers')

    def test_get_returns_all_researchers(self):
        researcher1 = Researcher.objects.create(
            first_name='Researcher1', surname='dos Santos'
        )
        researcher2 = Researcher.objects.create(
            first_name='Researcher2', surname='da Silva'
        )

        response = self.client.get(self.base_url)
        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            [
                {
                    'id': researcher1.id,
                    'first_name': researcher1.first_name,
                    'surname': researcher1.surname,
                    'email': researcher1.email,
                    'studies': []
                },
                {
                    'id': researcher2.id,
                    'first_name': researcher2.first_name,
                    'surname': researcher2.surname,
                    'email': researcher2.email,
                    'studies': []
                }
            ]
        )
