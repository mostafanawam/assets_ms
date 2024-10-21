from django.shortcuts import get_object_or_404, render, redirect
from .forms import AssetForm
from .models import Asset, Employee, Lending
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:asset_view')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('main:login_view')  # Redirect to the login page

@login_required(login_url=reverse_lazy('main:login_view')) # accessing this route need to be logged in else redirected to login
def asset_view(request):
    if request.method == 'POST':
        # Handle asset creation
        form = AssetForm(request.POST)
        if form.is_valid(): # validate the form
            form.save() # create the asset
            return redirect('main:asset_view')  # Redirect back to the asset list after saving
    else:
        # Handle GET: Display the list of assets
        assets = Asset.objects.all()
        form = AssetForm()  # Also prepare the form for adding a new asset
        context={
            'assets': assets, 
            'form': form,
            "employees":Employee.objects.all() # list of employees used in lending
        }
        return render(request, 'asset_list.html',context=context )

@login_required(login_url=reverse_lazy('main:login_view'))
def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id) # check if exist else 404
    if request.method == 'POST':
        asset.delete() # delete asset
        return redirect('main:asset_view') # Redirect back to the asset list after deleting
    
@login_required(login_url=reverse_lazy('main:login_view'))
def edit_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('main:asset_view')  # Redirect to the asset list view after successful edit
    else:
        form = AssetForm(instance=asset)
    
@login_required(login_url=reverse_lazy('main:login_view'))
def lend_asset(request,asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    
    if request.method == 'POST':
        employee = get_object_or_404(Employee, id=request.POST['employee'])
        Lending.objects.create( # create lending instance
            asset=asset,
            employee=employee   # assign the selected employee as the lender
        )
        asset.status="lent" # change the status to lent(not available )
        asset.save()
        return redirect('main:asset_view')


@login_required(login_url=reverse_lazy('main:login_view'))
def return_asset(request,asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST':
        asset.status="available" # update the status of the asset to available    
        asset.save()
        current_lending=asset.current_lending   # get the last active lending process
        current_lending.return_date=timezone.now()  # assign the lending returning date
        current_lending.save()
        return redirect('main:asset_view')
        