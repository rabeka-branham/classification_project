## **<ins>Steps to Reproduce</ins>**

1. Clone this repo.
2. Create an `env.py` file that follows the format below.
3. Save your `env.py` file into the cloned repo.
4. Run notebook.

**sample** `env.py` **file**<br>
host = 'data.codeup.com'<br>
username = 'sample_username'<br>
password = 'sample_password'<br>

def get_db_url(database_name, host_name=host, password=password, username=username):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return f'mysql+pymysql://{username}:{password}@{host_name}/{database_name}'