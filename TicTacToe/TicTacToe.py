import numpy as np
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///spielstand.db', echo=False)

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
session = Session()


class TicTacToe:
    def __init__(self):
        self.spieler_x_eingabe = ""
        self.spieler_0_eingabe = ""
        self.spielstand_x = 0
        self.spielstand_0 = 0
        self.spiel_zu_ende = False
        self.gewonnen_x = False
        self.gewonnen_0 = False
        self.pos = np.array([["1","2","3"], ["4","5","6"], ["7","8","9"]])


    def checken_sieg(self, spieler):
        for zeile in self.pos:
            reihe_voll = np.all(zeile == spieler)

            if reihe_voll == True:
                print(f"{spieler} hat gewonnen")
                if spieler == "X":
                    self.gewonnen_x = True
                    self.spiel_zu_ende = True

                    break
                elif spieler == "0":
                    self.gewonnen_0 = True
                    self.spiel_zu_ende = True

        # Vertikal checken
        for werte in range(3):
            vertikal_werte = self.pos[:, werte]
            reihe_voll = np.all(vertikal_werte == spieler)

            if reihe_voll:
                print(f"{spieler} hat gewonnen")
                if spieler == "X":
                    self.gewonnen_x = True
                    self.spiel_zu_ende = True
                    break
                elif spieler == "0":
                    self.gewonnen_0 = True
                    self.spiel_zu_ende = True



        # Diagonal checken
        for wert in range(3):
            if not self.pos[wert][wert] == spieler:
                break
            else:
                if wert == 2:
                    print(f"{spieler} hat gewonnen")
                    if spieler == "X":
                        self.gewonnen_x = True
                        self.spiel_zu_ende = True
                        break
                    elif spieler == "0":
                        self.gewonnen_0 = True
                        self.spiel_zu_ende = True

        if self.spiel_zu_ende:
            self.pos = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
            self.spiel_zu_ende =False


    def display_board(self):
        tic_tac_toe_bord = f"{self.pos[0][0]} | {self.pos[0][1]} | {self.pos[0][2]} \n" \
                           f"---------\n" \
                           f"{self.pos[1][0]} | {self.pos[1][1]} | {self.pos[1][2]} \n" \
                           f"---------\n" \
                           f"{self.pos[2][0]} | {self.pos[2][1]} | {self.pos[2][2]} \n "
        print(tic_tac_toe_bord)


    def spielstand(self, aktueller_spielstand):

        if self.gewonnen_x:

            self.gewonnen_x = False
            aktueller_spielstand.spieler_x += 1
            session.commit()
            """elf.spielstand_x += 1
            with open("gespeicherter_spielstand.txt", "a") as datei:
                datei.write("")"""

            print(f"Spielstand: \n X = {aktueller_spielstand.spieler_x}\n Y = {aktueller_spielstand.spieler_0}")
        elif self.gewonnen_0:
            self.gewonnen_0 = False
            aktueller_spielstand.spieler_0 += 1
            session.commit()
            print(f"Spielstand: \n X = {aktueller_spielstand.spieler_x}\n Y = {aktueller_spielstand.spieler_0}")



    def benutzereingabe_und_feld_setzen(self, spieler):
        if spieler == "X":
            self.spieler_x_eingabe = input("Spieler X: Geben Sie eine Zahl von 1 - 9 ein:")
            if not self.spieler_x_eingabe.isdigit():
                print("Der eingegebene Wert ist nicht gültig. Versuchen Sie es nochmal")
                #continue
            elif int(self.spieler_x_eingabe) > 9 or int(self.spieler_x_eingabe) < 1:
                print("Der eingegebene Wert ist nicht gültig")
                #continue
            spieler_x_position = np.where(self.pos == self.spieler_x_eingabe)
            self.pos[spieler_x_position] = "X"

        elif spieler == "0":
            self.spieler_0_eingabe = input("Spieler 0: Geben Sie eine Zahl von 1 - 9 ein:")
            if not self.spieler_0_eingabe.isdigit():
                print("Der eingegebene Wert ist nicht gültig. Versuchen Sie es nochmal")
                #continue
            elif int(self.spieler_0_eingabe) > 9 or int(self.spieler_0_eingabe) < 1:
                print("Der eingegebene Wert ist nicht gültig")
                #continue

            spieler_0_position = np.where(self.pos == self.spieler_0_eingabe)
            self.pos[spieler_0_position] = "0"