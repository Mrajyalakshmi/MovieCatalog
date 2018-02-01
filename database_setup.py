"""Database Setup for Movie Catalog."""
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import asc, desc


Base = declarative_base()

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# User functions
def create_user(login_session):
    """Create users."""
    new_user = User(
        name=login_session['username'],
        email=login_session['email'],
        picture=login_session['picture']
        )

    session.add(new_user)
    session.commit()
    return new_user.id


def get_user(user_id):
    """Return users."""
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    """Return user id."""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


class User(Base):
    """Create user class."""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(250))
    picture = Column(String)


# Genre functions
def create_genre(name):
    """Create genre."""
    new_genre = Genre(name=name)
    session.add(new_genre)
    session.commit()
    return new_genre.id


def get_genre(genre_id):
    """Get Genre."""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    return genre


def get_genre_id(name):
    """Get Genre Name."""
    genre = session.query(Genre).filter_by(name=name).one()
    return genre.id


def get_movie(genre_id):
    """Get movie list."""
    movies_list = session.query(Movie).filter_by(genre_id=genre_id).all()
    return movies_list


def get_all_genre():
    """Get all genres."""
    genres = session.query(Genre).order_by(asc(Genre.name))
    return genres


class Genre(Base):
    """Create class genre."""

    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id': self.id,
            'name': self.name
        }


def create_movies(name, description, picture, genre_id, user_id):
    """Movie functions."""
    new_movie = Movie(
        name=name,
        description=description,
        picture=picture,
        genre_id=genre_id,
        user_id=user_id
        )
    session.add(new_movie)
    session.commit()
    return new_movie


def get_movie(movie_id):
    """Return all movies."""
    movie = session.query(Movie).filter_by(id=movie_id).one_or_none()
    return movie


def delete_movie(movie):
    """Delete movies."""
    session.delete(movie)
    session.commit()


def edit_movie(movie, name, description, genre_id):
    """Edit Movie."""
    movie.name = name
    movie.description = description
    movie.genre_id = genre_id
    session.add(movie)
    session.commit()
    return movie


class Movie(Base):
    """Create class movie."""

    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text)
    picture = Column(String(250))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'picture': self.picture,
            'genre': self.genre.name
        }


if __name__ == '__main__':
    Base.metadata.create_all(engine)
