import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class BaiTap_2_AbstractLinkedList {
    public static void main(String[] args) {
        // 1
        List<Integer> list = new LinkedList<>(List.of(10, 20, 30, 40));
        PrintList(list);

        // 2
        List<Integer> templist = DeleteFirst(list);
        PrintList(templist);

        // 3
        templist = AddFirst(list, 50);
        PrintList(templist);

        // 4
        templist = Sort(list);
        PrintList(list);

        // 5
        int result = FindMax(list);
        System.out.println("Max: " + result);

        // 6
        result = FindMin(list);
        System.out.println("Min: " + result);

        // 7
        templist = Sort(list);
        PrintList(templist);
    }

    public static void PrintList(List<Integer> list)
    {
        Iterator<Integer> i = list.iterator();
        while (i.hasNext())
        {
            int element = i.next();
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static List<Integer> AddFirst(List<Integer> list, int IntegerToAdd)
    {
        List<Integer> tempList = new LinkedList<>(List.copyOf(list));
        tempList.add(0, IntegerToAdd);
        return tempList;
    }

    public static List<Integer> DeleteFirst(List<Integer> list)
    {
        List<Integer> tempList = new LinkedList<>(List.copyOf(list));
        tempList.remove(0);
        return tempList;
    }

    public static List<Integer> Sort(List<Integer> list)
    {
        List<Integer> tempList = new LinkedList<>(List.copyOf(list));
        Collections.sort(tempList);
        return tempList;
    }

    public static int FindMax(List<Integer> list)
    {
        int max = 0;
        Iterator<Integer> i = list.iterator();
        while (i.hasNext())
        {
            int element = i.next();
            if (element > max)
            {
                max = element;
            }
        }
        return max;
    }

    public static int FindMin(List<Integer> list)
    {
        int min = 0;
        Iterator<Integer> i = list.iterator();
        while (i.hasNext())
        {
            int element = i.next();
            if (element < min)
            {
                min = element;
            }
        }
        return min;
    }

    public static List<Integer> Swap(List<Integer> list, int index1, int index2)
    {
        List<Integer> tempList = new LinkedList<>(List.copyOf(list));
        Collections.swap(tempList, index1, index2);
        return tempList;
    }
}
