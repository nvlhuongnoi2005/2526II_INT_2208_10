# Báo Cáo Kiểm Thử Module Tam Giác

## 1. Mục tiêu kiểm thử

Module nhận 3 số nguyên `a`, `b`, `c` và trả về loại tam giác tương ứng. Kiểm thử tập trung vào 3 nhóm chính:

- Phân hoạch tương đương cho miền dữ liệu đầu vào.
- Giá trị biên cho các ràng buộc `1..100` và điều kiện bất đẳng thức tam giác.
- Bảng quyết định cho logic phân loại.

## 2. Thiết kế test case

### 2.1 Phân hoạch tương đương

| Nhóm dữ liệu | Test đại diện | Kết quả mong đợi |
| --- | --- | --- |
| Không hợp lệ: nhỏ hơn 1 | `(0, 1, 1)` | `Invalid Input` |
| Không hợp lệ: lớn hơn 100 | `(101, 50, 50)` | `Invalid Input` |
| Không hợp lệ: không phải số nguyên | `(3.5, 4, 5)` | `Invalid Input` |
| Hợp lệ nhưng không tạo thành tam giác | `(1, 1, 3)` | `Not a Triangle` |
| Tam giác đều | `(1, 1, 1)` | `Equilateral` |
| Tam giác cân | `(5, 5, 8)` | `Isosceles` |
| Tam giác thường | `(4, 5, 6)` | `Scalene` |

### 2.2 Giá trị biên

| Biên kiểm thử | Test đại diện | Kết quả mong đợi |
| --- | --- | --- |
| Cận dưới hợp lệ | `(1, 1, 1)` | `Equilateral` |
| Cận trên hợp lệ | `(100, 100, 100)` | `Equilateral` |
| Biên bất đẳng thức tam giác | `(1, 2, 3)` | `Not a Triangle` |
| Cận cao vẫn là tam giác hợp lệ | `(98, 99, 100)` | `Scalene` |

### 2.3 Bảng quyết định

| Luật | Input hợp lệ | Thỏa bất đẳng thức tam giác | 3 cạnh bằng nhau | Chỉ 2 cạnh bằng nhau | Kết quả mong đợi |
| --- | --- | --- | --- | --- | --- |
| R1 | Không | - | - | - | `Invalid Input` |
| R2 | Có | Không | - | - | `Not a Triangle` |
| R3 | Có | Có | Có | - | `Equilateral` |
| R4 | Có | Có | Không | Có | `Isosceles` |
| R5 | Có | Có | Không | Không | `Scalene` |

## 3. Bộ test đã thực thi

Tổng cộng có 12 test case. Kết quả chạy thực tế:

- Passed: 12
- Failed: 0
- Total: 12

Lệnh chạy:

```bash
cd /home/lap/Desktop/2526II_INT_2208_10/Triangle && /home/lap/Desktop/2526II_INT_2208_10/.venv/bin/python -m unittest discover -v
```

## 4. Ghi chú

- Code xử lý nằm trong [triangle_classifier.py](triangle_classifier.py).
- Bộ test nằm trong [test_triangle_classifier.py](test_triangle_classifier.py).