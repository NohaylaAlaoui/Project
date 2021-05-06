from django.shortcuts import render, redirect
from datetime import date
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now


# Create your views here.

def home(request):
    return render(request,'GestionHotel/home.html')


class Index(LoginRequiredMixin, View):
    """View function for index page of site."""
    def get(self, request):
        # Generate counts of some of the main objects
        num_demandes = OnlineRequest.objects.filter(request_confirmed__exact=False).count()
        num_reservations = Reservation.objects.filter(start_date__gt=now().date()).count()

        # Available books (status = 'a')
        num_chambers_available = Chamber.objects.filter(chamber_reserved__exact=False).count()

        context = {
            'num_demandes': num_demandes,
            'num_reservations': num_reservations,
            'num_chambers_available': num_chambers_available,
        }

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'index.html', context=context)

###########################################################################################
###################### Client Views   ####################################################
###########################################################################################
class ClientsListView(LoginRequiredMixin, generic.ListView):
    """ClientsListView: produce a list of all Clients """
    model = Client


class ClientCreationView(LoginRequiredMixin, CreateView):
    model = Client                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-clients')

###########################################################################################
###################### ChamberType Views   ####################################################
###########################################################################################
class ChamberTypesListView(LoginRequiredMixin, generic.ListView):
    """ChamberTypesListView: produce a list of all ChamberTypes """
    model = ChamberType


class ChamberTypeCreationView(LoginRequiredMixin, CreateView):
    model = ChamberType                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

class ChamberTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = ChamberType
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

class ChamberTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = ChamberType
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambertypes')

###########################################################################################
###################### Chamber Views   ####################################################
###########################################################################################
class ChambersListView(LoginRequiredMixin, generic.ListView):
    """ChambersListView: produce a list of all Chambers """
    model = Chamber


class ChamberCreationView(LoginRequiredMixin, CreateView):
    model = Chamber                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

class ChamberUpdateView(LoginRequiredMixin, UpdateView):
    model = Chamber
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

class ChamberDeleteView(LoginRequiredMixin, DeleteView):
    model = Chamber
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-chambers')

###########################################################################################
###################### Reservation Views   ####################################################
###########################################################################################
class ReservationsListView(LoginRequiredMixin, generic.ListView):
    """ReservationsListView: produce a list of all Reservations """
    model = Reservation



class ReservationsDetailView(LoginRequiredMixin, DetailView):

    model = Reservation


class ReservationCreationView(LoginRequiredMixin, CreateView):
    model = Reservation                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-reservations')

###########################################################################################
###################### Invoice Views   ####################################################
###########################################################################################
class InvoicesListView(LoginRequiredMixin, generic.ListView):
    """InvoicesListView: produce a list of all Invoices """
    model = Invoice



class InvoiceDetailView(LoginRequiredMixin, DetailView):

    model = Invoice


class InvoiceCreationView(LoginRequiredMixin, CreateView):
    model = Invoice                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-invoices')

###########################################################################################
###################### Online Request Views   ####################################################
###########################################################################################
class OnlineRequestsListView(LoginRequiredMixin, generic.ListView):
    """InvoicesListView: produce a list of all Invoices """
    model = OnlineRequest


class OnlineRequestDetailView(LoginRequiredMixin, DetailView):

    model = OnlineRequest


class OnlineRequestCreationView(CreateView):
    model = OnlineRequest                       #create a modal through a form
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:home')

class OnlineRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = OnlineRequest
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:all-onlinerequests')

class OnlineRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = OnlineRequest
    fields = '__all__'
    success_url = reverse_lazy('GestionHotel:index')
