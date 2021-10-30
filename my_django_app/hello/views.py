# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def index(APIView):
  return Response('Hola Prron >:v a ver si no me eliminan con git')