# Bài giải

## B1. Phân hoạch tương đương và Giá trị biên (EP & BVA) cho đầu vào

Ta xét riêng từng biến đầu vào theo miền giá trị đã cho.

### 1. Biến `age`

| Phân hoạch | Loại | Miền giá trị | Biên | Giá trị giữa |
| --- | --- | --- | --- | --- |
| age < 18 | Không hợp lệ | Nhỏ hơn 18 | 17 | 10 |
| 18 <= age <= 65 | Hợp lệ | Từ 18 đến 65 | 18, 65 | 30 |
| age > 65 | Không hợp lệ | Lớn hơn 65 | 66 | 80 |

### 2. Biến `income`

| Phân hoạch | Loại | Miền giá trị | Biên | Giá trị giữa |
| --- | --- | --- | --- | --- |
| income < 5.0 | Không hợp lệ | Nhỏ hơn 5.0 | 4.9 | 1.0 |
| 5.0 <= income <= 500.0 | Hợp lệ | Từ 5.0 đến 500.0 | 5.0, 500.0 | 20.0 |
| income > 500.0 | Không hợp lệ | Lớn hơn 500.0 | 500.1 | 700.0 |

### 3. Biến `credit_score`

| Phân hoạch | Loại | Miền giá trị | Biên | Giá trị giữa |
| --- | --- | --- | --- | --- |
| credit_score < 300 | Không hợp lệ | Nhỏ hơn 300 | 299 | 200 |
| 300 <= credit_score <= 850 | Hợp lệ | Từ 300 đến 850 | 300, 850 | 600 |
| credit_score > 850 | Không hợp lệ | Lớn hơn 850 | 851 | 900 |

| Điểm chuyển mức rủi ro | Giá trị |
| --- | --- |
| Low / Medium | 500, 501 |
| Medium / High | 700, 701 |

## B2. Lập và rút gọn Bảng quyết định (Decision Table)

### 1. Các điều kiện quyết định

| Mã điều kiện | Nội dung |
| --- | --- |
| C1 | Risk = High? |
| C2 | Income < 15.0? |
| C3 | Employment = Contract (C)? |
| C4 | Risk = Low? |
| C5 | Risk = Medium? |

### 2. Quy tắc rút gọn

| Quy tắc | High Risk | Income < 15.0 | Employment = C | Low Risk | Medium Risk | Hành động |
| --- | --- | --- | --- | --- | --- | --- |
| Rule 1 | T | Any (-) | Any (-) | Any (-) | Any (-) | REJECT |
| Rule 2 | F | T | T | T | F | MANUAL REVIEW |
| Rule 3 | F | T | F | T | F | REJECT |
| Rule 4 | F | T | T | F | T | REJECT |
| Rule 5 | F | F | T | T | F | APPROVE |
| Rule 6 | F | F | F | T | T | MANUAL REVIEW |

### 3. Diễn giải ngắn

| Trường hợp | Kết quả |
| --- | --- |
| High Risk | Luôn REJECT, bất kể income hay employment |
| Income >= 15.0, Contract | APPROVE |
| Income >= 15.0, Freelance | MANUAL REVIEW |
| Income < 15.0, Low Risk, Contract | MANUAL REVIEW |
| Các trường hợp còn lại | REJECT |

## B3. Thiết kế các ca kiểm thử (Test Cases)

Lồng ghép các giá trị biên từ Bước 1 vào các kịch bản của Bước 2 để tạo ra bộ kiểm thử hoàn chỉnh.

### Nhóm 1: Kiểm tra ngoại lệ (Invalid Inputs - Dựa trên biên)

| TC ID | age | income | credit_score | employment | Expected Output | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| TC_01 | 17 | 20.0 | 700 | C | Invalid Input | BVA (age < 18) |
| TC_02 | 66 | 20.0 | 700 | C | Invalid Input | BVA (age > 65) |
| TC_03 | 18 | 4.9 | 700 | C | Invalid Input | BVA (income < 5.0) |
| TC_04 | 18 | 500.1 | 700 | C | Invalid Input | BVA (income > 500.0) |
| TC_05 | 18 | 20.0 | 299 | C | Invalid Input | BVA (credit_score < 300) |
| TC_06 | 18 | 20.0 | 851 | C | Invalid Input | BVA (credit_score > 850) |
| TC_07 | 18 | 20.0 | 700 | X | Invalid Input | employment không hợp lệ |

### Nhóm 2: Kiểm tra logic nghiệp vụ

| TC ID | Áp dụng | age | income | credit_score | employment | Expected Output | Giải thích |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC_08 | Rule 1 | 18 | 20.0 | 500 | C | REJECT | High Risk luôn bị từ chối |
| TC_09 | Rule 2 | 30 | 14.9 | 701 | C | MANUAL REVIEW | Low Risk + income < 15 + Contract |
| TC_10 | Rule 3 | 30 | 14.9 | 701 | F | REJECT | Low Risk + income < 15 + Freelance |
| TC_11 | Rule 4 | 30 | 14.9 | 501 | C | REJECT | Medium Risk + income < 15 |
| TC_12 | Rule 5 | 65 | 15.0 | 701 | C | APPROVE | Low Risk + Contract |
| TC_13 | Rule 6 | 65 | 15.0 | 701 | F | MANUAL REVIEW | Low Risk + Freelance |
| TC_14 | Rule 5 | 30 | 20.0 | 700 | C | APPROVE | Medium Risk + Contract |
| TC_15 | Rule 6 | 30 | 20.0 | 700 | F | MANUAL REVIEW | Medium Risk + Freelance |
