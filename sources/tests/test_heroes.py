from sources import heroes
from sources.database import heroDto
from bson.json_util import dumps

def test_GetAll():
    #arrange
    #act
    result = heroes.GetAll()
    #assert
    assert result.count() == 734

def test_Get():
    #arrange
    hero = heroDto.heroDto()
    hero.id         = '2'
    hero.name       = 'Abin Sur'
    hero.Gender     = 'Male'
    hero.EyeColor   = 'blue'
    hero.Race       = 'Ungaran'
    hero.HairColor  = 'No Hair'
    hero.Height     = '185'
    hero.Publisher  = 'DC Comics'
    hero.SkinColor  = 'red'
    hero.Alignment  = 'good'
    hero.Weight     = '90'

    #act
    result = heroes.Get(hero.id)

    #assert
    assert hero.id         == result['id']
    assert hero.name       == result['name']
    assert hero.Gender     == result['Gender']
    assert hero.EyeColor   == result['EyeColor']
    assert hero.Race       == result['Race']
    assert hero.HairColor  == result['HairColor']
    assert hero.Height     == result['Height']
    assert hero.Publisher  == result['Publisher']
    assert hero.SkinColor  == result['SkinColor']
    assert hero.Alignment  == result['Alignment']
    assert hero.Weight     == result['Weight']

def goodWins():
    heroList = heroes.GetAll()
    good = 0
    bad = 0
    for hero in heroList:
        if (hero['Alignment'] == "good"):
            good += 1
        else:
            bad += 1
    assert good > bad