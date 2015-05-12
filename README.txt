README Tournament Challenge


Functions with their intended parameters:
1) connect()
2) deleteMatches()
3) deletePlayers()
4) countPlayers()
5) registerPlayers(name) - name should be text
6) playerStandings()
7) reportMatch(winner, loser) - winner and loser are names (i.e. text)
8) swissPairings()

In tournament SQL the following tables are created:
1) Players - list of player names and a unique ID
2) Matches - list of matches taken place so far (ID of Winner - ID of Loser)


In tournament SQL the following views are created:
1) num_matches - number of matches each player has has (ID - NAME - num_matches)
2) num_wins - number of wins each player has has (ID - Name - Wins)
3) player_standings - the rankings of the tournament (ID - Name - Wins - Matches)


Running the Function:
1) Install Vagrant and Virtualbox
2) Clone the nano degree repository
3) Launch the Vagrant VM
4) Use the command pqsl forum to get into a database
5) Run the command “create database tournament;” to create the database tournament
6) Next we will import the SQL file, run the command “\i tournament.sql;”  This should then create 2 tables and 3 views.
7) Use the command \q to exit the database
8) Now we can run our program using the command “python tournament_test.py”

