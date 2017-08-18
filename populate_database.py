from app.models import Category, CatalogItem, Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create categories - sports
c = Category(id=1, name="American Football", description="American Football description", picture="american-football.png")
session.add(c)
session.commit()

c2 = Category(id=2, name="Archery", description="Archery description", picture="archery.png")
session.add(c2)
session.commit()

c3 = Category(id=3, name="Badminton", description="American Football description", picture="badminton.png")
session.add(c3)
session.commit()

c4 = Category(id=4, name="Ballet", description="Ballet description", picture="ballet.png")
session.add(c4)
session.commit()

c5 = Category(id=5, name="Baseball", description="Baseball description", picture="baseball.png")
session.add(c5)
session.commit()

c6 = Category(id=6, name="Basketball", description="Basketball description", picture="basketball.png")
session.add(c6)
session.commit()

c8 = Category(id=8, name="Bowling", description="Bowling description", picture="bowling.png")
session.add(c8)
session.commit()

c9 = Category(id=9, name="Boxing", description="Boxing description", picture="boxing.png")
session.add(c9)
session.commit()

c10 = Category(id=10, name="Chess", description="Chess description", picture="chess.png")
session.add(c10)
session.commit()

c11 = Category(id=11, name="Cricket", description="Cricket description", picture="cricket.png")
session.add(c11)
session.commit()

c12 = Category(id=12, name="Curling", description="Curling description", picture="curling.png")
session.add(c12)
session.commit()

c7 = Category(id=7, name="Cycling", description="Cycling description", picture="cycling.png")
session.add(c7)
session.commit()

c13 = Category(id=13, name="Fishing", description="Fishing description", picture="fishing.png")
session.add(c13)
session.commit()

c14 = Category(id=14, name="Hiking", description="Hiking description", picture="hiking.png")
session.add(c14)
session.commit()

c15 = Category(id=15, name="Hockey", description="Hockey description", picture="hockey.png")
session.add(c15)
session.commit()

c16 = Category(id=16, name="Ice Skating", description="Ice skating description", picture="ice-skating.png")
session.add(c16)
session.commit()

c17 = Category(id=17, name="Karate", description="Karate description", picture="karate.png")
session.add(c17)
session.commit()

c18 = Category(id=18, name="Lacrosse", description="Lacrosse description", picture="lacrosse.png")
session.add(c18)
session.commit()

c19 = Category(id=19, name="Ping Pong", description="Ping Pong description", picture="ping-pong.png")
session.add(c19)
session.commit()

c20 = Category(id=20, name="Racing", description="Racing description", picture="racing.png")
session.add(c20)
session.commit()

c21 = Category(id=21, name="Rugby", description="Rugby description", picture="rugby.png")
session.add(c21)
session.commit()

c22 = Category(id=22, name="Skating", description="Skating description", picture="skateboard.png")
session.add(c22)
session.commit()

c23 = Category(id=23, name="Soccer", description="Soccer description", picture="soccer.png")
session.add(c23)
session.commit()

c24 = Category(id=24, name="Surf", description="Surf description", picture="surf.png")
session.add(c24)
session.commit()

c25 = Category(id=25, name="Tennis", description="Tennis description", picture="tennis.png")
session.add(c25)
session.commit()

c26 = Category(id=26, name="Volleyball", description="Volleyball description", picture="volleyball.png")
session.add(c26)
session.commit()

c27 = Category(id=27, name="Water Polo", description="Water polo description", picture="waterpolo.png")
session.add(c27)
session.commit()

c28 = Category(id=28, name="Yoga", description="Yoga description", picture="yoga.png")
session.add(c28)
session.commit()

# Sport Items

i = CatalogItem(id=1, name="Goalpost", description="Goal post", picture="goalpost.png", category=c)
session.add(i)
session.commit()

i2 = CatalogItem(id=2, name="Ball", description="Ball", picture="ball.png", category=c)
session.add(i2)
session.commit()

i3 = CatalogItem(id=3, name="Bow", description="Bow", picture="bow.png", category=c2)
session.add(i3)
session.commit()

i4 = CatalogItem(id=4, name="Arrow", description="Arrow", picture="arrow.png", category=c2)
session.add(i4)
session.commit()

session.close()
