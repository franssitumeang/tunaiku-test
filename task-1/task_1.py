import sys
import ConfigParser
import json


class GetDict:

    def __init__(self, config):
        self.config = config

    def get_dict(self):
        config = ConfigParser.SafeConfigParser()
        config.read(self.config)

        sections_dict = {}

        defaults = config.defaults()
        temp_dict = {}
        for key in defaults.iterkeys():
            temp_dict[key] = defaults[key]

        sections = config.sections()

        for section in sections:
            options = config.options(section)
            temp_dict = {}
            for option in options:
                temp_dict[option] = int(config.get(section, option))

            sections_dict[section] = temp_dict

        return sections_dict


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'Must provide the path to the config file as the argument'
        sys.exit(1)

    GetDict = GetDict(sys.argv[1])
    config_dict = GetDict.get_dict()

    print json.dumps(config_dict, indent=2)
