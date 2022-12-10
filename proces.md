# GIT

## 3-11-2022
Ik was in de veronderstelling dat we alle colleges nodig hadden voor Search, vandaar dat ik deze na “HTML, CSS” ben gaan kijken. Voor deze minor had ik ooit al een GitHub account aangemaakt. Echter, het enige dat ik wist is dat het iets met open source te maken had en dat je samen aan code kon werken en je projecten kon delen. Daarom vond ik het wel echt leuk om hier meer over te leren. Ik denk dat de stof vrij vanzelfsprekend is en dat ik er simpelweg gewoon mee aan de slag moet gaan.

## 24-11-2022
Inmiddels ben ik ook het GIT college grotendeels vergeten. Vandaar dat ik ook hiervoor de stof opnieuw heb bekeken en er aantekeningen bij heb gemaakt. Ook heb ik nog gezocht op internet naar een helder overzicht, daar vond ik een erg duidelijke afbeelding of freecodecamp.org. Na het lezen van dat artikel en een aantal verhalen gehoord te hebben over tokens leek het me handig om een SSH key aan te maken.

# Django

## 12-11-2022
Afgelopen Week (2) was ik erg druk met Programmeren 2, hierdoor helaas pas later met het project aan de slag kunnen gaan. Ook ben ik nog bezig geweest met de lay-out van Search (zie 10-11-2022). Het leek me daarom verstandig om alvast het college door te nemen om zo niet verder achterop te raken. In eerste instantie leek het college me helder, er kwamen veel bekende dingen terug en Brian behandeld de stof duidelijk stapsgewijs. Echter, de informatiedichtheid van dit college was zeer groot. Na de lecture gekeken te hebben, moest ik de lecture notes nog eens aandachtig lezen. Er zijn me veel details ontglipt tijdens het kijken. Het zal me daarom niets verbazen wanneer ik hetzelfde ervaar wanneer ik aan Wiki begin. Vooralsnog denk ik wel dat de grote lijnen me duidelijk zijn.

## 19-11-2022
Afgelopen week (3)  heb ik weinig kunnen studeren vanwege een last door een getrokken verstandskies. De tijd die ik heb kunnen besteden aan de minor is volledig uitgegaan naar Programmeren 2. Hierdoor heb ik helaas wederom het project uit moeten stellen, met als gevolg dat de stof wederom deels weggezakt was. Daarom besloot ik aantekeningen te maken van het college in de hoop het zo beter te onthouden.

# Wiki

## 19-11-2022
Zoals beschreven in Django heb ik de opdrachten al eerder doorgelezen. Ook voor de opdracht leek het me verstandig om het project te documenteren. Zo verklein ik de kans op het vergeten van de stof en denk ik actief na over het project.

## 24-11-2022
Ik ben begonnen met het maken van een schets voor het document design. Hierin werd het me duidelijk dat ik geen aparte page hoef te maken voor de error die zich voordoet wanneer de user een Wiki page wilt toevoegen waarvan de title al bestaat. Echter, ik had geen idee wat de conventie is voor het schetsen van een error. Na op Google wat afbeeldingen te hebben bekeken, heb ik ervoor gekozen om met een rode pijl de error aan te geven en daarbij de message te schrijven. Ik heb mijn schets uiteindelijk digitaal uitgewerkt, daarin ben ik geen ‘problemen’ tegengekomen. Het design spreekt voor zich, waardoor het me onnodig lijkt om te beschrijven hoe de webapplicatie werkt.

## 29/30-11-2022
Op de 29e heb ik een poging gedaan om een SSH key aan te maken door de stappen op Github door te lopen, dit verliep vrij soepel. Echter, ik begreep niet helemaal wat de key precies was en waar ik ‘m kon vinden. Daarom heeft Max mij de volgende dag geholpen met het linken van de key naar mijn Github account.

## 7-12-2022
Toen ik begon besefte ik hoe anders Wiki was ten opzichte van het college, ik ervaar het als zeer praktisch in plaats van theoretisch. Achteraf merk ik daarom ook dat ik de repository erbij had moeten houden toen ik aantekeningen maakte over de opdracht. Dit is iets wat ik ook zeker ga meenemen voor de opdracht Commerce.

Max heeft me geholpen met de eerste stappen van Wiki, hierdoor was het me duidelijk hoe de directories (views.py, urls.py en de templates) verbonden waren. Met behulp van de index functie lukte het vrij snel om de render functie juist toe te passen. Het enige waar ik tegen aanliep is dat ik niet wist hoe ik de titel van de entry op entry.html kon doorgeven. Uiteindelijk bleek ik geen komma gebruikt te hebben in de dictionary waardoor ik steeds foutmeldingen kreeg.
Wat betreft de foutmelding indien een entry wordt opgevraagd die niet bestaat, vraag ik me af of ik dit juist heb geïmplementeerd. Dit lijkt mij namelijk verbonden te zijn aan de zoekfunctie en niet aan de entry functie.

Als tweede heb ik in de indexpagina, van alle entry’s een link gemaakt met ‘a href’. De for loop was al geschreven dus het was puur het toepassen van de non-HTML logic, dit gaat precies zoals in de lecture notes staat aangegeven.

Daarna ben ik aan de search view begonnen. Hiervoor heb ik de lecture notes geraadpleegd, zodoende heb ik eerst een class gedefinieerd om een form te creëren. Vervolgens heb ik logischerwijs een functie search gemaakt zoals dat in de lecture notes gedaan wordt. Ik begrijp echter nog niet tot in de puntjes hoe dit werkt, hier zal ik me op focussen wanneer ik alles gedaan heb.
De gecleande form heb ik “query” genoemd. Indien util.get_entry(query) bestaat, wordt de entry view als return gegeven om zo de page weer te geven.

De code functioneert, echter niet zoals ik verwacht had. Zo werken de views (op entry na) enkel wanneer ik “wiki/” weglaat. Ik dacht dat ik hiervoor title moest toevoegen bij de url’s in de HTML templates, dit gaf echter een foutmelding. Aangezien dit geen prioriteit heeft zal ik hier later op terugkomen.


## 8-12-2022
Uiteindelijk had ik dus de ‘searchform’ goed aangemaakt in views.py, het werkte alleen niet omdat ik de variabele nog niet had geïntegreerd in layout.html. Vandaar dat ik de hardcoded input tag heb vervangen voor {{searchform}} en bij elke functie het in render aan de context toegevoegd. Hoewel de zoekfunctie hierdoor werkte, ziet de zoekbalk er anders uit dan eerst. Daarom heb ik gezocht naar het opmaken van een form in Django, uiteindelijk heb ik gevonden dat dit mogelijk is met ‘attrs’.
Nu stond me nog het geval te programmeren waar de query niet gelijk is aan een van de entry’s. Daarvoor loop ik over de util.list_entries() om zo te kijken of de query een substring is van een bepaalde title. De gevonden lijst geef ik dan weer terug aan de context in render om deze op de corresponderende HTML template mee te geven. In eerste instantie gaf ik hier ook de url van search mee, maar dit slaat natuurlijk nergens op aangezien eigenlijk deze pagina hetzelfde is als index.html maar dan met een kleinere lijst. Nadat ik de voorstellen goed werkend kreeg, kwam ik erachter dat een juist query nu een foutmelding geeft. Ik heb geen idee hoe dit mogelijk is, hier ga ik morgen aandacht aan besteden.

Daarna ben ik aan de slag gegaan met create. Omdat het hier wederom over een form ging leek het me logisch om ook hiervoor een class te definiëren. Echter, in de opdracht hebben ze het over een textarea voor de content. Ik heb nu 2 forms gemaakt, dus ik weet niet of ik het op de juiste manier heb geïmplementeerd ook al werkt het.
Ook ben ik begonnen met een eigen error page voor het geval de user een page wil aanmaken met een title die al bestaat, op deze manier kon ik gemakkelijk checken of mij code werkt. Morgen ga ik mij ook verdiepen in het verkrijgen van een error message.

Ik heb er nog voor gekozen om de de functie random te implementeren aangezien deze me vrij eenvoudig leek. Ik had ‘m ook inderdaad vrij rap voor elkaar met behulp van de functie random.choice().

Ter afsluiting wilde ik mijn progressie tot nu toe uploaden naar GitHub. Ik kreeg echter de volgende foutmelding in de staging fase: “fatal: not a git repository”. Terwijl, ik heb een repository in GitHub en ik begeef me in de juiste working directory. Daarom dat ik ook hier morgen achteraan ga.


## 9-12-2022
Samen met Yvette heb ik gekeken naar mijn search view. In plaats van render, returnde ik de entry view zoals beschreven op 7 december. Toen ik de volgende dag de resterende specifications geprogrammeerd had, werkte eerstgenoemde ineens niet meer. Ik kreeg een error dat entry niet als local variable herkend werd, terwijl entry een functie is. Daarom heb ik in plaats van de functie, de render uit entry als return gebruikt. Dit loste het probleem op, Yvette en ik weten echter niet waarom het fout ging.

Zoals ik vermoedde was mijn implementatie van create niet juist. Door gebruik te maken van twee charfields, limiteerde ik de user tot een maximale input van 255 karakters. Dit impliceerde dat ik een textarea moest definiëren in create.html. Yvette heeft me hierin begeleid dit juist te linken naar views.py. Waar ik dacht dat het een eenrichtiginsverkeer was (views > urls > template), werkt het dus ook de andere kant op. Bovendien kon ik hierdoor de forms gemakkelijker opmaken.
Tevens gaf Yvette aan dat een error page ook een vorm is van een error message, daarom is het niet nodig een message te implementeren zoals ik dat in mijn design document heb aangegeven.

Ten slotte heeft Yvette me geholpen met Github. De reden dat het niet mogelijk was voor mij om de bestanden te committen (in mijn geval zelf stagen), is omdat ik via de GUI het zip-bestand Wiki heb gedownload (in plaats van clone). Daarom heb ik m’n bestanden nu ook handmatig geüpload. Voor Commerce zal ik het uiteraard allemaal via Git en de terminal doen.

In ieder geval voldoet Wiki nu aan alle benodigde specificaties. Echter, er zijn nog een aantal punten waarop ik dit project kan verbeteren. Zoals het toevoegen van een edit view, de url’s fixen (wiki/), terugkoppeling voor wanneer er geen zoekresulaten zijn en opmaak van de forms bij create. Wanneer ik Commerce en Adventures afheb, zal ik hier tijd voor maken.

Voor de rest heb ik deze dag gebruikt om aantekeningen te maken over Commerce en bekend te worden met de bestanden.
