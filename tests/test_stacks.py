import unittest

from logic.stacks import *

class TestStacksAndQueues(unittest.TestCase):
    def setUp(self):
        self.stack = Stack([1,2,3,4,5])
        self.queue = Queue(['a', 'b', 'c', 'd', 'e'])

    def tearDown(self):
        pass

    def stacktest(self, test_stack):
        self.assertEqual(test_stack.pop(), 5)
        self.assertEqual(test_stack.pop(), 4)
        self.assertEqual(test_stack.pop(), 3)
        self.assertEqual(test_stack, Stack([1,2]))
        self.assertEqual(test_stack.pop(), 2)
        self.assertEqual(test_stack.pop(), 1)
        self.assertEqual(test_stack.pop(), None)
        self.assertEqual(test_stack.pop(), None)
        test_stack.push(0)
        test_stack.push(-2)
        self.assertEqual(test_stack, Stack([0, -2]))

    def test_stack_min(self):
        self.assertEqual(self.stack.min(), 1)
        self.stack.push(-2)
        self.stack.push(6)
        self.stack.push(-3)
        self.assertEqual(self.stack.min(), -3)
        self.stack.pop() # -3
        self.stack.pop() # 6
        self.assertEqual(self.stack.min(), -2)
        self.stack.pop() # -2
        self.stack.pop() # 5
        self.stack.pop() # 4
        self.stack.pop() # 3
        self.stack.pop() # 2
        self.stack.pop() # 1
        self.stack.pop() # None
        self.assertEqual(self.stack.min(), None)

    def test_stack(self):
        self.stacktest(self.stack)

    def test_set_of_stacks(self):
        sos = SetOfStacks(10)
        for x in range(1,6):
            sos.push(x)
        self.stacktest(sos)

    def test_queue(self):
        self.assertEqual(self.queue.dequeue(), 'a')
        self.assertEqual(self.queue.dequeue(), 'b')
        self.assertEqual(self.queue.dequeue(), 'c')
        self.assertEqual(self.queue, Queue(['d', 'e']))
        self.assertEqual(self.queue.dequeue(), 'd')
        self.assertEqual(self.queue.dequeue(), 'e')
        self.assertEqual(self.queue.dequeue(), None)
        self.assertEqual(self.queue.dequeue(), None)
        self.queue.enqueue('f')
        self.queue.enqueue('g')
        self.assertEqual(self.queue, Queue(['f', 'g']))

    def test_array_stack(self):
        astack = ArrayStack(stack_size=3)
        astack.push(0, "d")
        astack.push(0, "o")
        astack.push(0, "g")

        astack.push(1, "c")
        astack.push(1, "a")
        astack.push(1, "t")

        astack.push(2, "r")
        astack.push(2, "a")
        astack.push(2, "t")
        self.assertEqual(astack._data,
            ['d','c','r','o','a','a','g','t','t'])

        self.assertEqual(astack.pop(2), 't')
        self.assertEqual(astack.pop(2), 'a')
        self.assertEqual(astack.pop(2), 'r')
        self.assertEqual(astack.pop(2), None)
        self.assertEqual(astack.pop(2), None)

        astack.push(2, "f")
        astack.push(2, "u")
        astack.push(2, "l")
        self.assertRaises(ValueError, astack.push, 2, "l")
        self.assertRaises(IndexError, astack.push, 3, "x")