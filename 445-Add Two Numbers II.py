# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:13:31 2019

@author: hecongcong
"""



#definition for singly-linked list.
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
'''

####解法1：
class Solution:
    def addTwoNumbers(self,l1,l2):
        s1=[]
        s2=[]
        
        while(l1):
            s1.append(l1.val)
            l1=l1.next
        while(l2):
            s2.append(l2.val)
            l2=l2.next
        
        jinwei=0
        cur=None
        
        while(s1!=[] or s2!=[]):
            if(s1!=[]):
                val1=s1.pop()
            else:
                val1=0
            
            if(s2!=[]):
                val2=s2.pop()
            else:
                val2=0
            
            sums=val1+val2+jinwei
            jinwei=sums//10
            
            res=ListNode(sums%10)
            res.next=cur
            
            cur=res
        if(jinwei==0):
            return res
        else:
            res=ListNode(jinwei)
            res.next=cur
            return res
        
        
###精简
class Solution:
    def addTwoNumbers(self,l1,l2):
        s1=[]
        s2=[]
        while(l1):
            s1.append(l1.val)
            l1=l1.next
        
        while(l2):
            s2.append(l2.val)
            l2=l2.next
        
        sums=0
        cur=ListNode(0)
        while(s1!=[] or s2!=[]):
            if(s1!=[]):
                sums+=s1.pop()
            if(s2!=[]):
                sums+=s2.pop()
            
            cur.val=sums % 10
            res=ListNode(sums//10)
            res.next=cur
            cur=res
            sums//=10
        return(cur.next if(cur.val==0) else cur)
        
        
        
        
        
        
        
        