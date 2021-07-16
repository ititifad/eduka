from django.urls import path
from . import views

urlpatterns = [
    path('lipaonline/',views.OentListView.as_view(),name='opayment_list'),
]