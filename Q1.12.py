class Player:
    def __init__(self,id = 10,name = "Bob",teams = [],age = 18):
        self.id = id
        self.name = name
        self.teams = teams
        self.age = age
    def checkTeam(self,teamName):
        return teamName in self.teams
class Team:
    def __init__(self,name = "FCB",players = [], league = 0):
        self.name = name
        self.players = players
        self.league = league
    def addPlayer(self,player):
        self.players.append(player)
    def removePlayer(self,player):
        self.players.remove(player)
def maxLeague(team1,team2):
    if team1.league > team2.league:
        print(team1.players)
    else:
        print(team2.players)