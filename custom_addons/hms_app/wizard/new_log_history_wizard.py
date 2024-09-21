from odoo import models, fields

class NewLogHistory(models.TransientModel):
    _name = 'hms.new.log.history'

    patient_id = fields.Many2one('hms.patient', required=True)
    description = fields.Text()

    def action_new_log_history(self):
        self.ensure_one()
        self.patient_id.log_history_ids.create({
            'patient_id': self.patient_id.id,
            'description': self.description,
            'create_uid': self.env.uid,
        })