from django.urls import path
from . import views
from .views import ParticipantListView, ParticipantUpdateView, ParticipantDeleteView

urlpatterns = [
    path('', views.CombinedFormView.as_view(), name='index'),
    path('thank-you', views.thank_you, name='thank_you'),
    path('guest-list/', ParticipantListView.as_view(), name='participant_list'),
    path('guest-list/edit/<int:pk>/', ParticipantUpdateView.as_view(), name='participant_edit'),
    path('guest-list/delete/<int:pk>/', ParticipantDeleteView.as_view(), name='participant_delete'),

]
