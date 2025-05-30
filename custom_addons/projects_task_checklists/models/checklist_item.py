# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2025-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Dhanya B (odoo@cybrosys.com)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, models


class ChecklistItem(models.Model):
    """
    Model for check list items
    """
    _name = 'checklist.item'
    _description = "Checklist Item"

    name = fields.Char(string="Name", required=True,
                       help="Name of the checklist item")
    sequence = fields.Integer(string="Sequence", default=1,
                              help="Sequence number")
    description = fields.Char(string="Description",
                              help="Description of the check list item")
    checklist_id = fields.Many2one('task.checklist', string="Checklist",
                                   help="Checklist")
