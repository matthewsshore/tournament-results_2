-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Create database called tournament, then connect to that database
create database tournament;
	\c tournament;

-- Create a table of players using
-- Id (tpye serial) and name (type text)

	CREATE TABLE players (
		id serial PRIMARY KEY,
		name text
		);


-- Create table of matches with winner and losers
-- Winner and Loser reference serial from players

	CREATE TABLE matches (
		winner serial REFERENCES players,
		loser serial REFERENCES players
		);


-- Create a view for number of matches for players
-- Order in descending order
-- Counts the winner/loser column using a join

	CREATE VIEW num_matches AS
		SELECT players.id, players.name, count(winner) AS num_matches 
		FROM players 
			LEFT JOIN matches ON players.id = winner OR players.id = loser 
			GROUP BY players.id
			ORDER BY num_matches DESC;

-- Create a view for number of wins for players
-- Order in descending order by wins
-- Counts the winner column using a join to get player ID

	CREATE VIEW num_wins AS
		SELECT players.id AS id, players.name, count(winner) AS num_wins
		FROM players 
			LEFT JOIN matches ON players.id = winner 
			GROUP BY players.id
			ORDER BY num_wins DESC;

-- Create a view for player standings
-- Order in descending order by wins then matches
-- Combines num_wins and num_matches

	CREATE VIEW player_standings AS
		SELECT num_matches.id, num_matches.name, num_wins.num_wins, num_matches.num_matches 
		FROM num_matches, num_wins 
		WHERE num_wins.id = num_matches.id 
		ORDER BY num_wins DESC, num_matches DESC


	

