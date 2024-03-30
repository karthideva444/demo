from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

        # def update(self,instance,validated_data):
        #     instance.id = validated_data.get('id',instance.validated_data.id)
        #     instance.name = validated_data.get('name',instance.validated_data.name)
        #     instance.roll = validated_data.get('roll',instance.validated_data.roll)
        #     instance.city = validated_data.get('city',instance.validated_data.city)
        #     instance.save()
        #     return instance
        
    def update( self,instance,validated_data):
        # biz_locker_object = BizLkr.objects.get(id=biz_locker_id)
        print("hello")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate_roll(self,value):
        if(value < 100):
            raise serializers.ValidationError("less 100 is not valid")
        return value
    
    def validate_city(self,value):
        if(value != "chennai"):
            return value
        raise serializers.ValidationError("chennai is already in the list")


