from django.urls import path
from . import views

urlpatterns = [
    path('fibo/',views.Fibonacci.as_view(), name='fibonacci'),
    path('acker/',views.Ackermann.as_view(), name='ackermann'),
    path('fact/',views.Factorial.as_view(), name='factorial'),
]
