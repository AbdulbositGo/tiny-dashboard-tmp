from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'dashboard/index.html')

def analytics(request):
    return render(request, 'dashboard/analytics.html')

def e_commerce(request):
    return render(request, 'dashboard/e-commerce.html')

def saas_dashboard(request):
    return render(request, 'dashboard/saas-dashboard.html')

def systems(request):
    return render(request, 'dashboard/systems.html')

# UI

def buttons(request):
    return render(request, 'ui-elements/buttons.html')

def colors(request):
    return render(request, 'ui-elements/colors.html')

def icons(request):
    return render(request, 'ui-elements/icons.html')

def modals(request):
    return render(request, 'ui-elements/modals.html')

def notifications(request):
    return render(request, 'ui-elements/notifications.html')

def progress(request):
    return render(request, 'ui-elements/progress.html')

def tabs_accordion(request):
    return render(request, 'ui-elements/tabs-accordion.html')

def typograpy(request):
    return render(request, 'ui-elements/typograpy.html')

# Auth
def login(request):
    return render(request, 'auth/login.html')

def login_half(request):
    return render(request, 'auth/login-half.html')

def register(request):
    return render(request, 'auth/register.html')

def resetpw(request):
    return render(request, 'auth/resetpw.html')

def confirm(request):
    return render(request, 'auth/confirm.html')

# Charts
def apex(request):
    return render(request, 'charts/apex.html')

def chartjs(request):
    return render(request, 'charts/chartjs.html')

def datamaps(request):
    return render(request, 'charts/datamaps.html')

def inline(request):
    return render(request, 'charts/inline.html')

# Contacts
def contacts_grid(request):
    return render(request, 'contacts/grid.html')

def contacts_list(request):
    return render(request, 'contacts/list.html')

def contacts_new(request):
    return render(request, 'contacts/new.html')

# Files 
def files_grid(request):
    return render(request, 'files/grid.html')

def files_list(request):
    return render(request, 'files/list.html')

# Forms
def advanced(request):
    return render(request, 'forms/advanced.html')

def elements(request):
    return render(request, 'forms/elements.html')

def layouts(request):
    return render(request, 'forms/layouts.html')

def upload(request):
    return render(request, 'forms/upload.html')

def validation(request):
    return render(request, 'forms/validation.html')

def wizard(request):
    return render(request, 'forms/wizard.html')

# Pages
def blank(request):
    return render(request, 'pages/blank.html')

def invoice(request):
    return render(request, 'pages/invoice.html')

def orders(request):
    return render(request, 'pages/orders.html')

def timeline(request):
    return render(request, 'pages/timeline.html')

def page_404(request):
    return render(request, 'pages/404.html')

def page_500(request):
    return render(request, 'pages/500.html')

# Profiles
def notification(request):
    return render(request, 'profiles/notification.html')

def overview(request):
    return render(request, 'profiles/overview.html')

def security(request):
    return render(request, 'profiles/security.html')

def settings(request):
    return render(request, 'profiles/settings.html')

# Support
def detail(request):
    return render(request, 'support/detail.html')

def center(request):
    return render(request, 'support/center.html')

def faqs(request):
    return render(request, 'support/faqs.html')

def tickets(request):
    return render(request, 'support/tickets.html')

# Tables
def tables_advanced(request):
    return render(request, 'tables/advanced.html')

def tables_basic(request):
    return render(request, 'tables/basic.html')

def tables_datatables(request):
    return render(request, 'tables/datatables.html')

# Layaut
def horizontal(request):
    return render(request, 'layout/horizontal.html')


def widgets(request):
    return render(request, 'widgets.html')

def calendar(request):
    return render(request, 'calendar.html')