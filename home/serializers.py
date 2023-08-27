from rest_framework import serializers
from home.models import Student

"""for function based api"""
"""
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=200)
    mobile = serializers.IntegerField(default=0)



    def create(self, validated_data):
        return Student.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.save()
        return instance
"""

""" for class based api """


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address', 'mobile']