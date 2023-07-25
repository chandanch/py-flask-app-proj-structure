from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    biopic = fields.Str()
    country = fields.Str()


class UpdateUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    biopic = fields.Str()
    country = fields.Str()
    updated_at = fields.Date()


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    biopic = fields.Str()
    country = fields.Str()
