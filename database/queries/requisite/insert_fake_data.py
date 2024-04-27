import random
import MySQLdb
import datetime
import pandas as pd
from tqdm import tqdm
from faker import Faker
from faker.providers import DynamicProvider


class InsertFakeData:
  """
  It is used to insert fake data into the database
  """
  
  
  def __init__(self, connection: MySQLdb.Connection, fake_data_config: dict) -> None:
    self.fake_record_insertion_limit = int(fake_data_config["fakedatainsertionlimit"])
    self.fake_profile = Faker()
    reader_type_faker = DynamicProvider(
      provider_name="reader_type",
      elements=["student", "senior citizen", "staff", "doctor", "nurse", "surgeon", "clerk", "employee", "teacher", "professor", "lecturer", "researcher", "scientist", "engineer", "developer", "designer", "architect", "analyst", "manager", "director", "ceo", "coo", "cfo", "cto", "cmo", "cdo", "ciso", "ciso", "cso", "cio", "vp", "president", "chairman", "secretary", "treasurer", "accountant", "auditor", "consultant", "advisor", "coach", "mentor", "trainer", "instructor", "tutor", "professor", "lecturer", "researcher", "scientist", "engineer", "developer", "designer", "architect", "analyst", "manager", "director", "ceo", "coo", "cfo", "cto", "cmo", "cdo", "ciso", "ciso", "cso", "cio", "vp", "president", "chairman", "secretary", "treasurer", "accountant", "auditor", "consultant", "advisor", "coach", "mentor", "trainer", "instructor", "tutor", "professor", "lecturer", "researcher", "scientist", "engineer", "developer", "designer", "architect", "analyst", "manager", "director", "ceo", "coo", "cfo", "cto", "cmo", "cdo", "ciso", "ciso", "cso", "cio", "vp", "president", "chairman", "secretary", "treasurer", "accountant", "auditor", "consultant", "advisor", "coach", "mentor", "trainer", "instructor", "tutor", "professor", "lecturer", "researcher", "scientist", "engineer", "developer", "designer", "architect", "analyst", "manager", "director", "ceo", "coo", "cfo", "cto", "cmo", "cdo", "ciso", "ciso", "cso", "cio", "vp", "president", "chairman", "secretary", "treasurer", "accountant"],
    )
    branch_name_faker = DynamicProvider(
      provider_name="branch_name",
      elements=["Research", "Development", "Engineering", "Design", "Testing", "Quality Assurance", "Human Resources", "Finance", "Marketing", "Sales", "Operations", "Management", "Administration", "Legal", "Compliance", "Security", "Information Technology", "Information Security", "Information Systems", "Information Management", "Information Governance", "Information Assurance", "Information Architecture", "Information Design", "Information Engineering", "Information Development", "Information Testing", "Information Quality Assurance", "Information Human Resources", "Information Finance", "Information Marketing", "Information Sales", "Information Operations", "Information Management", "Information Administration", "Information Legal", "Information Compliance", "Information Security", "Information Technology", "Information Security", "Information Systems", "Information Management", "Information Governance", "Information Assurance", "Information Architecture", "Information Design", "Information Engineering", "Information Development", "Information Testing", "Information Quality Assurance", "Information Human Resources", "Information Finance", "Information Marketing", "Information Sales", "Information Operations", "Information Management", "Information Administration", "Information Legal", "Information Compliance", "Information Security", "Information Technology", "Information Security", "Information Systems", "Information Management", "Information Governance", "Information Assurance", "Information Architecture", "Information Design", "Information Engineering", "Information Development", "Information Testing", "Information Quality Assurance", "Information Human Resources", "Information Finance", "Information Marketing", "Information Sales", "Information Operations", "Information Management", "Information Administration", "Information Legal", "Information Compliance", "Information Security", "Information Technology", "Information Security", "Information Systems", "Information Management", "Information Governance", "Information Assurance", "Information Architecture", "Information Design", "Information Engineering", "Information Development", "Information Testing", "Information Quality Assurance", "Information Human Resources", "Information Finance", "Information Marketing", "Information Sales", "Information Operations", "Information Management", "Information Administration", "Information Legal", "Information Compliance", "Information Security", "Information Technology", "Information Security", "Information Systems", "Information Management", "Information Governance", "Information Assurance", "Information Architecture", "Information Design", "Information Engineering", "Information Development", "Information Testing", "Information Quality Assurance", "Information Human Resources", "Information Finance", "Information Marketing", "Information Sales", "Information Operations", "Information Management", "Information Administration", "Information Legal", "Information Compliance", "Information Security", "Information", "Research", "Development", "Engineering", "Design", "Testing", "Quality Assurance", "Human Resources"]
    )
    document_title_faker = DynamicProvider(
      provider_name="document_title",
      elements=["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye", "The Lord of the Rings", "Animal Farm", "The Hobbit", "Fahrenheit 451", "Brave New World", "The Diary of a Young", "Huckleberry Finn", "The Grapes of Wrath", "The Adventures of Sherlock Holmes", "The Picture of Dorian Gray", "The Scarlet Letter", "The Count of Monte Cristo", "The Three Musketeers", "The Brothers Karamazov", "The Idiot", "Crime and Punishment", "War and Peace", "Anna Karenina", "The Master and Margarita", "The Gulag Archipelago", "One Hundred Years of Solitude", "Love in the Time of Cholera", "Chronicle of a Death Foretold", "Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows", "The Hunger Games", "Catching Fire", "Mockingjay", "The Fault in Our Stars", "Looking for Alaska", "Paper Towns", "An Abundance of Katherines", "The Perks of Being a Wallflower", "The Alchemist", "Veronika Decides to Die", "Eleven Minutes", "Brida", "The Valkyries", "The Zahir", "The Witch of Portobello", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "The Pilgrimage", "The Spy", "The Winner Stands Alone", "The Devil and Miss Prym", "The Fifth Mountain", "By the River Piedra I Sat Down and Wept", "Marvel Comics", "DC Comics", "The Walking Dead", "The Sandman", "Watchmen", "V for Vendetta", "Maus", "Persepolis", "Fun Home", "Black Hole", "Spiderman Comics", "Batman Comics", "Superman"]
    )

    editor_name_faker = DynamicProvider(
      provider_name="editor_name",
      elements=["John Doe", "Jane Doe", "Alice Doe", "Bob Doe", "Charlie Doe", "David Doe", "Eve Doe", "Frank Doe", "Grace Doe", "Henry Doe", "Ivy Doe", "Jack Doe", "Kate Doe", "Liam Doe", "Mia Doe", "Noah Doe", "Olivia Doe", "Paul Doe", "Quinn Doe", "Ryan Doe", "Sophia Doe", "Tom Doe", "Uma Doe", "Violet Doe", "William Doe", "Xander Doe", "Yara Doe", "Zane Doe", "J.K. Rowling", "Stephen King", "Dan Brown", "Agatha Christie", "Arthur Conan Doyle", "George R.R. Martin", "J.R.R. Tolkien", "Leo Tolstoy", "Fyodor Dostoevsky", "Ernest Hemingway", "Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen", "Emily Bronte", "Charlotte Bronte", "Anne Bronte", "Virginia Woolf", "Sylvia Plath", "Maya Angelou", "Toni Morrison", "Alice Walker", "Zora Neale Hurston", "Harper Lee", "Margaret Atwood", "Jhumpa Lahiri", "Arundhati Roy", "Chimamanda Ngozi Adichie", "Zadie Smith", "Donna Tartt", "J.D. Salinger", "Kazuo Ishiguro", "Gabriel Garcia Marquez", "Isabel Allende", "Pablo Neruda", "Octavio Paz", "Mario Vargas Llosa", "Jorge Luis Borges", "Julio Cortazar", "Carlos Fuentes", "Juan Rulfo", "Miguel de Cervantes", "Federico Garcia Lorca", "Antonio Machado", "Lorca", "Garcia", "Machado", "Cervantes", "Rulfo", "Fuentes", "Cortazar", "Borges", "Llosa", "Paz", "Neruda", "Allende", "Marquez", "Ishiguro", "Salinger", "Smith", "Adichie", "Lahiri", "Tartt", "Ngozi", "Angelou", "Morrison", "Walker", "Hurston", "Lee", "Atwood", "Plath", "Woolf", "Bronte"]
    )

    library_name_faker = DynamicProvider(
      provider_name="library_name",
      elements=["City Library", "Town Library", "Village Library", "Municipal Library", "Public Library", "Private Library", "Community Library", "School Library", "College Library", "University Library", "Institution Library", "Academic Library", "Research Library", "Reference Library", "Lending Library", "Borrowing Library", "Reading Library", "Learning Library", "Educational Library", "Literary Library", "Cultural Library", "Historical Library", "Archival Library", "Digital Library", "Virtual Library", "Online Library", "Offline Library", "Physical Library", "Mobile Library", "Stationary Library", "Portable Library", "Compact Library", "Comprehensive Library", "Compact Library", "Comprehensive Library", "Special Library", "General Library", "Specific Library", "Unique Library", "Rare Library", "Common Library", "Ordinary Library", "Extraordinary Library", "Unusual Library", "Strange Library", "Weird Library", "Odd Library", "Even Library", "Normal Library", "Abnormal Library", "Regular Library", "Irregular Library", "Frequent Library", "Infrequent Library", "Occasional Library", "Rare Library", "Common Library", "Uncommon Library", "Popular Library", "Unpopular Library", "Famous Library", "Unknown Library", "Known Library", "Recognized Library", "Unrecognized Library", "Acknowledged Library", "Unacknowledged Library", "Accepted Library", "Rejected Library", "Approved Library", "Disapproved Library", "Authorized Library", "Unauthorized Library", "Legal Library", "Illegal Library", "Legitimate Library", "Illegitimate Library", "Genuine Library", "Fake Library", "Real Library", "Imaginary Library", "Virtual Library", "Physical Library", "Digital Library", "Analog Library", "Electronic Library", "Mechanical Library", "Manual Library", "Automatic Library", "Robotic Library", "Human Library", "Non-Human Library", "Artificial Library", "Natural Library", "Supernatural Library", "Paranormal Library", "Normal Library", "Abnormal Library", "Regular Library", "Irregular Library", "Frequent Library", "Infrequent Library", "Occasional Library", "Rare Library", "Common Library", "Uncommon Library", "Popular Library", "Unpopular Library", "Famous Library"]
    )

    self.fake_profile.add_provider(branch_name_faker)
    self.fake_profile.add_provider(reader_type_faker)
    self.fake_profile.add_provider(document_title_faker)
    self.fake_profile.add_provider(editor_name_faker)
    self.fake_profile.add_provider(library_name_faker)
    self.connection = connection
    self.__initialize_empty_dataframes()
    self.__initialize_constraints_enforcing_dict()
  

  def __initialize_empty_dataframes(self) -> None:
    """
    Used to initialize the empty dataframes for the purpose of following constraints in insertion of data later
    
    Args:
      None
    
    Returns:
      None
    """
    
    self.borrowing_data = pd.DataFrame(columns=["BOR_NO", "BDTIME", "RDTIME"])
    self.reservation_data = pd.DataFrame(columns=["RES_NO", "DTIME"])
    self.reader_data = pd.DataFrame(columns=["RID", "RTYPE", "RNAME", "RADDRESS", "PHONE_NO"])
    self.person_data = pd.DataFrame(columns=["PID", "PNAME"])
    self.branch_data = pd.DataFrame(columns=["BID", "BNAME", "BLOCATION"])
    self.publisher_data = pd.DataFrame(columns=["PUBID", "PUBNAME", "PUBADDRESS"])
    self.document_data = pd.DataFrame(columns=["DOCID", "TITLE", "PDATE", "PUBLISHERID"])
    self.copy_data = pd.DataFrame(columns=["DOCID", "COPYNO", "BID", "POSITION"])
    self.borrows_data = pd.DataFrame(columns=["BOR_NO", "DOCID", "COPYNO", "BID", "RID"])
    self.reserves_data = pd.DataFrame(columns=["RES_NO", "DOCID", "BID", "RID", "COPYNO"])
    self.journal_volume_data = pd.DataFrame(columns=["DOCID", "VOLUME_NO", "EDITOR"])
    self.book_data = pd.DataFrame(columns=["DOCID", "ISBN"])
    self.authors_data = pd.DataFrame(columns=["PID", "DOCID"])
    self.journal_issue_data = pd.DataFrame(columns=["DOCID", "ISSUE_NO", "SCOPE"])
    self.gedits_data = pd.DataFrame(columns=["DOCID", "iSSUE_NO", "PID"])
    self.proceedings_data = pd.DataFrame(columns=["DOCID", "CDATE", "CLOCATION", "CEDITOR"])
    self.chairs_data = pd.DataFrame(columns=["PID", "DOCID"])


  def __initialize_constraints_enforcing_dict(self) -> None:
    """
    Used to initialize the constraints enforcing dictionary
    
    Args:
      None
      
    Returns:
      None
    """
    
    self.readers_borrows = {}
    self.readers_reserves = {}
    self.document_issues = {}


  def  __get_actual_record_count(self, table_name: str) -> int:
    """
    Used to get the actual record count of a table

    Args:
        table_name (str): The name of the table

    Returns:
        int: The actual record count of the table
    """

    query = f"SELECT COUNT(*) FROM {table_name};"
    with self.connection.cursor() as cursor:
      cursor.execute(query)
      record_count = cursor.fetchone()[0]
    return record_count
  
  
  def __frame_dynamic_insert_query(self, table_name: str, columns: list, dtype: list, values: list) -> str:
    """
    Used to frame a dynamic insert query

    Args:
        table_name (str): The name of the table
        columns (list): The columns of the table
        dtype (list): The data types of the columns
        values (list): The values to be inserted into the table

    Returns:
        str: The framed insert query
    """

    columns = ", ".join(columns)
    modified_values = []
    for i in range(len(values)):
      if dtype[i] == "str":
        modified_values.append(str(values[i]))
      elif dtype[i] == "int":
        modified_values.append(int(values[i]))
      elif dtype[i] == "datetime":
        modified_values.append(values[i])

    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({str(modified_values)[1:-1]});"
    return insert_query
  

  def __execute_insert_query(self, query: str) -> None:
    """
    Used to execute an insert query

    Args:
        query (str): The insert query to be executed

    Returns:
        None
    """

    try:
      with self.connection.cursor() as cursor:
        cursor.execute(query)
      self.connection.commit()
    except MySQLdb.IntegrityError as e:
      if e.args[0] == 1062:
        pass
      else:
        print(f"Error in executing query: {query}. Error: {e}")
    except Exception as e:
      print(f"Error in executing query: {query}. Error: {e}")
    finally:
      self.connection.rollback()


  def __insert_fake_borrowing_data(self) -> dict:
    """
    Used to insert fake borrowing data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake borrowing data
    """
    
    borrowing_data_limit = self.fake_record_insertion_limit * 10
    for i in tqdm(range(borrowing_data_limit), total=borrowing_data_limit, desc="Inserting fake borrowing data"):
      random_day = random.randint(18, 50)
      fake_borno = "BOR" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_rdtime = datetime.datetime.now()
      fake_bdtime = fake_rdtime - datetime.timedelta(days=random_day, hours=random.randint(1, 23), minutes=random.randint(1, 59), seconds=random.randint(1, 59))
      fake_rdtime = fake_rdtime.strftime("%Y-%m-%d %H:%M:%S")
      fake_bdtime = fake_bdtime.strftime("%Y-%m-%d %H:%M:%S")
      row_to_append = pd.DataFrame([{
        "BOR_NO": fake_borno,
        "BDTIME": fake_bdtime,
        "RDTIME": fake_rdtime
      }])
      self.borrowing_data = pd.concat([self.borrowing_data, row_to_append], ignore_index=True)
      borrowing_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="BORROWING",
        columns=["BOR_NO", "BDTIME", "RDTIME"],
        dtype=["str", "datetime", "datetime"],
        values=[fake_borno, fake_bdtime, fake_rdtime]
      )
      self.__execute_insert_query(
        query = borrowing_data_inserting_query
      )
    actual_borrowing_record_count = self.__get_actual_record_count("BORROWING")
    return {
      "status": "success",
      "message": "Fake borrowing data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_borrowing_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_borrowing_record_count,
      "last_executed_query": borrowing_data_inserting_query
    }
  

  def __insert_fake_reservation_data(self) -> dict:
    """
    Used to insert fake reservation data
    
    Args:
      None
      
    Returns:
      dict: The status of the insertion of fake reservation data
    """
    
    reservation_data_limit = self.fake_record_insertion_limit * 10
    for i in tqdm(range(reservation_data_limit), total=reservation_data_limit, desc="Inserting fake reservation data"):
      fake_resno = "RES" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_dtime = datetime.datetime.now()
      random_day = random.randint(15, 50)
      fake_dtime -= datetime.timedelta(days=random_day, hours=random.randint(1, 23), minutes=random.randint(1, 59), seconds=random.randint(18, 59))
      fake_dtime = fake_dtime.strftime("%Y-%m-%d %H:%M:%S")
      row_to_append = pd.DataFrame([{
        "RES_NO": fake_resno,
        "DTIME": fake_dtime
      }])
      self.reservation_data = pd.concat([self.reservation_data, row_to_append], ignore_index=True)
      reservation_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="RESERVATION",
        columns=["RES_NO", "DTIME"],
        dtype=["str", "datetime"],
        values=[fake_resno, fake_dtime]
      )
      self.__execute_insert_query(
        query = reservation_data_inserting_query
      )
    actual_reservation_record_count = self.__get_actual_record_count("RESERVATION")
    return {
      "status": "success",
      "message": "Fake reservation data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_reservation_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_reservation_record_count,
      "last_executed_query": reservation_data_inserting_query
    }


  def __insert_fake_reader_data(self) -> dict:
    """
    Used to insert fake reader data
    
    Args:
      None
      
    Returns:
      dict: The status of the insertion of fake reader data
    """
    
    reader_insertion_limit = self.fake_record_insertion_limit * 12
    for i in tqdm(range(reader_insertion_limit), total=reader_insertion_limit, desc="Inserting fake reader data"):
      fake_profile = self.fake_profile.profile()
      fake_readerId = fake_profile['ssn'].replace('-', '')
      fake_readerType = self.fake_profile.reader_type().title()
      fake_readerName = fake_profile['name']
      fake_readerAddress = fake_profile['residence'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace(',', '')
      fake_readerPhone = int(str(self.fake_profile.msisdn()[:10]))
      row_to_append = pd.DataFrame([{
        "RID": fake_readerId,
        "RTYPE": fake_readerType,
        "RNAME": fake_readerName,
        "RADDRESS": fake_readerAddress,
        "PHONE_NO": fake_readerPhone
      }])
      self.reader_data = pd.concat([self.reader_data, row_to_append], ignore_index=True)
      reader_data_inserting_query = self.__frame_dynamic_insert_query(
          table_name="READER",
          columns=["RID", "RTYPE", "RNAME", "RADDRESS", "PHONE_NO"],
          dtype=["str", "str", "str", "str", "int"],
          values=[fake_readerId, fake_readerType, fake_readerName, fake_readerAddress, fake_readerPhone]
        )
      self.__execute_insert_query(
        query = reader_data_inserting_query
      )
    actual_reader_record_count = self.__get_actual_record_count("READER")
    return {
      "status": "success",
      "message": "Fake reader data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_reader_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_reader_record_count,
      "last_executed_query": reader_data_inserting_query
    }
  

  def __insert_fake_person_data(self) -> dict:
    """
    Used to insert fake person data
    
    Args:
      None
      
    Returns:
      dict: The status of the insertion of fake person data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake person data"):
      fake_profile = self.fake_profile.profile()
      fake_pid = "PER" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_personName = fake_profile['name']
      row_to_append = pd.DataFrame([{
        "PID": fake_pid,
        "PNAME": fake_personName
      }])
      self.person_data = pd.concat([self.person_data, row_to_append], ignore_index=True)
      person_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="PERSON",
        columns=["PID", "PNAME"],
        dtype=["str", "str"],
        values=[fake_pid, fake_personName]
      )
      self.__execute_insert_query(
        query = person_data_inserting_query
      )
    actual_person_record_count = self.__get_actual_record_count("PERSON")
    return {
      "status": "success",
      "message": "Fake person data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_person_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_person_record_count,
      "last_executed_query": person_data_inserting_query
    }
  

  def __insert_fake_branch_data(self) -> dict:
    """
    Used to insert fake branch data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake branch data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake branch data"):
      fake_profile = self.fake_profile.profile()
      fake_bid = "BR" + self.fake_profile.password(length=7, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_branchName = self.fake_profile.library_name().title()
      fake_branchLocation = fake_profile['residence'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace(',', '')
      row_to_append = pd.DataFrame([{
        "BID": fake_bid,
        "BNAME": fake_branchName,
        "BLOCATION": fake_branchLocation
      }])
      self.branch_data = pd.concat([self.branch_data, row_to_append], ignore_index=True)
      branch_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="BRANCH",
        columns=["BID", "BNAME", "BLOCATION"],
        dtype=["str", "str", "str"],
        values=[fake_bid, fake_branchName, fake_branchLocation]
      )
      self.__execute_insert_query(
        query = branch_data_inserting_query
      )
    actual_branch_record_count = self.__get_actual_record_count("BRANCH")
    return {
      "status": "success",
      "message": "Fake branch data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_branch_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_branch_record_count,
      "last_executed_query": branch_data_inserting_query
    }
  

  def __insert_fake_publisher_data(self) -> dict:
    """
    Used to insert fake publisher data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake publisher data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake publisher data"):
      fake_profile = self.fake_profile.profile()
      fake_pubid = "PUB" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_pubname = fake_profile['name']
      fake_pubAddress = fake_profile['residence'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace(',', '')
      row_to_append = pd.DataFrame([{
        "PUBID": fake_pubid,
        "PUBNAME": fake_pubname,
        "PUBADDRESS": fake_pubAddress
      }])
      self.publisher_data = pd.concat([self.publisher_data, row_to_append], ignore_index=True)
      publisher_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="PUBLISHER",
        columns=["PUBID", "PUBNAME", "PUBADDRESS"],
        dtype=["str", "str", "str"],
        values=[fake_pubid, fake_pubname, fake_pubAddress]
      )
      self.__execute_insert_query(
        query = publisher_data_inserting_query
      )
    actual_publisher_record_count = self.__get_actual_record_count("PUBLISHER")
    return {
      "status": "success",
      "message": "Fake publisher data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_publisher_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_publisher_record_count,
      "last_executed_query": publisher_data_inserting_query
    }
  

  def __insert_fake_document_data(self) -> dict:
    """
    Used to insert fake document data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake document data
    """
    
    document_insertion_limit = self.fake_record_insertion_limit * 10
    for i in tqdm(range(document_insertion_limit), total=document_insertion_limit, desc="Inserting fake document data"):
      fake_docid = "DOC" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_title = self.fake_profile.document_title().title()
      fake_docpubdate = self.fake_profile.date_time().strftime("%Y-%m-%d")
      doc_publisherid = self.publisher_data.sample(n=1)["PUBID"].values[0]
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "TITLE": fake_title,
        "PDATE": fake_docpubdate,
        "PUBLISHERID": doc_publisherid
      }])
      self.document_data = pd.concat([self.document_data, row_to_append], ignore_index=True)
      document_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="DOCUMENT",
        columns=["DOCID", "TITLE", "PDATE", "PUBLISHERID"],
        dtype=["str", "str", "datetime", "str"],
        values=[fake_docid, fake_title, fake_docpubdate, doc_publisherid]
      )
      self.__execute_insert_query(
        query = document_data_inserting_query
      )
    actual_document_record_count = self.__get_actual_record_count("DOCUMENT")
    return {
      "status": "success",
      "message": "Fake document data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_document_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_document_record_count,
      "last_executed_query": document_data_inserting_query
    }
  

  def __insert_fake_copy_data(self) -> dict:
    """
    Used to insert fake copy data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake copy data
    """
    
    list_of_docids = self.document_data["DOCID"].values
    for i in tqdm(range(len(list_of_docids)), total=len(list_of_docids), desc="Inserting fake copy data"):
      fake_docid = list_of_docids[i]
      for j in range(random.randint(3, 10)):
        fake_copyno = "COP" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
        for k in range(random.randint(3, 10)):
          fake_bid = self.branch_data.sample(n=1)["BID"].values[0]
          fake_position = self.fake_profile.password(length=3, special_chars=False, digits=True, upper_case=False, lower_case=False) + self.fake_profile.password(length=3, special_chars=False, digits=True, upper_case=True, lower_case=False)
          row_to_append = pd.DataFrame([{
            "DOCID": fake_docid,
            "COPYNO": fake_copyno,
            "BID": fake_bid,
            "POSITION": fake_position
          }])
          self.copy_data = pd.concat([self.copy_data, row_to_append], ignore_index=True)
          copy_data_inserting_query = self.__frame_dynamic_insert_query(
            table_name="COPY",
            columns=["DOCID", "COPYNO", "BID", "POSITION"],
            dtype=["str", "str", "str", "str"],
            values=[fake_docid, fake_copyno, fake_bid, fake_position]
          )
          self.__execute_insert_query(
            query = copy_data_inserting_query
          )
    actual_copy_record_count = self.__get_actual_record_count("COPY")
    return {
      "status": "success",
      "message": "Fake copy data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_copy_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_copy_record_count,
      "last_executed_query": copy_data_inserting_query
    }
  

  def __insert_fake_borrows_data(self) -> dict:
    """
    Used to insert fake borrows data

    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake borrows data
    """
    
    list_of_bor_no = self.borrowing_data["BOR_NO"].values
    i, r = 0, 0
    progress_bar = tqdm(total=len(list_of_bor_no), desc="Inserting fake borrows data")
    while i < len(list_of_bor_no):
      doc_count, limit_for_borrowed_document = [], random.randint(2, 10)
      for l in range(random.randint(2, 5)):
        if len(doc_count) > limit_for_borrowed_document:
            break
        if i < len(list_of_bor_no):
          fake_borrows_borno = list_of_bor_no[i]
        else:
          print("Borrowing data limit reached")
          break
        

        if r < len(self.reader_data):
          fake_reader_id = self.reader_data["RID"].values[r]
        else:
          print("Reader data limit reached")
          break
        
        list_of_accessed_bids = []
        for j in range(random.randint(2, 4)):
          if len(doc_count) > limit_for_borrowed_document:
            break
          while True:
            fake_sample = self.copy_data.sample(n=1)
            fake_borrows_bid = fake_sample["BID"].values[0]
            if fake_borrows_bid not in list_of_accessed_bids:
              list_of_accessed_bids.append(fake_borrows_bid)
              break
            else:
              continue
          all_indices_of_borrows_bid = [i for i in range(len(self.copy_data)) if self.copy_data["BID"].values[i] == fake_borrows_bid]
          limit = 10 if len(all_indices_of_borrows_bid) > 10 else len(all_indices_of_borrows_bid)
          limit = random.randint(1, limit)
          all_indices_of_borrows_bid = random.sample(all_indices_of_borrows_bid, limit)
          for k in range(len(all_indices_of_borrows_bid)):
            fake_sample = self.copy_data.iloc[all_indices_of_borrows_bid[k]]
            fake_borrows_docid = fake_sample["DOCID"]
            if fake_borrows_docid in doc_count:
              continue
            else:
              doc_count.append(fake_borrows_docid)
            
            if len(doc_count) > limit_for_borrowed_document:
              break
            all_indices_of_copyno = [i for i in all_indices_of_borrows_bid if self.copy_data["DOCID"].values[i] == fake_borrows_docid]
            limit = 10 if len(all_indices_of_copyno) > 10 else len(all_indices_of_copyno)
            limit = random.randint(1, limit)
            all_indices_of_copyno = random.sample(all_indices_of_copyno, limit)
            for m in range(len(all_indices_of_copyno)):
              fake_sample = self.copy_data.iloc[all_indices_of_copyno[m]]
              fake_borrows_copyno = fake_sample["COPYNO"]
              row_to_append = pd.DataFrame([{
                "BOR_NO": fake_borrows_borno,
                "DOCID": fake_borrows_docid,
                "COPYNO": fake_borrows_copyno,
                "BID": fake_borrows_bid,
                "RID": fake_reader_id
              }])
              self.borrows_data = pd.concat([self.borrows_data, row_to_append], ignore_index=True)
              borrows_data_inserting_query = self.__frame_dynamic_insert_query(
                table_name="BORROWS",
                columns=["BOR_NO", "DOCID", "COPYNO", "BID", "RID"],
                dtype=["str", "str", "str", "str", "str"],
                values=[fake_borrows_borno, fake_borrows_docid, fake_borrows_copyno, fake_borrows_bid, fake_reader_id]
              )
              self.__execute_insert_query(
                query = borrows_data_inserting_query
              )
        i += 1
        progress_bar.update(1)
      r += 1    
    progress_bar.close()
    actual_borrows_record_count = self.__get_actual_record_count("BORROWS")
    return {
      "status": "success",
      "message": "Fake borrows data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_borrows_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_borrows_record_count,
      "last_executed_query": borrows_data_inserting_query
    }
  

  def __insert_fake_reserves_data(self) -> dict:
    """
    Used to insert fake reserves data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake reserves data
    """
    
    list_of_res_no = self.reservation_data["RES_NO"].values
    i, r = 0, 0
    progess_bar = tqdm(total=len(list_of_res_no), desc="Inserting fake reserves data")
    while i < len(list_of_res_no):
      doc_count, limit_for_reserved_document = [], random.randint(2, 10)
      for l in range(random.randint(2, 5)):
        if len(doc_count) > limit_for_reserved_document:
          break

        if i < len(list_of_res_no):
          fake_reserves_resno = list_of_res_no[i]
        else:
          print("Reservation data limit reached")
          break
        
        if r < len(self.reader_data):
          fake_reader_id = self.reader_data["RID"].values[r]
        else:
          print("Reader data limit reached")
          break

        list_of_accessed_bids = []
        for j in range(random.randint(2, 4)):
          if len(doc_count) > limit_for_reserved_document:
            break

          while True:
            fake_sample = self.copy_data.sample(n=1)
            fake_reserves_bid = fake_sample["BID"].values[0]
            if fake_reserves_bid not in list_of_accessed_bids:
              list_of_accessed_bids.append(fake_reserves_bid)
              break
            else:
              continue
          all_indices_of_reserves_bid = [i for i in range(len(self.copy_data)) if self.copy_data["BID"].values[i] == fake_reserves_bid]
          limit = 10 if len(all_indices_of_reserves_bid) > 10 else len(all_indices_of_reserves_bid)
          limit = random.randint(1, limit)
          all_indices_of_reserves_bid = random.sample(all_indices_of_reserves_bid, limit)
          for k in range(len(all_indices_of_reserves_bid)):
            fake_sample = self.copy_data.iloc[all_indices_of_reserves_bid[k]]
            fake_reserves_docid = fake_sample["DOCID"]
            if fake_reserves_docid in doc_count:
              continue
            else:
              doc_count.append(fake_reserves_docid)
            if len(doc_count) > limit_for_reserved_document:
              break
            all_indices_of_copyno = [i for i in all_indices_of_reserves_bid if self.copy_data["DOCID"].values[i] == fake_reserves_docid]
            limit = 10 if len(all_indices_of_copyno) > 10 else len(all_indices_of_copyno)
            limit = random.randint(1, limit)
            all_indices_of_copyno = random.sample(all_indices_of_copyno, limit)
            for m in range(len(all_indices_of_copyno)):
              fake_sample = self.copy_data.iloc[all_indices_of_copyno[m]]
              fake_reserves_copyno = fake_sample["COPYNO"]
              row_to_append = pd.DataFrame([{
                "RESERVATION_NO": fake_reserves_resno,
                "DOCID": fake_reserves_docid,
                "BID": fake_reserves_bid,
                "RID": fake_reader_id,
                "COPYNO": fake_reserves_copyno
              }])
              self.reserves_data = pd.concat([self.reserves_data, row_to_append], ignore_index=True)
              reserves_data_inserting_query = self.__frame_dynamic_insert_query(
                table_name="RESERVES",
                columns=["RESERVATION_NO", "DOCID", "BID", "RID", "COPYNO"],
                dtype=["str", "str", "str", "str", "str"],
                values=[fake_reserves_resno, fake_reserves_docid, fake_reserves_bid, fake_reader_id, fake_reserves_copyno]
              )
              self.__execute_insert_query(
                query = reserves_data_inserting_query
              )
        i += 1
        progess_bar.update(1)
      r += 1 
    progess_bar.close()
    actual_reserves_record_count = self.__get_actual_record_count("RESERVES")
    return {
      "status": "success",
      "message": "Fake reserves data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_reserves_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_reserves_record_count,
      "last_executed_query": reserves_data_inserting_query
    }
  

  def __insert_fake_journal_volume_data(self) -> dict:
    """
    Used to insert fake journal volume data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake journal volume data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake journal volume data"):
      fake_docid = self.document_data.sample(n=1)["DOCID"].values[0]
      fake_volumeno = "VOL" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_editor = self.person_data.sample(n=1)["PID"].values[0]
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "VOLUME_NO": fake_volumeno,
        "EDITOR": fake_editor
      }])
      self.journal_volume_data = pd.concat([self.journal_volume_data, row_to_append], ignore_index=True)
      journal_volume_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="JOURNAL_VOLUME",
        columns=["DOCID", "VOLUME_NO", "EDITOR"],
        dtype=["str", "str", "str"],
        values=[fake_docid, fake_volumeno, fake_editor]
      )
      self.__execute_insert_query(
        query = journal_volume_data_inserting_query
      )
    actual_journal_volume_record_count = self.__get_actual_record_count("JOURNAL_VOLUME")
    return {
      "status": "success",
      "message": "Fake journal volume data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_journal_volume_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_journal_volume_record_count,
      "last_executed_query": journal_volume_data_inserting_query
    }
  

  def __insert_fake_book_data(self) -> dict:
    """
    Used to insert fake book data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake book data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake book data"):
      fake_docid = self.document_data.sample(n=1)["DOCID"].values[0]
      while len(self.journal_volume_data[self.journal_volume_data["DOCID"] == fake_docid]) > 0:
        fake_docid = self.document_data.sample(n=1)["DOCID"].values[0]
      fake_isbn = str(self.fake_profile.isbn13()).replace('-', '')
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "ISBN": fake_isbn
      }])
      self.book_data = pd.concat([self.book_data, row_to_append], ignore_index=True)
      book_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="BOOK",
        columns=["DOCID", "ISBN"],
        dtype=["str", "str"],
        values=[fake_docid, fake_isbn]
      )
      self.__execute_insert_query(
        query = book_data_inserting_query
      )
    actual_book_record_count = self.__get_actual_record_count("BOOK")
    return {
      "status": "success",
      "message": "Fake book data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_book_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_book_record_count,
      "last_executed_query": book_data_inserting_query
    }
  

  def __insert_fake_authors_data(self) -> dict:
    """
    Used to insert fake author data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake author data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake author data"):
      fake_pid = self.person_data.sample(n=1)["PID"].values[0]
      fake_docid = self.book_data.sample(n=1)["DOCID"].values[0]
      row_to_append = pd.DataFrame([{
        "PID": fake_pid,
        "DOCID": fake_docid
      }])
      self.authors_data = pd.concat([self.authors_data, row_to_append], ignore_index=True)
      author_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="AUTHORS",
        columns=["PID", "DOCID"],
        dtype=["str", "str"],
        values=[fake_pid, fake_docid]
      )
      self.__execute_insert_query(
        query = author_data_inserting_query
      )
    actual_author_record_count = self.__get_actual_record_count("AUTHORS")
    return {
      "status": "success",
      "message": "Fake author data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_author_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_author_record_count,
      "last_executed_query": author_data_inserting_query
    }
  

  def __insert_fake_journal_issue_data(self) -> dict:
    """
    Used to insert fake journal issue data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake journal issue data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake journal issue data"):
      fake_docid = self.journal_volume_data.sample(n=1)["DOCID"].values[0]
      if fake_docid in self.document_issues:
        self.document_issues[fake_docid] += 1
        while self.document_issues[fake_docid] > 10:
          fake_docid = self.journal_volume_data.sample(n=1)["DOCID"].values[0]
          if fake_docid not in self.document_issues:
            break
      else:
        self.document_issues[fake_docid] = 1
      fake_issueno = "ISS" + self.fake_profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      fake_scope = self.fake_profile.text(max_nb_chars=100)
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "ISSUE_NO": fake_issueno,
        "SCOPE": fake_scope
      }])
      self.journal_issue_data = pd.concat([self.journal_issue_data, row_to_append], ignore_index=True)
      journal_issue_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="JOURNAL_ISSUE",
        columns=["DOCID", "ISSUE_NO", "SCOPE"],
        dtype=["str", "str", "str"],
        values=[fake_docid, fake_issueno, fake_scope]
      )
      self.__execute_insert_query(
        query = journal_issue_data_inserting_query
      )
    actual_journal_issue_record_count = self.__get_actual_record_count("JOURNAL_ISSUE")
    return {
      "status": "success",
      "message": "Fake journal issue data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_journal_issue_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_journal_issue_record_count,
      "last_executed_query": journal_issue_data_inserting_query
    }
  

  def __insert_fake_gedits_data(self) -> dict:
    """
    Used to insert fake gedits data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake gedits data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake gedits data"):
      fake_sample = self.journal_issue_data.sample(n=1)
      fake_docid = fake_sample["DOCID"].values[0]
      fake_issueno = fake_sample["ISSUE_NO"].values[0]
      fake_pid = self.person_data.sample(n=1)["PID"].values[0]
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "ISSUE_NO": fake_issueno,
        "PID": fake_pid
      }])
      self.gedits_data = pd.concat([self.gedits_data, row_to_append], ignore_index=True)
      gedits_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="GEDITS",
        columns=["DOCID", "ISSUE_NO", "PID"],
        dtype=["str", "str", "str"],
        values=[fake_docid, fake_issueno, fake_pid]
      )
      self.__execute_insert_query(
        query = gedits_data_inserting_query
      )
    actual_gedits_record_count = self.__get_actual_record_count("GEDITS")
    return {
      "status": "success",
      "message": "Fake gedits data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_gedits_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_gedits_record_count,
      "last_executed_query": gedits_data_inserting_query
    }
  

  def __insert_fake_proceedings_data(self) -> dict:
    """
    Used to insert fake proceedings data
    
    Args:
      None
      
    Returns:
      dict: The status of the insertion of fake proceedings data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake proceedings data"):
      fake_profile = self.fake_profile.profile()
      fake_docid = self.document_data.sample(n=1)["DOCID"].values[0]
      while len(self.journal_volume_data[self.journal_volume_data["DOCID"] == fake_docid]) > 0 or len(self.book_data[self.book_data["DOCID"] == fake_docid]) > 0:
        fake_docid = self.document_data.sample(n=1)["DOCID"].values[0]
      fake_cdate = self.fake_profile.date_time().strftime("%Y-%m-%d")
      fake_clocation = fake_profile['residence'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace(',', '')
      fake_ceditor = self.fake_profile.editor_name()
      row_to_append = pd.DataFrame([{
        "DOCID": fake_docid,
        "CDATE": fake_cdate,
        "CLOCATION": fake_clocation,
        "CEDITOR": fake_ceditor
      }])
      self.proceedings_data = pd.concat([self.proceedings_data, row_to_append], ignore_index=True)
      proceedings_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="PROCEEDINGS",
        columns=["DOCID", "CDATE", "CLOCATION", "CEDITOR"],
        dtype=["str", "datetime", "str", "str"],
        values=[fake_docid, fake_cdate, fake_clocation, fake_ceditor]
      )
      self.__execute_insert_query(
        query = proceedings_data_inserting_query
      )
    actual_proceedings_record_count = self.__get_actual_record_count("PROCEEDINGS")
    return {
      "status": "success",
      "message": "Fake proceedings data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_proceedings_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_proceedings_record_count,
      "last_executed_query": proceedings_data_inserting_query
    }
  

  def __insert_fake_chairs_data(self) -> dict:
    """
    Used to insert fake chair data
    
    Args:
      None
    
    Returns:
      dict: The status of the insertion of fake chair data
    """
    
    for i in tqdm(range(self.fake_record_insertion_limit), total=self.fake_record_insertion_limit, desc="Inserting fake chair data"):
      fake_pid = self.person_data.sample(n=1)["PID"].values[0]
      fake_docid = self.proceedings_data.sample(n=1)["DOCID"].values[0]
      row_to_append = pd.DataFrame([{
        "PID": fake_pid,
        "DOCID": fake_docid
      }])
      self.chairs_data = pd.concat([self.chairs_data, row_to_append], ignore_index=True)
      chair_data_inserting_query = self.__frame_dynamic_insert_query(
        table_name="CHAIRS",
        columns=["PID", "DOCID"],
        dtype=["str", "str"],
        values=[fake_pid, fake_docid]
      )
      self.__execute_insert_query(
        query = chair_data_inserting_query
      )
    actual_chair_record_count = self.__get_actual_record_count("CHAIRS")
    return {
      "status": "success",
      "message": "Fake chair data has been inserted successfully",
      "wanted_record_count": self.fake_record_insertion_limit,
      "actual_record_count": actual_chair_record_count,
      "lost_records": self.fake_record_insertion_limit - actual_chair_record_count,
      "last_executed_query": chair_data_inserting_query
    }
  

  def insert(self, category: str) -> dict:
    """
    Used to insert fake data into the database
    
    Args:
      category (str): The category of the data to be inserted
    
    Returns:
      dict: The status of the insertion of fake data
    """
    
    if category == "reader":
      category_metadata = self.__insert_fake_reader_data()
    elif category == "borrowing":
      category_metadata = self.__insert_fake_borrowing_data()
    elif category == "reservation":
      category_metadata = self.__insert_fake_reservation_data()
    elif category == "person":
      category_metadata = self.__insert_fake_person_data()
    elif category == "branch":
      category_metadata = self.__insert_fake_branch_data()
    elif category == "publisher":
      category_metadata = self.__insert_fake_publisher_data()
    elif category == "document":
      category_metadata = self.__insert_fake_document_data()
    elif category == "copy":
      category_metadata = self.__insert_fake_copy_data()
    elif category == "borrows":
      category_metadata = self.__insert_fake_borrows_data()
    elif category == "reserves":
      category_metadata = self.__insert_fake_reserves_data()
    elif category == "journal_volume":
      category_metadata = self.__insert_fake_journal_volume_data()
    elif category == "book":
      category_metadata = self.__insert_fake_book_data()
    elif category == "authors":
      category_metadata = self.__insert_fake_authors_data()
    elif category == "journal_issue":
      category_metadata = self.__insert_fake_journal_issue_data()
    elif category == "gedits":
      category_metadata = self.__insert_fake_gedits_data()
    elif category == "proceedings":
      category_metadata = self.__insert_fake_proceedings_data()
    elif category == "chairs":
      category_metadata = self.__insert_fake_chairs_data()
    else:
      print("Invalid category. Please provide a valid category to insert fake data")
      return {
        "status": "failure",
      }
    return {
      "status": "success",
      "message": f"Fake {category} data has been inserted successfully",
      "metadata": {
        "category": category_metadata,
      }
    }
