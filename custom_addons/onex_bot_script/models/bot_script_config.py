from odoo import models, fields, api
from odoo.exceptions import UserError

class BotScriptConfig(models.Model):
    _name = 'onex.bot.script.config'
    _description = 'Bot Script Configuration'

    api_key = fields.Char("API Key")
    script_code = fields.Text("Script Code", default="<script>console.log('Bot script!');</script>")
    active = fields.Boolean("Active", default=True)

    @api.model
    def create(self, values):
        existing_record = self.search([], limit=1)
        if existing_record:
            # Nếu đã có bản ghi, cập nhật bản ghi đó thay vì tạo mới
            existing_record.write(values)
            return existing_record
        return super(BotScriptConfig, self).create(values)

    def write(self, values):
        # Kiểm tra nếu bản ghi không tồn tại, không thể sửa
        if not self:
            raise UserError("Không tìm thấy bản ghi để sửa!")

        # Cập nhật thông tin bản ghi hiện tại
        result = super(BotScriptConfig, self).write(values)
        return result

    @api.model
    def default_get(self, fields):
        # Trả về bản ghi hiện tại nếu đã có, hoặc tạo bản ghi mặc định
        existing_record = self.search([], limit=1)
        if existing_record:
            return existing_record[0].read(fields)[0]
        else:
            return super(BotScriptConfig, self).default_get(fields)
