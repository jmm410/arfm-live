from .models import Volunteer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    admin_emails = ["marcm1992@outlook.com", "j.marc.mccall@gmail.com", "zzaks23@gmail.com"]
   

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email not in self.admin_emails:
            raise ValidationError("The email provided is not authorized for account creation.")
        
        return email

    def save(self, commit=True):
        user = super().save(commit=False)


        if user.email in self.admin_emails:
            user.is_superuser = True
            user.is_staff = True
        
        if commit: 
            user.save()

        return user
    

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        labels = {
            "first_name": "First Name", 
            "last_name": "Last Name", 
            "phone": "Phone", 
            "email": "Email",
            "alt_phone": "Alt. Phone", 
            "alt_email": "Alt. Email", 
            "street": "Street", 
            "city": "City", 
            "state": "State",
            "zip_code": "Zip Code", 
            "local": "local",
            
            "host_small": "Host One or Two People", 
            "host_large": "Host Small Group or Family", 
            "host_long_term": "Long Term Hosting",
            "host_children": "Children Welcome", 
            "host_pets": "Pets Welcome", 
            "host_disable": "Disability Accessible",
            "host_smoke": "Drug or Smoke Friendly", 
            "host_mobile_accomodation": "Car Living Amenities", 
            "host_religious_kitchen": "Kosher or Halal Kitchen",
            "host_comment": "Shelter Comment",

            "transport_station": "Airport/Station Ride or Pickup", 
            "transport_local": "Drive to Local Destination", 
            "transport_pay_for_ride": "Pay for Rideshare", 
            "transport_pay_for_public": "Pay for Public Transit",
            "transport_advice_for_public": "Public Transit Advice",
            "transport_loan_bike": "Lend Bike",
            "transport_loan_car": "Lend Car", 
            "transport_moving_vehicle": "Moving Vehicle", 
            "transport_comment": "Transportation Comment",

            "donation_groceries": "Groceries or Meal", 
            "donation_hygiene": "Hygiene Products", 
            "donation_household": "Household Products",
            "donation_baby_item": "Baby Items", 
            "donation_gift_card": "Gift Cards", 
            "donation_winter_items": "Winter Items",
            "donation_affirming_clothes": "Gender Affiming Clothes", 
            "donation_custom": "Donation Other",
            "donation_comment": "Donation Comment",

            "settle_orient_to_city": "Orient to City", 
            "settle_orient_to_local_community": "Orient to Local LGBTQ Community", 
            "settle_find_healthcare": "Referral to LGBTQ Healthcare",
            "settle_parental_support": "Parent-to-Parent Support", 
            "settle_childcare": "Childcare", 
            "settle_foster_pet": "Foster Pet",
            "settle_disability_connections": "Disability Connections", 
            "settle_religious_connections": "Religious Connections", 
            "settle_language_translation": "Language Translation",
            "settle_custom": "Settling Other", 
            "settle_comment": "Settling Comment",

            "volunteering_administrative": "Administrative Services",
            "volunteering_data_entry": "Data Entry",
            "volunteering_organizer": "Organization",
            "volunteering_money_donation": "Financial Donation",
            "volunteering_custom": "Volunteer Other",

            "additional_professional":"Services",
            "additional_employment":"Services",
            "additional_custom": "Comments",

        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "alt_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Alt. Phone"}),
            "alt_email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Alt. Email"}),
            "street": forms.TextInput(attrs={"class": "form-control", "placeholder": "Street"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zip Code"}),
            "local": forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            "host_small": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_large": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_long_term": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_children": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_pets": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_disable": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_smoke": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_mobile_accomodation": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_religious_kitchen": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "host_comment": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            "transport_station": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_local": forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            "transport_pay_for_ride": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_pay_for_public": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_advice_for_public": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_loan_bike": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_loan_car": forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            "transport_moving_vehicle": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "transport_comment": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            "donation_groceries": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "donation_hygiene": forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            "donation_household": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "donation_baby_item": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "donation_gift_card": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "donation_winter_items": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "donation_affirming_clothes": forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            "donation_custom": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            "donation_comment": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            "settle_orient_to_city": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_orient_to_local_community": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_find_healthcare": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_parental_support": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_childcare": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_foster_pet": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_disability_connections": forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            "settle_religious_connections": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_language_translation": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "settle_custom": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), 
            "settle_comment": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            "volunteering_administrative": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "volunteering_data_entry": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "volunteering_organizer": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "volunteering_money_donation": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "volunteering_custom": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            "additional_professional": forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            "additional_employment": forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            "additional_custom": forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
        }
