from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from ticket import models, forms


class MainView(View):
    def get(self, request):
        tickets = models.Ticket.objects.all ()
        return render(request, "main.html", {"tickets": tickets})


class TicketDetailView(View):
    def get(self, request, ticket_id):
        ticket = get_object_or_404(models.Ticket, id = ticket_id)
        return render(request, "ticket_detail.html", {"ticket": ticket})


class AddTicketView(View):
    def get(self, request):
        form = forms.TicketForm()
        return render(request, "ticket_form.html", {"form": form})

    def post(self, request):
        form = forms.TicketForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("main")