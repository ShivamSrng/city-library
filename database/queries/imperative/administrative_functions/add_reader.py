import MySQLdb
from faker import Faker
from database.queries.database_utilities import DatabaseUtilities


class AddReader:
  """
  Used to add a reader to the database
  """
  
  
  def __init__(self, mysqlconnection: MySQLdb.Connection) -> None:
    self.connection = mysqlconnection
    self.database_utilities = DatabaseUtilities(mysqlconnection)
  

  def execute(self,
              reader_name: str,
              reader_type: str,
              reader_address: str,
              reader_phone: str) -> dict:
    """
    Used to add a reader to the database

    Args:
      reader_id (str): The reader_id to add
      reader_name (str): The reader_name to add
      reader_type (str): The reader_type to add
      reader_address (str): The reader_address to add
      reader_phone (str): The reader_phone to add

    Returns:
      dict: A dictionary containing the add reader details
    """

    fake_profile = Faker().profile()
    reader_id = fake_profile['ssn'].replace('-', '')
    check_if_reader_exists_query = f"""
    SELECT COUNT(*)
    FROM READER
    WHERE RID = '{reader_id}';
    """ 
    reader_exists_result = self.database_utilities.format_query_result(
      query=check_if_reader_exists_query,
      description="Check if the reader exists"
    )
    if reader_exists_result["query_result"][0]["COUNT(*)"] != 0:
      return reader_exists_result
    else:
      add_reader_query = f"""
      INSERT INTO READER (RID, RTYPE, RNAME, RADDRESS, PHONE_NO) VALUES ('{reader_id}', '{reader_type}', '{reader_name}', '{reader_address}', '{reader_phone}');
      """
      add_reader_result = self.database_utilities.format_query_result(
        query=add_reader_query,
        description="Add a reader to the database"
      )
      add_reader_result["new_reader_details"] = {
        "RID": reader_id,
        "RTYPE": reader_type,
        "RNAME": reader_name,
        "RADDRESS": reader_address,
        "PHONE_NO": reader_phone
      }
      return add_reader_result

