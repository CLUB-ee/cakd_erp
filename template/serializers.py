# from rest_framework import serializers
# from template.models import Cusord,Instock,Manager,Material,Menu,Ord,Outstock,Recipe

# class CusordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cusord
#         fields = ('cus_ord_num','out_time','menu_id')

# class InstockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instock
#         fields = ('in_num','in_time','ord_num','mate_id','in_quan')

#     # 신규 instance를 생성해서 리턴해준다
#     def create(self, validated_data):
#         return Instock.objects.create(**validated_data)

#     # 생성되어 있는 instance 를 저장한 후 리턴해준다
#     def update(self, instance, validated_data):
#         instance.in_time = validated_data.get('in_time', instance.in_time)
#         instance.ord_num = validated_data.get('ord_num', instance.ord_num)
#         instance.mate_id = validated_data.get('mate_id', instance.mate_id)
#         instance.in_quan = validated_data.get('in_quan', instance.in_quan)
#         instance.save()
#         return instance

# class OutstockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Outstock
#         fields = ('out_num','out_time','cus_ord_num','mate_id','out_quan')

#     # 신규 instance를 생성해서 리턴해준다
#     def create(self, validated_data):
#         return Outstock.objects.create(**validated_data)

#     # 생성되어 있는 instance 를 저장한 후 리턴해준다
#     def update(self, instance, validated_data):
#         instance.in_time = validated_data.get('in_time', instance.in_time)
#         instance.cus_ord_num = validated_data.get('cus_ord_num', instance.ord_num)
#         instance.mate_id = validated_data.get('mate_id', instance.mate_id)
#         instance.out_quan = validated_data.get('out_quan', instance.out_quan)
#         instance.save()
#         return instance

# class ManagerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manager
#         fields = '__all__'