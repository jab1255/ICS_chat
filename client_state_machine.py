"""
Created on Sun Apr  5 00:00:32 2015

@author: zhengzhang
"""
from chat_utils import *
import json

class ClientSM:
    def __init__(self, s):
        self.state = S_OFFLINE
        self.peer = ''
        self.me = ''
        self.out_msg = ''
        self.s = s
        self.game_peer = ''
<<<<<<< HEAD
        self.move = []
        

=======
        self.array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.key = ''
        
>>>>>>> 3f7a692a3757c2820248b89220ce64b12710b9bf
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_myname(self, name):
        self.me = name

    def get_myname(self):
        return self.me

    def connect_to(self, peer):
        msg = json.dumps({"action":"connect", "target":peer})
        mysend(self.s, msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.peer = peer
            self.out_msg += 'You are connected with '+ self.peer + '\n'
            return (True)
        elif response["status"] == "busy":
            self.out_msg += 'User is busy. Please try again later\n'
        elif response["status"] == "self":
            self.out_msg += 'Cannot talk to yourself (sick)\n'
        else:
            self.out_msg += 'User is not online, try again later\n'
        return(False)

    def disconnect(self):
        msg = json.dumps({"action":"disconnect"})
        mysend(self.s, msg)
        self.out_msg += 'You are disconnected from ' + self.peer + '\n'
        self.peer = ''
        
    def tictactoe_to(self, peer):
        msg = json.dumps({"action":"game_request", "from":peer})
        mysend(self.s, msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.game_peer = peer
            self.key = "X"
            self.out_msg += 'You are playing with '+ self.game_peer + '\n'
            return (True)
        elif response["status"] == "busy":
            self.out_msg += 'User is busy. Please try again later\n'
        elif response["status"] == "self":
            self.out_msg += 'You should not play with yourself (sick)\n'
        else:
            self.out_msg += 'User is not online, try again later\n'
        return(False)
        
    def print_array(self):
        for l in self.array:
            self.out_msg += str(l) + '\n'
        
    def player_move(self,command, key):
        self.move = []
        for c in command:
            try:
                self.move.append(int(c))
            except:
                pass
        
        if  self.array[self.move[1]][self.move[0]] == " ":
            self.array[self.move[1]][self.move[0]] = key
            self.print_array()
            return True
        else:
            self.out_msg += "Invalid move. Position is already taken."
        
        
    def proc(self, my_msg, peer_msg):
        self.out_msg = ''
        
        
       
#==============================================================================
# Once logged in, do a few things: get peer listing, connect, search
# And, of course, if you are so bored, just go
# This is event handling instate "S_LOGGEDIN"
#==============================================================================
        if self.state == S_LOGGEDIN:
            # todo: can't deal with multiple lines yet
            if len(my_msg) > 0:

                if my_msg == 'q':
                    self.out_msg += 'See you next time!\n'
                    self.state = S_OFFLINE

                elif my_msg == 'time':
                    mysend(self.s, json.dumps({"action":"time"}))
                    time_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += "Time is: " + time_in

                elif my_msg == 'who':
                    mysend(self.s, json.dumps({"action":"list"}))
                    logged_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += 'Here are all the users in the system:\n'
                    self.out_msg += logged_in

                elif my_msg[0] == 'c':
                    peer = my_msg[1:]
                    peer = peer.strip()
                    if self.connect_to(peer) == True:
                        self.state = S_CHATTING
                        self.out_msg += 'Connect to ' + peer + '. Chat away!\n\n'
                        self.out_msg += '-----------------------------------\n'
                    else:
                        self.out_msg += 'Connection unsuccessful\n'

                elif my_msg[0] == '?':
                    term = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"search", "target":term}))
                    search_rslt = json.loads(myrecv(self.s))["results"].strip()
                    if (len(search_rslt)) > 0:
                        self.out_msg += search_rslt + '\n\n'
                    else:
                        self.out_msg += '\'' + term + '\'' + ' not found\n\n'

                elif my_msg[0] == 'p' and my_msg[1:].isdigit():
                    poem_idx = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"poem", "target":poem_idx}))
                    poem = json.loads(myrecv(self.s))["results"]
                    # print(poem)
                    if (len(poem) > 0):
                        self.out_msg += poem + '\n\n'
                    else:
                        self.out_msg += 'Sonnet ' + poem_idx + ' not found\n\n'

                else:
                    self.out_msg += menu

            if len(peer_msg) > 0:
                peer_msg = json.loads(peer_msg)
                if peer_msg["action"] == "connect":
                    self.peer = peer_msg["from"]
                    self.out_msg += 'Request from ' + self.peer + '\n'
                    self.out_msg += 'You are connected with ' + self.peer
                    self.out_msg += '. Chat away!\n\n'
                    self.out_msg += '------------------------------------\n'
                    self.state = S_CHATTING
    
#==============================================================================
# Start chatting, 'bye' for quit
# This is event handling instate "S_CHATTING"
#==============================================================================
        elif self.state == S_CHATTING:
            if len(my_msg) > 0:     # my stuff going out
                mysend(self.s, json.dumps({"action":"exchange", "from":"[" + self.me + "]", "message":my_msg}))
                if my_msg == 'bye':
                    self.disconnect()
                    self.state = S_LOGGEDIN
                    self.peer = ''
                if my_msg[0:9] == 'tictactoe':
                    peer = my_msg[10:]
                    peer.strip()
                    if self.tictactoe_to(peer) == True:
                        self.out_msg += 'Connected to ' + peer + '. Match on!\n\n'
                        self.out_msg += '-----------------------------------\n'
                        self.state = S_PLAYING
                    else:
                        self.out_msg += 'Connection unsuccessful\n'
            
            if len(peer_msg) > 0:    # peer's stuff, coming in
                peer_msg = json.loads(peer_msg)
                if peer_msg["action"] == "connect":
                    self.out_msg += "(" + peer_msg["from"] + " joined)\n"
                elif peer_msg["action"] == "disconnect":
                    self.state = S_LOGGEDIN
            
                elif len(peer_msg) > 0:
                    if peer_msg["action"] == "game_request":
                        self.game_peer = peer_msg["from"]
                        self.key = "O"
                        self.out_msg += 'Request from ' + self.game_peer + '\n'
                        self.out_msg += 'You are connected with ' + self.peer
                        self.out_msg += '. Match on!\n\n'
                        self.out_msg += '------------------------------------\n'
                        self.state = S_PLAYING
                
                else:
                    self.out_msg += peer_msg["from"] + peer_msg["message"]


            # Display the menu again
            if self.state == S_LOGGEDIN:
                self.out_msg += menu
                
#==============================================================================
# TICTACTOE
#==============================================================================
                
        elif self.state == S_PLAYING:
<<<<<<< HEAD
            
            if len(my_msg) > 0:
                if self.player_move(my_msg, self.key) == TRUE:
                    msg = json.dumps({"action":"move", "from":self.me, "position" : my_msg, "key": self.key})
                    mysend(self.s, msg)
            if len(peer_msg) > 0: 
                if peer_msg["action"] == "move":
                    command = peer_msg['position']
                    key = peer_msg['key']
                    self.player_move(command, key)
=======
            for l in self.array:
                self.out_msg += str(l) + '\n'
            self.out_msg += 'Game functionality: type x,y coordinates\n\
                            0,0 is the top-left corner and 2,2 is the\n\
                            bottom-right corner' 
>>>>>>> 3f7a692a3757c2820248b89220ce64b12710b9bf
#==============================================================================
# invalid state
#==============================================================================

        else:
            self.out_msg += 'How did you wind up here??\n'
            print_state(self.state)

        return self.out_msg
