from matplotlib import pyplot as plt

class Team():
    def __init__(self, df):
        self.name = df['club']
        self.n_goals = df['goals']
        self.n_wins = df['wins']
        self.n_losses = df['losses']
        self.n_ties = df['ties']
        self.w_l_chart = None
        self.rain_win_rate = None
        self.games = None
        
    def create_w_l_chart(self):
        self.w_l_chart = plt.figure(figsize=(5,5))
        plt.bar(['wins', 'losses', 'ties'], [self.n_wins, self.n_losses, self.n_ties], 
                color = ['#1ebbd7', '#005073','#189ad3'])
        plt.title(f"{self.name.title()}'s 2011 Season")
        plt.ylabel('Games')
        plt.ylim(0,34)

    def set_games(self, games_df):
        self.games = games_df.loc[(games_df['HomeTeam']== str(self.name)) | (games_df['AwayTeam']== str(self.name))]

        
    def calc_rain_win_rate(self):
        games = self.games
        n_rain = games.loc[games['rainy']].shape[0]
        n_dry = games.loc[games['rainy'] == False].shape[0]
        n_rain_w = (games.query("('rainy' == True) and ('HomeTeam' == str(self.name) and ('FTR' == 'H')").shape[0]  
                    + games.query("('rainy'==True) and ('AwayTeam' == str(self.name) and ('FTR' == 'A')").shape[0])
        # n_rain_l =(games.loc[(games['rainy']) & (games['HomeTeam'] == self.name) 
        #                      & (games['FTR'] == 'A')].shape[0] 
        #            + games.loc[(games['rainy']) & (games['AwayTeam'] == self.name) 
        #                      & (games['FTR'] == 'H')].shape[0])
        # n_rain_d = (games.loc[(games['rainy']) & (games['HomeTeam'] == self.name) 
        #                      & (games['FTR'] == 'D')].shape[0] 
        #             + games.loc[(games['rainy']) & (games['AwayTeam'] == self.name) 
        #                      & (games['FTR'] == 'D')].shape[0])
        self.rain_win_rate = n_rain_w 
        # / (n_rain_w + n_rain_l + n_rain_d)


        # games = self.games
        # n_rain = games.loc[games['rainy']].shape[0]
        # n_dry = games.loc[games['rainy'] == False].shape[0]
        # n_rain_w = (games.loc[(games['rainy']) & (games['HomeTeam'] == self.name) 
        #                      & (games['FTR'] == 'H')].shape[0]  
        #             + games.loc[(games['rainy']) & (games['AwayTeam'] == self.name) 
        #                      & (games['FTR'] == 'A')].shape[0])
        # n_rain_l =(games.loc[(games['rainy']) & (games['HomeTeam'] == self.name) 
        #                      & (games['FTR'] == 'A')].shape[0] 
        #            + games.loc[(games['rainy']) & (games['AwayTeam'] == self.name) 
        #                      & (games['FTR'] == 'H')].shape[0])
        # n_rain_d = (games.loc[(games['rainy']) & (games['HomeTeam'] == self.name) 
        #                      & (games['FTR'] == 'D')].shape[0] 
        #             + games.loc[(games['rainy']) & (games['AwayTeam'] == self.name) 
        #                      & (games['FTR'] == 'D')].shape[0])
        # self.rain_win_rate = n_rain_w / (n_rain_w + n_rain_l + n_rain_d)

def main():
    pass

if __name__== "__main__":
    main()