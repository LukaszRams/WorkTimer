from applications.database.connect import database

database.create_table(table_name="accounts", firstname=("text", "PRIMARY KEY"),
                      lastname=("text", "NOT NULL"), password=("text", "NOT NULL"),
                      priority=("integer", "NOT NULL"),
                      position=("text",), comments=("text",))

database.add_record("Łukasz", "Rams", "luki", "3", "", "test", table_name="accounts")
