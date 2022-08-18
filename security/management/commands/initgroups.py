from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission

from patients.models import *
from therapists.models import *
# from accounting.models import *
from security.models import *

GROUPS_PERMISSIONS = {
    'Sysadmin': {
        UserAccount: ['create','change','delete','view'],
        Group: ['create','change','delete','view'],
        # Partners: ['change','delete','view'],
        # CapitalContributions: ['change','delete','view'],
        # CapitalWithdrawals: ['change','delete','view'],
        # Partners: ['view'],
        # CapitalContributions: ['view'],
        # CapitalWithdrawals: ['view'],
        Patients: ['view'],
        PatientDetails: ['view'],
        PatientSessions: ['view'],
        Rooms: ['view'],
        # Therapists: ['view'],
        # TherapistDetails: ['view'],
        # Clients: ['view'], 
        # PaymentMethods: ['view'], 
        # Rentals: ['view'], 
        # Bills: ['view'], 
        # CreditNotes: ['view'], 
        # Providers: ['view'], 
        # ProviderDetails: ['view'], 
        # ProviderServices: ['view'], 
        # PurchaseInvoices: ['view'], 
        # Assets: ['view'], 
        # MoneyInReceipts: ['view'], 
        # MoneyOutReceipts: ['view'],
    },
    'Owner': {
        # Partners: ['add', 'view'],
        # CapitalContributions: ['add','view'],
        # CapitalWithdrawals: ['add','view'],
        Patients: ['add','change','delete','view'],
        PatientDetails: ['add', 'change', 'delete', 'view'],
        PatientSessions: ['add', 'change', 'delete', 'view'],
        Rooms: ['add', 'change', 'delete', 'view'],
        # Therapists: ['add','change','delete','view'],
        # TherapistDetails: ['add','change','delete','view'],
        # Clients: ['view'], 
        # PaymentMethods: ['view'], 
        # Rentals: ['view'], 
        # Bills: ['view'], 
        # CreditNotes: ['view'], 
        # Providers: ['view'], 
        # ProviderDetails: ['view'], 
        # ProviderServices: ['view'], 
        # PurchaseInvoices: ['view'], 
        # Assets: ['view'], 
        # MoneyInReceipts: ['view'], 
        # MoneyOutReceipts: ['view'],
    },
    'Therapists': {
        Patients: ['view'],
        PatientDetails: ['add', 'change', 'delete', 'view'],
        PatientSessions: ['add', 'change', 'delete', 'view'],

    },
#     'Finance Analyst': {
#         Clients: ['add', 'view'], 
#         PaymentMethods: ['view'], 
#         Rentals: ['add', 'view'], 
#         Bills: ['add', 'view'], 
#         CreditNotes: ['add', 'view'], 
#         Providers: ['view'], 
#         ProviderDetails: ['view'], 
#         ProviderServices: ['view'], 
#         PurchaseInvoices: ['add', 'view'], 
#         Assets: ['add', 'view'], 
#         MoneyInReceipts: ['add', 'view'], 
#         MoneyOutReceipts: ['add', 'view'],
#     },
#     'Finance Leader': {
#         Clients: ['change', 'delete', 'view'], 
#         PaymentMethods: ['add', 'change', 'delete', 'view'], 
#         Rentals: ['change', 'delete', 'view'], 
#         Bills: ['add', 'view'], 
#         CreditNotes: ['add', 'view'], 
#         Providers: ['add', 'change', 'delete', 'view'], 
#         ProviderDetails: ['add', 'change', 'delete', 'view'], 
#         ProviderServices: ['add', 'change', 'delete', 'view'], 
#         PurchaseInvoices: ['change', 'delete', 'view'], 
#         Assets: ['change', 'delete', 'view'], 
#         MoneyInReceipts: ['change', 'delete', 'view'], 
#         MoneyOutReceipts: ['change', 'delete', 'view'],
#     },
}

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    help = "Create default groups"

    def handle(self, *args, **options):
        # Loop groups
        for group_name in GROUPS_PERMISSIONS:

            # Get or create group
            group, created = Group.objects.get_or_create(name=group_name)

            # Loop models in group
            for model_cls in GROUPS_PERMISSIONS[group_name]:

                # Loop permissions in group/model
                for perm_index, perm_name in \
                        enumerate(GROUPS_PERMISSIONS[group_name][model_cls]):

                    # Generate permission name as Django would generate it
                    codename = perm_name + "_" + model_cls._meta.model_name

                    try:
                        # Find permission object and add to group
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                        self.stdout.write("Adding "
                                          + codename
                                          + " to group "
                                          + group.__str__())
                    except Permission.DoesNotExist:
                        self.stdout.write(codename + " not found")