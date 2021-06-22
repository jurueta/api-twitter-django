from rest_framework import serializers
from .models import UserTwitter, AdditionalData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTwitter
        fields = ['id', 'name','last_name','email','phone','username','password','photo','cover_photo','verified','created_at','update_at']

    def to_representation(self, instance):
        """ forrmat data in response """
        url = "http://localhost:8000/"
        ret = super().to_representation(instance)
        ret['name'] = ret['name'].upper()
        ret['last_name'] = ret['last_name'].upper()
        ret['photo'] = url + ret['photo'] if ret['photo'] else ret['photo']
        ret.pop('password')
        return ret

class AditionalDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalData
        fields = ['country','gender','language','age']