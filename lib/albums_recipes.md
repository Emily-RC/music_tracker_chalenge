# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

Albums: 

 id |        title         | release_year | artist_id
----+----------------------+--------------+-----------
  1 | Doolittle            |         1989 |         1
  2 | Surfer Rosa          |         1988 |         1
  4 | Super Trouper        |         1980 |         2
  5 | Bossanova            |         1990 |         1
  6 | Lover                |         2019 |         3
  7 | Folklore             |         2020 |         3
  8 | I Put a Spell on You |         1965 |         4
  9 | Baltimore            |         1978 |         4
 10 | Here Comes the Sun   |         1971 |         4
 11 | Fodder on My Wings   |         1982 |         4
  3 | Waterloo             |         1972 |         2
 13 | Amazing Grace        |         1972 |         5
(12 rows)

Artists: 

 id |      name       | genre
----+-----------------+-------
  1 | Pixies          | Rock
  2 | ABBA            | Pop
  3 | Taylor Swift    | Pop
  4 | Nina Simone     | Jazz
  5 | Aretha Franklin | Soul

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql

-- EXAMPLE
file: spec/seeds_albums.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE albums RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO albums (id, title, release_year, artist_id) VALUES ('1', 'Doolittle', '1989', '1');
INSERT INTO albums (id, title, release_year, artist_id) VALUES ('2', 'Surfer Rosa', '1988', '1');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 music_library < seeds_albums.sql
```
-- EXAMPLE
file: spec/seeds_artists.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE artists RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO artists (id, title, release_year, artist_id) VALUES ('1', 'Pixies', 'Rock');
INSERT INTO artists (id, title, release_year, artist_id) VALUES ('2', 'ABBA', 'Pop');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 music_library < seeds_albums.sql

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: albums

# Model class
# (in lib/albums.py)
class Album


# Repository class
# (in lib/album_repository.py)
class AlbumRepository

```

```python
# EXAMPLE
# Table name: artists

# Model class
# (in lib/artists.py)
class Artist


# Repository class
# (in lib/album_repository.py)
class ArtistRepository

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: albums

# Model class
# (in lib/albums.py)

class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.release_year = 0  # Need to check whether this should be an int or a str 
        self.artist_id = 0


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> albums = Album()
# >>> albums.id = 1
# >>> albums.title = "Doolittle"
# >>> albums.release_year = "1989"
# >>> albums.artist_id = 1

# 'Dootlittle'
# >>> albums.release_year
# '1989'

class Artist:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.genre = ""


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> artists = Artist()
# >>> artists.id = 1
# >>> artists.name = "Pixies"
# >>> artists.genre = "Rock"

# 'Pixies'
# >>> artists.genre
# 'Rock'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of Album objects.

    #     # Gets a single record by its ID
    #     # One argument: the id (number)
    # def find(id):
    #     # Executes the SQL query:
    #     # SELECT id, name, cohort_name FROM students WHERE id = $1;

    #     # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    # 

    # def update(student)
    # 

    # def delete(student)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = AlbumRepository()

albums = repo.all()

albums[0].id # =>  1
albums[0].title # =>  'Doolittle'
albums[0].release_year# =>  '1989'
albums[1].artists_id# => '1'

albums[1].id # =>  2
albums[1].title # =>  'Surfer Rosa'
albums[1].release_year# =>  '1988'
albums[1].artists_id# => '1'

# # 2
# # Get a single student

# repo = StudentRepository()

# student = repo.find(1)

# student.id # =>  1
# student.name # =>  'David'
# student.cohort_name # =>  'April 2022'

# # Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->