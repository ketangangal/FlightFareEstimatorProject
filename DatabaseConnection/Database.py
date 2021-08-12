from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from CustomLogger.logger import Logger

logging = Logger('logFiles/test.log')

class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database when backend thread runs.
        """
        logging.info('INFO', 'Obj created')
        self.Client_id = 'fJFFnobyYrTUBsXcJpRWqJaE'
        self.Client_secret = 'QdOylwGMQyYm4m97DGhMARHWC2lETI4F.uwyNl4gq_ZT8fC8nfdkUro3KiA9C+CYtORBtJ9rxcJyC5dK+vO-pa6X_KtaBsg5hF4,xiJsMbEHbdq86qwR1B500wEFt1Zj'
        cloud_config = {'secure_connect_bundle': 'secure-connect-flightdatabase.zip'}
        auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()

    def master(self):
        """
        :DESC: Creates table if not existed into database
        :return:
        """
        self.session.execute("use flighpricedata")
        self.session.execute("select release_version from system.local")
        self.session.execute("CREATE TABLE Data(id uuid PRIMARY KEY,Airline text,Source text,Destination text,Total_Stops text,Total_Duration int,Journey_month int,Journey_day int);")

    def addData(self, result):
        """
        :param result: Gets data from user and puts it into database
        :return:
        """
        logging.info('INFO', "Inside addData")
        logging.info('INFO', "Inside addData")

        column = "id, Airline, Source,Destination, Total_Stops, Total_Duration, Journey_month, Journey_day"
        value = "{0},'{1}','{2}','{3}','{4}',{5},{6},{7}".format('uuid()', result['Airline'], result['Source'],
                                                                 result['Destination'], result['Total_Stops'],
                                                                 result['Total_Duration'], result['Journey_month'],
                                                                 result['Journey_day'])
        logging.info('INFO', "String created")
        custom = "INSERT INTO Data({}) VALUES({});".format(column, value)

        logging.info('INFO', "Key created")
        self.session.execute("USE flighpricedata")

        output = self.session.execute(custom)

        logging.info('INFO', "Column inserted {}".format(output))


    def getData(self):
        """
        :DESC: Retrieves Data from Database
        :return:
        """
        self.session.execute("use flighpricedata")
        row = self.session.execute("SELECT * FROM Data;")
        collection = []
        for i in row:
            collection.append(tuple(i))
        logging.info('INFO', "Retrieved Data from Database : {}".format(i))
        return tuple(collection)
