from django.urls import path

from . import views

app_name = 'photo'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:photo_id>/", views.detail, name="detail"),
    path("<int:photo_id>/like/", views.like, name="like"),
    path("<int:photo_id>/result/", views.result, name="result"),

]