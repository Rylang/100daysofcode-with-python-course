"""Extract datetimes from log entries and calculate the time
   between the first and last shutdown events"""
from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)"""
    return datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    """Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object."""
    shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_times = [convert_to_datetime(shutdown_event) for shutdown_event in shutdown_entries]
    return max(shutdown_times) - min(shutdown_times)

# Original Copy
# def time_between_shutdowns(loglines):
#     """Extract shutdown events ("Shutdown initiated") from loglines and calculate the
#        timedelta between the first and last one.
#        Return this datetime.timedelta object."""
#     first_shutdown = ''
#     last_shutdown = ''
#     first_shutdown_found = False
#     for line in loglines:
#         if 'Shutdown initiated' in line:
#             if not first_shutdown_found:
#                 first_shutdown = datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')
#                 first_shutdown_found = True
#             else:
#                 last_shutdown = datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')
#     return last_shutdown - first_shutdown
