# Báo cáo ý 1: Phân hoạch tương đương và giá trị biên

## 1. Phạm vi

Phần này chỉ phân tích 3 biến đầu vào cần dùng cho ý 1:

- `age`: số nguyên từ 18 đến 65.
- `income`: số thực từ 5.0 đến 500.0 triệu VNĐ, làm tròn 1 chữ số thập phân.
- `credit_score`: số nguyên từ 300 đến 850.

Biến `employment` chưa xét ở ý này vì yêu cầu hiện tại chỉ cần làm ý 1 cho 3 biến trên.

## 2. Phân hoạch tương đương

### 2.1 `age`

| Lớp dữ liệu | Mô tả | Giá trị đại diện | Kết quả mong đợi |
| --- | --- | --- | --- |
| A1 | Hợp lệ | 18 đến 65 | `18`, `30`, `65` | Hợp lệ |
| A2 | Không hợp lệ | Nhỏ hơn 18 | `17` | `Invalid Input` |
| A3 | Không hợp lệ | Lớn hơn 65 | `66` | `Invalid Input` |

### 2.2 `income`

| Lớp dữ liệu | Mô tả | Giá trị đại diện | Kết quả mong đợi |
| --- | --- | --- | --- |
| I1 | Hợp lệ | Từ 5.0 đến 500.0 | `5.0`, `14.9`, `15.0`, `500.0` | Hợp lệ |
| I2 | Không hợp lệ | Nhỏ hơn 5.0 | `4.9` | `Invalid Input` |
| I3 | Không hợp lệ | Lớn hơn 500.0 | `500.1` | `Invalid Input` |

### 2.3 `credit_score`

| Lớp dữ liệu | Mô tả | Giá trị đại diện | Kết quả mong đợi |
| --- | --- | --- | --- |
| C1 | Hợp lệ | Từ 300 đến 850 | `300`, `500`, `501`, `700`, `701`, `850` | Hợp lệ |
| C2 | Không hợp lệ | Nhỏ hơn 300 | `299` | `Invalid Input` |
| C3 | Không hợp lệ | Lớn hơn 850 | `851` | `Invalid Input` |

## 3. Phân tích giá trị biên

### 3.1 `age`

Giá trị biên cần kiểm thử:

- Cận dưới: `18`
- Dưới cận dưới: `17`
- Trên cận dưới: `19`
- Cận trên: `65`
- Dưới cận trên: `64`
- Trên cận trên: `66`

### 3.2 `income`

Giá trị biên cần kiểm thử:

- Cận dưới: `5.0`
- Dưới cận dưới: `4.9`
- Trên cận dưới: `5.1`
- Ngưỡng nghiệp vụ quan trọng: `15.0`
- Dưới ngưỡng: `14.9`
- Trên ngưỡng: `15.1`
- Cận trên: `500.0`
- Dưới cận trên: `499.9`
- Trên cận trên: `500.1`

### 3.3 `credit_score`

Giá trị biên cần kiểm thử:

- Cận dưới: `300`
- Dưới cận dưới: `299`
- Trên cận dưới: `301`
- Điểm chuyển mức rủi ro: `500`, `501`, `700`, `701`
- Cận trên: `850`
- Dưới cận trên: `849`
- Trên cận trên: `851`

## 4. Danh sách giá trị cần kiểm thử đề xuất

### 4.1 Bộ giá trị tối thiểu theo từng biến

| Biến | Giá trị hợp lệ cần có | Giá trị không hợp lệ cần có |
| --- | --- | --- |
| `age` | `18`, `65` | `17`, `66` |
| `income` | `5.0`, `15.0`, `500.0` | `4.9`, `500.1` |
| `credit_score` | `300`, `500`, `501`, `700`, `701`, `850` | `299`, `851` |

### 4.2 Gợi ý test case cho riêng ý 1

| TC | Dữ liệu | Mục đích | Kết quả mong đợi |
| --- | --- | --- | --- |
| TC01 | `(17, 20.0, 700)` | age dưới cận | `Invalid Input` |
| TC02 | `(66, 20.0, 700)` | age trên cận | `Invalid Input` |
| TC03 | `(18, 4.9, 700)` | income dưới cận | `Invalid Input` |
| TC04 | `(18, 500.1, 700)` | income trên cận | `Invalid Input` |
| TC05 | `(18, 20.0, 299)` | credit_score dưới cận | `Invalid Input` |
| TC06 | `(18, 20.0, 851)` | credit_score trên cận | `Invalid Input` |
| TC07 | `(18, 5.0, 300)` | giá trị biên thấp nhất hợp lệ | Hợp lệ |
| TC08 | `(65, 500.0, 850)` | giá trị biên cao nhất hợp lệ | Hợp lệ |

## 5. Kết luận

Ý 1 đã xác định được:

- Các lớp dữ liệu hợp lệ và không hợp lệ cho `age`, `income`, `credit_score`.
- Các giá trị biên cần kiểm thử để bao phủ các cận dưới, cận trên và các mốc chuyển trạng thái quan trọng.
- Bộ test tối thiểu đề xuất gồm cả trường hợp hợp lệ và không hợp lệ để phục vụ cho các ý tiếp theo.