from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, DeleteView
from .forms import RegistrationForm, DietSectionForm
from .models import Registration, DietSection


class CombinedFormView(View):
    template_name = 'event/registration.html'
    success_url = reverse_lazy('thank_you')

    def post(self, request):
        registration_form = RegistrationForm(request.POST)
        diet_section_form = DietSectionForm(request.POST)

        if registration_form.is_valid() and diet_section_form.is_valid():
            # Save the registration form first
            registration = registration_form.save()
            # Associate the diet section with the saved registration
            diet_section = diet_section_form.save(commit=False)
            diet_section.registration = registration
            diet_section.save()

            return redirect(self.success_url)
        else:
            print(registration_form.errors)
            print(diet_section_form.errors)

        return render(request, self.template_name, {
            'forms': [registration_form, diet_section_form]
        })

    def get(self, request):
        registration_form = RegistrationForm()
        diet_section_form = DietSectionForm()

        return render(request, self.template_name, {
            'forms': [registration_form, diet_section_form]
        })


class ParticipantListView(ListView):
    model = Registration
    template_name = 'event/guest_list.html'
    context_object_name = 'participants'


class ParticipantUpdateView(UpdateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'event/participant_edit.html'
    success_url = reverse_lazy('participant_list')


class ParticipantDeleteView(DeleteView):
    model = Registration
    template_name = 'event/guest_delete.html'
    success_url = reverse_lazy('participant_list')


def thank_you(request):
    return render(request, 'event/thank_you.html')
