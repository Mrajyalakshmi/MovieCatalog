"""Data for Movies."""
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Movie, engine


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# User functions
def create_user(name, email, picture):
    """Create User."""
    new_user = User(
        name=name,
        email=email,
        picture=picture
        )
    session.add(new_user)
    session.commit()
    return new_user.id


def get_user(user_id):
    """Get User."""
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    """Get User."""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# Genre functions


def create_genre(name):
    """create genre."""
    new_genre = Genre(name=name)
    session.add(new_genre)
    session.commit()
    return new_genre.id


def get_genre_id(name):
    """Genre ID."""
    genre = session.query(Genre).filter_by(name=name).first()
    return genre.id


def get_movie(genre_name):
    """Get Movies."""
    movies_list = session.query(Movie).join(
              Movie.genre).filter_by(name=genre_name)
    return movies_list


# Movie functions
def create_movies(name, description, picture, genre_id, user_id):
    """Create Movies."""
    new_movie = Movie(
        name=name,
        description=description,
        picture=picture,
        genre_id=genre_id,
        user_id=user_id
        )
    session.add(new_movie)
    session.commit()
    return new_movie.id


# set up functions:

def add_users():
    """Add users.""".
    user_list = [
        ['Raji M', 'raji.m@gmail.com', 'http://picture_url.com']
    ]

    for user in user_list:
        create_user(user[0], user[1], user[2])

# Default genres


def fill_genre():
    """Fill Genre."""
    genre_list = [
        'Action',
        'Comedy',
        'Education',
        'Fiction',
        'Horror',
        'Kids',
        'Science'
    ]

    for genre in genre_list:
        create_genre(genre)

# Inserting default movies into the database


def fill_movies():
    """Fill Movies."""
    movies = [
        (
            'Logan',
            'In the near future, a weary Logan cares'
            'for an ailing Professor X, somewhere on the Mexican border.',
            'https://goo.gl/NDHrkm',
            'Action'
            ),
        (
            'John Wick',
            'After returning to the criminal'
            'underworld to repay a debt, John Wick ',
            'https://goo.gl/Y1PqUp',
            'Action'
            ),
        (
            'Cult of Chucky',
            'Chucky returns to terrorize his human'
            'victim, Nica.',
            'https://i.ytimg.com/vi/NUH4AV7MQRc/movieposter.jpg',
            'Horror'
            ),
        (
            'Annable:Creation',
            '12 years after the tragic death of '
            'their little girl, a dollmaker and his wife.',
            'https://goo.gl/CmcEJc',
            'Horror'
            ),
        (
            'Bay Watch',
            'Devoted lifeguard Mitch Buchannon butts heads with a brash new.',
            'https://goo.gl/73SuDn',
            'Comedy'
            ),
        (
            'The Big Sick',
            'Pakistan-born comedian Kumail Nanjiani and'
            'grad student Emily Gardner fall in love.',
            'https://goo.gl/A881mS',
            'Comedy'
            ),
        (
            'Jumanji',
            'Four teenagers are sucked into a magical video'
            'game, and the only way they finish game.',
            'https://goo.gl/r8NS2H',
            'Fiction'
            ),
        (
            'Beauty and the Beast',
            'An adaptation of the fairy tale about a'
            'monstrous-looking prince and woman in love.',
            'https://goo.gl/pmMLZa',
            'Fiction'
            ),
        (
            'Justice League',
            'Fueled by his restored faith in humanity and'
            'inspired by Superman\'s selfless act.',
            'https://goo.gl/VV5KSa',
            'Action'
            ),
        (
            'Wonder Woman',
            'When a pilot crashes and tells of conflict'
            'in the outside world, Diana.',
            'https://goo.gl/2bJjes',
            'Action'
            ),
        (
            'Transformers: The Last Knight',
            'a Spielberg-inspired, boy-and-his-car adventure starring'
            'Shia LaBeouf and 8 bazillion CG pixels.',
            'https://goo.gl/ak8R2t',
            'Science'
            ),
        (
            'Guardians of the Galaxy  Vol. 2',
            'tar-Lord, Gamora, Drax, Rocket Raccoon, and Baby Groot needed'
            'to come to life and become more.',
            'https://goo.gl/qmufUx',
            'Science'
            ),
        (
            'Dead Poets Society',
            'A teacher who inspires his students to challenge'
            'the norm through his teaching of poetry.',
            'https://goo.gl/k2Nx9o',
            'Education'
            ),
        (
            'School Ties',
            'A movie set in the 1950 that deals with'
            'anti-Semitism and can easily be applied to'
            'discrimination of all types.',
            'https://goo.gl/S1pKhx',
            'Education'
            ),
        (
            'Boss Baby',
            'A suit-wearing, briefcase-carrying baby pairs up with'
            'his 7-year old brother to stop the dastardly.',
            'https://goo.gl/isSXUz',
            'Kids'
            ),
        (
            'Coco',
            'Aspiring musician Miguel, confronted with his family\'s'
            'ancestral ban on music, enters the Land of the Dead.',
            'https://goo.gl/jkP6Yr',
            'Kids'
            )
    ]

    for m in movies:
        create_movies(m[0], m[1], m[2], get_genre_id(m[3]), 1)


if __name__ == '__main__':
    add_users()
    fill_genre()
    fill_movies()
