# Smart Box Rules

## 1. Identity

**Box ID:** SBB-NUTE-IDENTITY-001  
**Capability:** `lis.identity.nute`  
**Version:** 0.1.0

---

## 2. Purpose of Rules

Các quy tắc trong file này điều khiển cách Smart Box
`nute_identity` sử dụng Knowledge để tạo output nhận diện NUTE.

Rules không định nghĩa HTML, CSS hoặc layout.

---

## 3. Institution Identity Rules

### R-NUTE-001

Tên trường mặc định phải là:

`Trường Đại học Sư phạm Kỹ thuật Nam Định`

### R-NUTE-002

Tên viết tắt mặc định phải là:

`NUTE`

### R-NUTE-003

Tên tiếng Anh mặc định phải là:

`Nam Dinh University of Technology Education`

### R-NUTE-004

Institution code mặc định phải là:

`NUTE`

---

## 4. Consistency Rules

### R-NUTE-010

Các thông tin nhận diện phải nhất quán giữa mọi nơi sử dụng capability này.

### R-NUTE-011

Không được tự ý thay đổi tên trường.

### R-NUTE-012

Không được tự ý thay đổi tên viết tắt.

### R-NUTE-013

Không được tự ý tạo tên tiếng Anh mới.

### R-NUTE-014

Nếu identity thay đổi chính thức, Box phải được version lại.

---

## 5. Logo Rules

### R-NUTE-020

Smart Box chỉ cung cấp tham chiếu đến logo.

### R-NUTE-021

Box không quyết định cách hiển thị logo.

### R-NUTE-022

Box không được nhúng CSS vào logo definition.

### R-NUTE-023

Logo path phải trỏ tới tài sản hợp lệ trong hệ thống.

---

## 6. Presentation Separation Rules

### R-NUTE-030

Smart Box không định nghĩa:

- font;
- màu;
- kích thước;
- vị trí;
- layout;
- animation;
- responsive behavior.

### R-NUTE-031

Presentation thuộc trách nhiệm của Component.

### R-NUTE-032

Việc kết nối Box với HOME hoặc các capability khác thuộc trách nhiệm của Smart Wire.

### R-NUTE-033

Việc xác định nơi nào sử dụng capability này thuộc trách nhiệm của Assembly.

---

## 7. Knowledge Rules

### R-NUTE-040

Output phải phù hợp với `knowledge.md`.

### R-NUTE-041

Không được tạo thêm thông tin tổ chức nếu Knowledge hiện tại không xác nhận.

### R-NUTE-042

Không được biến suy đoán thành dữ liệu nhận diện chính thức.

---

## 8. Reuse Rules

### R-NUTE-050

Capability `lis.identity.nute` phải có thể tái sử dụng bởi nhiều Assembly.

### R-NUTE-051

Implementation có thể thay đổi nhưng contract phải được duy trì giữa các phiên bản tương thích.

### R-NUTE-052

Một Component không được phụ thuộc trực tiếp vào implementation nội bộ của Box nếu Assembly quy định dữ liệu phải đi qua Wire.

---

## 9. Language Rules

### R-NUTE-060

Ngôn ngữ mặc định là:

`vi`

### R-NUTE-061

Nếu yêu cầu ngôn ngữ tiếng Anh, sử dụng tên tiếng Anh trong Knowledge.

### R-NUTE-062

Không tự tạo bản dịch mới nếu không có nguồn Knowledge tương ứng.

---

## 10. Output Principle

Smart Box phải vận hành theo nguyên tắc:

`Specification + Knowledge + Rules -> Identity Capability Output`

Prompt có thể hỗ trợ AI trong tương lai nhưng không được thay thế
Specification, Knowledge hoặc Rules.New-Item boxes\nute_identity\prompt.md -ItemType File