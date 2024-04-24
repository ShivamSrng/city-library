import sys
import MySQLdb
from database.consts import MYSQLConstants, FakeDataConstants

# imperative
from database.queries.imperative.reader_functions.search_document import SearchDocument
from database.queries.imperative.reader_functions.document_checkout import DocumentCheckout
from database.queries.imperative.reader_functions.document_return import DocumentReturn
from database.queries.imperative.reader_functions.document_reserve import DocumentReserve
from database.queries.imperative.reader_functions.reserved_documents import ReservedDocument
from database.queries.imperative.reader_functions.compute_fine import ComputeFine

from database.queries.imperative.administrative_functions.validate_admin_data import ValidateAdminData
from database.queries.imperative.administrative_functions.add_document_copy import AddDocumentCopy
from database.queries.imperative.administrative_functions.search_document_copy import SearchDocumentCopy
from database.queries.imperative.administrative_functions.add_reader import AddReader
from database.queries.imperative.administrative_functions.retrieve_branch_information import RetrieveBranchInformation
from database.queries.imperative.administrative_functions.most_borrowed_books_in_branch import MostBorrowedBooksInBranch
from database.queries.imperative.administrative_functions.compute_fine_collected_by_branch import ComputeFineCollectedByBranch
from database.queries.imperative.administrative_functions.most_borrowed_books_in_library import MostBorrowedBooksInLibrary
from database.queries.imperative.administrative_functions.most_frequently_borrowers import MostFrequentlyBorrowers
from database.queries.imperative.administrative_functions.most_popular_book_in_library_in_year import MostPopularBookInLibraryInYear
from database.queries.imperative.administrative_functions.most_frequent_borrowers_of_library import MostFrequentBorrowersOfLibrary


# requisite
from database.queries.requisite.table_creation import TableCreation
from database.queries.requisite.insert_admins_data import InsertAdminsData
from database.queries.requisite.populate_all_tables import PopulateAllTables

# superfluous
from database.queries.superfluous.show_all_tables import ShowAllTables
from database.queries.superfluous.clear_database import ClearDatabase


class DatabaseEngine:
  """
  Used to interact with the MySQL Local Database
  """
  
  
  def __init__(self) -> None:
    self.mysql_constants = MYSQLConstants()
    self.fake_data_constants = FakeDataConstants()
    self.connection = self.__establishConnection()
  

  def __establishConnection(self) -> MySQLdb.Connection:
    """
    Used to establish connection to the MySQL Local Database
    
    Args:
      None
    
    Returns:
      MySQLdb.Connection: The connection object to the MySQL Local Database
    """
    
    try:
      mysql_constants = self.mysql_constants.getMySQLConfig()
      self.connection = MySQLdb.connect(
        host=mysql_constants['host'],
        user=mysql_constants['user'],
        password=mysql_constants['password'],
        database=mysql_constants['database']
      )
      print("Connection to MySQL Local Database established successfully")
      return self.connection
    except MySQLdb.DatabaseError as e:
      self.connection = MySQLdb.connect(
        host=mysql_constants['host'],
        user=mysql_constants['user'],
        password=mysql_constants['password']
      )
      cursor = self.connection.cursor()
      cursor.execute(f"CREATE DATABASE {mysql_constants['database']}")
      cursor.execute(f"USE {mysql_constants['database']}")
      cursor.close()
    except Exception as e:
      print(f"Error in establishing connection to MySQL Local Database. A possible reason could be that the MySQL server is not running or the credentials are incorrect. Please check the error below:\n{e}")
      sys.exit(1)


  def insertAdminsData(self) -> dict:
    """
    Used to insert the admins data into the ADMINS table
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    return InsertAdminsData(self.connection).execute()
  

  def prepareDatabase(self) -> dict:
    """
    Used to prepare the database by creating the tables
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    InsertAdminsData(self.connection).execute()
    return TableCreation(self.connection).create_tables()


  def populateAllTables(self) -> dict:
    """
    Used to populate all the tables in the database with random data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    InsertAdminsData(self.connection).execute()
    return PopulateAllTables(self.connection, self.fake_data_constants.getFakeDataConfig()).insert_random_data()
  

  def clearDatabase(self) -> dict:
    """
    Used to clear all the tables in the database
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    return ClearDatabase(self.connection).execute()


  def showAllTables(self) -> dict:
    """
    Used to show all the tables in the database
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    return ShowAllTables(self.connection).execute()
  

  def searchDocumentByDocumentID(self, document_id: str) -> dict:
    """
    Used to search a document by its document_id

    Args:
      document_id (str): The document_id to search for
    
    Returns:
      dict: A dictionary containing the document details
    """

    return SearchDocument(self.connection).by_documentID(document_id)
  

  def searchDocumentByTitle(self, title: str) -> dict:
    """
    Used to search a document by its title
    
    Args:
      title (str): The title to search for
    
    Returns:
      dict: A dictionary containing the document details
    """
    
    return SearchDocument(self.connection).by_title(title)
  

  def searchDocumentByPublisherName(self, publisher_name: str) -> dict:
    """
    Used to search a document by its publisher_name

    Args:
      publisher_name (str): The publisher_name to search for
    
    Returns:
      dict: A dictionary containing the document details
    """

    return SearchDocument(self.connection).by_publisher_name(publisher_name)
  

  def checkoutDocument(self, document_id: str, reader_id: str, copy_no: str, branch_id: str) -> dict:
    """
    Used to checkout a document from the library using the given parameters
    
    Args:
      document_id (str): The document_id to checkout
      reader_id (str): The reader_id to checkout
      copy_no (str): The copy_no to checkout
      branch_id (str): The branch_id to checkout
    
    Returns:
      dict: A dictionary containing the checkout details
    """
    
    return DocumentCheckout(self.connection).checkout_document(document_id, reader_id, copy_no, branch_id)
  

  def getReservedDocument(self, reader_id: str) -> dict:
    """
    Used to get the reserved document for a reader
    
    Args:
      reader_id (str): The reader_id to get the reserved document for
    
    Returns:
      dict: A dictionary containing the reserved document details
    """
    
    return ReservedDocument(self.connection).get_reserved_document(reader_id)


  def reserveDocument(self, reader_id: str, document_id: str, copy_no: str, branch_id: str) -> dict:
    """
    Used to reserve a document for a reader
    
    Args:
      reader_id (str): The reader_id to reserve the document for
      document_id (str): The document_id to reserve
      copy_no (str): The copy_no to reserve
      branch_id (str): The branch_id to reserve
    
    Returns:
      dict: A dictionary containing the reservation details
    """

    return DocumentReserve(self.connection).execute(reader_id, document_id, copy_no, branch_id)


  def returnDocument(self, bor_no: str, docid: str, copyno: str, bid: str) -> dict:
    """
    Used to return a document to the library
    
    Args:
      bor_no (str): The bor_no to return the document for
      docid (str): The docid to return
      copyno (str): The copyno to return
      bid (str): The bid to return
    
    Returns:
      dict: A dictionary containing the return details
    """

    return DocumentReturn(self.connection).execute(bor_no, docid, copyno, bid)
  

  def validateAdminData(self, username: str, password: str) -> bool:
    """
    Used to validate the admin data
    
    Args:
      username (str): The username to validate
      password (str): The password to validate
    
    Returns:
      bool: A boolean indicating if the admin data is valid or not
    """

    return ValidateAdminData(self.connection).execute(username, password)

  def getDocumentByPublisherNameConstrained(self, publisher_name: str) -> dict:
    """
    Used to get the document by publisher_name constrained  

    Args:
      publisher_name (str): The publisher_name to search for
    
    Returns:
      dict: A dictionary containing the document details
    """

    return SearchDocument(self.connection).by_publisher_name_constrained(publisher_name)
  

  def computeFine(self, reader_id: str) -> dict:
    """
    Used to compute the fine for a reader

    Args:
      reader_id (str): The reader_id to compute the fine for
    
    Returns:
      dict: A dictionary containing the fine details
    """

    return ComputeFine(self.connection).execute(reader_id)
  

  def addDocumentCopy(self, document_id: str, branch_id: str) -> dict:
    """
    Used to add a document copy to the library

    Args:
      document_id (str): The document_id to add a copy for
      branch_id (str): The branch_id to add a copy for
    
    Returns:
      dict: A dictionary containing the add copy details
    """

    return AddDocumentCopy(self.connection).execute(document_id, branch_id)
  

  def searchDocumentCopy(self, document_id: str, copy_id: str, bid: str) -> dict:
    """
    Used to search for a document copy in the database

    Args:
      document_id (str): The document copy ID to search for
      copy_id (str): The copy ID to search for
      bid (str): The branch ID to search for
      
    Returns:
      dict: A dictionary containing the metadata of the document copy
    """
    
    return SearchDocumentCopy(self.connection).searchDocumentCopy(document_id, copy_id, bid)

  def addReader(self, reader_name: str, reader_type: str, reader_address: str, reader_phone: str) -> dict:
    """
    Used to add a reader to the library

    Args:
      reader_name (str): The reader_name to add
      reader_type (str): The reader_type to add
      reader_address (str): The reader_address to add
      reader_phone (str): The reader_phone to add
    
    Returns:
      dict: A dictionary containing the add reader details
    """

    return AddReader(self.connection).execute(reader_name, reader_type, reader_address, reader_phone)


  def retrieveBranchInformation(self, branch_id: str) -> dict:
    """
    Used to retrieve the branch information from the database

    Args:
      branch_id (str): The branch_id to retrieve the information for

    Returns:
      dict: A dictionary containing the branch information
    """

    return RetrieveBranchInformation(self.connection).execute(branch_id)
  

  def mostBorrowedBooksInBranch(self, limit: int, branch_no: str) -> dict:
    """
    Used to get the most borrowed books in a branch

    Args:
      limit (int): The limit to get the most borrowed books
      branch_no (str): The branch_no to get the most borrowed books
    
    Returns:
      dict: A dictionary containing the metadata of the most borrowed books
    """

    return MostBorrowedBooksInBranch(self.connection).execute(limit, branch_no)
  

  def computeFineCollectedByBranch(self, startdatetime: str, enddatetime: str) -> dict:
    """
    Get a start date S and an end date E as input and print, for each branch, the branch Id and name and the average fine paid by the borrowers for documents borrowed from this branch during the corresponding period of time.

    Args:
      branch_no (str): The branch_no to compute the fine collected for
    
    Returns:
      dict: A dictionary containing the fine collected details
    """

    return ComputeFineCollectedByBranch(self.connection).execute(startdatetime, enddatetime)
  

  def mostBorrowedBooksInLibrary(self, limit: int, library_name: str) -> dict:
    """
    Used to get the most borrowed books in the library

    Args:
      limit (int): The limit to get the most borrowed books
      library_name (str): The library name to get the most borrowed books
    
    Returns:
      dict: A dictionary containing the metadata of the most borrowed books
    """

    return MostBorrowedBooksInLibrary(self.connection).execute(limit, library_name)
  

  def mostFrequentBorrowers(self, limit: int, branch_no: str) -> dict:
    """
    Used to get the most frequently borrowing users

    Args:
      limit (int): The limit to get the most frequently borrowing users
      branch_no (str): The branch_no to get the most frequently borrowing users
    
    Returns:
      dict: A dictionary containing the metadata of the most frequently borrowing users
    """

    return MostFrequentlyBorrowers(self.connection).execute(limit, branch_no)
  

  def mostPopularBookInLibraryInYear(self, year: int) -> dict:
    """
    Used to get the most popular book in the library in a year

    Args:
      year (int): The year to get the most popular book in the library
    
    Returns:
      dict: A dictionary containing the metadata of the most popular book in the library in a year
    """

    return MostPopularBookInLibraryInYear(self.connection).execute(year)
  

  def mostFrequentBorrowersOfLibrary(self, limit: int, library_name: str) -> dict:
    """
    Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed.

    Args:
      limit (int): The limit to get the most frequent borrowers of the library
      library_name (str): The library name to get the most frequent borrowers of the library
    
    Returns:
      dict: A dictionary containing the metadata of the most frequent borrowers of the library
    """

    return MostFrequentBorrowersOfLibrary(self.connection).execute(limit, library_name)