from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string="Related Patient")

    # Making the Tax ID field mandatory
    vat = fields.Char(string="Tax ID", required=True)

    @api.constrains('email')
    def _check_patient_email(self):
        for rec in self:
            if rec.email:
                # Check if this email exists in the hms.patient model
                existing_patient = self.env['hms.patient'].search([('email', '=', rec.email)], limit=1)
                if existing_patient:
                    raise ValidationError(f"The email '{rec.email}' already exists in the Patient records.")

    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError("You cannot delete a customer linked to a patient.")
        return super(Customer, self).unlink()
