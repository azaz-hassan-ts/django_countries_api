from django.urls import path
from django.conf.urls import url
from . import views

app_name = "countries"

urlpatterns = [
    path("", views.index, name="index"),
    path("allinfo", views.information_of_users, name="info"),
    url(r"^api/countries$", views.countries_list, name="country_list"),
    url(r"^api/countries/(?P<pk>[0-9]+)$", views.countries_details, name="country_details")
]