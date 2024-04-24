import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class CheckReaderExists:
  """
  Check if a reader exists in the database
  """
  
  def __init__(self, connection: MySQLdb.Connection):
    self.dbutilities = DatabaseUtilities(connection)

  def execute(self, reader_id: str):
    """
    Check if a reader exists in the database
    """
    query_to_check_if_reader_exists = f"""
      SELECT COUNT(*)
      FROM READER
      WHERE RID = '{reader_id}';
    """
    result = self.dbutilities.format_query_result(
        query=query_to_check_if_reader_exists,
        description="Check if reader exists"
    )
    if result["query_result"][0]["COUNT(*)"] == 0:
      result["descriptive_error"] = "Reader does not exist"
    return result
