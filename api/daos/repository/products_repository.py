
from api.helpers.database import DatabaseSingleton
from api.models.product.product import ProductModel


class ProductModelRepository:
    def create(self, data):
        # Create a new record in the database
        session = DatabaseSingleton().get_session()
        new_record = ProductModel(**data)
        session.add(new_record)
        session.commit()
        return new_record

    def get_by_id(self, record_id):
        # Retrieve a record by its ID
        session = DatabaseSingleton().get_session()
        return session.query(ProductModel).query.get(record_id)

    def update(self, record, data):
        # Update an existing record
        session = DatabaseSingleton().get_session()
        for key, value in data.items():
            setattr(record, key, value)
        session.commit()
        return record

    def delete(self, record):
        # Delete a record
        session = DatabaseSingleton().get_session()
        session.delete(record)
        session.commit()
