import os
import shutil

summary_dir = os.path.join("data", "notebook_exports", "cnxhkh")
docs_topics_dir = os.path.join("docs", "data", "cnxhkh", "topics")
os.makedirs(summary_dir, exist_ok=True)
os.makedirs(docs_topics_dir, exist_ok=True)

summaries = {
    "su_ra_doi_va_phat_trien_cnxhkh_summary.md": """# Chuyên Đề: Sự Ra Đời và Các Giai Đoạn Phát Triển của Chủ Nghĩa Xã Hội Khoa Học

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 1 (Trang 11 - 50).

## 1. Hoàn Cảnh Lịch Sử Ra Đời
- **Kinh tế - xã hội (thập niên 40 của thế kỷ XIX):** Cách mạng công nghiệp thúc đẩy lực lượng sản xuất xã hội hóa cao độ mâu thuẫn với quan hệ sản xuất tư nhân TBCN. Giai cấp công nhân trưởng thành, phát động các phong trào đấu tranh chính trị độc lập (Lyon - Pháp, Hiến chương - Anh, Xilêzi - Đức).
- **Khoa học tự nhiên:** 3 phát minh trụ cột khẳng định phép biện chứng duy vật: Định luật bảo toàn & chuyển hóa năng lượng, Thuyết tế bào, Thuyết tiến hóa của Đác-uyn.
- **Tiền đề lý luận:** Triết học cổ điển Đức (Hêghen, Phoiơbắc), Kinh tế chính trị cổ điển Anh (Smith, Ricardo), Chủ nghĩa xã hội không tưởng - phê phán Pháp & Anh (Xanh Ximông, Phuriê, Ôoen).

## 2. Ba Phát Kiến Vĩ Đại của C.Mác và Ph.Ăngghen
1. **Chủ nghĩa duy vật lịch sử:** Phát hiện quy luật phát triển tự nhiên của xã hội thông qua sự thay thế của các hình thái kinh tế - xã hội.
2. **Học thuyết giá trị thặng dư:** Chỉ rõ bản chất của phương thức sản xuất TBCN và nguồn gốc bóc lột công nhân làm thuê.
3. **Sứ mệnh lịch sử của giai cấp công nhân:** Luận chứng vai trò tiên phong của GCCN trong việc lật đổ CNTB và xây dựng xã hội mới.

*Tác phẩm mốc:* **Tuyên ngôn của Đảng Cộng sản (tháng 2/1848)** đánh dấu sự ra đời của CNXHKH.

## 3. Các Giai Đoạn Phát Triển
- **C.Mác và Ph.Ăngghen:** Tổng kết bài học cách mạng 1848-1851, đúc kết kinh nghiệm Công xã Pari (1871), phân kỳ hai giai đoạn của hình thái kinh tế - xã hội CSCN.
- **V.I.Lênin:** Phát triển lý luận cách mạng vô sản trong thời kỳ đế quốc chủ nghĩa, lãnh đạo Cách mạng Tháng Mười Nga (1917), đề xuất Chính sách kinh tế mới (NEP - 1921), thành lập Quốc tế III.
- **Thời kỳ đổi mới:** Đảng Cộng sản Việt Nam khởi xướng Đổi mới (1986), xây dựng CNXH bỏ qua chế độ TBCN, phát triển kinh tế thị trường định hướng XHCN.
""",

    "su_menh_lich_su_giai_cap_cong_nhan_summary.md": """# Chuyên Đề: Sứ Mệnh Lịch Sử của Giai Cấp Công Nhân và GCCN Việt Nam

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 2 (Trang 51 - 85).

## 1. Bản Chất và Hai Phương Diện Xác Định Giai Cấp Công Nhân
- **Phương diện kinh tế - kỹ thuật:** Người lao động trực tiếp hoặc gián tiếp vận hành công cụ sản xuất công nghiệp hiện đại, có tính xã hội hóa cao.
- **Phương diện kinh tế - xã hội:** Người lao động không có tư liệu sản xuất chủ yếu, bán sức lao động và bị bóc lột giá trị thặng dư dưới CNTB.

## 2. Nội Dung Sứ Mệnh Lịch Sử Tổng Quát
GCCN lãnh đạo toàn thể nhân dân lao động xóa bỏ chế độ bóc lột TBCN, giải phóng giai cấp và nhân loại, xây dựng thành công CNXH và CNCS:
- **Kinh tế:** Xác lập chế độ công hữu về các TLSX chủ yếu, giải phóng và phát triển LLSX.
- **Chính trị - xã hội:** Lật đổ nhà nước tư sản, thiết lập nền chuyên chính vô sản / nhà nước XHCN.
- **Văn hóa - tư tưởng:** Xây dựng hệ tư tưởng Mác - Lênin, nền văn hóa mới và con người mới XHCN.

## 3. Điều Kiện Thực Hiện Sứ Mệnh
- **Khách quan:** Do địa vị kinh tế (đại diện LLSX tiên tiến) và địa vị chính trị - xã hội (triệt để cách mạng, có kỷ luật cao).
- **Chủ quan:** Sự phát triển về số lượng & chất lượng của GCCN, sự lãnh đạo của Đảng Cộng sản, và khối liên minh công - nông.

## 4. Giai Cấp Công Nhân Việt Nam
- Ra đời trước tư sản dân tộc, mang bản chất yêu nước nồng nàn, gắn bó máu thịt với nông dân.
- Sớm có Đảng Cộng sản Việt Nam lãnh đạo (1930).
- Hiện nay: Giữ vai trò lãnh đạo cách mạng, đi đầu trong CNH - HĐH gắn với kinh tế tri thức và hội nhập quốc tế.
""",

    "chu_nghia_xa_hoi_va_thoi_ky_qua_do_summary.md": """# Chuyên Đề: Chủ Nghĩa Xã Hội và Thời Kỳ Quá Độ Lên CNXH ở Việt Nam

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 3 (Trang 86 - 124).

## 1. Các Giai Đoạn của Hình Thái Kinh Tế - Xã Hội CSCN
- **Thời kỳ quá độ:** Giai đoạn cải biến cách mạng sâu sắc trên mọi lĩnh vực từ xã hội cũ sang xã hội mới.
- **Giai đoạn thấp (Chủ nghĩa xã hội):** Vừa thoát thai từ CNTB, còn nhiều tàn dư cũ. Nguyên tắc phân phối: "Làm theo năng lực, hưởng theo lao động".
- **Giai đoạn cao (Chủ nghĩa cộng sản):** LLSX cực kỳ phát triển, không còn giai cấp, nhà nước tự tiêu vong. Nguyên tắc phân phối: "Làm theo năng lực, hưởng theo nhu cầu".

## 2. Đặc Trưng Cốt Lõi của Thời Kỳ Quá Độ
- Tồn tại đan xen và đấu tranh gay gắt giữa những nhân tố của CNXH và những tàn dư của CNTB/phong kiến.
- Kinh tế: Nhiều thành phần kinh tế, nhiều hình thức sở hữu.
- Chính trị: Nhà nước chuyên chính vô sản củng cố quyền làm chủ của nhân dân.

## 3. Con Đường Quá Độ Bỏ Qua Chế Độ TBCN ở Việt Nam
- **Thực chất:** Bỏ qua việc xác lập vị trí thống trị của QHSX và kiến trúc thượng tầng TBCN.
- **Kế thừa:** Tiếp thu có chọn lọc các thành tựu khoa học, công nghệ, quản lý kinh tế của nhân loại dưới CNTB.
- **8 Đặc trưng của CNXH ở Việt Nam (Cương lĩnh 2011):** Dân giàu, nước mạnh, dân chủ, công bằng, văn minh; Do nhân dân làm chủ; Kinh tế phát triển cao dựa trên LLSX hiện đại và QHSX tiến bộ phù hợp; Nền văn hóa tiên tiến, đậm đà bản sắc dân tộc; Con người có cuộc sống ấm no, hạnh phúc; Các dân tộc bình đẳng, đoàn kết; Nhà nước pháp quyền XHCN do Đảng lãnh đạo; Quan hệ hữu nghị, hợp tác quốc tế.
""",

    "dan_chu_va_nha_nuoc_phap_quyen_xhcn_summary.md": """# Chuyên Đề: Nền Dân Chủ XHCN và Nhà Nước Pháp Quyền XHCN Việt Nam

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 4 (Trang 125 - 164).

## 1. Bản Chất Nền Dân Chủ Xã Hội Chủ Nghĩa
- Dân chủ là quyền lực thuộc về nhân dân ("Dân là gốc").
- **Chính trị:** Nền dân chủ rộng rãi nhất cho nhân dân lao động dưới sự lãnh đạo của Đảng Cộng sản.
- **Kinh tế:** Dựa trên chế độ công hữu về các TLSX chủ yếu, bảo đảm quyền làm chủ của người lao động.
- **Tư tưởng:** Lấy chủ nghĩa Mác - Lênin làm nền tảng, giải phóng tiềm năng sáng tạo của con người.
- **Thực hiện:** Kết hợp dân chủ trực tiếp (trưng cầu, tự quản) và dân chủ gián tiếp (Quốc hội, HĐND).

## 2. Bản Chất và Chức Năng Nhà Nước XHCN
- Là nhà nước "nửa nhà nước", mang bản chất giai cấp công nhân.
- Hai chức năng căn bản: Chức năng trấn áp kẻ thù và chức năng tổ chức, xây dựng xã hội mới (chức năng chủ yếu, quyết định).

## 3. Đặc Trưng Nhà Nước Pháp Quyền XHCN Việt Nam
1. Nhà nước của nhân dân, do nhân dân, vì nhân dân; nền tảng là liên minh công - nông - trí thức.
2. Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp và kiểm soát giữa các cơ quan lập pháp, hành pháp, tư pháp.
3. Thượng tôn Hiến pháp và pháp luật.
4. Tôn trọng, bảo đảm và bảo vệ quyền con người, quyền công dân.
5. Đặt dưới sự lãnh đạo duy nhất của Đảng Cộng sản Việt Nam.
""",

    "co_cau_giai_cap_va_lien_minh_cong_nong_tri_summary.md": """# Chuyên Đề: Cơ Cấu Xã Hội - Giai Cấp và Liên Minh Công - Nông - Trí Thức

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 5 (Trang 165 - 194).

## 1. Vị Trí Trung Tâm của Cơ Cấu Xã Hội - Giai Cấp
- Cơ cấu xã hội - giai cấp phản ánh trực tiếp quan hệ sở hữu và phương thức sản xuất, chi phối các cơ cấu xã hội khác (dân tộc, tôn giáo, dân số, nghề nghiệp).
- Biến đổi cùng với sự biến đổi của cơ cấu kinh tế nhiều thành phần trong thời kỳ quá độ.

## 2. Khối Liên Minh Giai Cấp, Tầng Lớp
- **Tính tất yếu:** Yêu cầu khách quan của nền sản xuất lớn hiện đại gắn kết công nghiệp - nông nghiệp - dịch vụ - khoa học công nghệ; nền tảng chính trị vững chắc của Nhà nước XHCN.
- **Nội dung kinh tế (then chốt nhất):** Kết hợp hài hòa lợi ích kinh tế, hợp tác sản xuất kinh doanh, chuyển giao kỹ thuật cho nông thôn.
- **Nội dung chính trị:** Giữ vững vai trò lãnh đạo của Đảng, bảo vệ an ninh trật tự và độc lập dân tộc.
- **Nội dung văn hóa - xã hội:** Nâng cao dân trí, phát triển nguồn nhân lực, bảo đảm an sinh xã hội.

## 3. Các Lực Lượng Xã Hội Cơ Bản ở Việt Nam
- **Giai cấp công nhân:** Lãnh đạo, nòng cốt trong CNH, HĐH.
- **Giai cấp nông dân:** Lực lượng đông đảo, chiến lược trong xây dựng nông thôn mới.
- **Đội ngũ trí thức:** Lao động sáng tạo đặc biệt quan trọng trong thời đại số và kinh tế tri thức.
- **Đội ngũ doanh nhân:** Động lực phát triển kinh tế, tạo việc làm và năng lực cạnh tranh.
""",

    "van_de_dan_toc_va_ton_giao_summary.md": """# Chuyên Đề: Vấn Đề Dân Tộc, Tôn Giáo và Khối Đại Đoàn Kết Toàn Dân Tộc

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 6 (Trang 195 - 238).

## 1. Cương Lĩnh Dân Tộc của V.I.Lênin
1. **Các dân tộc hoàn toàn bình đẳng:** Không có dân tộc đặc quyền hay bị áp bức.
2. **Các dân tộc được quyền tự quyết:** Tự quyết định chế độ chính trị và con đường phát triển.
3. **Liên hiệp công nhân tất cả các dân tộc:** Cốt lõi tư tưởng đoàn kết quốc tế vô sản.

## 2. Đặc Điểm và Chính Sách Dân Tộc ở Việt Nam
- Quốc gia có 54 dân tộc anh em; cư trú xen kẽ, truyền thống đoàn kết keo sơn.
- Nguyên tắc nhất quán: **"Bình đẳng, đoàn kết, tôn trọng và giúp nhau cùng phát triển"**.
- Ưu tiên phát triển kinh tế, giáo dục, y tế, văn hóa vùng đồng bào dân tộc thiểu số.

## 3. Quan Điểm Mác - Lênin về Tôn Giáo
- **Bản chất:** Hình thái ý thức xã hội phản ánh hư ảo hiện thực khách quan.
- **Nguồn gốc:** Tự nhiên - kinh tế - xã hội (bất lực trước thiên tai, áp bức), nhận thức (giới hạn hiểu biết), tâm lý (lo sợ, tìm nơi an ủi).
- **Tính chất:** Tính lịch sử, tính quần chúng, tính chính trị.
- **Nguyên tắc:** Tôn trọng tự do tín ngưỡng và không tín ngưỡng; phân biệt mặt tư tưởng và chính trị; bài trừ mê tín dị đoan và âm mưu lợi dụng tôn giáo chống phá Tổ quốc.
""",

    "xay_dung_gia_dinh_thoi_ky_qua_do_summary.md": """# Chuyên Đề: Xây Dựng Gia Đình Tiến Bộ, Hạnh Phúc trong Thời Kỳ Quá Độ

> **Nguồn trích xuất:** Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT), Chương 7 (Trang 239 - 270).

## 1. Khái Niệm, Vị Trí và Chức Năng của Gia Đình
- Gia đình hình thành dựa trên quan hệ hôn nhân, huyết thống và nuôi dưỡng.
- **Vị trí:** Tế bào của xã hội, tổ ấm yêu thương của mỗi cá nhân, cầu nối giữa cá nhân và xã hội.
- **4 Chức năng cơ bản:**
  1. Tái sản xuất ra con người (duy trì nòi giống).
  2. Nuôi dưỡng, giáo dục nhân cách.
  3. Kinh tế và tổ chức tiêu dùng gia đình.
  4. Thỏa mãn nhu cầu tâm sinh lý, duy trì tình cảm.

## 2. Cơ Sở Xây Dựng Gia Đình XHCN
- **Kinh tế:** Chế độ công hữu TLSX giải phóng phụ nữ khỏi phụ thuộc kinh tế.
- **Chính trị - pháp lý:** Nhà nước XHCN ban hành Luật Hôn nhân & Gia đình bảo đảm bình đẳng giới.
- **Văn hóa:** Xây dựng hệ giá trị đạo đức tiến bộ, văn minh.
- **Chế độ hôn nhân tiến bộ:** Hôn nhân tự nguyện; Một vợ một chồng, bình đẳng; Hôn nhân được pháp luật bảo đảm.

## 3. Biến Đổi của Gia Đình Việt Nam Hiện Nay
- Xu hướng thu nhỏ quy mô: Chuyển mạnh sang mô hình **gia đình hạt nhân**.
- Chức năng giáo dục và tình cảm đứng trước nguy cơ lỏng lẻo do tác động của mặt trái kinh tế thị trường và lối sống số hóa.
- Phương hướng: Kế thừa truyền thống hiếu đễ, hòa thuận; tiếp thu văn minh hiện đại; xây dựng gia đình no ấm, tiến bộ, hạnh phúc.
"""
}

for fname, content in summaries.items():
    p1 = os.path.join(summary_dir, fname)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    p2 = os.path.join(docs_topics_dir, fname)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    print(f"Wrote summary: {fname}")

print("Phase 2 summaries completed!")
