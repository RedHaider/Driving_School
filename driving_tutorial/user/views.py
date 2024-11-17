from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
 
def home(request):
    return render(request, 'index.html')  

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def appointment(request):
    return render(request,'appointment.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request,'template_admin/dashboard.html')




class UserRegistrationView(CreateView):
    model = User
    fields = [
        'first_name', 'last_name', 'username', 'email', 
        'phone', 'address', 'city', 'state', 'zip_code', 'photo'
    ]  # Exclude password fields here
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Custom form handling for password validation and saving
        """
        password = self.request.POST.get('password1')
        confirm_password = self.request.POST.get('password2')

        # Validate passwords
        if password != confirm_password:
            form.add_error('password', "Passwords do not match.")
            return self.form_invalid(form)

        # Save the user with hashed password
        user = form.save(commit=False)
        user.set_password(password)  # Hash the password
        user.save()

        # Add success message
        messages.success(self.request, "Registration successful. Please log in.")
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'  # Path to your login template
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = '/'  # Redirect here after successful login

    def form_valid(self, form):
        print("Login successful for user:", form.get_user())
        login(self.request, form.get_user())  # Log the user in
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Login failed. Errors:", form.errors)
        print("POST Data:", self.request.POST)  # Debug the submitted data
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
        logout(request)  # Log the user out
        return redirect('login')  # Redirect to the login page (or another page like 'home')


