# Smart Wire Rules

## 1. Identity

**Wire ID:** SW-NUTE-IDENTITY-001  
**Wire Name:** nute_identity_wire  
**Version:** 0.1.0

---

## 2. Connection Rules

### R-NUTE-WIRE-001

Wire chỉ nhận dữ liệu từ capability:

`lis.identity.nute`

### R-NUTE-WIRE-002

Wire có thể chuyển dữ liệu đến:

- `home_assembly`
- header component
- footer component
- about component

### R-NUTE-WIRE-003

Wire phụ thuộc vào capability contract,
không phụ thuộc vào implementation nội bộ của Box.

---

## 3. Contract Validation Rules

### R-NUTE-WIRE-010

Mọi output từ `lis.identity.nute` phải được kiểm tra trước khi chuyển tiếp.

### R-NUTE-WIRE-011

Các trường bắt buộc:

- institution_name
- institution_short_name
- institution_english_name
- institution_code
- logo_path
- identity_label

### R-NUTE-WIRE-012

Nếu thiếu bất kỳ trường bắt buộc nào,
output phải được coi là không hợp lệ.

### R-NUTE-WIRE-013

Nếu kiểu dữ liệu không đúng với interface,
output phải được coi là không hợp lệ.

### R-NUTE-WIRE-014

Output không hợp lệ không được truyền âm thầm sang Assembly hoặc Component.

---

## 4. Identity Integrity Rules

### R-NUTE-WIRE-020

Wire không được thay đổi identity của NUTE.

### R-NUTE-WIRE-021

Wire không được tự thay đổi:

- institution_name;
- institution_short_name;
- institution_english_name;
- institution_code;
- logo_path;
- identity_label.

### R-NUTE-WIRE-022

Nếu cần thay đổi identity,
thay đổi phải diễn ra tại Smart Box hoặc Knowledge nguồn.

---

## 5. Transformation Rules

### R-NUTE-WIRE-030

Wire chỉ được phép thực hiện transformation kỹ thuật.

Ví dụ:

- type validation;
- string normalization;
- schema normalization;
- safe field mapping.

### R-NUTE-WIRE-031

Transformation không được làm thay đổi ý nghĩa nhận diện.

### R-NUTE-WIRE-032

Transformation phải có thể kiểm tra và truy vết.

---

## 6. Context Rules

### R-NUTE-WIRE-040

Wire có thể truyền context từ Assembly đến Box.

Context có thể gồm:

- language;
- display_context;
- theme;
- accessibility_preferences.

### R-NUTE-WIRE-041

Wire không được tự tạo context nhận diện nếu không có nguồn hợp lệ.

---

## 7. Routing Rules

### R-NUTE-WIRE-050

Wire chỉ chịu trách nhiệm kết nối capability.

### R-NUTE-WIRE-051

Assembly quyết định Wire này có tham gia vào HOME hay không.

### R-NUTE-WIRE-052

Component không được truy cập trực tiếp implementation nội bộ của Box
nếu Assembly quy định dữ liệu phải đi qua Wire.

---

## 8. Error Rules

### R-NUTE-WIRE-060

Nếu validation thất bại, Wire phải trả lỗi có kiểm soát.

### R-NUTE-WIRE-061

Mã lỗi mặc định:

`INVALID_IDENTITY_OUTPUT`

### R-NUTE-WIRE-062

Wire không được tạo dữ liệu identity giả để che lỗi.

### R-NUTE-WIRE-063

Assembly phải có khả năng nhận biết lỗi từ Wire.

---

## 9. Observability Rules

### R-NUTE-WIRE-070

Wire nên cho phép ghi nhận:

- source capability;
- validation result;
- execution status;
- error code.

### R-NUTE-WIRE-071

Observability không được làm thay đổi payload identity.

---

## 10. Security Rules

### R-NUTE-WIRE-080

`logo_path` phải được coi là dữ liệu tham chiếu.

### R-NUTE-WIRE-081

Wire không được thực thi nội dung từ `logo_path`.

### R-NUTE-WIRE-082

Input ngoài hệ thống phải được xem là dữ liệu cho đến khi được xác thực.

---

## 11. Separation of Responsibility

Smart Wire:

`connects + validates + safely transforms + reports`

Smart Wire không:

`creates identity + renders UI + assembles the application`

Luồng trách nhiệm:

`nute_identity -> nute_identity_wire -> Assembly -> Component`