from django.urls import path

from . import views


urlpatterns = [
    path('t/', views.TagCreate.as_view(), name='tag-create'),
    path('t/<slug:slug>/', views.TagDetail.as_view(), name='tag-detail'),
    path('t/<slug:slug>/update/', views.TagUpdate.as_view(), name='tag-update'),
]