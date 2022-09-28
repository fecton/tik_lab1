#!/usr/bin/python3

# TODO:
"""
Варіанти:
                укр     рус      англ
    Варіант 1:  +       +(той же) +(той же)
    (зв'язаний)

    Варіант 3:  +       +(рівний по сим) +(рів по сим)
    (не зв'яз)

Варіант по номеру команди: 3
Середня кількість слів тексту: 2.000
Варіанти задач: 1,3


1. Розробити проект для дослідження кількості інформації та ентропії
дискретного джерела повідомлень відповідно до варіанта.

2. Проект повинен дозволяти:
- визначати кількість інформації в тексті українською, англійською та
німецькою мовами, а також:
- вводити текст повідомлення;
- здійснювати підрахунок частоти появи символу в тексті
повідомлення;
- упорядковувати частоту за зростанням будь-яким алгоритмом
сортування;
- Виводити на екран символ тексту та частоту його появи.
- Виводити кількість інформації у тексті.
"""


UKRAINIAN_TEXT = """
Тарас Шевченко біографія 
Народився 9 березня 1814 року у селі Моринці Звенигородського повіту Київської губернії в закріпаченій селянській родині. Рано став сиротою — мати померла, коли йому було 9 років, батько — у 11 років. Його доглядала сестра Катерина.
Восени 1822 року починає вчитися грамоти у місцевого дяка. Іде наймитувати до дяка Богорського, який прибув з Києва. Не витерпівши знущань дяка, тікає від нього і шукає в навколишніх селах учителя-маляра.
В 1828 році він потрапляє в число прислуги поміщика Енгельгардта, спочатку в ролі кухарчука, потім козачка. Помітивши у Тараса пристрасть до живопису, поміщик вирішує зробити його придворним художником. Він віддає свого кріпака в навчання викладачеві Віленського університету — портретисту Яну Рустему. У Вільні юний Тарас пробув 1,5 року.
Переїхавши 1831 року з Вільно до Петербурга, Енгельгардт взяв із собою Шевченка і віддав його в науку на 4 роки до живописця Василя Ширяєва.
Улітку 1836 р. він познайомився зі своїм земляком — художником І. Сошенком, а через нього — з Євгеном Гребінкою, В. Григоровичем і О. Венеціановим.
Навесні 1838 Карл Брюллов та Василь Жуковський викупили молодого поета з кріпацтва.
Незабаром став студентом Академії мистецтв.
Першу збірку своїх поетичних творів видав 1840 під назвою «Кобзар». У першому виданні було 8 творів.
25 травня 1843 року з Петербурга виїхав в Україну.
В лютому 1844 року виїхав з України до Петербурга через Москву.
У 1844р. написав гостро політичну поему «Сон» («У всякого своя доля»), ставши на шлях безкомпромісної боротьби проти самодержавної системи тодішньої Російської Імперії.
5 квітня рада Академії мистецтв видала квиток на право проїзду на Україну. Вже в листопаді 1845 року збори Академії мистецтв у Петербурзі затвердили рішення ради про надання звання некласного художника.
31 березня (12 квітня) 1845 року виїхав із Петербурга через Москву до Києва.
Навесні 1846 року прибув до Києва. У квітні пристав до Кирило-Мефодіївського братства.
Заарештували 5 квітня 1847.
"""


ENGLISH_TEXT = """
Taras Shevchenko biography
He was born on March 9, 1814 in the village of Moryntsi, Zvenigorod district, Kyiv province, in a well-established peasant family. He became an orphan early - his mother died when he was 9 years old, and his father - at 11 years old. His sister Kateryna took care of him.
In the fall of 1822, he began to learn literacy from a local count. He is going to pay customs duties to Count Bogorskyi, who has arrived from Kyiv. Unable to endure the taunts of the count, he runs away from him and looks for a teacher-painter in the surrounding villages.
In 1828, he became one of the servants of the landowner Engelhardt, first as a cook, then as a Cossack. Noticing Taras's passion for painting, the landlord decides to make him a court painter. He gives his serf to the teacher of the University of Vilnius - the portrait painter Jan Rustem. Young Taras stayed in Vilna for 1.5 years.
Having moved from Vilna to St. Petersburg in 1831, Engelhardt took Shevchenko with him and sent him to study for 4 years with the painter Vasyl Shiryaev.
In the summer of 1836, he met his compatriot, the artist I. Soshenko, and through him, Yevhen Hrebinka, V. Hryhorovych, and O. Venetsianov.
In the spring of 1838, Karl Bryullov and Vasyl Zhukovsky bought the young poet from serfdom.
Soon he became a student of the Academy of Arts.
He published the first collection of his poetic works in 1840 under the title "Kobzar". There were 8 works in the first edition.
On May 25, 1843, he left St. Petersburg for Ukraine.
In February 1844, he left Ukraine for St. Petersburg via Moscow.
In 1844 wrote the acutely political poem "Dream" ("Everybody has his own fate"), embarking on the path of uncompromising struggle against the autocratic system of the then Russian Empire.
On April 5, the Council of the Academy of Arts issued a ticket for the right of passage to Ukraine. Already in November 1845, the meeting of the Academy of Arts in St. Petersburg approved the council's decision to grant the title of non-class artist.
On March 31 (April 12) 1845, he left St. Petersburg via Moscow to Kyiv.
In the spring of 1846, he arrived in Kyiv. In April, he joined the Cyril and Methodius brotherhood.
Arrested on April 5, 1847.
"""

GERMAN_TEXT = """
Biografie von Taras Schewtschenko
Er wurde am 9. März 1814 im Dorf Moryntsi, Kreis Swenigorod, Gouvernement Kiew, in einer gut etablierten Bauernfamilie geboren. Er wurde früh Waise – seine Mutter starb, als er 9 Jahre alt war, und sein Vater – im Alter von 11 Jahren. Seine Schwester Kateryna kümmerte sich um ihn.
Im Herbst 1822 begann er bei einem örtlichen Grafen Alphabetisierung zu lernen. Er wird dem Grafen Bogorskyi, der aus Kiew eingetroffen ist, Zollgebühren zahlen. Unfähig, die Sticheleien des Grafen zu ertragen, rennt er vor ihm davon und sucht in den umliegenden Dörfern nach einem Malerlehrer.
1828 wurde er Knecht des Gutsbesitzers Engelhardt, zunächst als Koch, dann als Kosake. Als der Hausherr Taras' Leidenschaft für die Malerei bemerkt, beschließt er, ihn zum Hofmaler zu machen. Er gibt seinen Leibeigenen dem Lehrer der Universität Vilnius - dem Porträtmaler Jan Rustem. Der junge Taras blieb 1,5 Jahre in Wilna.
Nach seinem Umzug von Wilna nach St. Petersburg im Jahr 1831 nahm Engelhardt Shevchenko mit und schickte ihn für 4 Jahre zu dem Maler Vasyl Shiryaev, um dort zu studieren.
Im Sommer 1836 lernte er seinen Landsmann, den Künstler I. Soshenko, und durch ihn Yevhen Hrebinka, V. Hryhorovych und O. Venetsianov kennen.
Im Frühjahr 1838 kauften Karl Bryullov und Vasyl Zhukovsky den jungen Dichter aus der Leibeigenschaft.
Bald wurde er Student der Akademie der Künste.
Die erste Sammlung seiner poetischen Werke veröffentlichte er 1840 unter dem Titel „Kobzar“. Es gab 8 Werke in der Erstausgabe.
Am 25. Mai 1843 verließ er St. Petersburg in Richtung Ukraine.
Im Februar 1844 verließ er die Ukraine über Moskau nach St. Petersburg.
1844 schrieb das akut politische Gedicht „Dream“ („Jeder hat sein eigenes Schicksal“) und begab sich damit auf den Weg des kompromisslosen Kampfes gegen das autokratische System des damaligen Russischen Reiches.
Am 5. April stellte der Rat der Akademie der Künste ein Ticket für das Recht auf Durchreise in die Ukraine aus. Bereits im November 1845 billigte die Versammlung der Akademie der Künste in St. Petersburg den Beschluss des Rates, den Titel eines nicht klassenlosen Künstlers zu verleihen.
Am 31. März (12. April) 1845 verließ er St. Petersburg über Moskau nach Kiew.
Im Frühjahr 1846 kam er in Kiew an. Im April trat er der Cyril and Methodius Bruderschaft bei.
Verhaftet am 5. April 1847.
"""

ENGLISH_ALPHABET = "abcdefghiklmnopqrstvxyz"
UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
GERMAN_ALPHABET = "abcdefghijklmnopqrstuvwxyzäöüß"


def text_sizes():
    print("--= Розмірність у UTF-8 =---")

    print("[+] УКРАЇНСЬКИЙ ТЕКСТ:\t", len(UKRAINIAN_TEXT), f" символів ({len(UKRAINIAN_TEXT)*8} байтів)")
    print("[+] АНГЛІЙСЬКИЙ ТЕКСТ:\t", len(ENGLISH_TEXT), f" символів ({len(ENGLISH_TEXT)*8} байтів)")
    print("[+] НІМЕЦЬКИЙ ТЕКСТ:\t", len(GERMAN_TEXT), f" символів ({len(GERMAN_TEXT)*8} байтів)")


def alphabet_symbol_count() -> list:
    german, ukraine, english = {}, {}, {}

    arr = [english, ukraine, german]

    i = 0
    for text, alphabet in [(ENGLISH_TEXT, ENGLISH_ALPHABET), (UKRAINIAN_TEXT, UKRAINIAN_ALPHABET), (GERMAN_TEXT, GERMAN_ALPHABET)]:
        for symbol in alphabet:
            arr[i][symbol] = text.count(symbol)
        i+=1
            
    return arr


def main():
    op = 0
    while 1:
        match op:
            case 0:
                print("""Меню:
0. Показати це меню
1. Вивести текстів
2. Частота якогось символу
3. Розмір текстів""")
            case 1:
                print("УКРАЇНСЬКИЙ ТЕКСТ")
                print(UKRAINIAN_TEXT, end="\n"*3)

                print("АНГЛІЙСЬКИЙ ТЕКСТ")
                print(ENGLISH_TEXT, end="\n"*3)

                print("НІМЕЦЬКИЙ ТЕКСТ")
                print(GERMAN_TEXT, end="\n"*3)
            case 2:
                arr = alphabet_symbol_count()
                symbol = input("СИМВОЛ: ")

                names = ["німецькому", "українському", "англійському"]
                for i in range(3):
                    try:
                        print(f"У {names[i]} тексті символ '{symbol}' наявний {arr[i][symbol]} разів")
                    except KeyError:
                        print(f"У {names[i]} тексті символ '{symbol}' не наявний") 

            case 3:
                text_sizes()
        op = int(input(">> "))


# Якщо файл запускається як основний, то викликати основну функцію
if __name__ == "__main__":
    main()
# Інакше повідомити про помилку
else:
    print("[ERR] Sorry, it can't be used like a module")

