from django.shortcuts import render
# from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json

# Create your views here.

class SearchByNameApi(APIView):

    def get(self,request):
        name = request.GET.get('s','')
        _type = request.GET.get('type','movie')
        year = request.GET.get('y',None)
        if name=='':
            data = {'status':'movie title is required! koskesh'}
            return Response(data)
        else:
            api_url = "http://www.omdbapi.com/?s={0}&type={1}".format(name,_type)
            if year is not None:
                api_url+="&y={0}".format(year)
            api_key = "&apikey=24f4da70"
            api_url+= api_key
            response = requests.get(api_url)
            resp = json.loads(response.content)
            return Response(resp)


class SearchByImdbIdApi(APIView):

    def get(self,request):
        imdb_id = request.GET.get('i','')
        name = request.GET.get('t','')
        _type = request.GET.get('type','movie')
        year = request.GET.get('y',None)
        if name=='' and imdb_id=='':
            data = {'status':'movie title or imdb id are required! koskesh'}
            return Response(data)
        else:
            api_url = "http://www.omdbapi.com/?t={0}&i={1}&type={2}".format(name,imdb_id,_type)
            if year is not None:
                api_url+="&y={0}".format(year)
            api_key = "&apikey=24f4da70"
            api_url+= api_key
            response = requests.get(api_url)
            resp = json.loads(response.content)
            return Response(resp)

