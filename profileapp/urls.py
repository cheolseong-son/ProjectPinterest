from django.urls import path

app_name = 'profileapp'
urlpatterns = [
    path('', hello_world, name='hello_world'),
]