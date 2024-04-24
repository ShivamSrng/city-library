import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class InsertAdminsData:
  """
  Inserts data into the ADMINS table
  """
  
  
  def __init__(self, connection: MySQLdb.Connection):
    self.database_utilities = DatabaseUtilities(
      connection=connection
    )
  

  def __create_admins_table(self) -> dict:
    """
    This method creates the ADMINS table
    
    Args:
      None
    
    Returns:
      dict: A dictionary containing the results of the query
    """
    
    query_to_create_admins_table = """
      CREATE TABLE IF NOT EXISTS ADMINS (
        ID VARCHAR(255) NOT NULL,
        PASSWORD VARCHAR(255) NOT NULL,

        CONSTRAINT ADMINS_PK 
        PRIMARY KEY (ID)
      );
    """
    return self.database_utilities.format_query_result(
      query=query_to_create_admins_table,
      description="Creating admins table"
    )
  

  def __insert_admins_data(self) -> dict:
    """
    This method inserts data into the ADMINS table
    
    Args:
      None
    
    Returns:
      dict: A dictionary containing the results of the query
    """
    
    query_to_insert_admins_data = """
      INSERT INTO ADMINS (ID, PASSWORD)
      VALUES ('shivam', 'sms323'), ('rohit', 'rp2247'), ('devarsh', 'dk629')
    """
    return self.database_utilities.format_query_result(
      query=query_to_insert_admins_data,
      description="Inserting admins data"
    )
  

  def execute(self) -> dict:
    """
    This method executes the requisite queries
    
    Args:
      None
    
    Returns:
      dict: A dictionary containing the results of the queries
    """
    
    result_create_admins_table = self.__create_admins_table()
    result_inserting_in_admins_table = self.__insert_admins_data()
    return {
      "result_create_admins_table": result_create_admins_table,
      "result_inserting_in_admins_table": result_inserting_in_admins_table
    }