import configparser


class MYSQLConstants:
  """
  This class is used to get the MySQL configurations from the config.ini file.
  """


  def getMySQLConfig(self) -> dict:
    """
    Used to get the MySQL configurations from the config.ini file.
    
    Args:
      None
    
    Returns:
      dict: The MySQL configurations
    """
    
    config = configparser.ConfigParser()
    config.read('./database/config.ini')
    mysqlconfigurations =  config['MYSQL']
    
    return {
      'host': mysqlconfigurations['host'],
      'user': mysqlconfigurations['user'],
      'password': mysqlconfigurations['password'],
      'database': mysqlconfigurations['database']
    }


class FakeDataConstants:
  """
  This class is used to get the fake data configurations from the config.ini file.
  """


  def getFakeDataConfig(self) -> dict:
    """
    Used to get the fake data configurations from the config.ini file.
    
    Args:
      None
    
    Returns:
      dict: The fake data configurations
    """
    
    config = configparser.ConfigParser()
    config.read('./database/config.ini')
    fakedataconfigurations =  config['FAKEDATA']
    
    return {
      'fakedatainsertionlimit': fakedataconfigurations['fakedatainsertionlimit']
    }