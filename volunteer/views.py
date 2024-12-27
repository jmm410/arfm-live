from .models import Volunteer
from .forms import VolunteerForm, CreateUserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CreateUserForm()
    return render(request, "register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            if not User.objects.filter(username=username).exists():
                messages.error(request, "Invalid Login")
                return redirect('login')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Invalid Login")
                return redirect('login')
            else:
                login(request, user)
                return redirect('index')
        return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def index(request):
    volunteers = []
    if request.method == "POST":
        volunteer_need_list = request.POST.getlist("toggled[]")
        volunteer_list = Volunteer.objects.all()
        
        if volunteer_need_list:
            for volunteer in volunteer_list:
                match = [getattr(volunteer, item) for item in volunteer_need_list]
                if all(match):
                    volunteers.append(volunteer)
 
    return render(request, 'index.html', {"volunteers": volunteers})



@login_required(login_url="login")
def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})


@login_required(login_url="login")
def volunteer_create(request):
   
    volunteer_form = VolunteerForm(request.POST or None)
    if request.method == "POST":
        if volunteer_form.is_valid():
            volunteer = volunteer_form.save()
            messages.success(request, "Volunteer created successfully!")
            return redirect(reverse("volunteer", args=[volunteer.id]))
        else:
            messages.error(request, "Error creating volunteer.")
    
    return render(request, "volunteer_form.html", {"volunteer_form": volunteer_form})

@login_required(login_url="login")
def volunteer_read(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    def process_resources(resources, comment=None, custom=None):
        resource_list = [key for resource in resources for key, value in resource.items() if value]
        if comment:
            resource_list.append(comment)
        if custom:
            resource_list.append(custom)
        return resource_list
    
    shelter_resources = [
        {"Host One or Two People": volunteer.host_small}, 
        {"Host Small Group or Family": volunteer.host_large},
        {"Children Welcome": volunteer.host_children}, 
        {"Pets Welcome": volunteer.host_pets},
        {"Disability Accessible": volunteer.host_disable}, 
        {"Drug or Smoke Friendly": volunteer.host_smoke},
        {"Car Living Amenities": volunteer.host_mobile_accomodation}, 
        {"Long Term Hosting": volunteer.host_long_term},
        {"Kosher or Halal Kitchen": volunteer.host_religious_kitchen}
    ]
    shelter_list = process_resources(shelter_resources, volunteer.host_comment)

    transit_resources = [
        {"Airport/Station Ride or Pickup": volunteer.transport_station}, 
        {"Drive to Local Destination": volunteer.transport_local},
        {"Pay for Rideshare": volunteer.transport_pay_for_ride}, 
        {"Pay for Public Transit": volunteer.transport_pay_for_public},
        {"Public Transit Advice": volunteer.transport_advice_for_public}, 
        {"Lend Bike": volunteer.transport_loan_bike},
        {"Lend Car": volunteer.transport_loan_car}, 
        {"Moving Vehicle": volunteer.transport_moving_vehicle}
    ]
    transit_list = process_resources(transit_resources, volunteer.transport_comment)

    donation_resources = [
        {"Groceries or Meal": volunteer.donation_groceries}, 
        {"Hygiene Products": volunteer.donation_hygiene},
        {"Household Products": volunteer.donation_household}, 
        {"Baby Items": volunteer.donation_baby_item},
        {"Gift Cards": volunteer.donation_gift_card}, 
        {"Winter Items": volunteer.donation_winter_items}
    ]
    donation_list = process_resources(donation_resources, volunteer.donation_comment, volunteer.donation_custom)

    settle_resources = [
        {"Orient to City": volunteer.settle_orient_to_city}, 
        {"Orient to Local LGBTQ Community": volunteer.settle_orient_to_local_community},
        {"Referral to LGBTQ Healthcare": volunteer.settle_find_healthcare}, 
        {"Parent-to-Parent Support": volunteer.settle_parental_support},
        {"Childcare": volunteer.settle_childcare}, 
        {"Foster Pet": volunteer.settle_foster_pet},
        {"Disability Connections": volunteer.settle_disability_connections}, 
        {"Religious Connections": volunteer.settle_religious_connections},
        {"Language Translation": volunteer.settle_language_translation}
    ]
    settle_list = process_resources(settle_resources, volunteer.settle_comment, volunteer.settle_custom)

    volunteering_resources = [
        {"Administrative Services": volunteer.volunteering_administrative}, 
        {"Data Entry": volunteer.volunteering_data_entry},
        {"Organization": volunteer.volunteering_organizer}, 
        {"Financial Donation": volunteer.volunteering_money_donation}
    ]
    volunteering_list = process_resources(volunteering_resources, volunteer.volunteering_custom)
    professional_list = [volunteer.additional_professional] if volunteer.additional_professional else []
    employment_list = [volunteer.additional_employment] if volunteer.additional_employment else []
    custom_list = [volunteer.additional_custom] if volunteer.additional_custom else []

    return render(request, "volunteer.html", {
        "volunteer": volunteer,
        "shelter_list": shelter_list,
        "transit_list": transit_list,
        "donation_list": donation_list,
        "settle_list": settle_list,
        "volunteering_list": volunteering_list,
        "professional_list": professional_list,
        "employment_list": employment_list,
        "custom_list": custom_list,
    })


@login_required(login_url="login")
def volunteer_update(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    
    if request.method == "POST":
        volunteer_form = VolunteerForm(request.POST, instance=volunteer)
        if volunteer_form.is_valid():
            volunteer_form.save()
            messages.success(request, "Volunteer updated successfully!")
            return redirect(reverse("volunteer_detail", args=[volunteer.id]))
        else:
            messages.error(request, "Error updating volunteer.")
    else:

        volunteer_form = VolunteerForm(instance=volunteer)

    return render(request, "volunteer_update.html", {"volunteer_form": volunteer_form})

@login_required(login_url="login")
def volunteer_delete(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if request.method == "POST":
        volunteer.delete()
        return redirect("volunteer_list")
    return redirect(request, "volunteer_delete.html", {"volunteer": volunteer})

