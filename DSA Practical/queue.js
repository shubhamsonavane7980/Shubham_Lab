
class Node{
  constructor( data , next = null){
    this.data = data;
    this.next = next;
  }
}

class Queue{
  constructor(){
    this.head  = null;
    this.tail = null;
    this.size =0;
  }


  enqueu(data){
    if(!this.head){
      this.head = this.tail = new Node(data)
    }else{
 this.tail = this.tail.next = new Node ( data)
    }this.size++;
  }

  dequeu(){
if(!this.head){
  console.log("queue is empty")
}else{
    this.head = this.head.next
    this.size--;
  }
}

 

display(){
  let current = this.head

  while(current){
    console.log(current.data)
    current = current.next
  }
}
}

const ll = new Queue()
ll.enqueu(1000)
ll.enqueu(2000)
ll.enqueu(3000)
ll.enqueu(4000)
ll.dequeu()

ll.display()
