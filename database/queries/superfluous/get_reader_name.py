import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class GetReaderName:
  """
  Used to get the name of a reader from the database.
  """


  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.db__utilities = DatabaseUtilities(connection)
  

  def execute(self,
              reader_id: str) -> dict:
    """
    Get the name of the reader from the database.
    
    Args:
      reader_id (str): The id of the reader.
    
    Returns:
      dict: The name of the reader and other information.
    """

    query_to_get_reader_name = f"""
    SELECT RNAME
    FROM READER
    WHERE RID = '{reader_id}';
    """

    result_query_to_get_reader_name = self.db__utilities.format_query_result(
      query=query_to_get_reader_name,
      description="Get the name of the reader."
    )
    
    return result_query_to_get_reader_name
