'''
Vẽ 4 hình, mỗi hình cách nhau 5 giây

Draw 4 shapes, each shape separated by 5 seconds
'''
import time

def draw_1(empty: bool):
    if empty:
        print("      *      ")
        print("      * *    ")
        print("      *   *  ")
        print("* * * * * * *")
        print("*   *        ")
        print("* *          ")
        print("*            ")
    else:
        print("      *      ")
        print("      * *    ")
        print("      * * *  ")
        print("* * * * * * *")
        print("* * *        ")
        print("* *          ")
        print("*            ")
    time.sleep(5)

def draw_2(empty: bool):
    if empty:
        print("      * * * *")
        print("      *   *  ")
        print("      * *    ")
        print("      *      ")
        print("    * *      ")
        print("  *   *      ")
        print("* * * *      ")
    else:
        print("      * * * *")
        print("      * * *  ")
        print("      * *    ")
        print("      *      ")
        print("    * *      ")
        print("  * * *      ")
        print("* * * *      ")
    time.sleep(5)

draw_1(empty=True)
draw_1(empty=False)
draw_2(empty=True)
draw_2(empty=False)