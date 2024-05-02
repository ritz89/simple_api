from rest_framework import serializers

from calorie_diaries.models import Diary, DiaryEntry


class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'


class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = '__all__'