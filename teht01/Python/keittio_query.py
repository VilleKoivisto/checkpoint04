"""
Database queries with Python, simple basics
"""

import psycopg2
from config import config


def lisaa_astiat(table, nimi, lkm):
    """
    Lisää astioita keittiöön (ilmeisesti joku Ikean valmispaketti)
    """

    con = None

    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        # huom. käytän taulun nimen ympärillä kaksoislainausmerkkejä, koska loin taulukon niillä
        # ilmeisesti sen takia taulun nimi on case sensitive ja vaatii siksi lainausmerkit myös kyseleyissä
        SQL = f'INSERT INTO "{table}" (nimi, lkm) VALUES (%s,%s);'
        insert_values = (nimi, lkm)
        
        cursor.execute(SQL, insert_values)
        con.commit()

        count = cursor.rowcount
        print(count, "Line inserted.")
        
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if con is not None:
            con.close()


def tulosta_astiat(table):
    """
    Tulosta kaikkia astiat
    """

    con = None

    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = f'SELECT * FROM "{table}";'
        
        cursor.execute(SQL)
        # replace with fetchone() for just one row
        # change return line too: fetchall() returns a list
        all_data = cursor.fetchall()
        
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if con is not None:
            con.close()
    
    return all_data


def main():
    """
    Huom lisää astiat vain jos taulu on tyhjä, muuten keittiössä on kohta ihan hulluna astioita.
    """

    # määritellään astiat sanakirjassa
    astiat = {"Muki": 100, "Lasi": 80, "Iso lautanen": 40, "Pieni lautanen": 40}

    # lisätään koko setti keittiöön
    for astia in astiat:
        lisaa_astiat('Astia', astia, astiat.get(astia))


    # tulostetaan astiat
    astia_lista = tulosta_astiat("Astia")
    
    for item in astia_lista:
        print(f"{item[1]}, {item[2]}kpl")


if __name__ == "__main__":
    main()