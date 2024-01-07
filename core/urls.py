from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "core"

urlpatterns = [
    path('', views.SetProjectNameView, name = "ViewWelcomePage"),
    path('index/', views.IndexPageView, name="index"),
    path('person_registration/', views.RegisterPersonView, name="ViewRegisterPerson"),
    path('capture_image/', views.capture_image, name="ViewCaptureImage"),
    path('model_training/', views.TrainOnDataView, name="ViewTrainData"),
]
