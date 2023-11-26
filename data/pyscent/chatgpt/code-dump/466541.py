import unittest
import queue

class TestPrimAlgorithm(unittest.TestCase):

    def test_simple_graph(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        A.addOutNeighbor(B, 1)
        A.addOutNeighbor(C, 2)
        G = [A, B, C]
        MST = prim(G, A)
        self.assertEqual(len(MST), 3)
        self.assertIn(A, MST)
        self.assertIn(B, MST)
        self.assertIn(C, MST)

    def test_four_nodes_unique_MST(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        D = Node('D')
        A.addOutNeighbor(B, 2)
        A.addOutNeighbor(C, 3)
        B.addOutNeighbor(C, 1)
        B.addOutNeighbor(D, 3)
        C.addOutNeighbor(D, 2)
        G = [A, B, C, D]
        MST = prim(G, A)
        self.assertEqual(len(MST), 4)
        self.assertIn(A, MST)
        self.assertIn(B, MST)
        self.assertIn(C, MST)
        self.assertIn(D, MST)

    def test_empty_graph(self):
        G = []
        MST = prim(G, None)
        self.assertIsNone(MST)

    def test_single_node_graph(self):
        A = Node('A')
        G = [A]
        MST = prim(G, A)
        self.assertEqual(len(MST), 1)
        self.assertIn(A, MST)

if __name__ == '__main__':
    unittest.main()
