from datetime import date
from src import db
from src.database.models import Film, Actor


def populate_films():
    mafia_2 = Film(
        title='Mafia part-2',
        release_date=date(2004, 11, 4),
        description='Crime boss create a gang',
        distributed_by='Netflix',
        length=143,
        rating=8.1,
    )
    spider_man = Film(
        title='Spider man road to home',
        release_date=date(2021, 1, 24),
        description='Piter Parker this is a man which bitten spider',
        distributed_by='Netflix',
        length=110,
        rating=6.2,
    )
    interstellar = Film(
        title='Interstellar',
        release_date=date(2021, 7, 7),
        description='People flying to marc',
        distributed_by='Netflix',
        length=111,
        rating=9.4,
    )
    hacker = Film(
        title='Hacker',
        release_date=date(2017, 1, 24),
        description='Man to hack sistem of Americans banks',
        distributed_by='Netflix',
        length=101,
        rating=6.1,
    )
    warm = Film(
        title='Warm',
        release_date=date(2001, 12, 3),
        description='Film for war in 2 world war',
        distributed_by='Netflix',
        length=121,
        rating=8.8,
    )
    haski = Film(
        title='Haski',
        release_date=date(2012, 1, 14),
        description='Film about a dog waiting its owner',
        distributed_by='Netflix',
        length=111,
        rating=8.3,

    )

    daniel_radcliffe = Actor(name='Daniel Radcliffe', birthday=date(1989, 7, 23), is_active=True)
    cuintinn_tarantino = Actor(name='Cuentinn Tarantino', birthday=date(1989, 7, 23), is_active=True)
    berdd_pitt = Actor(name='Bredd Pitt', birthday=date(1980, 11, 13), is_active=True)
    jonni_depp = Actor(name='Jonni Dapp', birthday=date(1982, 4, 23), is_active=True)
    richard_harris = Actor(name='Richard Harris', birthday=date(1955, 7, 3), is_active=False)
    michael_gam = Actor(name='Michael Gam', birthday=date(1943, 1, 13), is_active=False)

    mafia_2.actors = [daniel_radcliffe, cuintinn_tarantino]
    interstellar.actors = [michael_gam, richard_harris]
    spider_man.actors = [jonni_depp, berdd_pitt, michael_gam]
    haski.actors = [cuintinn_tarantino, jonni_depp]
    hacker.actors = [michael_gam, berdd_pitt]
    warm.actors = [berdd_pitt, jonni_depp, daniel_radcliffe]

    db.session.add(mafia_2)
    db.session.add(interstellar)
    db.session.add(spider_man)
    db.session.add(haski)
    db.session.add(hacker)
    db.session.add(warm)

    db.session.add(daniel_radcliffe)
    db.session.add(cuintinn_tarantino)
    db.session.add(berdd_pitt)
    db.session.add(jonni_depp)
    db.session.add(richard_harris)
    db.session.add(michael_gam)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_films()
    print('Successfully populated!')