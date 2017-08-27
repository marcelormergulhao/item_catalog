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
    c = Category(id=1, name="American Football", description="American football, referred to as football in the United States and Canada, and also known as 'gridiron football' or simply 'gridiron', is a sport played by two teams of eleven players on a rectangular field with goalposts at each end. The offense, the team with control of the oval-shaped football, attempts to advance down the field by running with or passing the ball, while the team without control of the ball, the defense, aims to stop their advance and take control of the ball for themselves. The offense must advance at least ten yards in four downs, or plays, or else they turn over the football to the opposing team; if they succeed, they are given a new set of four downs. Points are primarily scored by advancing the ball into the opposing team's end zone for a touchdown or kicking the ball through the opponent's goalposts for a field goal. The team with the most points at the end of a game wins.", picture="american-football-1.png")
    session.add(c)
    session.commit()

    c2 = Category(id=2, name="Archery", description="Archery is the sport, practice or skill of using a bow to propel arrows. The word comes from the Latin arcus. Historically, archery has been used for hunting and combat. In modern times, it is mainly a competitive sport and recreational activity. A person who participates in archery is typically called an archer or a bowman, and a person who is fond of or an expert at archery is sometimes called a toxophilite.", picture="archery.png")
    session.add(c2)
    session.commit()

    c3 = Category(id=3, name="Badminton", description="Badminton is a racquet sport played using racquets to hit a shuttlecock across a net. Although it may be played with larger teams, the most common forms of the game are 'singles' (with one player per side) and 'doubles' (with two players per side). Badminton is often played as a casual outdoor activity in a yard or on a beach; formal games are played on a rectangular indoor court. Points are scored by striking the shuttlecock with the racquet and landing it within the opposing side's half of the court.", picture="badminton.png")
    session.add(c3)
    session.commit()

    c4 = Category(id=4, name="Ballet", description="Ballet /ˈbæleɪ/ (French: [balɛ]) is a type of performance dance that originated in the Italian Renaissance courts of the 15th century and later developed into a concert dance form in France and Russia. It has since become a widespread, highly technical form of dance with its own vocabulary based on French terminology. It has been globally influential and has defined the foundational techniques used in many other dance genres. Ballet has been taught in various schools around the world, which have historically incorporated their own cultures to evolve the art.", picture="ballet.png")
    session.add(c4)
    session.commit()

    c5 = Category(id=5, name="Baseball", description="Baseball is a bat-and-ball game played between two teams of nine players each, who take turns batting and fielding. The batting team attempts to score runs by hitting a ball that is thrown by the opposing team's pitcher with a bat swung by the batter, then running counter-clockwise around a series of four bases: first, second, third, and home plate. A run is scored when a player advances around the bases and returns to home plate.", picture="baseball.png")
    session.add(c5)
    session.commit()

    c6 = Category(id=6, name="Basketball", description="Basketball is a non-contact sport played on a rectangular court. While most often played as a team sport with five players on each side, three-on-three, two-on-two, and one-on-one competitions are also common. The objective is to shoot a ball through a hoop 18 inches (46 cm) in diameter and 10 feet (3.048 m) high that is mounted to a backboard at each end of the court. The game was invented in 1891 by Dr. James Naismith, who would be the first basketball coach of the Kansas Jayhawks, one of the most successful programs in the game's history.", picture="basketball.png")
    session.add(c6)
    session.commit()

    c8 = Category(id=8, name="Bowling", description="Bowling refers to a series of sports or leisure activities in which a player rolls or throws a bowling ball towards a target. It is one of the major forms of throwing sports. In pin bowling variations, the target is usually to knock over pins at the end of a lane. When all the pins are knocked down on the first roll, this is a strike. In target variations, the aim is usually to get the ball as close to a mark as possible. The pin version of bowling is often played on a flat wooden or other synthetic surface (which can be oiled in different patterns for different techniques),[1] while in target bowling, the surface may be grass, gravel or a synthetic surface.", picture="bowling.png")
    session.add(c8)
    session.commit()

    c9 = Category(id=9, name="Boxing", description="Boxing is a combat sport in which two people, usually wearing protective gloves, throw punches at each other for a predetermined set of time in a boxing ring.", picture="boxing.png")
    session.add(c9)
    session.commit()

    c10 = Category(id=10, name="Chess", description="Chess is a two-player strategy board game played on a chessboard, a checkered gameboard with 64 squares arranged in an 8×8 grid.[1] The game is played by millions of people worldwide.", picture="chess.png")
    session.add(c10)
    session.commit()

    c11 = Category(id=11, name="Cricket", description="Cricket is a bat-and-ball game played between two teams of eleven players each on a cricket field, at the centre of which is a rectangular 22-yard-long pitch with a target called the wicket (a set of three wooden stumps topped by two bails) at each end. Each phase of play is called an innings during which one team bats, attempting to score as many runs as possible, whilst their opponents field. Depending on the type of match, the teams have one or two innings apiece and, when the first innings ends, the teams swap roles for the next innings. Except in matches which result in a draw, the winning team is the one that scores the most runs, including any extras gained.", picture="cricket.png")
    session.add(c11)
    session.commit()

    c12 = Category(id=12, name="Curling", description="Curling is a sport in which players slide stones on a sheet of ice towards a target area which is segmented into four concentric circles. It is related to bowls, boules and shuffleboard. Two teams, each with four players, take turns sliding heavy, polished granite stones, also called rocks, across the ice curling sheet towards the house, a circular target marked on the ice.[2] Each team has eight stones. The purpose is to accumulate the highest score for a game; points are scored for the stones resting closest to the centre of the house at the conclusion of each end, which is completed when both teams have thrown all of their stones. A game usually consists of eight or ten ends.", picture="curling.png")
    session.add(c12)
    session.commit()

    c7 = Category(id=7, name="Cycling", description="Cycling, also called bicycling or biking, is the use of bicycles for transport, recreation, exercise or sport.[1] Persons engaged in cycling are referred to as 'cyclists',[2] 'bikers',[3] or less commonly, as 'bicyclists'.[4] Apart from two-wheeled bicycles, 'cycling' also includes the riding of unicycles, tricycles, quadracycles, recumbent and similar human-powered vehicles (HPVs).", picture="cycling.png")
    session.add(c7)
    session.commit()

    c13 = Category(id=13, name="Fishing", description="Fishing is the activity of trying to catch fish. Fish are normally caught in the wild. Techniques for catching fish include hand gathering, spearing, netting, angling and trapping. Fishing may include catching aquatic animals other than fish, such as molluscs, cephalopods, crustaceans, and echinoderms. The term is not normally applied to catching farmed fish, or to aquatic mammals, such as whales where the term whaling is more appropriate.", picture="fishing.png")
    session.add(c13)
    session.commit()

    c14 = Category(id=14, name="Hiking", description="Hiking is the preferred term, in Canada and the United States, for a long, vigorous walk, usually on trails (footpaths), in the countryside, while the word walking is used for shorter, particularly urban walks. On the other hand, in the United Kingdom, and the Republic of Ireland, the word 'walking' is acceptable to describe all forms of walking, whether it is a walk in the park or backpacking in the Alps. The word hiking is also often used in the UK, along with rambling (a slightly old-fashioned term), hillwalking, and fell walking (a term mostly used for hillwalking in northern England). The term 'bushwalking' is endemic to Australia, having been adopted by the Sydney Bush Walkers club in 1927.[1] In New Zealand a long, vigorous walk or hike is called tramping.[2] It is a popular activity with numerous hiking organizations worldwide, and studies suggest that all forms of walking have health benefits.", picture="hiking.png")
    session.add(c14)
    session.commit()

    c15 = Category(id=15, name="Hockey", description="Hockey is a sport in which two teams play against each other by trying to maneuver a ball or a puck into the opponent's goal using a hockey stick. There are many types of hockey such as bandy, field hockey and ice hockey.", picture="hockey-1.png")
    session.add(c15)
    session.commit()

    c17 = Category(id=17, name="Karate", description="Karate (空手) (English: /kəˈrɑːtiː/; Japanese pronunciation: [kaɾate] (About this sound listen); Okinawan pronunciation: Ryukyuan pronunciation: [kaɽati]) is a martial art developed in the Ryukyu Kingdom. It developed from the indigenous Ryukyuan martial arts (called te (手), 'hand'; tii in Okinawan) under the influence of Chinese martial arts, particularly Fujian White Crane.[1][2] Karate is now predominantly a striking art using punching, kicking, knee strikes, elbow strikes and open-hand techniques such as knife-hands, spear-hands, and palm-heel strikes. Historically, and in some modern styles, grappling, throws, joint locks, restraints, and vital-point strikes are also taught.[3] A karate practitioner is called a karateka (空手家).", picture="karate.png")
    session.add(c17)
    session.commit()

    c18 = Category(id=18, name="Lacrosse", description="Lacrosse is a team sport played between two teams using a long-handled stick called a crosse and a lacrosse ball. Players use the head of the lacrosse stick to carry (called cradling), pass, and catch the ball in order to score by shooting the ball into the opponent's goal.", picture="lacrosse.png")
    session.add(c18)
    session.commit()

    c19 = Category(id=19, name="Table Tennis", description="Table tennis, also known as ping pong, is a sport in which two or four players hit a lightweight ball back and forth across a table using a small bat. The game takes place on a hard table divided by a net. Except for the initial serve, the rules are generally as follows: players must allow a ball played toward them to bounce one time on their side of the table, and must return it so that it bounces on the opposite side at least once. A point is scored when a player fails to return the ball within the rules. Play is fast and demands quick reactions. Spinning the ball alters its trajectory and limits an opponent's options, giving the hitter a great advantage.", picture="ping-pong.png")
    session.add(c19)
    session.commit()

    c20 = Category(id=20, name="Auto Racing", description="Auto racing (also known as car racing, motor racing[1] or automobile racing) is a sport involving the racing of automobiles for competition.", picture="racing.png")
    session.add(c20)
    session.commit()

    c21 = Category(id=21, name="Rugby", description="Rugby is a game similar to football developed at Rugby School in Rugby, Warwickshire, one of many versions of football played at English public schools in the 19th century.[1] The two main types (known as codes) of rugby are rugby league and rugby union. Although rugby league initially used rugby union rules, they are now wholly separate sports.", picture="rugby.png")
    session.add(c21)
    session.commit()

    c22 = Category(id=22, name="Skating", description="Skating involves any sports or recreational activity which consists of traveling on surfaces or on ice using skates.", picture="skateboard.png")
    session.add(c22)
    session.commit()

    c23 = Category(id=23, name="Soccer", description="Association football, more commonly known as football or soccer,[a] is a team sport played between two teams of eleven players with a spherical ball. It is played by 250 million players in over 200 countries and dependencies, making it the world's most popular sport.[3][4][5][6] The game is played on a rectangular field with a goal at each end. The object of the game is to score by getting the ball into the opposing goal.", picture="soccer.png")
    session.add(c23)
    session.commit()

    c24 = Category(id=24, name="Surf", description="Surf is the wave activity in the area between the shoreline and outer limit of breakers. It may refer to a breaking wave in shallow water, upon the shore, or in the area in which waves break.", picture="surf-1.png")
    session.add(c24)
    session.commit()

    c25 = Category(id=25, name="Tennis", description="Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Each player uses a tennis racket that is strung with cord to strike a hollow rubber ball covered with felt over or around a net and into the opponent's court. The object of the game is to play the ball in such a way that the opponent is not able to play a valid return. The player who is unable to return the ball will not gain a point, while the opposite player will.", picture="tennis.png")
    session.add(c25)
    session.commit()

    c26 = Category(id=26, name="Volleyball", description="Volleyball is a team sport in which two teams of six players are separated by a net. Each team tries to score points by grounding a ball on the other team's court under organized rules.[1] It has been a part of the official program of the Summer Olympic Games since 1964.", picture="volleyball.png")
    session.add(c26)
    session.commit()

    c27 = Category(id=27, name="Water Polo", description="Water polo is a competitive team sport played in the water between two teams. The game consists of four quarters, in which the two teams attempt to score goals and throw the ball into their opponent's goal. The team with the most goals at the end of the game wins the match. Each team made up of six field players and one goalkeeper. Except for the goalkeeper, players participate in both offensive and defensive roles. Water polo is typically played in an all-deep pool seven feet (or two meters) deep.", picture="waterpolo.png")
    session.add(c27)
    session.commit()

    c28 = Category(id=28, name="Yoga", description="Yoga (/ˈjoʊɡə/;[1] Sanskrit, योगः Listen) is a group of physical, mental, and spiritual practices or disciplines which originated in ancient India. There is a broad variety of yoga schools, practices, and goals[2] in Hinduism, Buddhism, and Jainism.[3][4][5] Among the most well-known types of yoga are Hatha yoga and Rāja yoga.", picture="yoga.png")
    session.add(c28)
    session.commit()

    c29 = Category(id=29, name="Golf", description="Golf is a club and ball sport in which players use various clubs to hit balls into a series of holes on a course in as few strokes as possible.", picture="golf-1.png")
    session.add(c29)
    session.commit()

    # Sport Items

    i = CatalogItem(id=1, name="Goalpost", description="The crossbar of these posts is ten feet (3 meters) above the ground, with vertical uprights at the end of the crossbar 18 feet 6 inches (5.64 m) apart for professional and collegiate play and 23 feet 4 inches (7.11 m) apart for high school play.[62][63][64] The uprights extend vertically 35 feet on professional fields, a minimum of 10 yards on college fields, and a minimum of ten feet on high school fields. Goal posts are padded at the base, and orange ribbons are normally placed at the tip of each upright.", picture="goal-post.png", category=c)
    session.add(i)
    session.commit()

    i2 = CatalogItem(id=2, name="Ball", description="The football itself is an oval ball, similar to the balls used in rugby or Australian rules football.[65] At all levels of play, the football is inflated to  12 1⁄2 to  13 1⁄2 pounds per square inch (psi) and weighs 14 to 15 ounces (397 to 425 grams);[64][66][67] beyond that, the exact dimensions vary slightly. In professional play the ball has a long axis of 11 to  11 1⁄4 inches, a long circumference of 28 to  28 1⁄2 inches, and a short circumference of 21 to  21 1⁄4 inches,[68] while in college and high school play the ball has a long axis of  10 7⁄8 to  11 7⁄16 inches, a long circumference of  27 3⁄4 to  28 1⁄2 inches, and a short circumference of  20 3⁄4 to  21 1⁄4 inches.", picture="american-football.png", category=c)
    session.add(i2)
    session.commit()

    i3 = CatalogItem(id=3, name="Bow", description="While there is great variety in the construction details of bows (both historic and modern), all bows consist of a string attached to elastic limbs that store mechanical energy imparted by the user drawing the string. Bows may be broadly split into two categories: those drawn by pulling the string directly and those that use a mechanism to pull the string.", picture="bow.png", category=c2)
    session.add(i3)
    session.commit()

    i4 = CatalogItem(id=4, name="Arrow", description="The most common form of arrow consists of a shaft, with an arrowhead at the front end, and fletchings and a nock at the other end. Arrows across time and history have normally been carried in a container known as a quiver, which can take many different forms.", picture="arrow.png", category=c2)
    session.add(i4)
    session.commit()

    i5 = CatalogItem(id=5, name="Ball", description="A baseball is a ball used in the sport of the same name, baseball. The ball features a rubber or cork center, wrapped in yarn, and covered, in the words of the Official Baseball Rules 'with two strips of white horsehide or cowhide, tightly stitched together.' It is 9.00–9.25 inches (228.60–234.95 mm) in circumference, (2.86–2.94 in or 72.64–74.68 mm in diameter), and masses from 5.00 to 5.25 ounces (141.75 to 148.83 g).[1] The yarn or string used to wrap the baseball can be up to one mile (1.6 km) in length. Some are wrapped in a plastic-like covering", picture="baseball-1.png", category=c5)
    session.add(i5)
    session.commit()

    i6 = CatalogItem(id=6, name="Gloves", description="A baseball glove or mitt is a large leather glove worn by baseball players of the defending team, which assists players in catching and fielding balls hit by a batter or thrown by a teammate.", picture="baseball-2.png", category=c5)
    session.add(i6)
    session.commit()

    i7 = CatalogItem(id=7, name="Ball", description="A basketball is a spherical inflated ball used in basketball games. Basketballs typically range in size from very small promotional items only a few inches in diameter to extra large balls nearly a foot in diameter used in training exercises. For example, a basketball in high school would be about 27 inches in circumference, while an NBA ball would be about 29 inches. The actual standard size of a basketball in the NBA is 29.5 inches in circumference.", picture="basketball-1.png", category=c6)
    session.add(i7)
    session.commit()

    i8 = CatalogItem(id=8, name="Jersey", description="A jersey is an item of knitted clothing, traditionally in wool or cotton, with sleeves, worn as a pullover, as it does not open at the front, unlike a cardigan. It is usually close-fitting and machine knitted in contrast to a guernsey that is more often hand knit with a thicker yarn. The word is usually used interchangeably with sweater.", picture="basketball-jersey.png", category=c6)
    session.add(i8)
    session.commit()

    i9 = CatalogItem(id=9, name="Court", description="In basketball, the basketball court is the playing surface, consisting of a rectangular floor with tiles at either end. In professional or organized basketball, especially when played indoors, it is usually made out of a wood, often maple, and highly polished. Outdoor surfaces are generally made from standard paving materials such as concrete or asphalt.", picture="basketball-court.png", category=c6)
    session.add(i9)
    session.commit()

    i10 = CatalogItem(id=10, name="Bicycle", description="A bicycle, also called a cycle or bike, is a human-powered, pedal-driven, single-track vehicle, having two wheels attached to a frame, one behind the other. A bicycle rider is called a cyclist, or bicyclist.", picture="bicycle.png", category=c7)
    session.add(i10)
    session.commit()

    i11 = CatalogItem(id=11, name="Cycling Shoe", description="Cycling shoes are shoes purpose-built for cycling. There are a variety of designs depending on the type and intensity of the cycling for which they are intended. Key features include rigidity, for more-efficient transfer of power from the cyclist to the pedals, weight, a method of attaching the shoe firmly to the pedal and adaptability for use on and off the bicycle. Most high-performance cycling shoes can be adjusted while in use, via a quick-adjusting system that has largely replaced laces.", picture="boot.png", category=c7)
    session.add(i11)
    session.commit()

    i12 = CatalogItem(id=12, name="Bottle", description="A water bottle is a container that is used to hold water, liquids or other beverages for consumption. The use of a water bottle allows an individual to transport, and drink, a beverage from one place to another.", picture="bottle.png", category=c7)
    session.add(i12)
    session.commit()

    i13 = CatalogItem(id=13, name="Ball", description="A bowling ball is a piece of sporting equipment used to hit bowling pins in the sport of bowling. Balls used in ten-pin bowling are typically hard spheres with three holes drilled in them, one each for the ring and middle fingers, and one for the thumb. Regulating bodies such as the USBC maintain requirements for the properties of bowling balls, including size, hardness, and number of holes, as well as maintaining a list of bowling balls approved for competitive play.[1] Other bowling balls, such as those used in five-pin bowling, candlepin bowling, and duckpin bowling are smaller, lighter, and without holes, so that they may be held in the palm of the bowler's hand. Most bowling alleys provide balls for patrons to use within the establishment, often referred to as 'house balls.'", picture="bowling-1.png", category=c8)
    session.add(i13)
    session.commit()

    i14 = CatalogItem(id=14, name="Gloves", description="Boxing gloves are cushioned gloves that fighters wear on their hands during boxing matches and practices. Unlike the ancient cestus which were designed as a weapon, modern boxing gloves are designed to protect the fighter's hand during a bout, though competitions, sparring and other forms of training have their own specialized gloves. Modern boxing gloves reduce superficial facial injuries; however, as modern boxing gloves give their user the ability to throw stronger punches to head without damaging the hands, they also increase the risk of brain damage for participants.", picture="boxing-1.png", category=c9)
    session.add(i14)
    session.commit()

    i15 = CatalogItem(id=15, name="Boxing Ring", description="A boxing ring is the space in which a boxing match occurs. A modern ring, which is set on a raised platform, is square with a post at each corner to which four parallel rows of ropes are attached with a turnbuckle. Unlike its cousin the wrestling ring, the ropes in a boxing ring are generally connected together between the posts.", picture="boxing-ring-1.png", category=c9)
    session.add(i15)
    session.commit()

    i16 = CatalogItem(id=16, name="Shorts", description="Boxer shorts (also known as loose boxers or as simply boxers) are a type of undergarment typically worn by men. The term has been used in English since 1944 for all-around-elastic shorts, so named after the shorts worn by boxers, for whom unhindered leg movement ('footwork') is very important. Boxers come in a variety of styles and design but are characterized by their loose fit.", picture="boxing-shorts.png", category=c9)
    session.add(i16)
    session.commit()

    i17 = CatalogItem(id=17, name="Field", description="Football games are played on a rectangular field that measures 120 yards (110 m) long and 53.33 yards (48.76 m) wide. Lines marked along the ends and sides of the field are known respectively as the end lines and sidelines, and goal lines are marked 10 yards (9.1 m) inward from each end line. Weighted pylons are placed on the inside corner of the intersections of the goal lines and end lines.", picture="football-pitch.png", category=c)
    session.add(i17)
    session.commit()

    i18 = CatalogItem(id=18, name="Jersey", description="A jersey is an item of knitted clothing, traditionally in wool or cotton, with sleeves, worn as a pullover, as it does not open at the front, unlike a cardigan. It is usually close-fitting and machine knitted in contrast to a guernsey that is more often hand knit with a thicker yarn. The word is usually used interchangeably with sweater.", picture="football-jersey.png", category=c)
    session.add(i18)
    session.commit()

    i19 = CatalogItem(id=19, name="Field", description="A football pitch (also known as a football field[1] or soccer field) is the playing surface for the game of association football. its dimensions and markings are defined by Law 1 of the Laws of the Game,.'The Field of Play'.[2] The surface can be either natural or artificial, but FIFA's Laws of the Game specify that all artificial surfaces must be painted green. The pitch is typically made of turf (grass) or artificial turf, although amateur and recreational teams often play on dirt fields.", picture="football-field.png", category=c23)
    session.add(i19)
    session.commit()

    i20 = CatalogItem(id=20, name="Gloves", description="Since the 1980s significant advancements have been made in the design of gloves, which now feature protectors to prevent the fingers bending backwards, segmentation to allow greater flexibility, and palms made of materials designed to protect the hand and to enhance a player's grip.[23] Gloves are available in a variety of different cuts, including 'flat palm', 'roll finger' and 'negative', with variations in the stitching and fit.", picture="glove.png", category=c23)
    session.add(i20)
    session.commit()

    i21 = CatalogItem(id=21, name="Ball", description="A golf ball is a special ball designed to be used in the game of golf. Under the rules of golf, a golf ball has a mass no more than 1.620 oz (45.93 grams), has a diameter not less than 1.680 in (42.67 mm), and performs within specified velocity, distance, and symmetry limits. Like golf clubs, golf balls are subject to testing and approval by the R&A (formerly part of the Royal and Ancient Golf Club of St Andrews) and the United States Golf Association, and those that do not conform with regulations may not be used in competitions (Rule 5–1).", picture="golf.png", category=c29)
    session.add(i21)
    session.commit()

    i22 = CatalogItem(id=22, name="Hockey Stick", description="A hockey stick is a piece of equipment used by the players in most forms of hockey to move the ball or puck.", picture="hockey.png", category=c15)
    session.add(i22)
    session.commit()

    i23 = CatalogItem(id=23, name="Ice skates", description="Ice skates are boots with blades attached to the bottom, used to propel the bearer across a sheet of ice while ice skating.", picture="ice-skating.png", category=c15)
    session.add(i23)
    session.commit()

    i24 = CatalogItem(id=24, name="Punching bag", description="A punching bag (or, British English, punchbag) is a sturdy bag designed to be repeatedly punched. A punching bag is usually cylindrical, and filled with various materials of corresponding hardness.", picture="punch.png", category=c9)
    session.add(i24)
    session.commit()

    i25 = CatalogItem(id=25, name="Helmet", description="A racing helmet is a form of protective headgear worn by racing car and rally drivers. Motor racing has long been known to be an exceptionally risky sport:[1] sudden deceleration forces on the head can easily occur if a racing car loses control at the very high speeds of competitive motor racing or the rough terrain experienced in rallying.[1] A risk more nearly unique to motor racing is the possibility of drastically severe burns from fuel igniting when the fuel lines or fuel tank of the vehicle are jolted sufficiently to dislodge or breach them in a situation in which the driver cannot soon enough escape from his car. This happened to world champion driver Niki Lauda at the 1976 German Grand Prix race at the Nürburgring in a crash from which he barely escaped alive.", picture="racing-helmet.png", category=c20)
    session.add(i25)
    session.commit()

    i26 = CatalogItem(id=26, name="Ball", description="A football, soccer ball, or association football ball is the ball used in the sport of association football. The name of the ball varies according to whether the sport is called 'football', 'soccer', or 'association football'. The ball's spherical shape, as well as its size, weight, and material composition, are specified by Law 2 of the Laws of the Game maintained by the International Football Association Board. Additional, more stringent, standards are specified by FIFA and subordinate governing bodies for the balls used in the competitions they sanction.", picture="soccer-1.png", category=c23)
    session.add(i26)
    session.commit()

    i27 = CatalogItem(id=27, name="Jersey", description="A jersey is an item of knitted clothing, traditionally in wool or cotton, with sleeves, worn as a pullover, as it does not open at the front, unlike a cardigan. It is usually close-fitting and machine knitted in contrast to a guernsey that is more often hand knit with a thicker yarn. The word is usually used interchangeably with sweater.", picture="soccer-jersey.png", category=c23)
    session.add(i27)
    session.commit()

    i28 = CatalogItem(id=28, name="Steering Wheel", description="A steering wheel (also called a driving wheel or a hand wheel) is a type of steering control in vehicles and vessels (ships and boats).", picture="steering-wheel.png", category=c20)
    session.add(i28)
    session.commit()

    i29 = CatalogItem(id=29, name="Surfboard", description="A surfboard is an elongated platform used in the sport of surfing. Surfboards are relatively light, but are strong enough to support an individual standing on them while riding an ocean surface wave breaking wave. They were invented in ancient Hawaii, where they were known as papa he'e nalu in the Hawaiian language, they were usually made of wood from local trees, such as koa, and were often over 15 feet (5 m) in length and extremely heavy.[1][2] Major advances over the years include the addition of one or more fins on the bottom rear of the board to improve directional stability, and numerous improvements in materials and shape.", picture="surf.png", category=c24)
    session.add(i29)
    session.commit()

    i30 = CatalogItem(id=30, name="Target", description="Targets are marked with 10 evenly spaced concentric rings, which have score values from 1 through 10 assigned to them. In addition, there is an inner 10 ring, sometimes called the X ring. This becomes the 10 ring at indoor compound competitions. Outdoors, it serves as a tiebreaker with the archer scoring the most X's winning. Archers score each end by summing the scores for their arrows. Line breakers, an arrow just touching a scoring boundary line, will be awarded the higher score.", picture="target.png", category=c2)
    session.add(i30)
    session.commit()

    i31 = CatalogItem(id=31, name="Ball", description="A tennis ball is a ball designed for the sport of tennis. Tennis balls are fluorescent yellow at major sporting events,[1][2] but in recreational play can be virtually any color. Tennis balls are covered in a fibrous felt which modifies their aerodynamic properties, and each has a white curvilinear oval covering it.", picture="tennis-ball.png", category=c25)
    session.add(i31)
    session.commit()

    i32 = CatalogItem(id=32, name="Court", description="A tennis court is the venue where the sport of tennis is played. It is a firm rectangular surface with a low net stretched across the center. The same surface can be used to play both doubles and singles matches. A variety of surfaces can be used to create a tennis court, each with its own characteristics which affect the playing style of the game.", picture="tennis-court.png", category=c25)
    session.add(i32)
    session.commit()

    i33 = CatalogItem(id=33, name="Goggles", description="Goggles, or safety glasses, are forms of protective eyewear that usually enclose or protect the area surrounding the eye in order to prevent particulates, water or chemicals from striking the eyes. They are used in chemistry laboratories and in woodworking. They are often used in snow sports as well, and in swimming. Goggles are often worn when using power tools such as drills or chainsaws to prevent flying particles from damaging the eyes. Many types of goggles are available as prescription goggles for those with vision problems.", picture="goggles.png", category=c27)
    session.add(i33)
    session.commit()

    i34 = CatalogItem(id=34, name="Whistle", description="A whistle is an instrument which produces sound from a stream of gas, most commonly air. It may be mouth-operated, or powered by air pressure, steam, or other means. Whistles vary in size from a small slide whistle or nose flute type to a large multi-piped church organ.", picture="whistle.png", category=c23)
    session.add(i34)
    session.commit()

    i35 = CatalogItem(id=35, name="World Cup", description="The FIFA World Cup, often simply called the World Cup, is an international association football competition contested by the senior men's national teams of the members of Fédération Internationale de Football Association (FIFA), the sport's global governing body. The championship has been awarded every four years since the inaugural tournament in 1930, except in 1942 and 1946 when it was not held because of the Second World War. The current champion is Germany, which won its fourth title at the 2014 tournament in Brazil.", picture="world-cup.png", category=c23)
    session.add(i35)
    session.commit()

session.close()
