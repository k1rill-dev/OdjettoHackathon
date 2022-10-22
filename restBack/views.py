from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class ExponentView(LoginRequiredMixin, ListAPIView):
    queryset = Exponent.objects.all()
    serializer_class = ExponentSerializer


@csrf_exempt
@login_required
def exponent_detail(request, pk):
    try:
        ex = Exponent.objects.get(pk=pk)
    except Exponent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExponentSerializer(ex)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExponentSerializer(ex, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ex.delete()
        return HttpResponse(status=204)
