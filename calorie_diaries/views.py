from django.shortcuts import render
from rest_framework import viewsets

from calorie_diaries.models import Diary, DiaryEntry
from calorie_diaries.serializers import DiarySerializers, DiaryEntrySerializer


# Create your views here.
class DiaryViewsets(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializers
    filterset_fields = ['date']


class DiaryEntryViewsets(viewsets.ModelViewSet):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
    filterset_fields = ['diary']
