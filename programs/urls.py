from django.urls import path

from programs import views


urlpatterns = [
    path('p/', views.ProgramCreate.as_view(), name='program-create'),
    path('l/<slug:location_slug>/p/<slug:slug>/', views.ProgramDetail.as_view(), name='program-detail'),
    path('l/<slug:location_slug>/p/<slug:slug>/update/', views.ProgramUpdate.as_view(), name='program-update'),
    path('p/compare/<int:pk1>/<int:pk2>/', views.ProgramsCompare.as_view(), name='program-compare'),
]
