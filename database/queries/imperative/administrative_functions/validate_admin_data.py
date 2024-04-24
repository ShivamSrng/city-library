import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class ValidateAdminData:
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.db_utilities = DatabaseUtilities(connection)

  def execute(self,
              username: str,
              password: str) -> bool:
    query_to_validate_admin_data = f"""
    SELECT COUNT(*) FROM ADMINS WHERE ID = '{username}' AND PASSWORD = '{password}';
    """
    result = self.db_utilities.format_query_result(
      query=query_to_validate_admin_data,
      description="Validate Admin Data"
    )
    return {
      "result": result["query_result"][0]["COUNT(*)"] == 1
    }
