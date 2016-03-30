from fabric.api import *

filetoread = ""

def read_file():
	global filetoread
	sudo("tail -f " + str(filetoread))

def tail_logs():
	global filetoread
	hosts = raw_input('Enter hosts separated by a space to tail logs from: ')
	env.hosts=hosts.split()
	filetoread = raw_input('Enter file to read: ')

@task
def taillogs():
	execute(tail_logs)
	execute(parallel(read_file))
