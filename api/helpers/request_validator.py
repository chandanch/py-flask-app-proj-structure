from api.errors.request_validation_error import RequestValidatonError


def validate_request_body(request_data, DataSchema):
    schema = DataSchema()
    errors = schema.validate(request_data)

    if errors:
        validation_error = RequestValidatonError(errors)
        return validation_error.serialize_error()
    else:
        return False
