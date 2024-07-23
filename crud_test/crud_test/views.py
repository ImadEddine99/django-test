# from datetime import date, datetime, time
# from datetime import timedelta
# import statistics
# from unittest import result
# from django.utils import timezone
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db import connection
# from django.db.models import Q
# from django.db.models import Count, Avg
# from django.db.models.functions import Concat
# from collections import defaultdict
# from django.conf import settings
# from datetime import datetime
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from django.core import serializers
# from rest_framework import viewsets
# from django.utils.html import escape
# from rest_framework.exceptions import AuthenticationFailed
# import jwt
# import html
# import json
# # from dateutil import tz
# import pytz
# import html
# import re
# # import pytz
# # import html
# from environ import Env
# import requests
# import talentlms
# import bcrypt
# from mailjet_rest import Client
# from django.db.models import Max

# from django.views.decorators.csrf import csrf_protect
import concurrent.futures
from django.views.decorators.csrf import csrf_exempt

from django.core.files.base import ContentFile, File
import os

from .models import Centers, Images


def salutView(request):
    return HttpResponse('Salut les gens')

class testView(APIView):
    def post(self, request):
        print('TEST PASS')
        # return JsonResponse({ 'msg': 'TEST PASS' })
    

class PasDeHack(APIView):
    def get(self, request):
        return JsonResponse({ 'msg': 'Pas de hack' })    

class getImagesFromTest_2(APIView):
    def post(self, request):
        image_id=request.data['image_id']
        image_link=Images.objects.using("test_2").filter(id=image_id).first().link
        return JsonResponse({ 'image_link': image_link })  
class getCenterFromTest_1(APIView):
    def post(self, request):
        center_id=request.data['center_id']
        center_name=Centers.objects.db_manager("default").filter(id=center_id).first().name
        return JsonResponse({ 'center_name': center_name }) 