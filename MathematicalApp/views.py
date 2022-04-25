import logging

from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .serializers import FiboSerializers, AckermannSerializers, FactorialSerializers
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from functools import wraps
import time
from functools import reduce


# Create your views here.


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = (time.time() - start) * 1000
        print(30 * '*')
        logging.info('view {} takes {:.2f} ms'.format(
            func.__name__,
            duration
        ))
        print(30 * '*')
        return result

    return wrapper


@timer
def fibonacci(n):
    if n is None:
        return "n should not be empty"
    if n < 0:
        return "The value(s) must not be string or negative integer arguments"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class Fibonacci(views.APIView):
    serializer_class = FiboSerializers

    def post(self, request):
        n = request.data['n']
        try:
            result = {
                'result': fibonacci(int(n))
            }
            return JsonResponse(
                result, safe=False,
                content_type='application/json')
        except:
            result = {
                'result': 'The value(s) must not be string or negative integer arguments'
            }
            return JsonResponse(
                result, safe=False,
                content_type='application/json')


@timer
def ackermann(m, n):
    cache = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for rows in range(m + 1):
        for cols in range(n + 1):
            if rows == 0:
                cache[rows][cols] = cols + 1
            elif cols == 0:
                cache[rows][cols] = cache[rows - 1][1]
            else:
                r = rows - 1
                c = cache[rows][cols - 1]
                if r == 0:
                    ans = c + 1
                elif c <= n:
                    ans = cache[rows - 1][cache[rows][cols - 1]]
                else:
                    ans = (c - n) * (r) + cache[r][n]
                cache[rows][cols] = ans
    return cache[m][n]


class Ackermann(views.APIView):
    serializer_class = AckermannSerializers

    def post(self, request):
        m = request.data['m']
        n = request.data['n']
        try:
            result = {
                'result': ackermann(int(m), int(n))
            }
            return JsonResponse(result, safe=False)
        except:
            result = {
                'result': 'The value(s) must not be string or negative integer arguments'
            }
            return JsonResponse(
                result, safe=False,
                content_type='application/json')


@timer
def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce((lambda x, y: x * y), range(1, n + 1))


class Factorial(views.APIView):
    serializer_class = FactorialSerializers

    def post(self, request):
        n = request.data['n']
        try:
            result = {
                'result': factorial(int(n))
            }
            return JsonResponse(result, safe=False)
        except:
            result = {
                'result': 'The value(s) must not be string or negative integer arguments'
            }
            return JsonResponse(
                result, safe=False,
                content_type='application/json')
