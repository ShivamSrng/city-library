import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class ReservedDocument:
  """
  It retrieves the reserved document of a reader using the reader_id
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utils = DatabaseUtilities(connection=connection)
  

  def get_reserved_document(self, reader_id: str) -> dict:
    """
    Get the reserved document of a reader using the reader_id
    
    Args:
      reader_id (int): It is the unique identifier of the reader
      
    Returns:
      dict: A dictionary containing the information of the reserved document
    """
    
    reader_exists_query = f"""
    SELECT *
    FROM READER AS R
    WHERE R.RID = '{reader_id}';
    """
    reader = self.database_utils.format_query_result(
      query=reader_exists_query,
      description="Check if the reader exists"
    )
    
    if reader["query_result"] is None:
      reader["descriptive_error"] = "The reader does not exist."
      return reader
    else:
      reserved_document_query = f"""
      SELECT *
      FROM RESERVES AS RES
      WHERE RES.RID = '{reader_id}';
      """
      reserved_document = self.database_utils.format_query_result(
        query=reserved_document_query,
        description="Get the reserved document of the reader if any"
      )
      
      if reserved_document["query_result"] is None:
        reserved_document["descriptive_error"] = "The reader has not reserved any document yet."
        return reserved_document
      else:
        reserved_document_info_retrieval_query = f"""
        SELECT RES.RID, COP.COPYNO, COP.BID, DOC.TITLE, DOC.PDATE, PUB.PUBNAME
        FROM RESERVES AS RES, COPY AS COP, DOCUMENT AS DOC, PUBLISHER AS PUB
        WHERE RES.DOCID = COP.DOCID AND RES.COPYNO = COP.COPYNO AND RES.BID = COP.BID AND RES.DOCID = DOC.DOCID AND DOC.PUBLISHERID = PUB.PUBID AND RES.RID = '{reader_id}';
        """
        
        reserved_document_info = self.database_utils.format_query_result(
          query=reserved_document_info_retrieval_query,
          description="Get the information of the reserved document based on the reader_id"
        )
        return reserved_document_info