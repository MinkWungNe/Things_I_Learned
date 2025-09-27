import java.util.HashSet;
import java.util.Set;

public class BaiTap_6_TapHop {
    public static void main(String[] args) {
        // 1) & 2)
        Set<String> SetA = new HashSet<>(Set.of("10", "20", "50", "60", "70", "80", "1", "2", "3"));
        Set<String> SetB = new HashSet<>(Set.of("2", "3", "20", "55", "60", "7"));

        // 3) Intersect: 2, 3, 20, 60
        int result = Intersect(SetA, SetB);
        System.out.println(result);

        // 4) Union: 55, 1, 2, 3, 7, 80, 70, 60, 50, 20, 10
        result = Union(SetA, SetB);
        System.out.println(result);

        // 5) Difference: 1, 80, 70, 50, 10
        result = Difference(SetA, SetB);
        System.out.println(result);
    }

    public static int Intersect(Set<String> setA, Set<String> setB)
    {
        Set<String> intersect = new HashSet<>(setA);
        intersect.retainAll(setB);
        return intersect.size();
    }

    public static int Union(Set<String> setA, Set<String> setB)
    {
        Set<String> union = new HashSet<>(setA);
        union.addAll(setB);
        return union.size();
    }

    public static int Difference(Set<String> setA, Set<String> setB)
    {
        Set<String> difference = new HashSet<>(setA);
        difference.removeAll(setB);
        return difference.size();
    }

    
}
