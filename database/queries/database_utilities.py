import re
import MySQLdb


class DatabaseUtilities:
  """
  It contains the utility functions for the database
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
  

  def format_query_result(self,
                          query: str,
                          description: str) -> dict:
    """
    Used to format the query result in a dictionary format

    Args:
      query (str): The query to execute
      description (str): The description of the query

    Returns:
      dict: A dictionary containing the query, description and the result
    """

    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      result = cursor.fetchall()
      self.connection.commit()
      if len(result) == 0 or result is None:
        return {
          "query": re.sub(' +', ' ', query.replace("\n", "").replace("\t", "").strip()),
          "description": description,
          "query_result": None
        }
      field_names = [col[0] for col in cursor.description]
      formatted_result = [
        dict(zip(field_names, row))
        for row in result
      ]
      return {
        "query": re.sub(' +', ' ', query.replace("\n", "").replace("\t", "").strip()),
        "description": description,
        "query_result": formatted_result if formatted_result else True
      }
    except MySQLdb.Error as e:
      return {
        "query": re.sub(' +', ' ', query.replace("\n", "").replace("\t", "").strip()),
        "error": str(e),
      }