import mongoClient
from heroDto import heroDto
import csv

superHeroesCSVFilePath = 'assets/heroes_information.csv'

def populate():
    """
    param: user
    param: pasword
    populates the database with duymmy data
    """
    database = mongoClient.connect()[mongoClient.DatabaseName]

    for superHero in readCSVFile(superHeroesCSVFilePath):
        hero = heroDto()
        hero.id         = superHero[0]
        hero.name       = superHero[1]
        hero.Gender     = superHero[2]
        hero.EyeColor   = superHero[3]
        hero.Race       = superHero[4]
        hero.HairColor  = superHero[5]
        hero.Height     = superHero[6]
        hero.Publisher  = superHero[7]
        hero.SkinColor  = superHero[8]
        hero.Alignment  = superHero[9]
        hero.Weight     = superHero[10]

        exist = database.heroes.find({'id': hero.id })
        if (exist.count() == 0):
            database.heroes.insert(hero.__dict__)
            print("Added: {0}".format(hero.__dict__))

def readCSVFile(filePath):
    '''
    Read a CSV file and return every line as a table
    '''
    with open(filePath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        nbRows = 0
        for row in spamreader:
            #skip first row
            if (nbRows == 0):
                nbRows+= 1
                next
            else:
                nbRows+= 1
                yield row
populate()