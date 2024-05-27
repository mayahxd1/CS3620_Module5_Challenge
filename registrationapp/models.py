from django.db import models


class EventSession(models.Model):
    objects = None
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name


class Registration(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=12)
    event_session = models.ForeignKey(EventSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"


class DietSection(models.Model):
    dietary_restrictions = [
        ('None', 'None'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Keto', 'Keto'),
        ('Paleo', 'Paleo'),
        ('Gluten-Free', 'Gluten-Free'),
        ('Dairy-Free', 'Dairy-Free'),
        ('Nut-Free', 'Nut-Free'),
        ('Shellfish-Free', 'Shellfish-Free'),
        ('Soy-Free', 'Soy-Free'),
    ]
    diet_description = models.CharField(max_length=50, choices=dietary_restrictions, default='None')
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return self.diet_description
