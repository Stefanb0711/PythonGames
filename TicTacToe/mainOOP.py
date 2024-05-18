import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from TicTacToe import TicTacToe, Session, Spielstand
import random


"""engine = create_engine('sqlite:///spielstand.db', echo=False)

# Erstelle eine "Base" Klasse als Basis für ORM-Modelle
Base = sqlalchemy.orm.declarative_base()

class Spielstand(Base):
    __tablename__ = "spielstand"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    spieler_x = Column(Integer)
    spieler_0 = Column(Integer)



Base.metadata.create_all(engine)

# Erstelle eine Session-Fabrik
Session = sessionmaker(bind=engine)
session = Session()"""

session = Session()

aktueller_spielstand = session.query(Spielstand).filter(Spielstand.id == 1).first()
if not aktueller_spielstand:
    spielstand_erstellen = Spielstand(spieler_x=0, spieler_0=0)
    session.add(spielstand_erstellen)
    session.commit()


aktueller_spielstand.spieler_x = 0
aktueller_spielstand.spieler_0 = 0
session.commit()



tic_tac_toe = TicTacToe()
#aktueller_spielstand = session.query(Spielstand).filter(Spielstand.id == 1).first()

#print(f"Aktueller Spielstand: \n Spieler X: {aktueller_spielstand.spieler_x} Spieler 0: {aktueller_spielstand.spieler_0}")

aktueller_spieler = random.choice(["X", "0"])

while True:
    if aktueller_spieler == "X":
        tic_tac_toe.benutzereingabe_und_feld_setzen("X")
        tic_tac_toe.display_board()
        tic_tac_toe.checken_sieg("X")
        aktueller_spieler = "0"

        if tic_tac_toe.gewonnen_x:
            #aktueller_spielstand.spieler_x += 1
            #session.commit()
            tic_tac_toe.spielstand(aktueller_spielstand)

            continue
    else:
        tic_tac_toe.benutzereingabe_und_feld_setzen("0")
        tic_tac_toe.display_board()
        tic_tac_toe.checken_sieg("0")
        aktueller_spieler = "X"

        if tic_tac_toe.gewonnen_0:
            tic_tac_toe.spielstand(aktueller_spielstand)
            continue

"""
tic_tac_toe.spieler_x_eingabe = input("Spieler 0: Geben Sie eine Zahl von 1 - 9 ein: ")

    if not tic_tac_toe.spieler_0_eingabe.isdigit():
        print("Der eingegebene Wert ist nicht gültig. Versuchen Sie es nochmal")
        continue
    elif int(tic_tac_toe.spieler_0_eingabe) > 9 or int(tic_tac_toe.spieler_0_eingabe) < 1:
        print("Der eingegebene Wert ist nicht gültig")
        continue

    tic_tac_toe.checken_sieg("0")
"""


