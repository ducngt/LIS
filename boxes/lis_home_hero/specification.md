# Smart Box Specification

## 1. Identity

**Box ID:** SBB-LIS-HOME-HERO-001

**Box Name:** lis_home_hero

**Version:** 0.1.0

**Status:** Draft

**System:** LIS - Learning Intelligence Infrastructure

**Owner:** Trường Đại học Sư phạm Kỹ thuật Nam Định

---

## 2. Capability

### Capability ID

`lis.home.hero`

### Capability Name

LIS Home Hero

### Capability Statement

Cung cấp vùng giới thiệu chính của trang chủ LIS nhằm:

- nhận diện LIS;
- nhận diện Trường Đại học Sư phạm Kỹ thuật Nam Định;
- truyền tải slogan "Kiến tạo - Chuẩn mực";
- giới thiệu ngắn gọn triết lý LIS;
- cung cấp điểm truy cập đầu tiên vào hệ sinh thái LIS.

---

## 3. Purpose

Smart Box `lis_home_hero` chịu trách nhiệm cung cấp nội dung ngữ nghĩa cho vùng Hero của trang chủ LIS.

Box này không chịu trách nhiệm:

- quyết định bố cục giao diện cuối cùng;
- định nghĩa CSS;
- điều khiển toàn bộ trang HOME;
- quản lý điều hướng toàn hệ thống;
- thực hiện AI Reasoning;
- quản lý Knowledge Universe.

Các trách nhiệm trên thuộc về các Box, Wire, Assembly hoặc Component khác.

---

## 4. Inputs

Phiên bản 0.1 chưa yêu cầu input bắt buộc.

Các input có thể được hỗ trợ trong tương lai:

- language;
- user_context;
- learner_context;
- institution_context;
- theme;
- accessibility_preferences.

---

## 5. Outputs

Box phải có khả năng cung cấp tối thiểu các dữ liệu:

- institution_name;
- institution_short_name;
- lis_name;
- lis_full_name;
- slogan;
- hero_statement;
- primary_action_label;
- primary_action_target.

---

## 6. Default Semantic Content

### Institution

Trường Đại học Sư phạm Kỹ thuật Nam Định

### Institution Short Name

NUTE

### LIS

LIS

### LIS Full Name

Learning Intelligence Infrastructure

### Slogan

Kiến tạo - Chuẩn mực

### Hero Statement

LIS là hạ tầng trí tuệ nơi con người và AI cùng tham gia kiến tạo tri thức, phát triển năng lực và hình thành các trải nghiệm học tập, nghiên cứu và sáng tạo mới.

### Primary Action

Khám phá LIS

---

## 7. Contract

Smart Box phải:

1. Có thể hoạt động độc lập.
2. Trả về dữ liệu theo interface chuẩn của Box.
3. Không phụ thuộc trực tiếp vào giao diện HTML cụ thể.
4. Không phụ thuộc vào CSS.
5. Không hard-code việc điều hướng của toàn website.
6. Có thể được Assembly sử dụng mà không cần biết implementation bên trong.
7. Có thể thay implementation trong tương lai mà không làm thay đổi contract.
8. Tách biệt nội dung tri thức khỏi mã thực thi.

---

## 8. Dependencies

### Required Capabilities

Phiên bản `0.1.0`:

`None`

### Future Optional Capabilities

- `lis.identity.nute`
- `lis.navigation`
- `lis.localization`
- `lis.personalization`
- `lis.ai.context`

---

## 9. Consumers

Các thành phần dự kiến sử dụng capability này:

- `home_hero_wire`
- `home_assembly`
- `home component`

---

## 10. Non-Functional Requirements

Box phải đảm bảo:

- nội dung có thể tái sử dụng;
- không phụ thuộc framework giao diện;
- hỗ trợ versioning;
- có thể kiểm thử độc lập;
- có thể mở rộng đa ngôn ngữ;
- có khả năng được AI đọc và hiểu specification;
- contract ổn định giữa các phiên bản tương thích.

---

## 11. Evolution

### Version 0.1.0

Mục tiêu:

Cung cấp semantic content cơ bản cho Hero của LIS.

### Future

Có thể bổ sung:

- personalized hero;
- multilingual hero;
- AI-generated contextual statement;
- learner-aware hero;
- role-aware hero;
- dynamic LIS knowledge visualization;
- context-aware call-to-action.

---

## 12. SBBS Role

`lis_home_hero` là một Smart Box.

Nó biểu diễn một đơn vị năng lực độc lập:

> Cung cấp nội dung và ngữ nghĩa của vùng Hero LIS.

Box không tự quyết định cách nó được trình bày trên website.

Việc kết nối Box với các phần khác thuộc trách nhiệm của Smart Wire.

Việc xác định Box nào được lắp ráp thành trang HOME thuộc trách nhiệm của Assembly.

Việc biểu diễn trực quan thuộc trách nhiệm của Component.