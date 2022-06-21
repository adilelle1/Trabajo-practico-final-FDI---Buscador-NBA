class Teams:

    def __init__(self, team_id, name, city, season, games, points, rebounds, assists):
        self.__team_id = team_id
        self.name = name
        self.city = city
        self.season = season
        self.games = games
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __str__(self) -> str:
        return super().__str__()

    def serialize(self):
        return {
            'name': self.name,
            'city': self.city,
            'season': self.season,
            'games': self.games,
            'points': self.points,
            'rebounds': self.rebounds,
            'assists': self.assists
        }
