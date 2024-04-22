import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class SearchDocument:
  """
  It searches for a document in the database using the given parameters
  """
  
  
  def __init__(self, connection: MySQLdb.Connection):
    self.connection = connection
    self.dbutilities = DatabaseUtilities(connection)
  

  def by_documentID(self,
                    document_id: str) -> dict:
    """
    Search for a document in the database using the given parameters
    
    Args:
      document_id (int): It is the unique identifier of the document
    
    Returns:
      dict: A dictionary containing the information of the document
    """

    search_document_query = f"""
    SELECT *
    FROM DOCUMENT AS DOC
    WHERE DOC.DOCID = '{document_id}';
    """
    document = self.dbutilities.format_query_result(
      query=search_document_query,
      description="Search for a document by Document ID"
    )
    return document


  def by_title(self,
              title: str) -> dict:
    """
    Search for a document in the database using the given parameters
    
    Args:
      title (str): It is the title of the document
    
    Returns:
      dict: A dictionary containing the information of the document
    """

    search_document_query = f"""
    SELECT *
    FROM DOCUMENT AS DOC
    WHERE DOC.TITLE = '{title}';
    """
    document = self.dbutilities.format_query_result(
      query=search_document_query,
      description="Search for a document by Title"
    )
    return document
  

  def by_publisher_name(self,
                        publisher_name: str) -> dict:
    """
    Search for a document in the database using the given parameters
    
    Args:
      publisher_name (str): It is the name of the publisher
    
    Returns:
      dict: A dictionary containing the information of the document
    """

    search_document_query = f"""
    SELECT DOC.*
    FROM DOCUMENT AS DOC, PUBLISHER AS PUB
    WHERE DOC.PUBLISHERID = PUB.PUBID AND PUB.PUBNAME = '{publisher_name}';
    """
    document = self.dbutilities.format_query_result(
      query=search_document_query,
      description="Search for a document by Publisher Name"
    )
    return document
  

  def by_publisher_name_constrained(self,
                                    publisher_name: str) -> dict:
    """
    Search for a document in the database using the given parameters
    
    Args:
      publisher_name (str): It is the name of the publisher
    
    Returns:
      dict: A dictionary containing the information of the document
    """

    search_document_query = f"""
    SELECT DOC.DOCID, DOC.TITLE
    FROM DOCUMENT AS DOC, PUBLISHER AS PUB
    WHERE DOC.PUBLISHERID = PUB.PUBID AND PUB.PUBNAME = '{publisher_name}';
    """
    document = self.dbutilities.format_query_result(
      query=search_document_query,
      description="Search for a document by Publisher Name and get only the Document ID and Title"
    )
    return document