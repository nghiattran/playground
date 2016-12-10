#include <stdio.h>

struct Node
{
  Node* next;
  int value;
  
  Node(int value) {
    this->value = value;
  }
};

struct LinkedList
{
  Node* head;

  LinkedList() {}

  LinkedList(Node* node) 
  {
    this->head = node;
  }

  ~LinkedList() 
  {
    if (!this->head) {
      return;
    }

    Node* tmp = this->head;
    Node* previousNode = this->head;
    while(tmp) {
      previousNode = tmp;
      tmp = tmp->next;
      printf("delete %d\n", previousNode->value);
      delete previousNode;
    }
  }

  void addNode(Node* node) {
    if (!this->head) {
      this->head = node;
      return;
    }

    Node* tmp = this->head;
    if (node->value < tmp->value) {
      node->next = tmp;
      this->head = node;
    } else {
      while(tmp->next && tmp->next->value < node->value) {
        tmp = tmp->next;
      }

      if (tmp->next)
      {
        node->next = tmp->next;
      }
      tmp->next = node;
    }
  }

  void deleteNode(Node* node) {
    if (!this->head) {
      return;
    }

    Node* tmp = this->head;
    if (node->value == tmp->value) {
      this->head = this->head->next;
    } else {
      while(tmp->next) {
        if (tmp->next->value == node->value)
        {
          Node* foundNode = tmp->next;
          tmp->next = tmp->next->next;
          delete foundNode;
          return;
        }
        tmp = tmp->next;
      }
    }
  }

  void print() {
    Node* tmp = this->head;
    printf("Print LinkedList\n");
    while(tmp) {
      printf("%d\n", tmp->value);
      tmp = tmp->next;
    }
    printf("\n");
  }
};

int main(int argc, char const *argv[])
{
  LinkedList* list = new LinkedList();
  Node* node1 = new Node(4);
  Node* node2 = new Node(5);
  Node* node3 = new Node(1);
  Node* node4 = new Node(26);
  Node* node5 = new Node(15);
  Node* node6 = new Node(65);
  Node* node7 = new Node(8);
  Node* node8 = new Node(102);

  list->addNode(node1);
  list->addNode(node2);
  list->addNode(node3);
  list->addNode(node4);
  list->addNode(node5);
  list->addNode(node6);
  list->addNode(node7);
  list->addNode(node8);

  list->print();

  list->deleteNode(node3);
  list->deleteNode(node6);

  list->print();

  delete list;
  return 0;
}