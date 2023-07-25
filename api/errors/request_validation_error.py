class RequestValidatonError:
    status_code = 400

    def __init__(self, errors):
        self.errors = errors

    def serialize_error(self):
        errors = []
        for error in self.errors:
            errors.append({"message": error.value, "field": error.field})
