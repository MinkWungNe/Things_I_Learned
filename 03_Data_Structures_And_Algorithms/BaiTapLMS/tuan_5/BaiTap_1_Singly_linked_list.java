class Node  // Tạo class Node
{
    int data;   // Để lưu giá trị
    Node next;  // Để lưu địa chỉ tới node tiếp theo

    public Node(int dataInput)
    {
        data = dataInput;   // Gắn giá trị vào
        next = null;        // Mặc định rỗng
    }
}

public class BaiTap_1_Singly_linked_list {
    Node head;

    public void InsertFirst(int input)
    {
        Node newNode = new Node(input);
        newNode.next = head;
        head = newNode;
    }

    public void DeleteFirst()
    {
        head = head.next;
    }

    public void displayList()
    {
        System.out.println("List (first -> last): ");
        Node current = head;
        while(current != null)
        {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        BaiTap_1_Singly_linked_list List = new BaiTap_1_Singly_linked_list();   // Dùng để khởi tạo chương trình
        int arr[] = {1,2,3,4,5};

        for (int i : arr)
        {
            List.InsertFirst(i);
        }

        List.displayList();

        List.DeleteFirst();

        List.displayList();
        
    }
}
