Just an sqlite starter for my other work. 

### What is it?
- contains scripts to initialize and use an sqlite database with pydantic models.

**What tables or data does it initialize the db with?**
- the database has two tables and corresponding db schemas for them in models.py
- the pydantic models are located in pydantic_models.py
- the database conn object is retrieved from database.py using get_db(), a function that automatically terminates the connection after use

**CRUD**
- Some basic crud-operation abstractions are located in crud.py
- The functions also have some callables prefixed with "agnostic". These are some sure to break MacGyver-functions I take no responsibility for. I hope they work.
