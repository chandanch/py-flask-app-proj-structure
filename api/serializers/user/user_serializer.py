class UserSerializer:
    @staticmethod
    def serialize(user):
        return {
            "id": user.id,
            "name": user.name,
            "biopic": user.biopic,
            "country": str(user.country) if user.country else None,
        }
