# ==============================================================================
# Project Title : Implementation of Queue using Two Stacks
# Course        : PCC-201-COM : Data Structures Laboratory (SPPU 2024 Pattern)
# Student Name  : Shripad Suresh Jadhav (Roll No: 39)[cite: 43]
# Guide         : Prof. Tejal. H. Patil[cite: 43]
# ==============================================================================

class QueueUsingTwoStacks:
    """Queue implementation using two stacks with amortized O(1) time complexity."""
    def __init__(self):
        self.stack1 = []  # Main stack for incoming elements (Enqueue)
        self.stack2 = []  # Auxiliary stack for outgoing elements (Dequeue / Peek)

    def enqueue(self, item):
        """Add an element to the rear of the queue — O(1) time."""
        self.stack1.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front element of the queue — Amortized O(1) time."""
        if not self.stack1 and not self.stack2:
            print("Queue Underflow! The queue is empty.")
            return None

        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        removed_item = self.stack2.pop()
        print(f"Dequeued: {removed_item}")
        return removed_item

    def peek(self):
        """View the front element without removing it."""
        if not self.stack1 and not self.stack2:
            print("Queue is empty.")
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        front_item = self.stack2[-1]
        print(f"Front element: {front_item}")
        return front_item

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def display(self):
        """Display current queue contents from front to rear."""
        # stack2 elements are reversed (front at top), stack1 elements are in insertion order
        current_queue = self.stack2[::-1] + self.stack1
        if not current_queue:
            print("Queue is empty.")
        else:
            print("Queue contents (Front -> Rear):", current_queue)


# ==============================================================================
# INTERACTIVE CONSOLE / JUPYTER EXECUTION DEMO
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("       QUEUE USING TWO STACKS IMPLEMENTATION      ")
    print("==================================================")
    
    q = QueueUsingTwoStacks()
    
    # Test Enqueue Operations
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    # Display Queue
    q.display()
    
    # Test Dequeue Operation
    q.dequeue()
    
    # Test Peek Operation
    q.peek()
    
    # Display Queue After Operations
    q.display()
    
    # Additional Enqueue & Dequeue
    q.enqueue(40)
    q.dequeue()
    q.display()