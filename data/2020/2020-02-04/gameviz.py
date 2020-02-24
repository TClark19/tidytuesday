import plotly
import pandas as pd

gamesdf = pd.read_csv("data/2020/2020-02-04/games.csv")
attendancedf = pd.read_csv("data/2020/2020-02-04/attendance.csv")
standingsdf = pd.read_csv("data/2020/2020-02-04/standings.csv")
wdf = pd.merge(gamesdf,attendancedf,standingsdf,on=["team","team_name","year"])
print(wdf.head())