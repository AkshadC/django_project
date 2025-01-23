from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage

def auto_login(request):
    # Hardcoded credentials (use cautiously)
    username = 'aksha'
    password = 'password@2023'
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('admin:index')  # Redirect to the main admin page
    else:
        return redirect('login')  # Redirect to login if authentication fails

def index(request):
    return render(request, 'index.html')

def add_site_data(request):
    return render(request, 'edit_add_site.html') 

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        fs = FileSystemStorage(location='your/specified/path/')  # Specify your desired path
        filename = fs.save(excel_file.name, excel_file)
    return render(request, 'add_new_auth.html')
   
def redirect_to_admin_page(request):
    return redirect('admin:index')  