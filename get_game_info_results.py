def get_game_info(score_box):
	"""
    get_game_info gets the basic betting info for a single game.

    :param score_box: a div html block that contains the score info for a single game
    :return: a GameInfo object with the home/away teams, home/away team lines, and the O/U
    """ 
    odds = score_box.find_all('td', {'class': 'in-progress-odds'})
    over_under = float(odds[0].text.strip()[1:])
    home_line = float(odds[1].text.strip())
    teams = score_box.find_all('td', {'class': 'team'})
    away_team = teams[0].find('a')['href'].split('/')[5]
    home_team = teams[1].find('a')['href'].split('/')[5]
    game_info_obj = GameInfo(home_team, away_team, home_line, home_line * -1, over_under)
    return(game_info_obj)

def get_game_info_list(week_num):
	"""
    get_game_info_list gets the basic betting info for a week of games.

    :param week_num: an int that represents what week number you want info from
    :return: a list of GameInfo objects
    """ 
    link = 'https://www.cbssports.com/nfl/scoreboard/all/2021/regular/' + str(week_num) + '/'
    with urllib.request.urlopen(link) as url:
        page = url.read()
    soup = BeautifulSoup(page, "html.parser")
    # list of game info boxes for all games
    score_boxes = soup.find_all('div', {'class':'live-update'})
    game_info_list = []
    for score_box in score_boxes:
        #print(score_box)
        game_info_list.append(get_game_info(score_box))
    return(game_info_list)

def get_game_result(t):
	"""
    get_game_result gets the results from a single game after it is completed.

    :param t: a div html block with information on the final results of a game
    :return: a GameResults object
    """ 
    teams = t.find_all('a', {'class': 'team'})
    away_team = teams[0]['href'].split('/')[5]
    home_team = teams[1]['href'].split('/')[5]
    scores = t.find_all('td', {'class': 'total-score'})
    game_result_obj = GameResults(home_team, away_team, int(scores[1].text), int(scores[0].text))
    return(game_result_obj)

def get_game_result_list(week_num):
	"""
    get_game_result_list gets the results from a week of games.

    :param week_num: an int that represents what week number you want info from
    :return: a list of GameResults objects
    """ 
    link = 'https://www.cbssports.com/nfl/scoreboard/all/2021/regular/' + str(week_num) + '/'
    with urllib.request.urlopen(link) as url:
        page = url.read()
    soup = BeautifulSoup(page, "html.parser")
    t_list = soup.find_all('div', {'class': 'live-update'})
    game_result_list = []
    for t in t_list:
        game_result_list.append(get_game_result(t))
    return(game_result_list)

def get_fake_data():
    """
    get_fake_data creates a list of 16 GameInfo objects and a corresponding list of GameResults objects.

    :return: a tuple of a list of GameInfo objects and list of GameResults objects
    """ 
    # initiate possible values
    teams = ['HOU', 'CAR', 'JAC', 'ARI', 'NYG', 'ATL', 'DET', 'BAL', 'CLE', 'CHI', 'PIT', 'CIN', 'TEN', 'IND', 'KC', 'LAC', 'NE', 'NO', 'BUF', 'WAS', 'LV', 'MIA', 'DEN', 'NYJ', 'MIN', 'SEA', 'LAR', 'TB', 'SF', 'GB', 'DAL', 'PHI']
    spreads = list(np.arange(-10, 10, 0.5))
    over_unders = list(np.arange(33, 53, 0.5))
    scores = range(14, 42)
    # generate a full week of fake games
    fake_games_list = []
    fake_results_list = []
    for i in range(16):
        spread = random.choice(spreads)
        home_team = random.choice(teams)
        teams.remove(home_team)
        away_team = random.choice(teams)
        teams.remove(away_team)
        ou = random.choice(over_unders)
        fake_games_list.append(GameInfo(home_team, away_team, spread, -1 * spread, ou))
        fake_results_list.append(GameResults(home_team, away_team,
                                            random.choice(scores), random.choice(scores)))
    return(fake_games_list, fake_results_list)