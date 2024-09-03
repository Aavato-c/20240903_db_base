# SB - A ``s``imple ``d``atabase
This is just a personal project I've built to grab as a skeleton for my other projects.

### What is it?
- It's a python module that contains scripts to initialize and use an sqlite database.

**What tables or data does it initialize the db with?**
- The database has two tables and corresponding db schemas for them in models.py
- The pydantic models are located in pydantic_models.py
- The database conn object is retrieved from database.py using get_db(), a function that automatically terminates the connection after use

**CRUD**
- Some basic crud-operation abstractions are located in crud.py
- The functions also have some callables prefixed with "agnostic". These are some sure to break MacGyver-functions I take no responsibility for. I hope they work.
