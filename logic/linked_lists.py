# Chapter 2
# Linked Lists

class Node(object):
    @staticmethod
    def gen_nodes(n=1, head=None):
        if not head:
            head = Node(n)

        if n < 1:
            return Node()
        else:
            head.next = Node.gen_nodes(n-1, head.next)
            return head

    @staticmethod
    def from_list(intlist):
        head = ret = Node()
        for i in intlist:
            head.data = i
            head.next = Node()
            head = head.next
        return ret

    def __init__(self, data=None):
        self.data = data
        self.next = None if data is None else Node()

    def __bool__(self):
         return not (self.data is None and self.next is None)

    def __str__(self):
        if not self.next:
            return '{}'.format(self.data)
        else:
            return '{} --> {}'.format(self.data, self.next.__str__())

    def __repr__(self):
        return str(self)

    def __len__(self):
        count = 0
        head = self
        while(head.next):
            count += 1
            head = head.next
        return count

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        while(self):
            if not self.data == other.data:
                return False
            if bool(self.next) != bool(other.next):
                # if one is longer than the other
                return False
            self = self.next
            other = other.next
        return True

    def add(self, node):
        self.next = node

    def append(self, node):
        head = self
        while(head.next):
            head = head.next
        head.next = node

    def reversed(self):
        head = self
        last = Node()

        while(head.next):
            future = head.next
            head.next = last
            last = head
            head = future

        head.next = last

        return head

# 2.4
def add_lists(lhs, rhs):
    carry = 0
    ret = rethead = Node()

    while(lhs or rhs or carry):
        lhsd = lhs.data if lhs else 0
        rhsd = rhs.data if rhs else 0

        result = lhsd + rhsd + carry
        carry = result // 10
        ones = result % 10

        ret.data = ones
        ret.next = Node()

        ret = ret.next
        lhs = lhs.next or Node()
        rhs = rhs.next or Node()

    return rethead

# 2.3
def delete_node(target):
    if not target.next:
        target.data = None
    else:
        target.data = target.next.data
        target.next = target.next.next

# 2.2
def n_to_last(head, n):
    list_len = 1
    cur = head
    while(cur.next):
        list_len += 1
        cur = cur.next

    cur = head
    target_node = list_len - n

    if target_node < 0:
        return head

    counter = 0
    while(cur.next):
        if counter == target_node:
            return cur
        counter += 1
        cur = cur.next

# 2.1
def remove_duplicates(head):
    record = set()
    cur = head
    while (cur.next):
        record.add(cur.data)
        if cur.next.data in record:
            cur.next = cur.next.next
        else:
            cur = cur.next

def remove_duplicates_ip(head):
    if not head or not head.next:
        return

    approved = head

    while(approved.next):
        explorer = approved.next
        while(explorer.next):
            if explorer.data == approved.data:
                explorer.data = explorer.next.data
                explorer.next = explorer.next.next
            else:
                explorer = explorer.next
        else:
            if explorer.data == approved.data:
                explorer.data = explorer.next.data
                explorer.next = explorer.next.next

        approved = approved.next
