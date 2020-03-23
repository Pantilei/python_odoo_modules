from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'cirus.configuration'
    _description = 'This model stores configuration for control center!'
    
    @api.multi
    def configure(self):
        conf = self.env["cirus.configuration"].search([])
        a = len(conf)
        if a == 0:
            return {
                'name': 'Configuration',
                'domain': "[]",
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'cirus.configuration',
                'res_id': self.id,
                'view_id': False,
                'context': "{'create': False}",
                'type': 'ir.actions.act_window',
            }
        else:
            return {
                'name': 'Configuration',
                'domain': "[]",
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'cirus.configuration',
                'res_id': 1,
                'view_id': False,
                'context': "{'create': False}",
                'type': 'ir.actions.act_window',
            }

    url = fields.Char(string="API endpoint")
    name = fields.Boolean(string='Product Name', default=True)
    description = fields.Boolean(string='Description', default=True)
    description_purchase = fields.Boolean(string='Purchase Description', default=True)
    description_sale = fields.Boolean(string='Sale Description', default=True)
    type = fields.Boolean(string='Type', default=True)
    rental = fields.Boolean(string='Rental', default=True)
    categ_id = fields.Boolean(string='Category Id', default=True)
    list_price = fields.Boolean(string='List Price', default=True)
    standard_price = fields.Boolean(string='Standard Price', default=True)
    volume = fields.Boolean(string='Volume', default=True)
    weight = fields.Boolean(string='Weight', default=True)
    sale_ok = fields.Boolean(string='Sale OK', default=True)
    purchase_ok = fields.Boolean(string='Purchase OK', default=True)
    uom_id = fields.Boolean(string='UoM Id', default=True)
    uom_po_id = fields.Boolean(string='UoM PO ID', default=True)
    company_id = fields.Boolean(string='Company Id', default=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Boolean(string='Color', default=True)
    default_code = fields.Boolean(string='Default Code', default=True)
    uid_create = fields.Boolean(string='Create User ID', default=True)
    date_create = fields.Boolean(string='Create Date', default=True)
    uid_write = fields.Boolean(string='Write User ID', default=True)
    date_write = fields.Boolean(string='Write Date', default=True)
    responsible_id = fields.Boolean(string='Responsible ID', default=True)
    sale_delay = fields.Boolean(string='Sale Delay', default=True)
    tracking = fields.Boolean(string='Tracking', default=True)
    description_picking = fields.Boolean(string='Description Piking', default=True)
    description_pickingout = fields.Boolean(string='Description Piking Out', default=True)
    description_pickingin = fields.Boolean(string='Description Piking In', default=True)
    service_type = fields.Boolean(string='Service Type', default=True)
    sale_line_warn = fields.Boolean(string='Sale Line Warning', default=True)
    sale_line_warn_msg = fields.Boolean(string='Sale Line Warning Message', default=True)
    expense_policy = fields.Boolean(string='Expense Policy', default=True)
    invoice_policy = fields.Boolean(string='Invoice Policy', default=True)
    purchase_method = fields.Boolean(string='Purchase Method', default=True)
    purchase_line_warn = fields.Boolean(string='Purchase Line Warning', default=True)
    purchase_line_warn_msg = fields.Boolean(string='Purchase line warning', default=True)
    service_to_purchase = fields.Boolean(string='Service to Purchase', default=True)






