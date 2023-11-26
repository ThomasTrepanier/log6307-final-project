from ma import ma
from models.model import Company

from marshmallow import fields, validate


class CompanySchema(ma.ModelSchema):

    name = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    addressLine1 = fields.Str(required=True, validate=[validate.Length(min=5, max=250)])
    addressLine2 = fields.Str(required=False, validate=[validate.Length(max=250)])
    city = fields.Str(required=True, validate=[validate.Length(min=5, max=100)])
    state = fields.Str(required=True, validate=[validate.Length(min=2, max=10)])
    zipCode = fields.Str(required=True, validate=[validate.Length(min=5, max=250)])
    logo = fields.Str(required=False, validate=[validate.Length(max=250)])
    website = fields.Str(required=True, validate=[validate.Length(min=5, max=250)])
    recognition = fields.Str(required=False, validate=[validate.Length(max=250)])
    vision = fields.Str(required=False, validate=[validate.Length(max=250)])
    history = fields.Str(required=False, validate=[validate.Length(max=250)])
    mission = fields.Str(required=False, validate=[validate.Length(max=250)])

    class Meta:
        model = Company
