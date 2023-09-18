

class Node {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  class BinarySearchTree {
    constructor() {
      this.root = null;
    }
  
    insert(value) {
      const newNode = new Node(value);
      if (!this.root) {
        this.root = newNode;
        return this;
      }
  
      let current = this.root;
      while (true) {
        if (value === current.value) return undefined;
        if (value < current.value) {
          if (!current.left) {
            current.left = newNode;
            return this;
          }
          current = current.left;
        } else {
          if (!current.right) {
            current.right = newNode;
            return this;
          }
          current = current.right;
        }
      }
    }
  
    find(value) {
      if (!this.root) return false;
      let current = this.root,
        found = false;
      while (current && !found) {
        if (value < current.value) {
          current = current.left;
        } else if (value > current.value) {
          current = current.right;
        } else {
          found = true;
        }
      }
      if (!found) return undefined;
      return current;
    }
  
  //without recursion
    displayInOrder() {
        if (this.root === null) return;
        let current = this.root;
        let stack = [];
        while (current || stack.length) {
          while (current) {
            stack.push(current);
            current = current.left;
          }
          current = stack.pop();
          console.log(current.value);
          current = current.right;
        }
      }

      //without recursion
      displayPreOrder() {
        if (this.root === null) return;
        let current = this.root;
        let stack = [];
        while (current || stack.length) {
          while (current) {
            console.log(current.value);
            stack.push(current);
            current = current.left;
          }
          current = stack.pop();
          current = current.right;
        }
      }
      
      //without recursion
      displayPostOrder() {
        if (this.root === null) return;
        let current = this.root;
        let stack = [];
        let prev = null;
        while (current || stack.length) {
          while (current) {
            stack.push(current);
            current = current.left;
          }
          current = stack.pop();
          if (!current.right || prev === current.right) {
            console.log(current.value);
            prev = current;
            current = null;
          } else {
            stack.push(current);
            current = current.right;
          }
        }
      }
      
  
      //with recursion
      postOrderPrint() {
        const result = [];
        function traverse(node) {
          if (!node) return;
          traverse(node.left);
          traverse(node.right);
          result.push(node.value);
        }
        traverse(this.root);
        return result;
      }

      //with recursion
      preOrderPrint() {
        const result = [];
        function traverse(node) {
          if (!node) return;
          result.push(node.value);
          traverse(node.left);
          traverse(node.right);
        }
        traverse(this.root);
        return result;
      }
 
  
      //with recursion
    inOrderPrint() {
      const result = [];
      function traverse(node) {
        if (!node) return;
        traverse(node.left);
        result.push(node.value);
        traverse(node.right);
      }
      traverse(this.root);
      return result;
    }
  }


  const bst = new BinarySearchTree();
  bst.insert(2);
  bst.insert(5);
  bst.insert(55);
  bst.insert(4);
  bst.insert(9);
  bst.insert(22);
  bst.insert(19);
  bst.displayInOrder()
  console.log("hello")
  bst.displayPreOrder()
  console.log("hello")
  bst.displayPostOrder()
  
 
 
  

  console.log(bst.inOrderPrint());  // prints [2, 5, 7, 10, 12, 15, 17]
  console.log(bst.preOrderPrint());  // prints [10, 5, 2, 7, 15, 12, 17]
  console.log(bst.postOrderPrint());  // prints [2, 7, 5, 12, 17, 15, 10]
  

  console.log(bst.find(9));  // returns true
  console.log(bst.find(56));  // returns false