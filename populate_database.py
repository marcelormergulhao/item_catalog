from app.models import Category, CatalogItem, Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# If we find records in the database we don't need to populate it again
test = session.query(Category).count()

if test == 0:
    # Create categories - sports
    c = Category(id=1, name="American Football", description="American Football description", picture="american-football-1.png")
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

    c15 = Category(id=15, name="Hockey", description="Hockey description", picture="hockey-1.png")
    session.add(c15)
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

    c24 = Category(id=24, name="Surf", description="Surf description", picture="surf-1.png")
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

    c29 = Category(id=29, name="Golf", description="Golf description", picture="golf-1.png")
    session.add(c29)
    session.commit()

    # Sport Items

    i = CatalogItem(id=1, name="Goalpost", description="Goal post", picture="goal-post.png", category=c)
    session.add(i)
    session.commit()

    i2 = CatalogItem(id=2, name="Ball", description="Ball", picture="american-football.png", category=c)
    session.add(i2)
    session.commit()

    i3 = CatalogItem(id=3, name="Bow", description="Bow", picture="bow.png", category=c2)
    session.add(i3)
    session.commit()

    i4 = CatalogItem(id=4, name="Arrow", description="Arrow", picture="arrow.png", category=c2)
    session.add(i4)
    session.commit()

    i5 = CatalogItem(id=5, name="Ball", description="Ball", picture="baseball-1.png", category=c5)
    session.add(i5)
    session.commit()

    i6 = CatalogItem(id=6, name="Gloves", description="Gloves", picture="baseball-2.png", category=c5)
    session.add(i6)
    session.commit()

    i7 = CatalogItem(id=7, name="Ball", description="Ball", picture="basketball-1.png", category=c6)
    session.add(i7)
    session.commit()

    i8 = CatalogItem(id=8, name="Jersey", description="Jersey", picture="basketball-jersey.png", category=c6)
    session.add(i8)
    session.commit()

    i9 = CatalogItem(id=9, name="Court", description="Court", picture="basketball-court.png", category=c6)
    session.add(i9)
    session.commit()

    i10 = CatalogItem(id=10, name="Bicycle", description="Bicycle", picture="bicycle.png", category=c7)
    session.add(i10)
    session.commit()

    i11 = CatalogItem(id=11, name="Boot", description="Boot", picture="boot.png", category=c7)
    session.add(i11)
    session.commit()

    i12 = CatalogItem(id=12, name="Bottle", description="Bottle", picture="bottle.png", category=c7)
    session.add(i12)
    session.commit()

    i13 = CatalogItem(id=13, name="Ball", description="Ball", picture="bowling-1.png", category=c8)
    session.add(i13)
    session.commit()

    i14 = CatalogItem(id=14, name="Gloves", description="Gloves", picture="boxing-1.png", category=c9)
    session.add(i14)
    session.commit()

    i15 = CatalogItem(id=15, name="Boxing Ring", description="Boxing Ring", picture="boxing-ring-1.png", category=c9)
    session.add(i15)
    session.commit()

    i16 = CatalogItem(id=16, name="Shorts", description="Shorts", picture="boxing-shorts.png", category=c9)
    session.add(i16)
    session.commit()

    i17 = CatalogItem(id=17, name="Field", description="Football field", picture="football-pitch.png", category=c)
    session.add(i17)
    session.commit()

    i18 = CatalogItem(id=18, name="Jersey", description="Football Jersey", picture="football-jersey.png", category=c)
    session.add(i18)
    session.commit()

    i19 = CatalogItem(id=19, name="Field", description="Soccer field", picture="football-field.png", category=c23)
    session.add(i19)
    session.commit()

    i20 = CatalogItem(id=20, name="Gloves", description="Soccer gloves", picture="glove.png", category=c23)
    session.add(i20)
    session.commit()

    i21 = CatalogItem(id=21, name="Ball", description="Golf ball", picture="golf.png", category=c29)
    session.add(i21)
    session.commit()

    i22 = CatalogItem(id=22, name="Club", description="Hockey club", picture="hockey.png", category=c29)
    session.add(i22)
    session.commit()

    i23 = CatalogItem(id=23, name="Ice skates", description="Ice skates", picture="ice-skating.png", category=c29)
    session.add(i23)
    session.commit()

    i24 = CatalogItem(id=24, name="Punching bag", description="Punching bag", picture="punch.png", category=c9)
    session.add(i24)
    session.commit()

    i25 = CatalogItem(id=25, name="Helmet", description="Racing Helmet", picture="racing-helmet.png", category=c20)
    session.add(i25)
    session.commit()

    i26 = CatalogItem(id=26, name="Ball", description="Soccer ball", picture="soccer-1.png", category=c23)
    session.add(i26)
    session.commit()

    i27 = CatalogItem(id=27, name="Jersey", description="Soccer jersey", picture="soccer-jersey.png", category=c23)
    session.add(i27)
    session.commit()

    i28 = CatalogItem(id=28, name="Steering Wheel", description="Steering Wheel", picture="steering-wheel.png", category=c20)
    session.add(i28)
    session.commit()

    i29 = CatalogItem(id=29, name="Surfboard", description="Surfboard", picture="surf.png", category=c24)
    session.add(i29)
    session.commit()

    i30 = CatalogItem(id=30, name="Target", description="Target", picture="target.png", category=c2)
    session.add(i30)
    session.commit()

    i31 = CatalogItem(id=31, name="Ball", description="Tennis ball", picture="tennis-ball.png", category=c25)
    session.add(i31)
    session.commit()

    i32 = CatalogItem(id=32, name="Court", description="Tennis court", picture="tennis-court.png", category=c25)
    session.add(i32)
    session.commit()

    i33 = CatalogItem(id=33, name="Goggles", description="Goggles", picture="goggles.png", category=c27)
    session.add(i33)
    session.commit()

    i34 = CatalogItem(id=34, name="Whistle", description="Whistle", picture="whistle.png", category=c23)
    session.add(i34)
    session.commit()

    i35 = CatalogItem(id=35, name="World Cup", description="World Cup", picture="world-cup.png", category=c23)
    session.add(i35)
    session.commit()

session.close()
