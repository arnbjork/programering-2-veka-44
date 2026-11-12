
from typing import TypeVar, Generic
T=TypeVar("T")

class lager(Generic[T]):
    count=0
    def __init__(self,objekt_namn,inehåll:T): 
        self.inehåll=inehåll
        self.objekt_namn=objekt_namn
        lager.count += 1

    def visa_information(self):
        meddelande = "Information om lagret:"

        def skriv_ut():
            print(meddelande)
            print("Objekt:", self.objekt_namn)
            print("Innehåll:", self.innehåll)

        skriv_ut()

frukt1=lager[str]("äpppl","frön")
frukt2 = lager[str]("päron", "kärnor")

print(lager.count)