from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Address
from .forms import ProfileForm, AddressForm

# Create your views here.

def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile_edit_form = ProfileForm(instance=profile)
    address_user = get_object_or_404(Address, profile = profile)

    context = {'form': profile_edit_form,
               'profile':profile}
    
    return render(request, 'a_profile/profile.html', context)

def profile_edit_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect back to profile view
    else:
        form = ProfileForm(instance=profile)

    # Return only the partial HTML for HTMX
    return render(request, 'a_profile/profileedit.html', {'form': form})

def address_edit_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    address_user = get_object_or_404(Address, profile=profile)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address_user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect back to profile view
    else:
        form = AddressForm(instance=address_user)

    # Return only the partial HTML for HTMX
    return render(request, 'a_profile/addressedit.html', {'form': form})

