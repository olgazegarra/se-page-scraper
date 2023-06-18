import configparser


class Configuration:
    def __init__(self, config_file) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_variable(self, section, variable):
        try:
            value = self.config.get(section, variable)
            return value
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None
