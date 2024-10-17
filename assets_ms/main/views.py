from django.shortcuts import get_object_or_404, render, redirect
from .forms import AssetForm
from .models import Asset, Lending
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:asset_view')  # Redirect to a success page, replace 'home' with your URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'assets/login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('main:login_view')  # Redirect to the login page (or any page you prefer)

def asset_view(request):
    if not request.user.is_authenticated:
        return redirect('main:login_view')
    if request.method == 'POST':
        # Handle asset creation
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:asset_view')  # Redirect back to the asset list after saving
    else:
        # Handle GET: Display the list of assets
        assets = Asset.objects.all()
        form = AssetForm()  # Also prepare the form for adding a new asset
        return render(request, 'assets/asset_list.html', {'assets': assets, 'form': form})

def delete_asset(request, asset_id):
    if not request.user.is_authenticated:
        return redirect('main:login_view')
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('main:asset_view')
    
def edit_asset(request, asset_id):
    if not request.user.is_authenticated:
        return redirect('main:login_view')
    asset = get_object_or_404(Asset, id=asset_id)
    
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('main:asset_view')  # Redirect to the asset list view after successful edit
    else:
        form = AssetForm(instance=asset)
    
def lend_asset(request,asset_id):
    if not request.user.is_authenticated:
        return redirect('main:login_view')
    
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        Lending.objects.create(
            asset=asset,
            employee=request.user
        )
        asset.status="lent"
        asset.save()
        return redirect('main:asset_view')
    
def return_asset(request,asset_id):
    if not request.user.is_authenticated:
        return redirect('main:login_view')
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.status="available"
        asset.save()
        return redirect('main:asset_view')
        