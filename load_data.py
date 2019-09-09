import pandas as pd

def get_clubs_df(conn):
    """returns a dataframe of club, home_goals, away_goals, goals, wins, losses,
    ties, total games, and season FOR 2011"""

    cur = conn.cursor()

    q = """SELECT HomeTeam AS club, home_goals, away_goals,
                    (home_goals + away_goals) as goals,
                (HomeWins + AwayWins) as wins,
                (HomeLosses + AwayLosses) as losses,
                (HomeTies + AwayTies) as ties,
                (HomeWins + AwayWins + HomeLosses + AwayLosses + HomeTies + AwayTies) AS total_games,
                home.Season As season
        FROM
        
        (SELECT HomeTeam, Season,
                SUM(FTHG) As home_goals,
                SUM(CASE WHEN FTR='H' THEN 1 ELSE 0 END) AS HomeWins,
                SUM(CASE WHEN FTR='A' THEN 1 ELSE 0 END) AS HomeLosses,
                SUM(CASE WHEN FTR='D' THEN 1 ELSE 0 END) AS HomeTies
        FROM Matches
        WHERE Season = '2011'
        GROUP BY HomeTeam) AS home
        
        JOIN
        (SELECT AwayTeam, Season,
                SUM(FTAG) As away_goals,
                SUM(CASE WHEN FTR='H' THEN 1 ELSE 0 END) AS AwayLosses,
                SUM(CASE WHEN FTR='A' THEN 1 ELSE 0 END) AS AwayWins,
                SUM(CASE WHEN FTR='D' THEN 1 ELSE 0 END) AS AwayTies
        FROM Matches
        WHERE Season = '2011'
        GROUP BY AwayTeam)
        
        ON HomeTeam=AwayTeam
        
        ORDER BY Club;
        """

    cur.execute(q)

    return pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description])

def get_matches_df(conn):
        """Returns a dataframe of each match in 2011. columns: Date, HomeTeam, 
        Away Team, FTR (final record: Home, Away, Draw)"""
        cur = conn.cursor()
        cur.execute("""SELECT Date, HomeTeam, AwayTeam, FTR 
                        FROM Matches WHERE Season = '2011';""")
        return pd.DataFrame(cur.fetchall(), columns=[x[0] for x in cur.description])

def main():
        pass

if __name__== "__main__":
        main()