# Smart Wire Specification

## 1. Identity

**Wire ID:** SW-NUTE-IDENTITY-001

**Wire Name:** nute_identity_wire

**Version:** 0.1.0

**Status:** Draft

**System:** LIS - Learning Intelligence Infrastructure

---

## 2. Purpose

Smart Wire `nute_identity_wire` chịu trách nhiệm kết nối capability:

`lis.identity.nute`

với các Assembly và Component cần sử dụng nhận diện NUTE.

Wire không tạo hoặc thay đổi identity của NUTE.

---

## 3. Source

### Source Capability

`lis.identity.nute`

### Source Box

`SBB-NUTE-IDENTITY-001`

### Source Interface

`boxes/nute_identity/interface.json`

---

## 4. Consumers

Wire có thể cung cấp dữ liệu cho:

- `home_assembly`
- header component
- footer component
- about component

---

## 5. Responsibilities

Smart Wire phải:

1. Nhận output từ `lis.identity.nute`.
2. Kiểm tra output theo contract.
3. Xác nhận các trường identity bắt buộc.
4. Không thay đổi thông tin nhận diện.
5. Chuyển dữ liệu đúng định dạng cho Assembly hoặc Component.
6. Báo lỗi nếu output không đáp ứng contract.
7. Cho phép thay implementation của Box mà không phá Wire nếu contract vẫn tương thích.

---

## 6. Validation

Wire phải kiểm tra tối thiểu:

- institution_name
- institution_short_name
- institution_english_name
- institution_code
- logo_path
- identity_label

Nếu thiếu trường bắt buộc, output phải được xem là không hợp lệ.

---

## 7. Transformation

Phiên bản `0.1.0` không thực hiện biến đổi ngữ nghĩa.

Wire chỉ được phép thực hiện các biến đổi kỹ thuật an toàn như:

- kiểm tra kiểu dữ liệu;
- chuẩn hóa chuỗi;
- chuẩn hóa schema;
- field mapping an toàn.

Wire không được:

- đổi tên trường;
- đổi tên viết tắt;
- đổi tên tiếng Anh;
- thay logo reference;
- tạo identity mới.

---

## 8. Context

Wire có thể truyền context trong tương lai, ví dụ:

- language;
- display_context;
- theme;
- accessibility_preferences.

Phiên bản `0.1.0` chưa yêu cầu context bắt buộc.

---

## 9. Observability

Wire nên hỗ trợ trong các phiên bản sau:

- logging;
- validation status;
- execution tracing;
- error reporting.

---

## 10. Error Handling

Nếu output không hợp lệ:

Wire không được âm thầm tiếp tục.

Wire phải trả lỗi có kiểm soát.

Mã lỗi mặc định:

`INVALID_IDENTITY_OUTPUT`

---

## 11. Boundary

Smart Wire không chịu trách nhiệm:

- tạo identity;
- render logo;
- định nghĩa CSS;
- quyết định vị trí logo;
- quyết định layout;
- lắp ráp toàn bộ HOME.

---

## 12. SBBS Role

`nute_identity_wire` là Smart Wire.

Vai trò:

> Kết nối và bảo vệ contract giữa capability `lis.identity.nute`
> và các lớp Assembly / Component phía ngoài.

Luồng:

`nute_identity -> nute_identity_wire -> home_assembly -> home component`