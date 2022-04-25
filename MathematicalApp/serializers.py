from rest_framework import serializers


class FiboSerializers(serializers.Serializer):
    n = serializers.IntegerField()


class AckermannSerializers(serializers.Serializer):
    m = serializers.IntegerField(min_value=0)
    n = serializers.IntegerField(min_value=0)


class FactorialSerializers(serializers.Serializer):
    n = serializers.IntegerField(min_value=0)






    # def fibo(self, num):
    #     if self.number < 0:
    #         print("Incorrect input")
    #     elif self.number == 0:
    #         return 0
    #     elif self.number == 1:
    #         return 1
    #     else:
    #         return self.fibo(num - 1) + self.fibo(num - 2)