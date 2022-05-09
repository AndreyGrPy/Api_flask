"""
SELECT QUERIES
"""
from sqlalchemy import and_

from src import db
from src.database import models

films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
interstellar = db.session.query(models.Film).filter(
    models.Film.title == 'Interstellar'
).first()
# print(interstellar)
mafia_2 = db.session.query(models.Film).filter_by(
    title='Mafia part-2'
).first()
# print(mafia_2)
and_statement_films = db.session.query(models.Film).filter(
    models.Film.title != 'Mafia part-2',
    models.Film.rating >= 7.0
).all()
# print(and_statement_films)
next_vary = db.session.query(models.Film).filter(
    and_(
        models.Film.title != 'Interstellar',
        models.Film.rating >= 7.5
    )
).all()
# print(next_vary)
deathly_hallows = db.session.query(models.Film).filter(
    models.Film.title.like('%Haski%')
).all()
# print(deathly_hallows)
films_sorted_by_length = db.session.query(models.Film).filter(
    models.Film.length.in_([101, 143])
).all()
# print(films_sorted_by_length)
films_sorted = db.session.query(models.Film).filter(
    ~models.Film.length.in_([101, 143])
)[:1]
# print(films_sorted)
"""
QUERYING WITH JOINS
"""
films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
print(films_with_actors)