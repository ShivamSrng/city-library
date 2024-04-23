import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class SearchDocumentCopy:
  """
  Used to search for a document copy in the database
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def searchDocumentCopy(self,
                        document_id: str,
                        copy_id: str,
                        bid: str) -> dict:
    """
    Used to search for a document copy in the database
    
    Args:
      document_id (str): The document copy ID to search for
      copy_id (str): The copy ID to search for
      bid (str): The branch ID to search for
      
    Returns:
      dict: A dictionary containing the metadata of the document copy
    """
    
    check_copy_existance_query = f"""
    SELECT COUNT(*)
    FROM COPY COP
    WHERE COP.DOCID = '{document_id}' AND COP.COPYNO = '{copy_id}' AND COP.BID = '{bid}';
    """
    copy_exists = self.database_utilities.format_query_result(
      query=check_copy_existance_query,
      description="Check if the copy exists"
    )
    if copy_exists["query_result"][0]["COUNT(*)"] == 0:
      return copy_exists
    
    search_copy_query_in_borrows = f"""
    SELECT COUNT(*)
    FROM BORROWS BOR
    WHERE BOR.DOCID = '{document_id}' AND BOR.COPYNO = '{copy_id}' AND BOR.BID = '{bid}';
    """
    copy_borrowed = self.database_utilities.format_query_result(
      query=search_copy_query_in_borrows,
      description="Check if the copy is borrowed"
    )
    search_copy_query_in_reserves = f"""
    SELECT COUNT(*)
    FROM RESERVES RES
    WHERE RES.DOCID = '{document_id}' AND RES.COPYNO = '{copy_id}' AND RES.BID = '{bid}';
    """
    copy_reserved = self.database_utilities.format_query_result(
      query=search_copy_query_in_reserves,
      description="Check if the copy is reserved"
    )
    if "query_result" in copy_borrowed and copy_borrowed["query_result"][0]["COUNT(*)"] >= 1:
      search_query = f"""
      SELECT BOR.*, BORW.BDTIME, BORW.RDTIME
      FROM BORROWS BOR, BORROWING BORW
      WHERE BOR.DOCID = '{document_id}' AND BOR.COPYNO = '{copy_id}' AND BOR.BID = '{bid}' AND BOR.BOR_NO = BORW.BOR_NO;
      """
      return self.database_utilities.format_query_result(
        query=search_query,
        description="Search for the document copy"
      )
    
    elif "query_result" in copy_reserved and copy_reserved["query_result"][0]["COUNT(*)"] >= 1:
      search_query = f"""
      SELECT RES.*, RESV.DTIME
      FROM RESERVES RES, RESERVATION RESV
      WHERE RES.DOCID = '{document_id}' AND RES.COPYNO = '{copy_id}' AND RES.BID = '{bid}' AND RES.RESERVATION_NO = RESV.RES_NO;
      """
      return self.database_utilities.format_query_result(
        query=search_query,
        description="Search for the document copy"
      )
    else:
      search_query = f"""
      SELECT *
      FROM COPY
      WHERE DOCID = '{document_id}' AND COPYNO = '{copy_id}' AND BID = '{bid}';
      """
      return self.database_utilities.format_query_result(
        query=search_query,
        description="Search for the document copy, which is not borrowed or reserved"
      )