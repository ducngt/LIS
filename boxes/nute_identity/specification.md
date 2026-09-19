# Smart Box Specification

## 1. Identity

**Box ID:** SBB-NUTE-IDENTITY-001

**Box Name:** nute_identity

**Version:** 0.1.0

**Status:** Draft

**System:** LIS - Learning Intelligence Infrastructure

**Owner:** Trường Đại học Sư phạm Kỹ thuật Nam Định

---

## 2. Capability

### Capability ID

`lis.identity.nute`

### Capability Name

NUTE Identity

### Capability Statement

Cung cấp thông tin nhận diện chính thức của
Trường Đại học Sư phạm Kỹ thuật Nam Định
để các Assembly và Component trong LIS có thể tái sử dụng thống nhất.

---

## 3. Purpose

Smart Box `nute_identity` chịu trách nhiệm cung cấp
dữ liệu nhận diện của NUTE.

Bao gồm tối thiểu:

- tên trường;
- tên viết tắt;
- tên tiếng Anh;
- định danh thương hiệu;
- logo reference;
- slogan hoặc thông điệp nhận diện khi được xác định.

---

## 4. Boundary

Box này không chịu trách nhiệm:

- render header;
- quyết định kích thước logo;
- quyết định layout;
- quản lý CSS;
- điều khiển navigation;
- tạo nội dung LIS;
- quản lý toàn bộ branding của website.

Các trách nhiệm trình bày thuộc Component.

---

## 5. Inputs

Phiên bản 0.1.0 không yêu cầu input bắt buộc.

Future optional inputs:

- language;
- display_context;
- theme;
- accessibility_preferences.

---

## 6. Outputs

Box phải có khả năng cung cấp:

- institution_name;
- institution_short_name;
- institution_english_name;
- institution_code;
- logo_path;
- identity_label.

---

## 7. Default Semantic Content

### Institution Name

Trường Đại học Sư phạm Kỹ thuật Nam Định

### Institution Short Name

NUTE

### Institution English Name

Nam Dinh University of Technology Education

### Institution Code

NUTE

### Identity Label

Trường Đại học Sư phạm Kỹ thuật Nam Định

---

## 8. Contract

Smart Box phải:

1. Có danh tính độc lập.
2. Cung cấp capability `lis.identity.nute`.
3. Trả dữ liệu theo interface chuẩn.
4. Không phụ thuộc HTML.
5. Không phụ thuộc CSS.
6. Không phụ thuộc frontend framework.
7. Không quyết định layout.
8. Có thể được tái sử dụng bởi nhiều Assembly.
9. Cho phép thay implementation mà không phá capability contract.

---

## 9. Dependencies

### Required Capabilities

`None`

### Future Optional Capabilities

- `lis.asset.logo`
- `lis.localization`
- `lis.branding`

---

## 10. Consumers

Capability này có thể được sử dụng bởi:

- `home_assembly`
- header component
- footer component
- about component
- authentication component
- future LIS applications

---

## 11. Non-Functional Requirements

Box phải:

- nhất quán;
- có thể kiểm thử độc lập;
- có thể version;
- không phụ thuộc giao diện;
- có thể được AI đọc và hiểu;
- có thể tái sử dụng xuyên suốt hệ thống LIS.

---

## 12. Evolution

### Version 0.1.0

Cung cấp identity dữ liệu cơ bản của NUTE.

### Future

Có thể mở rộng:

- logo variants;
- bilingual identity;
- brand guidelines;
- institutional metadata;
- organization units;
- digital identity references.

---

## 13. SBBS Role

`nute_identity` là một Smart Box độc lập.

Nó biểu diễn capability:

> Cung cấp nhận diện chuẩn của NUTE cho toàn bộ hệ sinh thái LIS.

Presentation không thuộc trách nhiệm của Box.