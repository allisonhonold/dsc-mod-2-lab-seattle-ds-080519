import pymongo

class MongoHandler():
    """Interfaces with Mongodb assumes a mongo instance is already running
    (start with $ mongod)"""
    def __init__(self):
        client = MongoClient()
        db = client.teams_db
        teams = db.team_collection
        
           
    def add_team(self, team):
        team_dict = {'name': team.name, 
                     'goals': team.n_goals, 
                        }
        teams.insert_one(team_dict)

    def get_team(self, team_name):
        return teams.find_one({'name' : team_name})

