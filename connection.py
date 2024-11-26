import pymysql
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import os 

import logging  # You need to import logging if you use logging in verbose mode

def getpwds():
    """Read passwords from the passwd file. Assumes file is named 
    passwd (no file extension!). 
    
    :return ssh,db ssh password and db password"""
    pathname = os.path.dirname(__file__)  
    with open(pathname + '/passwd', encoding="utf-8") as f:
        ssh = f.readline().strip()
        db = f.readline().strip()
    return ssh, db

def open_ssh_tunnel(host, user, pwd, verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    
    :param host: host name
    :param user: username on host 
    :param pwd: password on host
    :param verbose: Set to True to show logging
    :return tunnel: SSH tunnel connection
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    # Start the SSH tunnel
    tunnel = SSHTunnelForwarder(
        (host, 22),  # SSH connection to the remote host on port 22
        ssh_username=user,  # SSH username
        ssh_password=pwd,  # SSH password
        remote_bind_address=('127.0.0.1', 3306)  # Remote MySQL server (localhost:3306)
    )
    tunnel.start()  # Start the tunnel
    print("SSH Tunnel Established.")
    return tunnel

def mysql_connect(dbname, dbuser, dbpwd, tunnel):
    """Connect to a MySQL server using the SSH tunnel connection.
    
    :param dbname: name of the database 
    :param dbuser: username for the database 
    :param dbpwd: password for the database 
    :param tunnel: SSH tunnel connection to the database host server

    :return connection: MySQL database connection
    """
    
    # Create the connection to MySQL via the local bind port of the tunnel
    connection = pymysql.connect(
        host='127.0.0.1',  # Local address for the tunnel
        user=dbuser,  # Database username
        passwd=dbpwd,  # Database password
        db=dbname,  # Database name
        port=tunnel.local_bind_port  # Local bind port of the SSH tunnel
    )
    print("MYSQL database connection established.")
    return connection









        

"""
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))


route_names=['apple','banana','cherry','dragonfruit','pear']
setters=['a','b','c','d']
dates=[dateset(2024,11,19),dateset(2024,11,20),dateset(2024,11,21)]

"""

