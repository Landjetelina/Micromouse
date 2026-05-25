## Popravci, opažanja
- fotosenzori su bili obrnuti, Q5 je skroz zamjenjen => sad rade svi
- rad IR ledice moguć provjeriti s kamerom
- kvalitetnija brzina okretanja dobije se frekvencijomm 500 umjesto 1000 (manje modificiranja brzine)
- zamjenjeni su motor left i right na pcbu ("sjever" su ledice, znači desni je left, a lijevi je right --> napisano markerom)
- ne stisnuti kotače do kraja jer osovina izlazi kod konektora i ako ju tamo nešto češe, ide sporije
- bolje jedna umjesto 2 coaster balls (u suprotnom se jako jako jako slabo kreće), dovoljno je težak straga i ide sporo da to ne bi trebao biti problem + baterija premještena gore da ne smeta u vožnji 
- da bi se program pokrenuo treba biti nazvan "main.py"
- reset tipka ne radi ništa kada je uploadan program na robota, samo na sekundu ga zaustavi i normalno nastavlja dalje
- pri uključenju na laptop, pokreće se uploadani program jer pico vidi dovod napona s laptopa no onda ne rade baš fototranz (nez zaš, to je neki bug, jer "run this file on pico" i "upload this file" rade normalno i bez problemma)

### prebacivanje programa
1. desni klik na program i "upload file"
2. provjera pohrane se može preko ispod navedenih komandi
3. isključiti pico od laptopa, OFF pa ON i onda će sam krenuti

### terminal i provjera pohrane
``` 
import os
os.listdir()
os.remove()
```

### ideje za daljnju implementaciju 
- mapiranje "desnom rukom" bi moglo trajati iznimno dugo s obzirom da je brzina motora užasna
- zadržati frekveniciju motora na 500, eventualno malo sniziti da se smanji pogreška
- razmotriti potrebu PID regulatora
