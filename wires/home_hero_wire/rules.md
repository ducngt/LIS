# Smart Wire Rules

## 1. Identity

**Wire ID:** SW-LIS-HOME-HERO-001  
**Wire Name:** home_hero_wire  
**Version:** 0.1.0

---

## 2. Connection Rule

### R-WIRE-001

Wire chỉ kết nối từ capability:

`lis.home.hero`

đến:

- `home_assembly`
- `home component`

### R-WIRE-002

Wire không phụ thuộc vào implementation nội bộ của
`lis_home_hero`.

Wire phụ thuộc vào contract của capability.

---

## 3. Contract Validation Rules

### R-WIRE-010

Mọi output nhận từ `lis.home.hero` phải được kiểm tra trước
khi chuyển tiếp.

### R-WIRE-011

Các trường bắt buộc gồm:

- institution_name
- institution_short_name
- lis_name
- lis_full_name
- slogan
- hero_statement
- primary_action_label
- primary_action_target

### R-WIRE-012

Nếu thiếu bất kỳ trường bắt buộc nào, output không hợp lệ.

### R-WIRE-013

Nếu kiểu dữ liệu không phù hợp với interface của Box,
output không hợp lệ.

### R-WIRE-014

Output không hợp lệ không được chuyển âm thầm sang Component.

---

## 4. Semantic Integrity Rules

### R-WIRE-020

Wire không được thay đổi ý nghĩa của output từ Box.

### R-WIRE-021

Wire không được tự viết lại:

- slogan;
- hero_statement;
- institution identity;
- LIS identity.

### R-WIRE-022

Wire không được tạo tri thức LIS mới.

### R-WIRE-023

Nếu cần thay đổi nội dung ngữ nghĩa, thay đổi phải được xử lý
ở Smart Box hoặc một capability thích hợp khác.

---

## 5. Transformation Rules

### R-WIRE-030

Wire được phép thực hiện transformation kỹ thuật không làm
thay đổi ngữ nghĩa.

Ví dụ:

- type validation;
- string normalization;
- schema normalization;
- safe field mapping.

### R-WIRE-031

Transformation phải có tính xác định và có thể kiểm tra.

### R-WIRE-032

Không được sử dụng transformation để phá vỡ contract nguồn.

---

## 6. Context Rules

### R-WIRE-040

Wire có thể truyền context từ Assembly đến Box.

Context có thể bao gồm:

- language;
- user_context;
- learner_context;
- accessibility_preferences.

### R-WIRE-041

Wire không được tự suy diễn user context nếu context chưa
được cung cấp bởi nguồn hợp lệ.

---

## 7. Routing Rules

### R-WIRE-050

Wire chịu trách nhiệm kết nối capability, không chịu trách nhiệm
quyết định kiến trúc toàn bộ HOME.

### R-WIRE-051

Assembly quyết định Wire nào tham gia vào một ứng dụng hoặc trang.

### R-WIRE-052

Component không được truy cập implementation nội bộ của Box
để bỏ qua Wire khi Assembly quy định dữ liệu phải đi qua Wire.

---

## 8. Error Rules

### R-WIRE-060

Khi validation thất bại, Wire phải trả lỗi có kiểm soát.

### R-WIRE-061

Mã lỗi mặc định:

`INVALID_CAPABILITY_OUTPUT`

### R-WIRE-062

Lỗi phải có khả năng được Assembly nhận biết.

### R-WIRE-063

Wire không được tự tạo dữ liệu giả để che giấu lỗi của Box.

---

## 9. Observability Rules

### R-WIRE-070

Wire nên cho phép ghi nhận:

- source capability;
- validation result;
- execution status;
- error code.

### R-WIRE-071

Observability không được làm thay đổi payload ngữ nghĩa.

---

## 10. Security Boundary

### R-WIRE-080

Wire không được thực thi nội dung không tin cậy như mã lệnh.

### R-WIRE-081

Input bên ngoài phải được coi là dữ liệu cho đến khi được
một capability chuyên trách xác thực hoặc xử lý.

---

## 11. Separation of Responsibility

Smart Wire:

`connects + validates + safely transforms + reports`

Smart Wire không:

`creates knowledge + renders UI + assembles the application`

Luồng trách nhiệm:

`Smart Box -> Smart Wire -> Assembly -> Component`