# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# brute force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        listToArray=list()

        for linkedLists in lists:

            while linkedLists:
                listToArray.append(linkedLists.val)
                linkedLists=linkedLists.next
            

        listToArray.sort()
        dummy=ListNode()
        current=dummy

        for num in listToArray:
            current.next=ListNode(num)
            current=current.next

        sortedList=[dummy]
        
        return dummy.next


            
# optmized
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minHeap=list()


        for i,node in enumerate(lists):

            if node:
                heapq.heappush(minHeap,(node.val,i,node))

        
        dummy=ListNode()
        current=dummy

        while minHeap:

            value,index,smallest_node=heapq.heappop(minHeap)

            current.next=smallest_node
            current=current.next


            if(smallest_node.next):
                heapq.heappush(minHeap,(smallest_node.next.val,index,smallest_node.next))

        return dummy.next


                



        