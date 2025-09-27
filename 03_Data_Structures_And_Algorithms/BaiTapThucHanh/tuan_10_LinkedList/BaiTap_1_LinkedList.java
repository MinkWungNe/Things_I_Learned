import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class BaiTap_1_LinkedList {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>(List.of("Hung", "Vuong", "University", "of", "Ho", "Chi", "Minh", "City"));

        LinkedList<String> FirstAddedList = AddFirst(list, "Hello!");
        PrintList(FirstAddedList);

        LinkedList<String> EvenLengthDeletedList = DeleteEvenLength(list);
        PrintList(EvenLengthDeletedList);

        FindMax(list);
        
        SpecialSprint(list);
    }

    public static void PrintList(LinkedList<String> list)
    {
        Iterator<String> i = list.iterator();
        while (i.hasNext())
        {
            String element = i.next();
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static LinkedList<String> AddFirst(LinkedList<String> list, String StringToAdd)
    {
        LinkedList<String> tempList = new LinkedList<>(List.copyOf(list));
        tempList.add(0, StringToAdd);
        return tempList;
    }

    public static LinkedList<String> DeleteEvenLength(LinkedList<String> list)
    {
        LinkedList<String> tempList = new LinkedList<>(List.copyOf(list));
        Iterator<String> i = tempList.iterator();
        
        while (i.hasNext())
        {
            String element = i.next();
            if (element.length() % 2 == 0)
            {
                i.remove();
            }
        }
        return tempList;
    }

    public static void FindMax(LinkedList<String> list)
    {
        Iterator<String> i = list.iterator();
        String max = i.next();
        while (i.hasNext())
        {
            String element = i.next();
            if (element.length() > max.length())
            {
                max = element;
            }
        }

        System.out.println("Chuoi co chieu dai dai nhat: " + max);
    }

    public static void SpecialSprint(LinkedList<String> list)
    {
        Iterator<String> i = list.iterator();
        while (i.hasNext())
        {
            String element = i.next();
            System.out.println(element + "\t" + element.length());
        }
    }
}
