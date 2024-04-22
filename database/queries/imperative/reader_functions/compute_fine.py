import re
import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class ComputeFine:
  """
  It computes the fine of a reader using the reader_id
  """


  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.dbutilities = DatabaseUtilities(connection)
  
  
  def execute(self, reader_id: str) -> dict:
    """
    Compute the fine of a reader using the reader_id
    
    Args:
      reader_id (int): It is the unique identifier of the reader
      
    Returns:
      dict: A dictionary containing the information of the fine
    """
    
    reader_exists_query = f"""
    SELECT *
    FROM READER AS R
    WHERE R.RID = '{reader_id}';
    """
    reader = self.dbutilities.format_query_result(
      query=reader_exists_query,
      description="Check if the reader exists"
    )
    
    if reader["query_result"] is None:
      return reader
    else:
      fine_query = f"""
      SELECT R.RID, R.RNAME, DOC.TITLE, BO.BDTIME, BO.RDTIME, GREATEST(DATEDIFF(BO.RDTIME, BO.BDTIME) - 20, 0) AS ADDITIONAL_DAYS_BORROWED, 0.2 * GREATEST(DATEDIFF(BO.RDTIME, BO.BDTIME) - 20, 0) AS FINE_IMPOSED
      FROM READER AS R, BORROWS AS B, BORROWING AS BO, COPY AS COP, DOCUMENT AS DOC
      WHERE R.RID = '002185055' AND R.RID = B.RID AND B.BOR_NO = BO.BOR_NO AND B.DOCID = COP.DOCID AND B.COPYNO = COP.COPYNO AND B.BID = COP.BID AND COP.DOCID = DOC.DOCID ;
      """
      fine = self.dbutilities.format_query_result(
        query=fine_query,
        description="Compute the fine of the reader"
      )
      return fine