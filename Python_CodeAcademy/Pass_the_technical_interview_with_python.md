<h2>Why Data Structures?</h2>

**DataStructures:**
- backbone of every program: data and algorithms
- algorithms transform data into something a program can effectively use
- important to know how to structure data so algorithms can maintain, utilize and iterate throught data quickly
- DSs are the way we are able to store and retireve data
- Python:
1. lists are sequential with data accessed by index
2. dictionaries use a named key to store and retrieve information

Data structures handle four main functions for us:
- Inputting information
- Processing information
- Maintaining information
- Retrieving information


<h2>Nodes</h2>
Nodes are the fundamental building blocks of many computer science data structures. They form the basis for linked, stacks, queues, trees, and more.

- an individual node contains data and links to other nodes. Each data scructure adds additional constraints or behavior to these features to create the desired structure.

A Node is a basic building block of data structures like:
- Linked List
- Tree
- Graph

A Node typically has two parts:
1. Data – the value it holds.
2. Reference (or pointer) – a link to another node.

**Node Linking**
- Nodes may only be linked to from a single other node (consider how implement modifying or removing nodes)
- inadvertently remove the single link to a node -> node's data is lost -> orphaned node
- most logical way is to not create a straight line of nodes but to link more nodes to one