import streamlit as st

GAME_WEIGHT = 40

#def calculate_betting_points(team1_points, team2_points, points_difference):
#    st.write(f"#### Calculate_betting_points: ")
#    betting_points_team1 = 1 / (1 + 10 ** (-points_difference / 400))
#    st.write(f"betting_points_team1: {betting_points_team1}")
#    betting_points_team2 = 1 / (1 + 10 ** (points_difference / 400))
#    st.write(f"betting_points_team2: {betting_points_team2}")

def calculate_betting_points_team_home  (home_points, team2_points, points_difference):
    st.markdown("--f>>calculate_betting_points_team_home--")
    ##st.write(f"#### calculate_betting_points_team_home: ")
    betting_points_home = 1 / (1 + 10 ** (points_difference / GAME_WEIGHT))
    st.write(f"betting_points_home: {betting_points_home}")
    return betting_points_home

def calculate_betting_points_team_away (home_points, team2_points, points_difference):
    st.markdown("--f>>calculate_betting_points_team_away--")
    ##st.write(f"#### calculate_betting_points_team_away: ")
    betting_points_away = 1 / (1 + 10 ** (-points_difference / GAME_WEIGHT))
    st.write(f"betting_points_away: {betting_points_away}")
    return betting_points_away
   


def calculate_game(team1_points, team2_points, team1_goals, team2_goals):
    st.markdown("--f>>calculate_game--")
    points_difference = team1_points - team2_points
    return_object = []
    st.write(f"#### points_difference: {points_difference}")
    return_object.append(points_difference)
    st.write(f"return_object: {return_object}") 

    st.write(f"#### Betting: ")
    betting_points_team1 = calculate_betting_points_team_home(team1_points, team2_points, points_difference)
    st.write(f"betting_points_team1: {betting_points_team1}")
    betting_points_team2 = calculate_betting_points_team_away(team1_points, team2_points, points_difference)
    st.write(f"betting_points_team2: {betting_points_team2}")
    st.write(f"betting_points_team2: (under construction)")




    #if points_difference > 0:
#
    #    reward = 1 / (1 + 10 ** (-points_difference / GAME_WEIGHT)*10)
    #    st.write(f"reward = 1 / (1 + 10 ** (-points_difference / GAME_WEIGHT)")
    #    st.write(f"(1 + 10 ** (-points_difference / 400): {1 + 10 ** (-points_difference / GAME_WEIGHT)}")
    #    st.write(f"reward: {reward}")
    #    st.write(f"reward: {reward}")
    #    penalty = -reward 
    #    st.write(f"penalty: {penalty}")


    #else:
    #    penalty = 1 / (1 + 10 ** (points_difference / GAME_WEIGHT)*10)
    #    st.write(f"penalty = 1 / (1 + 10 ** (points_difference / 400)")
    #    st.write(f"penalty: {penalty}")
    #    reward = -penalty
    #    st.write(f"reward: {reward}")
    st.write(f"## Final result: ")
    st.write(f"team1_points: {team1_points + 1}")
    st.write(f"team2_points: {team2_points + 1}")

    return []

def draw_headers():
    st.markdown("--f>>draw_headers--") 
    st.markdown("# My ELO alternative Calculator")
    st.write("This is a simple calculator")
    st.write("It is used to calculate the point outcam of a game (reward/penalty).") 
    st.write("The idea is to reward fairly the winner and penalize the loser based on the difference of points between the teams.")
    st.write("## The formula is: ")


def main():
    st.markdown("--f>>main--") 
    draw_headers()
    st.write("### Teams points:")
    team1_points = st.number_input("team 1 points", value=1000)
    team2_points = st.number_input("team 2 points", value=1000)
    st.write("### Game result:")
    team1_goals = st.number_input("team 1 goals", value=1)
    team2_goals = st.number_input("team 2 goals", value=1)
    st.write("### Game type")
    st.write("**Some day now....**")
    st.radio("game type", ("friendly", "tournament") )

    if st.button("Calculate points"):
        calculate_game(team1_points, team2_points, team1_goals, team2_goals)
    
    

if __name__ == "__main__":
    main()