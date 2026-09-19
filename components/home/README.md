# Home Component

## 1. Identity

**Component Name:** home

**Version:** 0.1.0

**System:** LIS - Learning Intelligence Infrastructure

---

## 2. Role

`home` là Presentation Component của trang HOME.

Component chịu trách nhiệm:

- nhận dữ liệu đã đi qua Smart Wire;
- biểu diễn dữ liệu thành giao diện người dùng;
- trình bày Hero của LIS;
- giữ trải nghiệm trực quan nhất quán với LIS.

Component không phải là Smart Box.

Component không chứa Knowledge cốt lõi của LIS.

---

## 3. Data Source

Component nhận dữ liệu từ:

`home_hero_wire`

thông qua:

`home_assembly`

Luồng chuẩn:

`lis_home_hero -> home_hero_wire -> home_assembly -> home`

---

## 4. Expected Data

Component kỳ vọng các trường:

- institution_name
- institution_short_name
- lis_name
- lis_full_name
- slogan
- hero_statement
- primary_action_label
- primary_action_target

---

## 5. Presentation Responsibilities

Component có thể quyết định:

- HTML structure;
- typography;
- spacing;
- visual hierarchy;
- responsive layout;
- iconography;
- imagery;
- animation;
- accessibility presentation.

---

## 6. Presentation Constraints

Component không được:

- thay đổi slogan;
- thay đổi ý nghĩa hero_statement;
- tự tạo Knowledge mới;
- bỏ qua Smart Wire;
- truy cập trực tiếp implementation bên trong Smart Box;
- thay đổi capability contract;
- chứa logic AI Reasoning cốt lõi.

---

## 7. Initial Visual Direction

Trang HOME phiên bản đầu tiên hướng tới phong cách:

- AI-Native;
- hiện đại;
- học thuật;
- công nghệ;
- tối giản;
- tin cậy;
- dễ mở rộng.

Hero cần thể hiện:

- NUTE Identity;
- LIS;
- slogan `Kiến tạo - Chuẩn mực`;
- Hero Statement;
- CTA `Khám phá LIS`.

---

## 8. Future Expansion

Component HOME có thể mở rộng để biểu diễn thêm:

- LIS Core;
- AI-Native Campus;
- Knowledge nodes;
- Capability nodes;
- Ecosystem;
- Standards & Governance.

Các nội dung này phải được cấp bởi các Smart Box tương ứng,
không nên hard-code toàn bộ vào Home Component.

---

## 9. SBBS Principle

Component biểu diễn capability.

Component không định nghĩa capability.

Nguyên tắc:

`Capability != Presentation`

và:

`Smart Box -> Smart Wire -> Assembly -> Component`