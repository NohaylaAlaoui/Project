from django.urls import path
from . import views

app_name= 'GestionHotel'
urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.ClientsListView.as_view(), name= 'all-clients'),
    path('ClientCreation', views.ClientCreationView.as_view(), name= 'client-creation'),
    path('<int:pk>/ClientUpdate', views.ClientUpdateView.as_view(), name= 'client-update'),
    path('<int:pk>/ClientDeletion', views.ClientDeleteView.as_view(), name= 'client-delete'),
    path('chambertypes', views.ChamberTypesListView.as_view(), name= 'all-chambertypes'),
    path('chambertypeCreation', views.ChamberTypeCreationView.as_view(), name= 'chambertype-creation'),
    path('<int:pk>/chambertypeUpdate', views.ChamberTypeUpdateView.as_view(), name= 'chambertype-update'),
    path('<int:pk>/chambertypeDeletion', views.ChamberTypeDeleteView.as_view(), name= 'chambertype-delete'),
    path('chambers', views.ChambersListView.as_view(), name= 'all-chambers'),
    path('chamberCreation', views.ChamberCreationView.as_view(), name= 'chamber-creation'),
    path('<int:pk>/chamberUpdate', views.ChamberUpdateView.as_view(), name= 'chamber-update'),
    path('<int:pk>/chamberDeletion', views.ChamberDeleteView.as_view(), name= 'chamber-delete'),
    path('reservations', views.ReservationsListView.as_view(), name= 'all-reservations'),
    path('<int:pk>/reservation', views.ReservationsDetailView.as_view(), name='reservation-detail'),
    path('reservationCreation', views.ReservationCreationView.as_view(), name= 'reservation-creation'),
    path('<int:pk>/reservationUpdate', views.ReservationUpdateView.as_view(), name= 'reservation-update'),
    path('<int:pk>/reservationDeletion', views.ReservationDeleteView.as_view(), name= 'reservation-delete'),
    path('invoices', views.InvoicesListView.as_view(), name= 'all-invoices'),
    path('<int:pk>/invoice', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoiceCreation', views.InvoiceCreationView.as_view(), name= 'invoice-creation'),
    path('<int:pk>/invoiceUpdate', views.InvoiceUpdateView.as_view(), name= 'invoice-update'),
    path('<int:pk>/invoiceDeletion', views.InvoiceDeleteView.as_view(), name= 'invoice-delete'),
    path('onlinerequests', views.OnlineRequestsListView.as_view(), name= 'all-onlinerequests'),
    path('<int:pk>/onlinerequest', views.OnlineRequestDetailView.as_view(), name='onlinerequest-detail'),
    path('onlinerequestcreation', views.OnlineRequestCreationView.as_view(), name= 'onlinerequest-creation'),
    path('<int:pk>/onlinerequestupdate', views.OnlineRequestUpdateView.as_view(), name= 'onlinerequest-update'),
    path('<int:pk>/onlinerequestdelete', views.OnlineRequestDeleteView.as_view(), name= 'onlinerequest-delete'),
]
