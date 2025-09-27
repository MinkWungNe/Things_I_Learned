public interface Shape {
    public double getArea();      // Diện tích
    public double getPerimeter(); // Chu vi
}

/*========================[ NOTE]=======================================================================*
 * - interface: là tập hợp các hàm được khai báo nhưng chưa được định nghĩa.                            *
 * - Để sử dụng interface, cần có 1 class để [implements] nó,                                           *
 *  khi implement, bắt buộc phải định nghĩa tất cả các hàm từ interface.                                *
 *                                                                                                      *
 * - Đây là một ứng dụng của 1 trong 4 tính chất cơ bản của Class: Tính trừu tượng (abstract).          *
 *                                                                                                      *
 *======================================================================================================*/