from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import json
import re
import wikipediaapi

class Line(object):
    def __init__(self, season, ep, text):
        self.season = season
        self.ep = ep
        self.text = text
        self.wordCounter=len(text.split())

class Character(object):
    def __init__(self, name, line,gender,house):
        self.name = name
        self.lines = [line]
        self.wordCounte =0
        self.alias = [name]
        self.gender = gender
        self.house = house

main_characters = []
def getMainCharactersWiki():
    wiki = wikipediaapi.Wikipedia('en')
    mutcd = wiki.page('List_of_Game_of_Thrones_characters')
    characters = mutcd.section_by_title('Main characters')
    # main_characters = []
    houses = ['Targaryen', 'Stark', 'Lannister', 'Greyjoy', 'Arryn', 'Baratheon', 'Tully', 'Tyrell']
    for character in characters.sections:
        name = character.title
        for house in houses:
            if (house in name):
                ch_house = house
        if ("She" in character.text or 'she' in character.text):
            gender = 'Female'
        elif ("He" in character.text or 'he' in character.text):
            gender = 'Male'
        else:
            gender = ' '
        new_character = Character(name, ' ', gender, ch_house)
        main_characters.append(new_character)

    for c in main_characters:
        print('Name: ' + c.name)
        print('Gender: ' + c.gender)
        print('House: ' + c.house)

# def addAlias():


def existCharacter(name):
    for c in Characters:
        if(c.name == name):
            return c
    return False

def addText(character, season, ep, text):
    line = Line(season,ep,text)
    character.lines.append(line)

def countWordPerCharacter(character):
    counter=0
    for l in character.lines:
        counter=counter+l.wordCounter
    return  counter

def writeToFile():
    with open('data.json', 'w') as outfile:
        json.dump(Characters, outfile)

def openScript():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.set_window_position(-10000, 0)
    driver.get("https://genius.com/albums/Game-of-thrones/Season-1-scripts")
    episodes_num = len(driver.find_elements_by_class_name("chart_row-content"))
    for i in range(episodes_num):
        episodes = driver.find_elements_by_class_name("chart_row-content")
        episode = episodes[i]
        href = episode.find_element_by_tag_name('a').get_attribute('href')
        driver.get(href)
        content = driver.find_element_by_class_name('lyrics')
        parser(content,1,i)
        driver.back()

    driver.close()
def getCharacterFromArray(alias):
    for c in main_characters:
        if(alias in c.alias):
            return c
    return False

def parser(content,season,ep):
    lines = content.text.splitlines()
    for l in lines:
        words = l.split(":")
        if(len(words) >= 2):
            if (True):
                c = getCharacterFromArray(words[0])
                addText(c, season,ep, words[1])


def printForCheck():
    for c in Characters:
        print('Name: ' + c.name)
        words = countWordPerCharacter(c)
        print('words: ' + str(words))
        i = 1
        for l in c.lines:
            # print('season: '+ l.season)
            # print('episode: ' + l.ep)
            print(str(i) + ' ' + l.text)
            i = i + 1

getMainCharactersWiki()
openScript()
printForCheck()

#driver.close()
