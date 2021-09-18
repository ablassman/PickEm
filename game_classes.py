class GameInfo:
    def __init__(self, home_team, away_team, home_spread, away_spread, over_under=None):
        self.home_team = home_team
        self.away_team = away_team
        self.home_spread = home_spread
        self.away_spread = away_spread
        self.over_under = over_under

class GameResults:
    def __init__(self, home_team, away_team, home_score, away_score):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.total = home_score + away_score
        self.winner = home_team if home_score > away_score else away_team if away_score > home_score else 'tie' 