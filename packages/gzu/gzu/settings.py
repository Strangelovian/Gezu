import logging, logging.handlers, configparser, sys, os


class Gzu:
    def init(rcfile):
        try:
            config = configparser.ConfigParser()
            config.read(rcfile)
            Gzu.GANDI_API_KEY = config['gandi']['api_key']
            Gzu.GANDI_ZONE_ID = int(config['gandi']['zone_id'])
            Gzu.GANDI_XMLRPC_URL = config['gandi']['xml_rpc_url']

            root = logging.getLogger()
            root.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

            logfile = os.path.expanduser(config['log']['path'])
            splat = os.path.splitext(logfile)
            handler = logging.handlers.RotatingFileHandler(splat[0] + ".debug" + splat[1], maxBytes=500 * 1024,
                                                           backupCount=10)
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            root.addHandler(handler)

            handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=50 * 1024, backupCount=10)
            handler.setFormatter(formatter)
            handler.setLevel(logging.INFO)
            root.addHandler(handler)

        except:
            print('init error:', sys.exc_info()[0])
            raise
