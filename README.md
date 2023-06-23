# ConnectFour
Deze repository is aangemaakt voor de afstudeerstage bij Alten voor de Master HCAI. De opdracht voor het afsturen is het maken van een addaptive AI voor het spel vier op een rij. De repository bevat een zelf geschreven digitale versie van vier op een rij en hiernaast ook de AI. Er is gekozen om Python te gebruiken als programeer taal omdat dit gebruikt wordt in de opleiding en ik hier het meeste ervaring mee heb. Hiernaast heeft python enorm veer libraries waardoor het eenvoudiger is om het programma voor dit project te schrijven. Wanneer de AI gebruikt zal worden voor de machine kan deze echter in elke taal geschreven worden aangezien het een algoritme is en deze dus het zelfde zal doen in elke taal indien de zelfde keuze worden gemaakt.

## libraries
Om de code te runnen zijn de volgende libraries nodig:
- pygame 
- math (standard in python)
- random (standard in python)

Om ervoor te zorgen dat het programma eenvoudig uit te voeren is, is ervoor gekozen zo min mogelijk libraries te gebruiken die geinstaleerd moeten worden. Er zijn twee libraries (math en random) gebruikt die standaard bij python worden geinstalleerd. De enige library die appart geinstalleerd moet worden is pygame, deze library is nodig voor alle informatie die op het scherm gezet wordt. In een eind versie van de AI kan dit eruit gehaald worden aangezien het spel dan gespeeld wordt op de machine van alten. Echter is het ook hier nog handig om een visualisatie te hebben om makkelijk te debuggen en bij te houden wat de AI doet en waarom.  

## Hoe run je de code
De code is aan te roepen door "main.py" te runnen. 
Instellingen voor de AI kunnen verandert worden in constants.py. niet alle waarden kunnen veranderd worden in de huidige versie van het programma, hieronder een beschrijving van alle constanten:
WIDTH, HEIGHT = de breedte en de hoogte van het scherm dat door pygame wordt gebruikt om het spel op te tekenen. deze waarden kunnen veranderd worden maar de rest schaald niet mee.
STONE_SIZE = De radius van de stenen. deze kan beter niet veranderd worden aangezien hier ook niet het hele spel met meeschaald. 

RED = Dit is de RGB code voor de rode kleur gebruikt in het spel.
YELLOW = Dit is de RGB code voor de gele kleur gebruikt in het spel.

GLOW_IMAGE = Dit is de afbeelding die wordt gebruikt in het spel om mogelijke zetten aan te geven.

SAVE_GAME = geeft aan of het spel wordt opgeslagen. Als True word het spel opgeslagen met PLAYER_NAME,PLAYER_AGE,SEARCH_DEPTH,player_win,moves in saved_games.txt 

SEARCH_DEPTH = Dit geeft aan hoeveel beurten de AI vooruit kijkt. als 0: de AI kijkt alleen naar zijn eigen eerstvolgende zet. als 1: AI kijkt naar eigen eerstvolgende en tegenstander eerstvolgende zet. etc. 
                Hiermee wordt ook het niveau van de AI aangegeven.

ALPHA_BETA_PRUNING = True: Alpha Beta pruning staat aan. False: Alpha Beta pruning staat uit. Advies laat altijd aanstaan. maakt het algorithme sneller zonder performance te verliezen. 

VALUE_SYSTEM = geeft aan op basis van welke informatie uit de positie de AI de posities scored. hiervoor zijn de volgende vier opties mogelijk: 

-   "possible_connect_fours"  
-   "connected_pieces"  
-   "random"  
-   "combination"

PLAYER_NAME = de naam van de speler die wordt opgeslagen met het spel, als SAVE_GAME = True

PLAYER_AGE = de leeftijd van de speler die wordt opgeslagen met het spel, als SAVE_GAME = True


## Hoe kan de code gebruikt worden
De code zoals hij nu is kan gebruikt worden om het spel op een laptop te spelen. hij staat op dit moment ingespeld om te spelen met één persoon tegen de computer. hierbij begind geel en wordt gespeeld door de mens en rood wordt gespeeld door de AI. Dit wordt ingesteld door de code in main.py. main.py regeld alle input van het programma, door deze te veranderen kan deze volgorde aangepast worden of kunnen twee computers of mensen tegen elkaar spelen. 

de main.py file kan ook gebruikt worden om input te krijgen van een ander apperaat. je kan hiervoor bijvoorbeeld een poort van de laptop of raspberry pi uitlezen.

Als het programma uiteindelijk op de machine gezet wordt zijn alleen de main.py en minimax.py nodig.
