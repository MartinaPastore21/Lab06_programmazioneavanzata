from database.DB_connect import get_connection
from model.prestito import Prestito
from model.strumento import Strumento

"""
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
"""


class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """Funzione che legge tutti gli strumenti nel database"""
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM strumento")
            for row in cursor:
                result.append(
                    Strumento(
                        row["codice"],
                        row["tipo"],
                        row["marca"],
                        row["anno_acquisto"],
                        row["valore"],
                        row["disponibile"],
                    )
                )
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo"""
        cnx = get_connection()
        result = []
        query = """SELECT *
                   FROM strumento
                   WHERE strumento.tipo LIKE %s"""
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (f"%{tipo}%",))
            for row in cursor:
                result.append(
                    Strumento(
                        row["codice"],
                        row["tipo"],
                        row["marca"],
                        row["anno_acquisto"],
                        row["valore"],
                        row["disponibile"],
                    )
                )
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None