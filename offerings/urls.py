from django.urls import path

from offerings.views import delete_offering, edit_offering, create_offering, offerings, create_offering_type, \
    edit_offering_type, delete_offering_type, offering_types

urlpatterns = [
    path('', offerings, name='offerings'),
    path('add/', create_offering, name='create-offering'),
    path('edit/<int:offering_pk>', edit_offering, name='edit-offering'),
    path('delete/<int:offering_pk>', delete_offering, name='delete-offering'),


    # offering types
    path('offering-types/', offering_types, name='offering-types'),
    path('add/offering-types/', create_offering_type, name='create-offering-type'),
    path('edit/offering-types/<int:offering_type_pk>', edit_offering_type, name='edit-offering-type'),
    path('delete/offering-types/<int:offering_type_pk>', delete_offering_type, name='delete-offering-type'),

]