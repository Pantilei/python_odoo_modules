# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, values):
        # Override the original create function
        record = super(ProductTemplate, self).create(values)
        data = {
            "id": record.id,
            "name": record.name,
            "description": record.description,
            "description_purchase": record.description_purchase,
            "description_sale": record.description_sale,
            "type": record.type,
            "rental": record.rental,
            "categ_id": record.categ_id,
            "list_price": record.list_price,
            "standard_price": record.standard_price,
            "volume": record.volume,
            "weight": record.weight,
            "sale_ok": record.sale_ok,
            "purchase_ok": record.purchase_ok,
            "uom_id": record.uom_id,
            "uom_po_id": record.uom_po_id,
            "company_id": record.company_id,
            "active": record.active,
            "color": record.color,
            "default_code": record.default_code,
            "uid_create": record.create_uid,
            "date_create": record.create_date,
            "uid_write": record.write_uid,
            "date_write": record.write_date,
            "responsible_id": record.responsible_id,
            "sale_delay": record.sale_delay,
            "tracking": record.tracking,
            "description_picking": record.description_picking,
            "description_pickingout": record.description_pickingout,
            "description_pickingin": record.description_pickingin,
            "service_type": record.service_type,
            "sale_line_warn": record.sale_line_warn,
            "sale_line_warn_msg": record.sale_line_warn_msg,
            "expense_policy": record.expense_policy,
            "invoice_policy": record.invoice_policy,
            "purchase_method": record.purchase_method,
            "purchase_line_warn": record.purchase_line_warn,
            "purchase_line_warn_msg": record.purchase_line_warn_msg,
            "service_to_purchase": record.service_to_purchase,
        }

        configurations = self.env['cirus.configuration'].browse(1)
        fields = self.env['ir.model.fields'].search([('model_id', '=', 'cirus.configuration')])
        for field in fields:
            if not getattr(configurations, field.name, 'No %s field' % field.name):
                data.pop(field.name, None)

        api_endpoint = configurations.url
        headers = {"content-type": "application/json"}
        data_json = json.dumps(data, default=str)
        r = requests.post(url=api_endpoint, data=data_json, headers=headers)
        # print(r.text)
        return record

    def write(self, values):
        super(ProductTemplate, self).write(values)
        configurations = self.env['cirus.configuration'].browse(1)
        api_endpoint = configurations.url
        headers = {'content-type': 'application/json'}
        data = {}
        data.update({'id_update': self.id})
        data.update(values)
        data_json = json.dumps(data)
        r = requests.put(url=api_endpoint, data=data_json, headers=headers)
        print(r.text)
        return True
