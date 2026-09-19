# Smart Wire Specification

## 1. Identity

**Wire ID:** SW-LIS-HOME-HERO-001

**Wire Name:** home_hero_wire

**Version:** 0.1.0

**Status:** Draft

**System:** LIS - Learning Intelligence Infrastructure

---

## 2. Purpose

Smart Wire `home_hero_wire` chịu trách nhiệm kết nối capability:

`lis.home.hero`

với các thành phần lắp ráp và biểu diễn của trang HOME.

Wire không tạo ra tri thức cốt lõi của Hero.

Wire chịu trách nhiệm điều phối dữ liệu giữa:

- Smart Box;
- Assembly;
- Component.

---

## 3. Source

### Source Capability

`lis.home.hero`

### Source Box

`SBB-LIS-HOME-HERO-001`

### Source Interface

`boxes/lis_home_hero/interface.json`

---

## 4. Consumers

Wire cung cấp dữ liệu cho:

- `home_assembly`
- `home component`

---

## 5. Responsibilities

Smart Wire phải có khả năng:

1. Nhận output từ `lis.home.hero`.
2. Kiểm tra output theo contract.
3. Chuẩn hóa dữ liệu trước khi chuyển tiếp.
4. Không làm thay đổi ý nghĩa ngữ nghĩa của dữ liệu.
5. Chuyển dữ liệu đúng định dạng cho Assembly hoặc Component.
6. Báo lỗi nếu output không đáp ứng contract.
7. Cho phép thay implementation của Box mà không thay đổi Wire nếu contract vẫn tương thích.

---

## 6. Validation

Wire phải kiểm tra tối thiểu các trường:

- institution_name
- institution_short_name
- lis_name
- lis_full_name
- slogan
- hero_statement
- primary_action_label
- primary_action_target

Nếu thiếu trường bắt buộc, Wire phải xem output là không hợp lệ.

---

## 7. Transformation

Phiên bản `0.1.0` không thực hiện biến đổi ngữ nghĩa.

Wire chỉ có thể thực hiện các biến đổi kỹ thuật an toàn như:

- chuẩn hóa chuỗi;
- kiểm tra kiểu dữ liệu;
- loại bỏ giá trị null không hợp lệ;
- chuẩn hóa cấu trúc output.

Wire không được:

- thay slogan;
- viết lại hero_statement;
- tạo thêm thông điệp mới;
- thay đổi capability contract.

---

## 8. Context

Wire có thể truyền context giữa Assembly và Box trong tương lai.

Ví dụ:

- language;
- user_context;
- theme;
- learner_context;
- accessibility_preferences.

Phiên bản `0.1.0` chưa yêu cầu context bắt buộc.

---

## 9. Observability

Wire nên hỗ trợ trong các phiên bản sau:

- logging;
- validation status;
- error reporting;
- execution tracing;
- latency measurement.

---

## 10. Error Handling

Nếu Box trả về output không hợp lệ:

Wire không được âm thầm tiếp tục.

Wire phải trả về lỗi có kiểm soát cho Assembly.

Ví dụ trạng thái:

`INVALID_CAPABILITY_OUTPUT`

---

## 11. Boundary

Smart Wire không chịu trách nhiệm:

- định nghĩa Knowledge của LIS;
- tạo Hero content;
- định nghĩa CSS;
- quyết định layout;
- lắp ráp toàn bộ trang HOME;
- thực hiện global routing.

---

## 12. SBBS Role

`home_hero_wire` là Smart Wire.

Vai trò của nó là:

> Kết nối và bảo vệ contract giữa capability `lis.home.hero` và các lớp lắp ráp/biểu diễn phía ngoài.

Luồng cơ bản:

`lis_home_hero -> home_hero_wire -> home_assembly -> home component`