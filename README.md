# CPSC 449 - Bookstore

### A bookstore api made with FastAPI supporting a no-sql DB


## Usage

1) Clone the repository
    - `$ git clone https://github.com/JustinStitt/bookstore-449.git`

2) Go into the directory and set-up a **virtual environment**
    - `$ cd bookstore-449 && python -m virtualenv .venv`

3) Activate the **virtual environment**
    - `$ source ./.venv/bin/activate`

4) Install necessary **dependencies**
    - `$ pip install -r requirements.txt`

5) Make a mongoDB database and collection

> Name the database `cpsc449`
> and the collection `bookstore`

6) Set your mongoDB Atlas credentials in `example.env` then rename to `.env`

> Find your password at `Security > Database Access` section of the mongoDB dashboard

7) Run `./tesh.sh` to ensure all packages installed correctly and database connection is formed

8) Run the api
    - `$ ./run.sh`

*Optional*

9) You can populate your database with *dummy* data
    - `$ python -m bookstore.populate`

#### References
* [FastAPI docs](https://fastapi.tiangolo.com)
* [mongoDB docs](https://www.mongodb.com/docs/)
* [Python3 docs](https://docs.python.org/3/)

#### Group
> **Note**
Group #5

[▶ Watch our Video!](https://youtu.be/B7US33upu6s)
