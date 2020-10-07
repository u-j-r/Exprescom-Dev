
from odoo import _, api, models

from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.multi
    def button_confirm(self):
        if self.partner_id.l10n_mx_in_blocklist == 'blocked':
            raise ValidationError(
                _('The SAT provides a block list with all the VATs whose '
                  'owners have committed some illegality the selected partner '
                  'is on that list. If you sell/buy to this customer, the SAT '
                  'could audit your company. To avoid this error you can go '
                  'to the partner and set the "Partner State" field as OK'))
        return super(PurchaseOrder, self).button_confirm()
