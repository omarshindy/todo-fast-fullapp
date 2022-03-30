from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Development Database
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

#Production Databse
# POSTGRESQL_DATABASE_URL = "postgresql://postgres:postgres@localhost/TodoApplicationDatabase"

# MYSQL Series
MYSQL_DATABASE_URL = "mysql+pymysql://root:password@127.0.0.1:3306/todoapp"

engine = create_engine(
    # POSTGRESQL_DATABASE_URL
    MYSQL_DATABASE_URL
)

# MYSQL Series
# engine = create_engine(
#     MYSQL_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
