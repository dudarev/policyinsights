from django.urls import path

from programs import views


urlpatterns = [
    path('p/', views.ProgramCreate.as_view(), name='program-create'),
    path('l/<slug:program_slug>/p/<slug:slug>/', views.ProgramDetail.as_view(), name='program-detail'),
    path('l/<slug:program_slug>/p/<slug:slug>/update/', views.ProgramUpdate.as_view(), name='program-update'),
]
