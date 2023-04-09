import unittest
from singlyLinkedListIterator import SinglyLinkedListIterator
from doublyLinkedListIterator import DoublyLinkedListIterator

class TestList(unittest.TestCase):
    singly_list = SinglyLinkedListIterator()
    
    def test_last_node(self):
        singlylist = SinglyLinkedListIterator()
        
        singlylist.addNode(1, None)
        
        singlylist.insNode(2, None)
        
        singlylist.insNode(3, None)
        
        singlylist.last_Node()
        
        self.assertEqual(singlylist.lastNode.data, 1, "Last Node Should be 1")

    def test_next_node(self):
        singlylist = SinglyLinkedListIterator()
        
        singlylist.addNode(1, None)
        
        singlylist.insNode(2, None)
        
        singlylist.insNode(3, None)
        
        singlylist.last_Node()
        
        self.assertEqual(singlylist.lastNode.data, 1, "Last Node Should be 3")
        
    
    def test_add_node(self):
        singlylist = SinglyLinkedListIterator()
        
        singlylist.addNode(10, None)
        
        singlylist.first_Node()
        
        self.assertEqual(singlylist.iterator.data, 10, "Added node data Should be 10.")
    
    def test_ins_node(self):
        singlylist = SinglyLinkedListIterator()
        
        singlylist.addNode(10, None)
        
        singlylist.insNode(9, None)
        
        singlylist.first_Node()
        
        self.assertEqual(singlylist.iterator.data, 9, "Inserted node data Should be 9.")
    
    def test_elim_node(self):
        singlylist = SinglyLinkedListIterator()
        
        singlylist.addNode(9, None)
        
        singlylist.addNode(10, None)
        
        singlylist.elimNode()
        
        self.assertEqual(singlylist.firstNode == singlylist.lastNode, True, "List firstNode must be equal to list lastNode")

if __name__ == '__main__':
    unittest.main()