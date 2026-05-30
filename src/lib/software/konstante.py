import math

# senzori 0 i 1 imaju negativne x-eve jer su na lijevoj strani
# sin(-x) = -sin(x), cos(-x) = cos(x), pa ne moramo dodavati minus u računu dalje
# alpha = [-56.45, -27.45, 58.79, 23.07] # vrijednost u stupnjevima, računato sa skice
alpha = [33.5-90, 61-90, 68, 90-31]  # izmjereno kutomjerom
alpha = [math.radians(x) for x in alpha] # pretvara u radijane
d_cntr_trans = [6.7, 8.2, 6.5, 8.7]  # udaljenost od centra PCB-a do vrha tranzistora u cm, osim za tranzistor 1!
 


# Kalibracija senzora
"{Kanal: [(Vrijednost senzora, udaljenost u cm)]}"

# MIJENJATI OVO SAMO UZ TESTIRANJE SENZORA!
lookup_table = {
    0: [
        (24600, 1.5),
        (23870, 2.0),
        (23020, 2.5),
        (21195, 3.0),
        (18540, 3.5),
        (14800, 4.0),
        (13260, 4.5),
        (12000, 5.0),
        (7800, 6.0),
        (6750, 7.0),
        (5950, 8.0),
        (5250, 9.0),
        (4700, 10)
    ],
    1: [
        (43450, 1.5),
        (41550, 2.0),
        (38000, 2.5),
        (26130, 3.0),
        (23950, 3.5),
        (19330, 4.0),
        (16480, 4.5),
        (14680, 5.0),
        (11150, 6.0),
        (9850, 7.0),
        (8550, 8.0),
        (7820, 9.0),
        (7050, 10.0)
    ],
    2: [
        (34500, 1.5),
        (31500, 2.0),
        (28300, 2.5),
        (24900, 3.0),
        (21000, 3.5),
        (18750, 4.0),
        (15600, 4.5),
        (13300, 5.0),
        (10200, 6.0),
        (8850, 7.0),
        (7700, 8.0),
        (7300, 9.0),
        (6580, 10.0)
    ],
    3: [
        (20400, 1.5),
        (19850, 2.0),
        (19050, 2.5),
        (18100, 3.0),
        (17150, 3.5),
        (16050, 4.0),
        (14200, 4.5),
        (11600, 5.0),
        (9150, 6.0),
        (8000, 7.0),
        (7300, 8.0),
        (6650, 9.0),
        (6110, 10.0)
    ]
}