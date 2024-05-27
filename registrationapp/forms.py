from django import forms
from .models import Registration, EventSession, DietSection


class RegistrationForm(forms.ModelForm):
    event_session = forms.ModelChoiceField(
        queryset=EventSession.objects.all(),
        empty_label='Select Event',
        label='Please Choose an Event to Attend:'
    )

    class Meta:
        model = Registration
        fields = ['user_first_name', 'user_last_name', 'user_email', 'user_phone', 'event_session']
        labels = {
            'user_first_name': 'First Name',
            'user_last_name': 'Last Name',
            'user_email': 'Email Address',
            'user_phone': 'Phone Number'
        }
        error_messages = {
            'user_email': {
                'required': 'Your email address must not be empty!',
                'invalid': 'Please enter a valid email address'
            }
        }


class EventSessionForm(forms.ModelForm):
    class Meta:
        model = EventSession
        fields = '__all__'
        labels = {
            'event_name': 'Event Name',
            'event_description': 'Event Description'
        }


class DietSectionForm(forms.ModelForm):
    class Meta:
        model = DietSection
        exclude = ['registration']
        widgets = {
            'diet_description': forms.RadioSelect
        }
        labels = {
            'diet_description': 'Dietary Restrictions',
        }
