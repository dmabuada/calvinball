import csv
from calvinball.models import Comic
from calvinball.settings import BASE_DIR


def load_data():
    with open(BASE_DIR + '/calvinball/scripts/candh.csv') as csvfile:
        comics = csv.DictReader(csvfile)
        for row in comics:
            t = Comic(
                title=row['title'],
                description=row['description'])
            t.save()
