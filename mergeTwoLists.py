# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 14:58:34 2016

@author: yaoxia
"""

import linklst as ll
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def insert(l1,l2):
            n2 = l2
        #    print ll.CrtList(l1),ll.CrtList(l2)
            l2 =n2.next
        #    print ll.CrtList(l1),ll.CrtList(l2)
            n1 = l1.next
        #    print ll.CrtList(l1),ll.CrtList(l2)
            l1.next = n2
        #    print ll.CrtList(l1),ll.CrtList(l2)
            n2.next = n1
            n3 = l1
        #    print ll.CrtList(l1),ll.CrtList(l2)
        #    a = l1.next.next
            return n3,l2 
        
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        if not l1 and not l2:
            return l1


        if l1.val >= l2.val:
            b,s = l1, l2
        else:
            s,b = l1, l2    
        result = s
        while s.next and b: 
            if b.val <= s.next.val:
                (s,b) = insert(s,b)
            else: 
                s = s.next
    #        print ll.CrtList(result),ll.CrtList(b),ll.CrtList(s)
            
        if not s.next:
            s.next = b
    #        print ll.CrtList(result),ll.CrtList(b),ll.CrtList(s)
        return result
        
l1 = [3,4,5,6]
l2 = [1,2,3,4]
a1 = ll.CreatLinkList(l1)
a2 = ll.CreatLinkList(l2)
print ll.CrtList(a1),ll.CrtList(a2)
#(a3,a2) = insert(a1,a2)
#(a3,a2) = insert(a3,a2)
b = Solution()
c = b.mergeTwoLists(a1,a2)

#a2 = insert(a1.next.next,a2)
#a1 = insert(a1,a2)
#print ll.CrtList(a1),ll.CrtList(a2),ll.CrtList(a3)
#a2 = insert(a1,a2)
#print ll.CrtList(a1),ll.CrtList(a2)
#print ll.CrtList(dum.next)
#print ll.CrtList(swap(dum).next)


#b = Solution()
#c = b.mergeTwoList(a)
#
##
print ll.CrtList(c), 'Results'        