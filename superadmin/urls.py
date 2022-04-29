from django.urls import path
from .import views
urlpatterns = [

    path('index',views.index,name='index'),
    path('index-doc',views.index_doc,name='index-doc'),
    path('index-pat',views.index_pat,name='index-pat'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    #----------------------------Doctor-----------------------------------#
    path('create-doctor/',views.create_doctor,name='create-doctor'),
    path('view-doctor/',views.view_doctor,name='view-doctor'),
    path('update-doctor/<int:pk>',views.update_doctor,name='update-doctor'),
    path('delete-doctor/<int:pk>',views.delete_doctor,name='delete-doctor'),
    path('profile-doc',views.profile_doc,name='profile-doc'),


    #----------------------------patient---------------------------------#
    path('create-patient/',views.create_patient,name='create-patient'),
    path('view-patient/',views.view_patient,name='view-patient'),
    path('update-patient/<int:pk>',views.update_patient,name='update-patient'),
    path('delete-patient/<int:pk>',views.delete_patient,name='delete-patient'),
    path('profile-pat',views.profile_pat,name='profile-pat'),

]