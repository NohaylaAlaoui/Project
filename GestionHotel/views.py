from django.shortcuts import render, redirect
from datetime import date
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Create your views here.

def index(request):
    return render(request,'GestionHotel/home.html')

###########################################################################################
###################### Client Views   ####################################################
###########################################################################################
class ClientsListView(generic.ListView):
    """ClientsListView: produce a list of all Clients """
    model = Client


class ClientCreationView(CreateView):
    model = Client                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

class ClientDeleteView(DeleteView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

###########################################################################################
###################### ChamberType Views   ####################################################
###########################################################################################
class ChamberTypesListView(generic.ListView):
    """ChamberTypesListView: produce a list of all ChamberTypes """
    model = ChamberType


class ChamberTypeCreationView(CreateView):
    model = ChamberType                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

class ChamberTypeUpdateView(UpdateView):
    model = ChamberType
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

class ChamberTypeDeleteView(DeleteView):
    model = ChamberType
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

###########################################################################################
###################### Chamber Views   ####################################################
###########################################################################################
class ChambersListView(generic.ListView):
    """ChambersListView: produce a list of all Chambers """
    model = Chamber


class ChamberCreationView(CreateView):
    model = Chamber                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

class ChamberUpdateView(UpdateView):
    model = Chamber
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

class ChamberDeleteView(DeleteView):
    model = Chamber
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

###########################################################################################
###################### Reservation Views   ####################################################
###########################################################################################
class ReservationsListView(generic.ListView):
    """ReservationsListView: produce a list of all Reservations """
    model = Reservation



class ReservationsDetailView(DetailView):

    model = Reservation


class ReservationCreationView(CreateView):
    model = Reservation                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

class ReservationDeleteView(DeleteView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

###########################################################################################
###################### Invoice Views   ####################################################
###########################################################################################
class InvoicesListView(generic.ListView):
    """InvoicesListView: produce a list of all Invoices """
    model = Invoice



class InvoiceDetailView(DetailView):

    model = Invoice


class InvoiceCreationView(CreateView):
    model = Invoice                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

class InvoiceDeleteView(DeleteView):
    model = Invoice
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

###########################################################################################
###################### Online Request Views   ####################################################
###########################################################################################
class OnlineRequestsListView(generic.ListView):
    """InvoicesListView: produce a list of all Invoices """
    model = OnlineRequest


class OnlineRequestDetailView(DetailView):

    model = OnlineRequest


class OnlineRequestCreationView(CreateView):
    model = OnlineRequest                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-onlinerequests')

class OnlineRequestUpdateView(UpdateView):
    model = OnlineRequest
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-onlinerequests')

class OnlineRequestDeleteView(DeleteView):
    model = OnlineRequest
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:index')
