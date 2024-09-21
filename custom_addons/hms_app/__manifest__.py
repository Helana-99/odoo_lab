{
    "name": "HMS App",
    "summary": "Hospital Management System",
    "description": "A module to manage hospital.",
    "author": "Helana N Eskander",
    "category": "Tools",
    "version": "17.0.0.1.0",
    "depends": ["base", "contacts", "crm"],
    "application": True,
    "data": [
             'security/ir.model.access.csv',
             'views/base_menus.xml',
             'views/patient_view.xml',
             'views/doctor_view.xml',
             'views/department_view.xml',
             'wizard/new_log_history_wizard_view.xml',
             'views/crm_customer_view.xml'


             ]
}
