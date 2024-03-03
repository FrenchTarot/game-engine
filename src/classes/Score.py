class Score:
    def __init__(self, players) -> None:
        self.scores = {player: 0 for player in players}

    def add_score(self, player, score):
        self.scores[player] += score

    def add_scores(self, scores):
        for player in scores:
            self.scores[player] += scores[player]

    def get_scores(self):
        return self.scores
