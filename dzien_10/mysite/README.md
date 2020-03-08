
## Instalacja django

    pip install django
    
    
## Tworzenie projektu:

    django-admin startproject <nazwa projektu>

## Tworzenie aplikacji:

    python manage.py startapp <nazwa aplikacji>
    
## Settings:

Dodaną aplikację warto dodać do sekcji `INSTALLED_APPS` w pliku `settings.py`

## Routing:

W plikach urls.py wiążemy urle (adresy)  z funkcjami widoków, które powinny być w pliku views.py dla danej aplikajci

## Modele

Modele tworzymy w plikach models.py. Są to klasy dziedziczące po models.Model

## Migracje

    python manage.py makemigrations
    
    python manage.py migrate
 
 przygotowujemy i wykonyjemy migracje. Naniesione one będa na bazę danych zdefiniowaną w pliku settings
 
## Shell

    python manage.py shell
    
Uruchomi nam REPL w kontekście naszego projektu

## Tworzenie instancji modeli

jeśl mamy model `Maths`

    from maths.models imoport Math

by utworzyć instancje możemy:

    Maths.objects.create(... odpowiednie pola i wartosci, np operation="add")
    
by pobrać

    Maths.objects.all()
    Maths.objects.first()
    Maths.objects.last()
    Maths.objects.get(<kolumna>=<wartosc>)
    Maths.objects.filter(<kolumna>=<wartosc>)