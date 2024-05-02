from django.urls import path, include
from rest_framework.routers import DefaultRouter

from calorie_diaries.views import DiaryViewsets, DiaryEntryViewsets

diary_router = DefaultRouter()

diary_router.register( r'diaries', DiaryViewsets)
diary_router.register( r'diary_entries', DiaryEntryViewsets)

urlpatterns = [
    path('api/v1/', include(diary_router.urls)),
]