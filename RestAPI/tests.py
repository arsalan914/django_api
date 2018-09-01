# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase
from rest_framework.test import RequestsClient
import json
#from dateutil.parser import parse


class RestTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        self.test_2 = []
        self.test_3 = []
        self.test_4 = []
        self.test_5 = []
        with open('TestData/http01.json') as f:
            for line in f:
                self.test_1.append(line)
        with open('TestData/http02.json') as f:
            for line in f:
                self.test_2.append(line)
        with open('TestData/http03.json') as f:
            for line in f:
                self.test_3.append(line)
        with open('TestData/http04.json') as f:
            for line in f:
                self.test_4.append(line)
        with open('TestData/http05.json') as f:
            for line in f:
                self.test_5.append(line)

    def test_set_1(self):
        client = RequestsClient()
        for ro in self.test_1:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            print (row['request']['method'])
            print (row['request']['url'])
            print (res.status_code)
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['request']['url'] == '/actors' and row['request']['method'] == 'GET':
                self.assertEqual(sorted(json.loads(res.text)), sorted(row['response']['body']))
            elif row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['created_at']:
                        temp = parse(resp['created_at'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['created_at'] = temp
                self.assertEqual(sorted(response), sorted(row['response']['body']))

    def test_set_2(self):
        client = RequestsClient()
        for ro in self.test_2:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['request']['url'] == '/actors' and row['request']['method'] == 'GET':
                self.assertEqual(sorted(json.loads(res.text)), sorted(row['response']['body']))
            elif row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['created_at']:
                        temp = parse(resp['created_at'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['created_at'] = temp
                self.assertEqual(sorted(response), sorted(row['response']['body']))

    def test_set_3(self):
        client = RequestsClient()
        for ro in self.test_3:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['request']['url'] == '/actors' and row['request']['method'] == 'GET':
                self.assertEqual(sorted(json.loads(res.text)), sorted(row['response']['body']))
            elif row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['created_at']:
                        temp = parse(resp['created_at'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['created_at'] = temp
                self.assertEqual(sorted(response), sorted(row['response']['body']))

    def test_set_4(self):
        client = RequestsClient()
        for ro in self.test_4:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['request']['url'] == '/actors' and row['request']['method'] == 'GET':
                self.assertEqual(sorted(json.loads(res.text)), sorted(row['response']['body']))
            elif row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['created_at']:
                        temp = parse(resp['created_at'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['created_at'] = temp
                self.assertEqual(sorted(response), sorted(row['response']['body']))

    def test_set_5(self):
        client = RequestsClient()
        for ro in self.test_5:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            elif row['request']['method'] == "PUT":
                res = client.put('http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['request']['url'] == '/actors' and row['request']['method'] == 'GET':
                self.assertEqual(sorted(json.loads(res.text)), sorted(row['response']['body']))
            elif row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['created_at']:
                        temp = parse(resp['created_at'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['created_at'] = temp
                self.assertEqual(sorted(response), sorted(row['response']['body']))