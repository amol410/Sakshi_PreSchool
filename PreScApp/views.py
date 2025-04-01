from django.shortcuts import render
from django.http import Http404

# Create your views here.


def index(request):
    """Home page view"""
    return render(request, 'PreScApp/index.html')

def about(request):
    """About page view"""
    return render(request, 'PreScApp/about.html')

def contact(request):
    """Contact page view"""
    return render(request, 'PreScApp/contact.html')

def facility(request):
    """Facilities page view"""
    return render(request, 'PreScApp/facility.html')

def projects(request):
    """Projects page view"""
    return render(request, 'PreScApp/projects.html')

def team(request):
    """Team page view"""
    return render(request, 'PreScApp/team.html')

def testimonial(request):
    """Testimonials page view"""
    return render(request, 'PreScApp/testimonial.html')

def classes(request):
    """Classes page view"""
    return render(request, 'PreScApp/classes.html')

def call_to_action(request):
    """Call to action page view"""
    return render(request, 'PreScApp/call-to-action.html')

def appointment(request):
    """Appointment page view"""
    return render(request, 'PreScApp/appointment.html')



def page_not_found(request, exception=None):
    """
    Custom 404 error page view.
    Can be accessed directly via /404/ or will be shown for actual 404 errors.
    """
    context = {
        'page_title': 'Page Not Found',
        'error_message': 'The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.'
    }
    return render(request, '404.html', context, status=404)