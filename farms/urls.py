from django.urls import path
from . import views

urlpatterns = [
    path("", views.farm_list, name="farm_list"),
    path("dashboard", views.dashboard_overview, name="dashboard_overview"),
    path("create/", views.farm_create, name="farm_create"),
    path("<int:pk>/update/", views.farm_update, name="farm_update"),
    path("<int:pk>/delete/", views.farm_delete, name="farm_delete"),
]
