#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select count(*) from players;")
    result = c.fetchone()
    num_players = result[0]
    conn.close()
    return num_players


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    name = bleach.clean(name)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    conn = connect()
    c = conn.cursor()
    c.execute("select * from player_standings;")
    # Grabs data from the SQL query
    standings = [[int(row[0]), str(row[1]), int(row[2]), int(row[3])]
                 for row in c.fetchall()]
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = bleach.clean(winner)
    loser = bleach.clean(loser)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO matches (winner,loser) VALUES (%s, %s)",
                   (winner, loser,))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    conn = connect()
    c = conn.cursor()
    c.execute("select * from player_standings;")
    standings = [[int(row[0]), str(row[1]), int(row[2]), int(row[3])]
                 for row in c.fetchall()]
    # Finds number of players
    length = len(standings)
    # Determines number of matches needed
    matches_needed = length/2
    # Creates an empty matches array
    match_array = []
    y = 0
    # Loops through the players matching up
    # players who are next to eachother
    # Y acts as the iterator
    for x in range(0, matches_needed):
        match_array.append([standings[y][0], standings[y][1],
                           standings[y+1][0], standings[y+1][1]])
        y = y + 2
    conn.close()
    print match_array
    return match_array
