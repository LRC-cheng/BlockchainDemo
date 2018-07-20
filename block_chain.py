# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:29:05 2018

@author: LRC
"""
import hashlib as hasher
import datetime as date
import threading
import time
import random as r

class Block:
    rand = 1
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.rand = r.uniform(0,1024)
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + 
                      str(self.timestamp) + 
                      str(self.data) + 
                        str(self.previous_hash)).encode(encoding='utf-8') +
                           str(self.rand).encode(encoding='utf-8'))
        return sha.hexdigest()
    
def creat_this_block(Block,rand):
    this_rand = rand
    return Block

def check_block(Block):
    s = hasher.sha256()
    s.update((str(Block.index) + 
                      str(Block.timestamp) + 
                      str(Block.data) + 
                        str(Block.previous_hash)).encode(encoding='utf-8') +
                           str(Block.rand).encode(encoding='utf-8'))
    return s.hexdigest()
    
def create_genesis_block():
    # Manually construct ablock with
    # index zero andarbitrary previous hash
    return Block(0, date.datetime.now(), "GenesisBlock", "0")

def next_block(last_block):
    this_index =last_block.index + 1
    this_timestamp =date.datetime.now()
    this_data = "Hey! I'm block " +str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
    
    # Create the blockchain and add the genesis block



class mythread(threading.Thread):
    def run(self):
        global x            #声明一个全局变量
        thread = threading.current_thread()
        while(x<num_of_blocks):
            
            block_to_add = next_block(blockchain[x])
            shash = str(block_to_add.hash)
            if (shash[0:1])!='0':
                time.sleep(0.00001)
                continue   
            r = block_to_add.rand
            
            lock.acquire()      #上锁，acquire()和release()之间的语句一次只能有一个线程进入，其余线程在acquire()处等待
            if(x>=num_of_blocks):
                lock.release()
                break
                       
            if(len(blockchain) > block_to_add.index):
                continue
            
            blockchain.append(creat_this_block(block_to_add,r))
            previous_block = block_to_add
            
            print("I 'am "+thread.getName())
            print ("Block #{} has been added to the blockchain!".format(blockchain[x].index)+
                   "\ndata:"+blockchain[x].data)
            print ("random:{}".format(str(blockchain[x].rand)))
            print ("time:{}".format(str(blockchain[x].timestamp)))
            print ("previous Hash:{}".format(blockchain[x].previous_hash))
            print ("this Hash:{}".format(blockchain[x].hash))
            print ("block len:{}".format(len(blockchain)-1))
            
            h = check_block(blockchain[x])
            print ("check Hash:{}\n".format(h))
            
            x+=1
            lock.release()      #解锁
            time.sleep(0.00001)
            

# How many blocks should we add to the chain

#after the genesis block

num_of_blocks= 20
x=0

lock = threading.RLock()    #创建 可重入锁
lock2 = threading.RLock()    #创建 可重入锁
blockchain = [create_genesis_block()]
previous_block = blockchain[0]


def main():
    l = []
    for i in range(8):
        l.append(mythread())    #创建 5 个线程，并把他们放到一个列表中
    for i in l:
        i.start()               #开启列表中的所有线程

if __name__ =='__main__':
    main()

   
   