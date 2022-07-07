class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("The list is Empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " ==> "
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_begining(10)
    # ll.insert_at_begining(12)
    # ll.insert_at_begining(1)
    # ll.insert_at_end(2)
    ll.insert_values(["Pear", "Coconut"])
    ll.print()
