## Popravci, opažanja
- kvalitetnija brzina okretanja dobije se frekvencijomm 500 umjesto 1000 (manje modificiranja brzine)
- zamjenjeni su motor left i right na pcbu ("sjever" su ledice, znači desni je left, a lijevi je right --> napisano markerom)
- ne stisnuti kotače do kraja jer osovina izlazi kod konektora i ako ju tamo nešto češe, ide sporije
- bolje jedna umjesto 2 coaster balls (u suprotnom se jako jako jako slabo kreće), dovoljno je težak straga i ide sporo da to ne bi trebao biti problem + baterija premještena gore da ne smeta u vožnji 
- da bi se program pokrenuo treba biti nazvan "main.py"

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
