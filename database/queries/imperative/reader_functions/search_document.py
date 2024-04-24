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

    query_check_document_id = f"""
    SELECT COUNT(*)
    FROM DOCUMENT AS DOC
    WHERE DOC.DOCID = '{document_id}';
    """
    result_document_id_exists = self.dbutilities.format_query_result(
      query=query_check_document_id,
      description="Check if the Document ID exists"
    )
    if result_document_id_exists["query_result"][0]["COUNT(*)"] == 0:
      result_document_id_exists["descriptive_error"] = f"Document with ID as '{document_id}' does not exist"
      return result_document_id_exists
    
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

    query_check_title = f"""
    SELECT COUNT(*)
    FROM DOCUMENT AS DOC
    WHERE DOC.TITLE = '{title}';
    """
    result_title_exists = self.dbutilities.format_query_result(
      query=query_check_title,
      description="Check if the Title exists"
    )
    if result_title_exists["query_result"][0]["COUNT(*)"] == 0:
      result_title_exists["descriptive_error"] = f"Document with Title as '{title}' does not exist"
      return result_title_exists
    
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
    query_check_publisher_name = f"""
    SELECT COUNT(*)
    FROM PUBLISHER AS PUB
    WHERE PUB.PUBNAME = '{publisher_name}';
    """
    result_publisher_name_exists = self.dbutilities.format_query_result(
      query=query_check_publisher_name,
      description="Check if the Publisher Name exists"
    )
    if result_publisher_name_exists["query_result"][0]["COUNT(*)"] == 0:
      result_publisher_name_exists["descriptive_error"] = f"No document exists for the Publisher Name as '{publisher_name}'"
      return result_publisher_name_exists
    
    search_document_query = f"""
    SELECT DOC.*, PUB.PUBNAME
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
    query_check_publisher_name = f"""
    SELECT COUNT(*)
    FROM PUBLISHER AS PUB
    WHERE PUB.PUBNAME = '{publisher_name}';
    """
    result_publisher_name_exists = self.dbutilities.format_query_result(
      query=query_check_publisher_name,
      description="Check if the Publisher Name exists"
    )
    if result_publisher_name_exists["query_result"][0]["COUNT(*)"] == 0:
      result_publisher_name_exists["descriptive_error"] = f"No document exists for the Publisher Name as '{publisher_name}'"
      return result_publisher_name_exists
    
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