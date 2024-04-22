import sys
from database.queries.superfluous.show_all_tables import ShowAllTables
from database.queries.requisite.prevent_chicken_egg import PreventChickenEgg


class TableCreation:
	"""
	Used to create all the tables in the database
	"""
	
	
	def __init__(self, connection):
		self.connection = connection
		self.already_present_tables = [str(table).upper() for table in ShowAllTables(connection).execute()["tables"]]
	

	def _query_executor(self, query: str):
		"""
		Used to execute a query

		Args:
			query (str): The query to be executed
		
		Returns:
			bool: True if the query is executed successfully, False otherwise
		"""
		
		try:
				with self.connection.cursor() as cursor:
						cursor.execute(query)
				self.connection.commit()
		except Exception as e:
				print(f"Error in executing query: {query}. Error: {e}")
				sys.exit(1)
	

	def __generate_person_table(self) -> dict:
		"""
		Used to create the PERSON table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "PERSON" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS PERSON(
			PID CHAR(9) NOT NULL,
			PNAME VARCHAR(64),
			
			CONSTRAINT PERSONPK
			PRIMARY KEY(PID)
		);
		"""
		self._query_executor(query)
		
		return {
			"status": "success",
			"message": "Person table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_reader_table(self) -> dict:
		"""
		Used to create the READER table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "READER" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS READER(
			RID CHAR(9) NOT NULL,
			RTYPE VARCHAR(64),
			RNAME VARCHAR(64),
			RADDRESS VARCHAR(1024),
			PHONE_NO VARCHAR(15) NOT NULL UNIQUE,

			CONSTRAINT READER_PK
			PRIMARY KEY(RID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Reader table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}


	def __generate_reservation_table(self) -> dict:
		"""
		Used to create the RESERVATION table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "RESERVATION" in self.already_present_tables:
			return
		
		query = """
		CREATE TABLE IF NOT EXISTS RESERVATION(
			RES_NO CHAR(9) NOT NULL,
			DTIME DATETIME,

			CONSTRAINT RESERVATION_PK
			PRIMARY KEY(RES_NO)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Reservation table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def _generate_borrowing_table(self) -> dict:
		"""
		Used to create the BORROWING table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "BORROWING" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS BORROWING(
			BOR_NO CHAR(9) NOT NULL,
			BDTIME DATETIME,
			RDTIME DATETIME,

			CONSTRAINT BORROWING_PK
			PRIMARY KEY(BOR_NO)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Borrowing table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_branch_table(self) -> dict:
		"""
		Used to create the BRANCH table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "BRANCH" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS BRANCH(
			BID CHAR(9) NOT NULL,
			BNAME VARCHAR(64),
			BLOCATION VARCHAR(1024),

			CONSTRAINT BRANCH_PK
			PRIMARY KEY(BID)
		);
		"""
		self._query_executor(query)
		
		return {
			"status": "success",
			"message": "Branch table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_publisher_table(self) -> dict:
		"""
		Used to create the PUBLISHER table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "PUBLISHER" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS PUBLISHER(
			PUBID CHAR(9) NOT NULL,
			PUBNAME VARCHAR(64),
			PUBADDRESS VARCHAR(1024),

			CONSTRAINT PUBLISHER_PK
			PRIMARY KEY(PUBID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Publisher table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_authors_table(self) -> dict:
		"""
		Used to create the AUTHORS table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "AUTHORS" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS AUTHORS(
			PID CHAR(9) NOT NULL,
			DOCID CHAR(9) NOT NULL,

			CONSTRAINT AUTHORS_PK
			PRIMARY KEY(PID, DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Authors table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_gedits_table(self) -> dict:
		"""
		Used to create the GEDITS table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "GEDITS" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS GEDITS(
			DOCID CHAR(9) NOT NULL,
			ISSUE_NO CHAR(9) NOT NULL,
			PID CHAR(9) NOT NULL,

			CONSTRAINT GEDITS_PK
			PRIMARY KEY(DOCID, ISSUE_NO, PID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Gedits table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_chairs_table(self) -> dict:
		"""
		Used to create the CHAIRS table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "CHAIRS" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS CHAIRS(
			PID CHAR(9) NOT NULL,
			DOCID CHAR(9) NOT NULL,

			CONSTRAINT CHAIRS_PK
			PRIMARY KEY(PID, DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Chairs table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}


	def __generate_book_table(self) -> dict:
		"""
		Used to create the BOOK table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "BOOK" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS BOOK(
			DOCID CHAR(9) NOT NULL,
			ISBN CHAR(20) NOT NULL UNIQUE,

			CONSTRAINT BOOK_PK
			PRIMARY KEY(DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Book table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_journal_issue_table(self) -> dict:
		"""
		Used to create the JOURNAL_ISSUE table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "JOURNAL_ISSUE" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS JOURNAL_ISSUE(
			DOCID CHAR(9) NOT NULL,
			ISSUE_NO CHAR(9) NOT NULL,
			SCOPE VARCHAR(1024),

			CONSTRAINT JOURNAL_ISSUE_PK
			PRIMARY KEY(DOCID, ISSUE_NO)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Journal Issue table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_proceedings_table(self) -> dict:
		"""
		Used to create the PROCEEDINGS table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "PROCEEDINGS" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS PROCEEDINGS(
			DOCID CHAR(9) NOT NULL,
			CDATE DATE,
			CLOCATION VARCHAR(1024),
			CEDITOR VARCHAR(2048) NOT NULL,

			CONSTRAINT PROCEEDINGS_PK
			PRIMARY KEY(DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Proceedings table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_journal_volume_table(self) -> dict:
		"""
		Used to create the JOURNAL_VOLUME table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "JOURNAL_VOLUME" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS JOURNAL_VOLUME(
			DOCID CHAR(9) NOT NULL,
			VOLUME_NO CHAR(9) NOT NULL,
			EDITOR CHAR(9) NOT NULL,

			CONSTRAINT JOURNAL_VOLUME_PK
			PRIMARY KEY(DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Journal Volume table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_document_table(self) -> dict:
		"""
		Used to create the DOCUMENT table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "DOCUMENT" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS DOCUMENT(
			DOCID CHAR(9) NOT NULL,
			TITLE VARCHAR(1024),
			PDATE DATE,
			PUBLISHERID CHAR(9) NOT NULL,

			CONSTRAINT DOCUMENT_PK
			PRIMARY KEY(DOCID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Document table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_copy_table(self) -> dict:
		"""
		Used to create the COPY table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "COPY" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS COPY(
			DOCID CHAR(9) NOT NULL,
			COPYNO CHAR(9) NOT NULL,
			BID CHAR(9) NOT NULL,
			POSITION VARCHAR(6),

			CONSTRAINT COPY_PK
			PRIMARY KEY(COPYNO, DOCID, BID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Copy table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_reserves_table(self) -> dict:
		"""
		Used to create the RESERVES table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "RESERVES" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS RESERVES(
			RID CHAR(9) NOT NULL,
			RESERVATION_NO CHAR(9) NOT NULL,
			DOCID CHAR(9) NOT NULL,
			COPYNO CHAR(9) NOT NULL,
			BID CHAR(9) NOT NULL,

			CONSTRAINT RESERVES_PK
			PRIMARY KEY(RESERVATION_NO, DOCID, COPYNO, BID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Reserves table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}
	

	def __generate_borrows_table(self) -> dict:
		"""
		Used to create the BORROWS table

		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query
		"""
		
		if "BORROWS" in self.already_present_tables:
			return
		query = """
		CREATE TABLE IF NOT EXISTS BORROWS(
			BOR_NO CHAR(9) NOT NULL,
			DOCID CHAR(9) NOT NULL,
			COPYNO CHAR(9) NOT NULL,
			BID CHAR(9) NOT NULL,
			RID CHAR(9) NOT NULL,

			CONSTRAINT BORROWS_PK
			PRIMARY KEY(BOR_NO, DOCID, COPYNO, BID)
		);
		"""
		self._query_executor(query)
		return {
			"status": "success",
			"message": "Borrows table created successfully",
			"query": query.replace("\n", " ").replace("\t", "").strip()
		}

	
	def create_tables(self) -> dict:
		"""
		Used to create all the tables in the database
		
		Args:
			None
		
		Returns:
			dict: The status of the query execution along with the query and metadata
		"""
		
		return {
			"status": "success",
			"message": "Tables created successfully",
			"metadata": {
				"person": self.__generate_person_table(),
				"reader": self.__generate_reader_table(),
				"reservation": self.__generate_reservation_table(),
				"borrowing": self._generate_borrowing_table(),
				"branch": self.__generate_branch_table(),
				"publisher": self.__generate_publisher_table(),
				"authors": self.__generate_authors_table(),
				"gedits": self.__generate_gedits_table(),
				"chairs": self.__generate_chairs_table(),
				"book": self.__generate_book_table(),
				"journal_issue": self.__generate_journal_issue_table(),
				"proceedings": self.__generate_proceedings_table(),
				"journal_volume": self.__generate_journal_volume_table(),
				"document": self.__generate_document_table(),
				"copy": self.__generate_copy_table(),
				"reserves": self.__generate_reserves_table(),
				"borrows": self.__generate_borrows_table()
			},
			"prevent_chicken_egg_metadata": PreventChickenEgg(self.connection).execute(),
		}