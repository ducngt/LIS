# Smart Box Rules

## 1. Box

**Box ID:** SBB-LIS-HOME-HERO-001  
**Capability:** `lis.home.hero`  
**Version:** 0.1.0

---

## 2. Purpose of Rules

Các quy tắc trong file này điều khiển cách Smart Box
`lis_home_hero` sử dụng Knowledge để tạo ra output.

Rules không định nghĩa HTML, CSS hoặc bố cục giao diện.

---

## 3. Identity Rules

### R-HERO-001

Tên hệ thống phải được biểu diễn là:

`LIS`

### R-HERO-002

Tên đầy đủ của LIS phải là:

`Learning Intelligence Infrastructure`

### R-HERO-003

Tổ chức chủ quản phải được nhận diện là:

`Trường Đại học Sư phạm Kỹ thuật Nam Định`

### R-HERO-004

Tên viết tắt của trường:

`NUTE`

---

## 4. Slogan Rules

### R-HERO-010

Slogan chuẩn là:

`Kiến tạo - Chuẩn mực`

### R-HERO-011

Hai thành tố "Kiến tạo" và "Chuẩn mực" phải được giữ
trong cùng một thông điệp.

### R-HERO-012

Không tự ý thay slogan bằng một slogan do AI sinh ra.

### R-HERO-013

Ở giao diện desktop, slogan ưu tiên hiển thị trên một dòng.

---

## 5. Semantic Rules

### R-HERO-020

LIS phải được mô tả như một:

`Learning Intelligence Infrastructure`

### R-HERO-021

Không mô tả LIS đơn thuần là:

- LMS;
- chatbot;
- website;
- AI assistant;
- kho tài liệu.

### R-HERO-022

Thông điệp Hero phải thể hiện vai trò của cả:

- Human;
- AI;
- Knowledge;
- Capability.

### R-HERO-023

AI không được mô tả là chủ thể duy nhất của LIS.

### R-HERO-024

Con người phải được duy trì như một chủ thể của hệ sinh thái LIS.

---

## 6. Content Rules

### R-HERO-030

Hero phải cung cấp tối thiểu:

- LIS identity;
- institution identity;
- slogan;
- hero statement;
- primary action.

### R-HERO-031

Hero statement phải ngắn hơn nội dung của trang giới thiệu LIS.

### R-HERO-032

Hero không được chứa toàn bộ kiến trúc LIS.

Nội dung chuyên sâu phải được chuyển sang các capability hoặc
Smart Box chuyên biệt.

---

## 7. Action Rules

### R-HERO-040

Primary action mặc định:

`Khám phá LIS`

### R-HERO-041

Primary action phải dẫn người dùng từ HOME vào không gian
khám phá LIS.

### R-HERO-042

Box chỉ cung cấp ý nghĩa của action.

Việc routing cụ thể không thuộc trách nhiệm nội tại của Box.

---

## 8. Separation Rules

### R-HERO-050

Smart Box không được chứa CSS.

### R-HERO-051

Smart Box không quyết định layout cuối cùng của trang HOME.

### R-HERO-052

Smart Box không được phụ thuộc trực tiếp vào một frontend
framework cụ thể.

### R-HERO-053

Presentation thuộc trách nhiệm của Component.

### R-HERO-054

Kết nối với các capability khác thuộc trách nhiệm của Smart Wire.

### R-HERO-055

Việc lắp ráp thành HOME thuộc trách nhiệm của Assembly.

---

## 9. Knowledge Rules

### R-HERO-060

Nội dung được sinh ra phải phù hợp với `knowledge.md`.

### R-HERO-061

Không được tạo thêm tuyên bố nền tảng về LIS nếu tuyên bố đó
mâu thuẫn với Knowledge hiện có.

### R-HERO-062

Nếu Knowledge không đủ để xác định một nội dung quan trọng,
Box không được tự coi suy đoán là tri thức đã được xác lập.

---

## 10. Evolution Rules

### R-HERO-070

Các phiên bản tương thích phải duy trì capability:

`lis.home.hero`

### R-HERO-071

Có thể thay implementation mà không làm thay đổi contract
của capability.

### R-HERO-072

Các tính năng mới như personalization, multilingual hoặc
AI-generated content phải được bổ sung mà không phá vỡ
semantic contract hiện tại.

---

## 11. Output Principle

Smart Box phải vận hành theo nguyên tắc:

`Specification + Knowledge + Rules -> Capability Output`

Prompt có thể hỗ trợ AI thực thi capability nhưng không được
thay thế Specification, Knowledge hoặc Rules.