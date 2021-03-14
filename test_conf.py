import configparser
config = configparser.ConfigParser()
config.read('config.py')
print(config['WINDGEOMETRY']['x_win'])