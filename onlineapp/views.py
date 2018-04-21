# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from rest_framework import status


from django.shortcuts import render
from rest_framework.views import APIView

from models import Card, Tag

from serializer import CardSerializer, TagSerializer

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.http import Http404
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    # Render the index.html template with a context dictionary
    # that has a key called 'time' with current time obtained from
    # the datetime module as the value.
    return render(request, "index.html")


class Getcards(APIView):
    print "in wrng her"
    def get(self, request, format=None):
            lists = Card.objects.all()

            serializer = CardSerializer(lists, many=True)
            print(serializer.data)


            return JsonResponse(serializer.data,safe=False)

from django.utils.html import escape
class GetMyCards(APIView):
    # print "its here"
    def get(self, request, format=None):

            lists = Card.objects.filter(created_by=2)

            serializer = CardSerializer(lists, many=True)
            print(serializer.data)


            return JsonResponse(serializer.data,safe=False)
class GetTags(APIView):
    def get(self, request, format=None):
            tags = Tag.objects.all()

            serializer = TagSerializer(tags, many=True)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False)

class Get_card(APIView):
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):

        newcard = self.get_object(pk)
        print(newcard)
        serializer = CardSerializer(newcard)
        return JsonResponse(serializer.data)


class Edit_card(APIView):
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    @method_decorator(csrf_exempt)
    def get(self, request,pk, format=None):
        newcard = self.get_object(pk)
        print(newcard)
        serializer = CardSerializer(newcard)

        return JsonResponse(serializer.data)

    @method_decorator(csrf_exempt)
    def post(self, request,pk, format=None):
        uidata = request.data
        print(pk)
        card_data = Card.objects.filter(id=pk).update(title=uidata["title"], description=uidata["description"])
        print(uidata)


        # print(serializer.data)
        instance = Tag.objects.filter(card_id=pk)
        instance.delete()
        for i in uidata["tags"]:

            tagob = {}
            tagob["tagname"] = i
            tagob["card"] = pk

            serializertag = TagSerializer(data=tagob)
            if serializertag.is_valid():
                serializertag.save()
        return JsonResponse("success", status=status.HTTP_201_CREATED, safe=False)
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class Delete_card(APIView):
    def get(self, request,pk, format=None):
        instance = Card.objects.get(id=pk)
        instance.delete()
        return JsonResponse("dhh", status=status.HTTP_201_CREATED, safe=False)

from django.contrib.auth.models import User
class InsertCard(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        uidata=request.data


        card_data={}
        card_data["title"]=uidata["title"]
        card_data["description"]=uidata["description"]
        card_data["created_by"]=2
        print card_data


        serializer = CardSerializer(data=card_data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            for i in uidata["tags"]:
                tagob={}
                tagob["tagname"]=i
                tagob["card"]=serializer.data["id"]
                serializertag=TagSerializer(data=tagob)
                if serializertag.is_valid():
                    serializertag.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)

class Search_card(APIView):
    def post(self, request, format=None):
        searchkey=request.data.keys
        for k in searchkey:
            title_card=Card.objects.filter(string__contains=k)
            tag_card=Card.objects.get(tags=k)
            # title_result=CardSerializer(title_card,many=True)
            # tag_card=Card.objects.get(tags=k)
            # tag_result=CardSerializer(tag_card,many=True)



