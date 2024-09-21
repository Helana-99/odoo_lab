from email.policy import default

from odoo import models,fields


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Ticket'


    name =fields.Char()
    number =fields.Integer()
    description = fields.Text()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ],default='new')
    file = fields.Binary()

    def action_new (self):
        self.state='new'

    def action_done (self):
        self.state='done'


    def action_cancelled (self):
        self.state='cancelled'