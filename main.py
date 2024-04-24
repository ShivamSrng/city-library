import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database_engine import DatabaseEngine

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
dbengine = DatabaseEngine()


@app.get("/")
def read_root() -> dict:
	"""
	Root endpoint that returns the status of the project
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the project name and its status
	"""
	return {
		"project": "City Library Management System",
		"status": "running"
	}


# ---------------------------------------------------------------#
# imperative
@app.get(
  path="/cityLibrary/reader/searchDocumentByDocumentId/{document_id}",
  tags=["imperative reader"],
  description="Get all documents that matches the given document_id",
)
def searchDocument(
	document_id: str,
):
	"""
	Search for a document using the document_id
	
	Args:
		document_id (str): The document_id to search for
		
	Returns:
		dict: A dictionary containing the document details
	"""
	return dbengine.searchDocumentByDocumentID(document_id)


@app.get(
  path="/cityLibrary/reader/searchDocumentByTitle/{title}",
  tags=["imperative reader"],
  description="Get all documents that matches the given title",
)
def searchDocumentByTitle(
	title: str,
):
	"""
	Search for a document using the title
	
	Args:
		title (str): The title to search for
	
	Returns:
		dict: A dictionary containing the document details
	"""
	return dbengine.searchDocumentByTitle(title)


@app.get(
	path="/cityLibrary/reader/searchDocumentByPublisherName/{publisher_name}",
	tags=["imperative reader"],
	description="Get all documents that matches the given publisher_name"
)
def searchDocumentByPublisherName(
	publisher_name: str,
):
	"""
	Search for a document using the publisher_name
	
	Args:
		publisher_name (str): The publisher_name to search for
	
	Returns:
		dict: A dictionary containing the document details
	"""
	return dbengine.searchDocumentByPublisherName(publisher_name)


@app.get(
	path="/cityLibrary/reader/checkoutDocument/{document_id}/{reader_id}",
	tags=["imperative reader"],
	description="Checkout a document from the library using the given parameters"
)
def checkoutDocument(
	document_id: str,
  copy_no: str,
  branch_id: str,
	reader_id: str,
):
	"""
	Checkout a document from the library using the given parameters
	
	Args:
		document_id (str): The document_id to checkout
		reader_id (str): The reader_id to checkout the document to
		copy_no (str): The copy_no of the document
		branch_id (str): The branch_id of the document
	
	Returns:
		dict: A dictionary containing the checkout details
	"""
	return dbengine.checkoutDocument(document_id, reader_id, copy_no, branch_id)


@app.get(
	path="/cityLibrary/reader/computeFine/{reader_id}",
	tags=["imperative reader"],
	description="Compute the fine of a reader using the reader_id"
)
def computeFine(
	reader_id: str,
):
	"""
	Compute the fine of a reader using the reader_id
	
	Args:
		reader_id (str): The reader_id to compute the fine for
	
	Returns:
		dict: A dictionary containing the fine details
	"""
	return dbengine.computeFine(reader_id)


@app.get(
	path="/cityLibrary/reader/getReservedDocument/{reader_id}",
	tags=["imperative reader"],
	description="Get the reserved document of a reader using the reader_id"
)
def getReservedDocument(
	reader_id: str,
):
	"""
	Get the reserved document of a reader using the reader_id

	Args:
		reader_id (str): The reader_id to get the reserved document for
	
	Returns:
		dict: A dictionary containing the reserved document details
	"""
	return dbengine.getReservedDocument(reader_id)


@app.get(
	path="/cityLibrary/reader/reserveDocument/{reader_id}/{document_id}/{copy_no}/{branch_id}",
	tags=["imperative reader"],
	description="Reserve a document using the given parameters"
)
def reserveDocument(
	reader_id: str,
	document_id: str,
	copy_no: str,
	branch_id: str,
):
	"""
	Reserve a document using the given parameters
	
	Args:
		reader_id (str): The reader_id to reserve the document for
		document_id (str): The document_id to reserve
		copy_no (str): The copy_no of the document
		branch_id (str): The branch_id of the document
	
	Returns:
		dict: A dictionary containing the reserve details
	"""
	return dbengine.reserveDocument(reader_id, document_id, copy_no, branch_id)


@app.get(
	path="/cityLibrary/reader/returnDocument/{bor_no}/{docid}/{copyno}/{bid}",
	tags=["imperative reader"],
	description="Return a document using the given parameters"
)
def returnDocument(
	bor_no: str,
	docid: str,
	copyno: str,
	bid: str,
):
	"""
	Return a document using the given parameters
	
	Args:
		bor_no (str): The bor_no to return the document for
		docid (str): The docid to return
		copyno (str): The copyno of the document
		bid (str): The bid of the document
	
	Returns:
		dict: A dictionary containing the return details
	"""
	return dbengine.returnDocument(bor_no, docid, copyno, bid)


@app.get(
	path="/cityLibrary/reader/getDocumentByPublisherNameConstrained/{publisher_name}",
	tags=["imperative reader"],
	description="Get all documents that matches the given publisher_name"
)
def getDocumentByPublisherNameConstrained(
	publisher_name: str,
):
	"""
	Get all documents that matches the given publisher_name
	
	Args:
		publisher_name (str): The publisher_name to search for
	
	Returns:
		dict: A dictionary containing the document details
	"""
	return dbengine.getDocumentByPublisherNameConstrained(publisher_name)



@app.get(
	path="/cityLibrary/admin/validation/{username}/{password}",
	tags=["imperative admin"],
	description="Validate the admin using the given parameters"
)
def validation(
	username: str,
	password: str,
):
	"""
	Validate the admin using the given parameters
	
	Args:
		username (str): The username to validate
		password (str): The password to validate
	
	Returns:
		dict: A dictionary containing the validation details
	"""
	return dbengine.validateAdminData(username, password)

@app.get(
	path="/cityLibrary/admin/addDocumentCopy/{document_id}/{branch_id}",
	tags=["imperative admin"],
	description="Add a copy of a document to a branch using the given parameters"
)
def addDocumentCopy(
	document_id: str,
	branch_id: str,
):
	"""
	Add a copy of a document to a branch using the given parameters
	
	Args:
		document_id (str): The document_id to add a copy to
		branch_id (str): The branch_id to add the copy to
	
	Returns:
		dict: A dictionary containing the add copy details
	"""
	return dbengine.addDocumentCopy(document_id, branch_id)


@app.get(
	path="/cityLibrary/admin/searchDocumentCopy/{document_id}/{copy_id}/{bid}",
	tags=["imperative admin"],
	description="Search for a document copy using the given parameters"
)
def searchDocumentCopy(
	document_id: str,
	copy_id: str,
	bid: str,
):
	"""
	Search for a document copy using the given parameters
	
	Args:
		document_id (str): The document_id to search for
		copy_id (str): The copy_id to search for
		bid (str): The branch_id to search for
	
	Returns:
		dict: A dictionary containing the metadata of the document copy
	"""
	return dbengine.searchDocumentCopy(document_id, copy_id, bid)


@app.get(
	path="/cityLibrary/admin/addReader/{reader_name}/{reader_type}/{reader_address}/{reader_phone}",
	tags=["imperative admin"],
	description="Add a reader to the database using the given parameters"
)
def addReader(
	reader_name: str,
	reader_type: str,
	reader_address: str,
	reader_phone: str,
):
	"""
	Add a reader to the database using the given parameters
	
	Args:
		reader_name (str): The reader_name to add
		reader_address (str): The reader_address to add
		reader_phone (str): The reader_phone to add
	
	Returns:
		dict: A dictionary containing the add reader details
	"""
	return dbengine.addReader(reader_name, reader_type, reader_address, reader_phone)


@app.get(
	path="/cityLibrary/admin/retrieveBranchInformation/{branch_id}",
	tags=["imperative admin"],
	description="Retrieve the branch information using the given branch_id"
)
def retrieveBranchInformation(
	branch_id: str,
):
	"""
	Retrieve the branch information using the given branch_id
	
	Args:
		branch_id (str): The branch_id to retrieve the information for
	
	Returns:
		dict: A dictionary containing the branch information
	"""
	return dbengine.retrieveBranchInformation(branch_id)


@app.get(
	path="/cityLibrary/admin/computeFineCollectedByBranch/{startdatetime}/{enddatetime}/{branch_id}",
	tags=["imperative admin"],
	description="Get a start date S and an end date E as input and print, for each branch, the branch Id and name and the average fine paid by the borrowers for documents borrowed from this branch during the corresponding period of time."
)
def computeFineCollectedByBranch(
	startdatetime: str,
	enddatetime: str,
	branch_id: str,
):
	"""
	Get a start date S and an end date E as input and print, for each branch, the branch Id and name and the average fine paid by the borrowers for documents borrowed from this branch during the corresponding period of time.
	
	Args:
		startdatetime (str): The startdatetime to compute the fine collected for
		enddatetime (str): The enddatetime to compute the fine collected for
		branch_id (str): The branch_id to compute the fine collected for
	
	Returns:
		dict: A dictionary containing the fine collected details
	"""
	return dbengine.computeFineCollectedByBranch(startdatetime=startdatetime, enddatetime=enddatetime, branchid=branch_id)


@app.get(
	path="/cityLibrary/admin/mostFrequentBorrowersOfLibrary/{limit}/{library_name}",
	tags=["imperative admin"],
	description="Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed."
)
def mostFrequentBorrowersOfLibrary(
	limit: int,
	library_name: str,
):
	"""
	Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed.
	
	Args:
		limit (int): The limit to get the most frequent borrowers of the library
		library_name (str): The library name to get the most frequent borrowers of the library
	
	Returns:
		dict: A dictionary containing the most frequent borrowers of the library
	"""
	return dbengine.mostFrequentBorrowersOfLibrary(limit, library_name)


@app.get(
	path="/cityLibrary/admin/mostPopularBookInLibraryInYear/{year}/{library_name}",
	tags=["imperative admin"],
	description="Get a year as input and print the 10 most popular books of that year in the library."
)
def mostPopularBookInLibraryInYear(
	year: int,
	library_name: str,
):
	"""
	Get a year as input and print the 10 most popular books of that year in the library.
	
	Args:
		year (int): The year to get the most popular book in the library
		library_name (str): The name of the library to get the most popular book in the year
	
	Returns:
		dict: A dictionary containing the metadata of the most popular book in the library in a year
	"""
	return dbengine.mostPopularBookInLibraryInYear(year, library_name)


@app.get(
	path="/cityLibrary/admin/mostFrequentBorrowers/{limit}/{branch_no}",
	tags=["imperative admin"],
	description="Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed"
)
def mostFrequentBorrowers(
	limit: int,
	branch_no: str,
):
	"""
	Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed
	
	Args:
		limit (int): The limit to get the most frequent borrowing users
		branch_no (str): The branch_no to get the most frequent borrowing users
	
	Returns:
		dict: A dictionary containing the metadata of the most frequent borrowing users
	"""
	return dbengine.mostFrequentBorrowers(limit, branch_no)


@app.get(
	path="/cityLibrary/admin/mostBorrowedBooksInLibrary/{limit}/{library_name}",
	tags=["imperative admin"],
	description="Get number N as input and print the N most borrowed books in the library"
)
def mostBorrowedBooksInLibrary(
	limit: int,
	library_name: str,
):
	"""
	Get number N as input and print the N most borrowed books in the library
	
	Args:
		limit (int): The limit to get the most borrowed books in the library
		library_name (str): The library name to get the most borrowed books in the library
	
	Returns:
		dict: A dictionary containing the metadata of the most borrowed books in the library
	"""
	return dbengine.mostBorrowedBooksInLibrary(limit, library_name)


@app.get(
	path="/cityLibrary/admin/mostBorrowedBooksInBranch/{limit}/{branch_no}",
	tags=["imperative admin"],
	description="Get number N and branch number I as input and print the N most borrowed books in branch I"
)
def mostBorrowedBooksInBranch(
	limit: int,
	branch_no: str,
):
	"""
	Get number N and branch number I as input and print the N most borrowed books in branch I
	
	Args:
		limit (int): The limit to get the most frequently borrowing users
		branch_no (str): The branch_no to get the most frequently borrowing users
	
	Returns:
		dict: A dictionary containing the metadata of the most frequently borrowing users
	"""
	return dbengine.mostBorrowedBooksInBranch(limit, branch_no)
# ---------------------------------------------------------------#


# ---------------------------------------------------------------#
# requisite

@app.get(
	path="/cityLibrary/insertAdminsData",
	tags=["requisite"],
	description="Insert data into the ADMINS table"
)
def insertAdminsData():
	"""
	Insert data into the ADMINS table
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database after inserting the data
	"""
	return dbengine.insertAdminsData()


@app.get(
	path="/cityLibrary/createAndPopulateDatabase", 
	tags=["requisite"], 
	description="Newly create and populate all tables in the database using random data"
)
def newlycreateAndPopulateDatabase():
	"""
	Newly create and populate all tables in the database using random data
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database after clearing, creating and populating the tables
	"""
	clear_metadata = dbengine.clearDatabase()
	table_metadata = dbengine.prepareDatabase()
	populate_metadata = dbengine.populateAllTables()
	return {
			"clear_metadata": clear_metadata,
			"table_metadata": table_metadata, 
			"populate_metadata": populate_metadata,
	}


@app.get(
	path="/cityLibrary/createTables", 
	tags=["requisite"], 
	description="Create all tables in the database"
)
def createTables():
	"""
	Create all tables in the database
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database after creating the tables
	"""
	return dbengine.prepareDatabase()


@app.get(
  path="/cityLibrary/populateAllTables", 
  tags=["requisite"], 
  description="Populate all tables in the database using random data"
)
def populateAllTables():
	"""
	Populate all tables in the database using random data
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database after populating the tables
	"""
	return dbengine.populateAllTables()


# ---------------------------------------------------------------#-


# ---------------------------------------------------------------#-
# superfluous
@app.get(
  path="/cityLibrary/showAllTables", 
  tags=["superfluous"], 
  description="Show all tables in the database along with the number of records in each table"
)
def showAllTables():
	"""
	Show all tables in the database along with the number of records in each table
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database
	"""	
	return dbengine.showAllTables()


@app.get(
  path="/cityLibrary/clearDatabase", 
  tags=["superfluous"], 
  description="Clear all tables in the database"
)
def clearDatabase():
	"""
	Clear all tables in the database
	
	Args:
		None
	
	Returns:
		dict: A dictionary containing the metadata of the database after clearing the tables
	"""
	return dbengine.clearDatabase()


# ---------------------------------------------------------------#-


if __name__ == "__main__":
    uvicorn.run(
      app="main:app", 
      reload=True, 
    	host="localhost", 
      port=8000
    )