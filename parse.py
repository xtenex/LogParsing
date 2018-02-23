#!/usr/bin/python

#This script sort user agent and shows the IP's related with it
# we need  to import defaultdict from collections library 'cause we're gonna need it to create a list on a dictionary
# the script could be improved adding more arguments like fields to use as keys and items
# Dependencies pip install pyyaml ua-parser user-agents
# filter([char_to_filter], [list_to_filter]) is used to clean quotes and blank spaces

import sys
from  collections import defaultdict
from user_agents import parse

def main():
    r = [] # usgin it to save data temp
    i = defaultdict(list) # we use defaultdict to create an item array related to a key it means {key:[item1, item2, ..., itemN]}
    f = open(sys.argv[1],"r") # We open a file from command line
    for line in f.readlines():
        r = line.strip("\"") #Striping first and last on each readed line
        ip = r.split(" ")[0] #extracting IP address from readed line
        ua = parse(filter(None, line.split("\""))[5]) # striping quotes and using parse to save user-agent
#        print ua.browser[0] #for debug
#        print "la ip:" + ip # for debugging prupose
#        raw_input() # for debug
        if i.has_key(ua.browser[0]): #verify if browser user-agent exist 
            i[ua.browser[0]].append(ip) #if exist, append IP address to the browserkey
        else:
            i[ua.browser[0]] = [] #if not, we create the key on dictionary
            i[ua.browser[0]].append(ip) # and append IP address to the item list

    f.close()
    for key in i.keys(): #reading dictionary key and items
        print key + ":\n" + str(i[key])[1:-1] #Showing browser and ip´s related with that browser


if __name__ == '__main__':
    main()
