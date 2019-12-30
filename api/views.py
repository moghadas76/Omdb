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



class GetTags(APIView):

    def get(self,request):
        api_endpint = 'http://moviesapi.ir/api/v1/genres'
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)


class SearchByTagApi(APIView):

    def get(self,request,g_id,page):
        # pg = request.GET.get('page','')
        api_endpint = 'http://moviesapi.ir/api/v1/genres/{0}/movies?page={1}'.format(g_id,page)
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)

    

class InfoByIp(APIView):

    def get(self,request):
        api_endpint = 'https://api.ipgeolocation.io/ipgeo?apiKey=3099885ac5d746899364c64640b53a6c'
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)

def build_url(page):
    return "http://127.0.0.1:8000" + page

class ObtainAddress(APIView):

    def get(self,request):
        api_endpint = build_url('/api/v1/ip')
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        lat = resp['latitude']
        lang = resp['longitude']
        api_endpint = 'https://api.neshan.org/v2/reverse?lat={0}&lng={1}'.format(lat,lang)
        headers = {'Api-Key':'service.YDy990oXoofQgcTGLj5bwiIl8m36DqxC46Md7bav'}
        response = requests.get(api_endpint,headers=headers)
        resp = json.loads(response.content)
        return Response(resp)



class FindCountryInfo(APIView):

    def get(self,request,country):
        api_endpint = 'https://restcountries.eu/rest/v2/name/{0}'.format(country)
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)


class UrlShorten(APIView):

    def get(self,request):
        api_endpint = 'http://api.ipstack.com/check?access_key=32b2d4ff44a25e933213340faf94e3ea&format=1'
        response = requests.get(api_url)
        resp = json.loads(response.content)
        return Response(resp)




class Weather(APIView):

    def get(self,request):
        api_endpint =build_url('/api/v1/ip')
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        lat = resp['latitude']
        lang = resp['longitude']
        api_endpint = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID={2}'.format(lat,lang,'4b492e893c215c7ef16db91abd94effc')
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)


# Move to frontend
class TextToSpeech(APIView):

    def get(self,request,text):
        api_endpint = 'http://api.voicerss.org/?key=0781320d756a454181c8047b5dbfaf7f&hl=en-us&src={0}'.format(text)
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)


# Move to frontend
class QrGenerator(APIView):

    def get(self,request,text):
        api_endpint = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={0}'.format(text)
        response = requests.get(api_endpint)
        resp = json.loads(response.content)
        return Response(resp)

