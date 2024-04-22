import re
import MySQLdb


class ClearDatabase:
  """
  Used to clear all the tables in the database
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection


  def __drop_database(self) -> str:
    """
    Used to drop the database
    
    Args:
      None
    
    Returns:
      str: The query to drop the database
    """
    
    drop_database_query = f"""
    DROP DATABASE CITY_LIBRARY;
    """
    cursor = self.connection.cursor()
    cursor.execute(drop_database_query)
    self.connection.commit()
    cursor.close()
    return re.sub(' +', ' ', drop_database_query.replace("\n", " ").strip())
  

  def __create_database(self) -> str:
    """
    Used to create the database
    
    Args:
      None
    
    Returns:
      str: The query to create the database
    """
    
    create_database_query = f"""
    CREATE DATABASE CITY_LIBRARY;
    """
    cursor = self.connection.cursor()
    cursor.execute(create_database_query)
    use_database_query = f"""
    USE CITY_LIBRARY;
    """
    cursor.execute(use_database_query)
    self.connection.commit()
    cursor.close()
    return re.sub(' +', ' ', create_database_query.replace("\n", " ").strip()), re.sub(' +', ' ', use_database_query.replace("\n", " ").strip())
  
  
  def execute(self) -> dict:
    """
    Used to clear all the tables in the database
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    drop_database_query = self.__drop_database()
    create_database_query, use_database_query = self.__create_database()

    return {
      "status": "success",
      "queries": {
        "drop_database": drop_database_query,
        "create_database": create_database_query,
        "use_database": use_database_query
      },
      "message": "All tables have been dropped successfully"
    }