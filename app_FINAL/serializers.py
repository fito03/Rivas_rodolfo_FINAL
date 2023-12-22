from rest_framework import serializers
from app_FINAL.models import Inscritos, Instituciones

class Instituciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'

class Inscritos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'