from logic.linked_lists import Node


class CommonStack(object):
    def __init__(self):
        self._count = 0

    def __len__(self):
        return self._count

    def __eq__(self, other):
        # this is all quite silly

        if not isinstance(other, CommonStack):
            return False

        selfb = [self.pop()]
        otherb = [other.pop()]

        def do_rollback():
            nonlocal selfb, otherb

            if selfb[-1] is None:
                selfb = selfb[:-1]
            if otherb[-1] is None:
                otherb = otherb[:-1]
            for i in reversed(selfb):
                self.push(i)
            for j in reversed(otherb):
                other.push(j)

        while (selfb[-1] is not None):
            if selfb[-1] != otherb[-1]:
                do_rollback()
                return False

            selfb.append(self.pop())
            otherb.append(other.pop())

        ret = selfb[-1] == otherb[-1]
        do_rollback()
        return ret

    def peek(self):
        ret = self.pop()
        self.push(ret)
        return ret



class Stack(CommonStack):
    def __init__(self, initial=[]):
        super().__init__()
        self._head = Node()
        self._min = None

        for x in initial:
            self.push(x)

    def __eq__(self, other):
        if isinstance(other, Stack):
            return self._head == other._head
        else:
            return super(Stack, self).__eq__(other)

    def __repr__(self):
        return self._head.__repr__()

    def _push_min(self, value):
        if not self._min:
            self._min = Node(value)
        else:
            if self._min.data >= value:
                update = Node(value)
                update.next = self._min
                self._min = update

    def _pop_min(self, value):
        assert self._min is not None

        if value <= self._min.data:
            self._min = self._min.next

    def min(self):
        return self._min.data

    def push(self, val):
        new_head = Node(val)
        new_head.next = self._head
        self._head = new_head
        self._push_min(val)
        self._count += 1

    def pop(self):
        ret = self._head.data

        if self._head:
            self._pop_min(ret)
            self._head = self._head.next
            self._count -= 1

        return ret


class ArrayStack(CommonStack):
    def __init__(self, stack_size=10, num_stacks=3):
        super().__init__()
        self._data = [None] * stack_size * num_stacks
        self._heads = [0] * num_stacks

    def __repr__(self):
        return str(self._data)

    def __eq__(self, other):
        if isinstance(other, ArrayStack):
            return self._data == other._data
        else:
            return super(ArrayStack, self).__eq__(other)

    def push(self, stack, val):
        if stack >= len(self._heads) or stack < 0:
            raise IndexError("Stack index out of bounds!")

        current = self._heads[stack]
        abs_index = current * len(self._heads) + stack

        if abs_index >= len(self._data):
            raise ValueError("Out of room!")
        else:
            self._heads[stack] += 1
            self._data[abs_index] = val
            self._count += 1

    def pop(self, stack):
        target = self._heads[stack] - 1
        abs_index = target * len(self._heads) + stack

        if stack >= len(self._heads) or stack < 0:
            raise IndexError("Stack index out of bounds!")

        if target < 0:
            return None
        else:
            self._heads[stack] = target
            self._count -= 1
            return self._data[abs_index]


class SetOfStacks(ArrayStack):
    def __init__(self, threshold):
        super(SetOfStacks, self).__init__(stack_size=threshold)
        self.threshold = threshold
        self._current = 0

    def push(self, val):
        if self._heads[self._current] >= self.threshold:
            self._current += 1
        if self._current >= len(self._heads):
            raise ValueError("Stack overflow!")
        super(SetOfStacks, self).push(self._current, val)

    def pop(self, at=None):
        if at is not None:
            return super(SetOfStacks, self).pop(at)
        ret = super(SetOfStacks, self).pop(self._current)
        if ret is None:
            if self._current == 0:
                return ret  # all stacks are empty
            else:
                self._current -= 1
                return self.pop()
        return ret


class CommonQueue(object):
    def __init__(self):
        self._count = 0

    def __len__(self):
        return self._count

    def __eq__(self, other):
        if not isinstance(other, CommonQueue):
            return False
        elif len(self) != len(other):
            return False
        else:
            result = True
            for _ in range(len(self)):
                ts = self.dequeue()
                to = other.dequeue()
                if ts != to:
                    result = False
                self.enqueue(ts)
                other.enqueue(to)
            return result

    def enqueue(self):
        self._count += 1

    def dequeue(self):
        self._count -= 1


class Queue(CommonQueue):
    def __init__(self, initial=[]):
        super().__init__()
        self._front = Node()
        self._back = self._front
        for x in initial:
            self.enqueue(x)

    def __eq__(self, other):
        if isinstance(other, CommonQueue):
            return self._front == other._front and self._back == other._back
        else:
            return super().__eq__(other)

    def enqueue(self, val):
        super().enqueue()
        if not self._front:
            self._front = Node(val)
            self._back = self._front.next
        else:
            self._back.data = val
            self._back.next = Node()
            self._back = self._back.next

    def dequeue(self):
        if self._front:
            super().dequeue()
            ret = self._front.data
            self._front = self._front.next
            return ret


class MyQueue(CommonQueue):
    def __init__(self, initial=[]):
        super().__init__()
        self.inq = Stack()
        self.outq = Stack()
        for x in initial:
            self.enqueue(x)

    def enqueue(self, val):
        super().enqueue()
        self.inq.push(val)

    def dequeue(self):
        if len(self.outq):
            super().dequeue()
            return self.outq.pop()
        elif len(self.inq) == 0:
            return None
        else:
            # flush the in queue and run from the top
            for _ in range(len(self.inq)):
                self.outq.push(self.inq.pop())
            return self.dequeue()


# Hanoi stuff!
def move_stack(src, aux, dst, h, print_fn=None):
    if h == 1:
        dst.push(src.pop())
    else:
        move_stack(src, dst, aux, h - 1, print_fn)
        if print_fn: print_fn()

        move_stack(src, aux, dst, 1, print_fn)
        if print_fn: print_fn()

        move_stack(aux, src, dst, h - 1, print_fn)
        if print_fn: print_fn()


def hanoi():
    count = 5
    s0 = Stack(initial=range(1, count + 1)[::-1])
    s1 = Stack()
    s2 = Stack()

    def string_rows(stack):
        tmp = Stack()
        ret = []

        for _ in range(count - len(stack)):
            ret.append(' ' * count)

        for _ in range(len(stack)):
            val = stack.pop()
            if val is not None:
                tmp.push(val)
                ret.append('-' * val + ' ' * (count - val))

        # undo your dastardly scheme
        for _ in range(len(tmp)):
            stack.push(tmp.pop())

        return ret

    def printer():
        for a, b, c in zip(string_rows(s0), string_rows(s1), string_rows(s2)):
            print(' '.join([a, b, c]))

    move_stack(s0, s1, s2, len(s0), printer)


def pour(from_stack, to_stack):
    for _ in range(len(from_stack)):
        to_stack.push(from_stack.pop())

def sort_stack(stack):
    if len(stack) < 2:
        return stack

    head = stack.pop()
    sgt = Stack()
    sleq = Stack()
    tmp = Stack()

    for _ in range(len(stack)):
        val = stack.pop()
        if val > head:
            sgt.push(val)
        else:
            sleq.push(val)

    small = sort_stack(sleq)
    large = sort_stack(sgt)
    large.push(head)

    pour(small, tmp) # reverse small
    pour(tmp, large) # combine
    return large