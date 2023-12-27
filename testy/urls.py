from django.urls import path
from . import views


urlpatterns = [
    # Dashboard
    path('', views.home, name='dashboard'),
    path('analytics/', views.analytics, name='dashboard-analytics'),
    path('e-commerce/', views.e_commerce, name='dashboard-e-commerce'),
    path('saas-dashboard/', views.saas_dashboard, name='dashboard-saas-dashboard'),
    path('systems/', views.systems, name='dashboard-sytems'),

    # UI
    path('ui-buttons/', views.buttons, name='ui-buttons'),
    path('ui-colors/', views.colors, name='ui-colors'),
    path('ui-icons/', views.icons, name='ui-icons'),
    path('ui-modals/', views.modals, name='ui-modals'),
    path('ui-notifications/', views.notifications, name='ui-notifications'),
    path('ui-progress/', views.progress, name='ui-progress'),
    path('ui-tabs-accordion/', views.tabs_accordion, name='ui-tabs-accordion'),
    path('ui-typograpy/', views.typograpy, name='ui-typograpy'),

    # Auth
    path('auth-login', views.login, name="auth-login"),
    path('auth-login-half', views.login_half, name="auth-login-half"),
    path('auth-register', views.register, name="auth-register"),
    path('auth-resetpw', views.resetpw, name="auth-resetpw"),
    path('auth-confirm', views.confirm, name="auth-confirm"),

    # Charts
    path('charts-apex', views.apex, name="charts-apex"),
    path('charts-chartsjs', views.chartjs, name="charts-chartjs"),
    path('charts-datamaps', views.datamaps, name="charts-datamaps"),
    path('charts-inline', views.inline, name="charts-inline"),

    # Contacts 
    path('contacts-grid', views.contacts_grid, name="contacts-grid"),
    path('contacts-list', views.contacts_list, name="contacts-list"),
    path('contacts-new', views.contacts_new, name="contacts-new"),

    # Files
    path('files-grid', views.files_grid, name="files-grid"),
    path('files-list', views.files_list, name="files-list"),

    # Forms
    path('forms-advanced', views.advanced, name="forms-advanced"),
    path('forms-elements', views.elements, name="forms-elements"),
    path('forms-layouts', views.layouts, name="forms-layouts"),
    path('forms-upload', views.upload, name="forms-upload"),
    path('forms-validation', views.validation, name="forms-validation"),
    path('forms-wizard', views.wizard, name="forms-wizard"),

    # Pages 
    path('pages-blank', views.blank, name="pages-blank"),
    path('pages-invoice', views.invoice, name="pages-invoice"),
    path('pages-timeline', views.timeline, name="pages-timeline"),
    path('pages-orders', views.orders, name="pages-orders"),
    path('404', views.page_404, name="pages-404"),
    path('500', views.page_500, name="pages-500"),

    # Profiles 
    path('profiles-notification', views.notification, name="profiles-notification"),
    path('profiles-overview', views.overview, name="profiles-overview"),
    path('profiles-security', views.security, name="profiles-security"),
    path('profiles-settings', views.settings, name="profiles-settings"),

    # Support
    path('support-detail', views.detail, name="support-detail"),
    path('support-center', views.center, name="support-center"),
    path('support-faqs', views.faqs, name="support-faqs"),
    path('support-tickets', views.tickets, name="support-tickets"),

    # Tables
    path('tables-advanced', views.tables_advanced, name="tables-advanced"),
    path('tables-basic', views.tables_basic, name="tables-basic"),
    path('tables-datatables', views.tables_datatables, name="tables-datatables"),

    path('horizontal', views.horizontal, name="horizontal"),
    path('widgets', views.widgets, name="widgets"),
    path('calendar', views.calendar, name="calendar"),
]
