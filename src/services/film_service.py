from src.database.models import Film


class FilmService:
    @staticmethod
    def fetch_all_films(session):
        return session.query(Film)

    @classmethod
    def fetch_film_by_uuid(cls, session, id):
        return cls.fetch_all_films(session).filter_by(
            id=id
        ).first()