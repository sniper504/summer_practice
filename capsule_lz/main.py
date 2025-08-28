from Playstation import PlayerStats


def main():
    
    file_path = 'playstation_players.csv'
    stats = PlayerStats(file_path)
    stats.plot_country_distribution()

if __name__ == "main":
    main()