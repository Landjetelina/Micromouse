## Čemu poseban folder?
Tu spremati relevantne kodove 
- algoritmi mapiranja
- traženje najbržeg puta
- ostali potrebni algoritmi koji nisu samo testiranje ispravnosti

## Organizacija koda
`izvedba.py` - funkcije koje rade nešto konkretno, npr. pomiču robota naprijed, okreću ga lijevo ili desno... <br>
`utility.py` - funkcije koje obavljaju neku korisnu funkciju, npr. pale senzore, čitaju senzore, dohvaćaju vrijednost s multipleksora... <br>
`robot.py` - nalazi se OOP klasa koja poziva funkcije unutar datoteka `izvedba.py` i `utility.py`, sprema dobivene vrijednosti u strukture podataka, čuva globalne varijable...  


Klasa Robot bi se trebala instancirati izvana, npr. unutar datoteke main.py <br>
Prije pokretanja koda mora se pritisnuti na folder Micromouse pa Upload project to Pico` ili odabrati file koji se izmijenio i kliknuti `Upload file to Pico` <br>

### Nije još dodana nova funkcionalnost, samo se promijenila organizacija koda
