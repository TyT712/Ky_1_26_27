import os

docs_cnxhkh_dir = os.path.join("docs", "data", "cnxhkh")
os.makedirs(docs_cnxhkh_dir, exist_ok=True)

theories = {
    "chuong_1_theory.md": """# CHƯƠNG 1: NHẬP MÔN CHỦ NGHĨA XÃ HỘI KHOA HỌC

### 1. Sơ đồ Cấu trúc Logic & Nguồn gốc Lý luận
```mermaid
graph TD
    A["Cách Mạng Công Nghiệp & Phong Trào Công Nhân (Lyon, Hiến Chương, Xilêzi)"] --> E["CHỦ NGHĨA XÃ HỘI KHOA HỌC (Tháng 2/1848)"]
    B["Tiền đề KHTN: Bảo toàn năng lượng, Thuyết tế bào, Thuyết tiến hóa"] --> E
    C["Tiền đề Lý luận: Triết học Đức, KTCT Anh, CNXH không tưởng Pháp - Anh"] --> E
    D["Ba Phát Kiến Vĩ Đại của C.Mác & Ph.Ăngghen"] --> E

    subgraph BaPhatKien ["3 Phát Kiến Vĩ Đại"]
        style BaPhatKien fill:#f8fafc,stroke:#64748b,stroke-dasharray: 4 4
        F["1. Chủ nghĩa duy vật lịch sử"]
        G["2. Học thuyết giá trị thặng dư"]
        H["3. Sứ mệnh lịch sử của giai cấp công nhân"]
    end
    BaPhatKien --> D
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Chủ nghĩa xã hội khoa học (CNXHKH):** Là một trong ba bộ phận cấu thành chủ nghĩa Mác - Lênin; nghiên cứu các quy luật chính trị - xã hội của quá trình phát sinh, hình thành và phát triển của hình thái kinh tế - xã hội cộng sản chủ nghĩa; con đường, phương pháp để giai cấp công nhân hoàn thành sứ mệnh lịch sử.
- **Quan hệ giữa ba bộ phận của chủ nghĩa Mác - Lênin:**
  - *Triết học Mác - Lênin:* Thế giới quan duy vật và phương pháp luận biện chứng.
  - *Kinh tế chính trị Mác - Lênin:* Cơ sở kinh tế, vạch trần bản chất bóc lột giá trị thặng dư của chủ nghĩa tư bản.
  - *Chủ nghĩa xã hội khoa học:* Kết luận chính trị - xã hội tất yếu và trực tiếp của triết học và kinh tế chính trị Mác - Lênin.
- **Tác phẩm khai sinh:** *"Tuyên ngôn của Đảng Cộng sản"* (tháng 2/1848) do C.Mác và Ph.Ăngghen soạn thảo - văn kiện có tính chất cương lĩnh cách mạng đầu tiên của phong trào cộng sản và công nhân quốc tế.
- **Những cống hiến lịch sử của V.I.Lênin:**
  - Phát hiện quy luật phát triển không đều của CNTB thời kỳ đế quốc chủ nghĩa -> Cách mạng vô sản có thể thắng lợi trước hết ở một số nước hoặc một nước riêng lẻ.
  - Lãnh đạo thắng lợi Cách mạng Tháng Mười Nga (1917) khai sinh nhà nước Xô viết.
  - Đề xướng Chính sách kinh tế mới (NEP - 1921), đặt nền móng cho thời kỳ quá độ với nền kinh tế nhiều thành phần.
- **Ý nghĩa nghiên cứu:** Là kim chỉ nam cho công cuộc Đổi mới toàn diện, xây dựng CNXH và bảo vệ nền tảng tư tưởng của Đảng Cộng sản Việt Nam.
""",

    "chuong_2_theory.md": """# CHƯƠNG 2: SỨ MỆNH LỊCH SỬ CỦA GIAI CẤP CÔNG NHÂN

### 1. Sơ đồ Điều kiện Quy định Sứ mệnh Lịch sử
```mermaid
graph TD
    A["SỨ MỆNH LỊCH SỬ CỦA GIAI CẤP CÔNG NHÂN"]
    A --> B["Nội dung Sứ mệnh"]
    B --> B1["Kinh tế: Xác lập sở hữu công cộng TLSX"]
    B --> B2["Chính trị: Lật đổ tư sản, lập nhà nước XHCN"]
    B --> B3["Văn hóa: Xây dựng hệ tư tưởng Mác - Lênin"]

    A --> C["Điều kiện Khách quan"]
    C --> C1["Địa vị kinh tế: Đại diện LLSX tiên tiến"]
    C --> C2["Địa vị CT-XH: Bị bóc lột trực tiếp, kỷ luật cao"]

    A --> D["Nhân tố Chủ quan"]
    D --> D1["Sự lớn mạnh của bản thân GCCN"]
    D --> D2["Đảng Cộng sản: Đội tiên phong lãnh đạo"]
    D --> D3["Khối liên minh Công - Nông - Trí thức"]
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Giai cấp công nhân (GCCN):** Tập đoàn xã hội ổn định, đại biểu cho LLSX tiên tiến, phương thức sản xuất hiện đại; dưới CNTB là người làm thuê không có TLSX, bị bóc lột giá trị thặng dư.
- **Hai phương diện xác định GCCN:**
  1. *Kinh tế - kỹ thuật:* Trực tiếp hoặc gián tiếp vận hành công cụ sản xuất công nghiệp, tính xã hội hóa cao.
  2. *Kinh tế - xã hội:* Bị bóc lột giá trị thặng dư, đối kháng lợi ích trực tiếp với giai cấp tư sản.
- **Sứ mệnh lịch sử tổng quát:** Lãnh đạo quần chúng nhân dân lao động lật đổ ách thống trị TBCN, xóa bỏ áp bức bóc lột, giải phóng giai cấp và nhân loại, xây dựng thành công CNXH và CNCS.
- **Đảng Cộng sản:** Sự kết hợp giữa chủ nghĩa Mác - Lênin với phong trào công nhân. Là nhân tố chủ quan quyết định nhất để GCCN hoàn thành sứ mệnh.
- **Giai cấp công nhân Việt Nam:**
  - Ra đời trước tư sản dân tộc, chịu 3 tầng áp bức (đế quốc, phong kiến, tư sản ngoại bang).
  - Có mối liên minh tự nhiên máu thịt với giai cấp nông dân.
  - Sớm được Đảng Cộng sản Việt Nam (1930) lãnh đạo, là lực lượng tiên phong trong sự nghiệp công nghiệp hóa, hiện đại hóa đất nước.
""",

    "chuong_3_theory.md": """# CHƯƠNG 3: CHỦ NGHĨA XÃ HỘI VÀ THỜI KỲ QUÁ ĐỘ LÊN CHỦ NGHĨA XÃ HỘI

### 1. Sơ đồ Tiến trình Hình thái Kinh tế - Xã hội CSCN
```mermaid
graph LR
    A["Chủ nghĩa Tư bản"] --> B["THỜI KỲ QUÁ ĐỘ (Đan xen, đấu tranh gay gắt)"]
    B --> C["Giai đoạn thấp: CHỦ NGHĨA XÃ HỘI (Làm theo năng lực, hưởng theo lao động)"]
    C --> D["Giai đoạn cao: CHỦ NGHĨA CỘNG SẢN (Làm theo năng lực, hưởng theo nhu cầu)"]
    
    subgraph DacTrungCNXH ["Đặc trưng CNXH ở Việt Nam (Cương lĩnh 2011)"]
        E["Dân giàu, nước mạnh, dân chủ, công bằng, văn minh"]
        F["Do nhân dân làm chủ"]
        G["Kinh tế phát triển cao, QHSX phù hợp"]
        H["Nhà nước pháp quyền XHCN của dân, do dân, vì dân"]
    end
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Thời kỳ quá độ lên CNXH:** Thời kỳ cải biến cách mạng sâu sắc, toàn diện từ xã hội cũ sang xã hội mới; bắt đầu từ khi giai cấp công nhân giành chính quyền cho đến khi xây dựng xong cơ sở vật chất - kỹ thuật của CNXH.
- **Hai con đường quá độ:**
  - *Quá độ trực tiếp:* Từ các nước tư bản phát triển cao tiến thẳng lên CNXH.
  - *Quá độ gián tiếp:* Từ các nước tiền tư bản hoặc nông nghiệp lạc hậu tiến lên CNXH bỏ qua chế độ TBCN.
- **Nội hàm "Quá độ bỏ qua chế độ tư bản chủ nghĩa" ở Việt Nam:**
  - Bỏ qua việc xác lập vị trí thống trị của quan hệ sản xuất và kiến trúc thượng tầng tư bản chủ nghĩa.
  - Kế thừa và phát huy những thành tựu của nhân loại dưới CNTB, nhất là khoa học công nghệ và lực lượng sản xuất.
- **8 Đặc trưng của xã hội XHCN mà Việt Nam xây dựng:** Cương lĩnh xây dựng đất nước thời kỳ quá độ lên CNXH (bổ sung, phát triển năm 2011).
""",

    "chuong_4_theory.md": """# CHƯƠNG 4: DÂN CHỦ XÃ HỘI CHỦ NGHĨA VÀ NHÀ NƯỚC XÃ HỘI CHỦ NGHĨA

### 1. Sơ đồ Mối Quan hệ Biện chứng giữa Dân chủ & Nhà nước XHCN
```mermaid
graph TD
    A["DÂN CHỦ XÃ HỘI CHỦ NGHĨA (Quyền lực thuộc về nhân dân)"] <--> B["NHÀ NƯỚC XÃ HỘI CHỦ NGHĨA (Công cụ pháp lý & quyền lực)"]
    A -->|Là cơ sở, bản chất| B
    B -->|Là công cụ bảo vệ, hiện thực hóa| A

    subgraph HinhThucDanChu ["Hình thức Dân chủ"]
        C["Dân chủ trực tiếp (Trưng cầu, biểu quyết, tự quản)"]
        D["Dân chủ gián tiếp (Quốc hội, HĐND các cấp)"]
    end
    A --- HinhThucDanChu

    subgraph NhaNuocPhapQuyen ["Nhà nước Pháp quyền XHCN Việt Nam"]
        E["Quyền lực nhà nước thống nhất, có phân công, phối hợp, kiểm soát"]
        F["Thượng tôn Hiến pháp và Pháp luật"]
        G["Đặt dưới sự lãnh đạo của Đảng Cộng sản Việt Nam"]
    end
    B --- NhaNuocPhapQuyen
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Dân chủ:** Là giá trị nhân loại; là quyền lực thuộc về nhân dân; là một hình thái nhà nước; là nguyên tắc tổ chức quản lý (tập trung dân chủ).
- **Bản chất nền dân chủ XHCN:**
  - *Chính trị:* Do Đảng Cộng sản lãnh đạo; nhân dân lao động làm chủ bộ máy nhà nước.
  - *Kinh tế:* Xác lập chế độ sở hữu công cộng về TLSX chủ yếu; phân phối theo kết quả lao động.
  - *Tư tưởng - văn hóa:* Nền tảng tư tưởng là chủ nghĩa Mác - Lênin; giải phóng con người.
- **Nhà nước XHCN:** Là nhà nước "nửa nhà nước", mang bản chất giai cấp công nhân; có chức năng trấn áp và chức năng tổ chức, xây dựng xã hội mới (chức năng căn bản nhất).
- **Đặc trưng Nhà nước pháp quyền XHCN Việt Nam:** Của dân, do dân, vì dân; thượng tôn pháp luật; tôn trọng và bảo đảm quyền con người; quyền lực thống nhất, phân công phối hợp giữa lập pháp, hành pháp và tư pháp.
""",

    "chuong_5_theory.md": """# CHƯƠNG 5: CƠ CẤU XÃ HỘI - GIAI CẤP VÀ LIÊN MINH GIAI CẤP, TẦNG LỚP TRONG THỜI KỲ QUÁ ĐỘ

### 1. Sơ đồ Khối Liên Minh Giai Cấp, Tầng Lớp ở Việt Nam
```mermaid
graph TD
    A["ĐẢNG CỘNG SẢN VIỆT NAM (Lãnh đạo tuyệt đối)"] --> B["KHỐI LIÊN MINH VỮNG CHẮC"]
    
    subgraph CacLucLuongNongCot ["Các Lực Lượng Nòng Cốt"]
        C["Giai cấp Công nhân (Lực lượng lãnh đạo, tiên phong)"]
        D["Giai cấp Nông dân (Lực lượng đông đảo, chiến lược nông thôn)"]
        E["Đội ngũ Trí thức (Lực lượng lao động sáng tạo, KH-CN)"]
        F["Đội ngũ Doanh nhân (Lực lượng nòng cốt phát triển kinh tế)"]
    end

    B --- CacLucLuongNongCot

    subgraph BaNoiDungLienMinh ["3 Nội Dung Liên Minh"]
        G["Kinh tế (Quan trọng nhất, giữ vai trò quyết định)"]
        H["Chính trị (Bảo vệ chính quyền, độc lập chủ quyền)"]
        I["Văn hóa - Xã hội (Nâng cao dân trí, an sinh xã hội)"]
    end
    B --> BaNoiDungLienMinh
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Cơ cấu xã hội - giai cấp:** Hệ thống các giai cấp, tầng lớp xã hội tồn tại khách quan và mối quan hệ giữa chúng về sở hữu TLSX, tổ chức quản lý và phân phối của cải.
- **Vị trí trung tâm:** Cơ cấu xã hội - giai cấp giữ vị trí trung tâm, chi phối cơ cấu dân tộc, tôn giáo, dân số, nghề nghiệp.
- **Tính quy luật của sự biến đổi:** Do cơ cấu kinh tế nhiều thành phần quy định; cơ cấu giai cấp biến đổi đa dạng, phức tạp, vừa hợp tác vừa đấu tranh, từng bước xích lại gần nhau dưới định hướng XHCN.
- **Tính tất yếu của liên minh:** Xuất phát từ quy luật kinh tế của nền đại công nghiệp hiện đại và yêu cầu chính trị củng cố nền tảng chế độ XHCN.
- **Nội dung kinh tế của liên minh:** Là nội dung quan trọng nhất, giữ vai trò quyết định; kết hợp hài hòa lợi ích kinh tế, phát triển chuỗi giá trị nông - công nghiệp - dịch vụ.
""",

    "chuong_6_theory.md": """# CHƯƠNG 6: VẤN ĐỀ DÂN TỘC VÀ TÔN GIÁO TRONG THỜI KỲ QUÁ ĐỘ LÊN CHỦ NGHĨA XÃ HỘI

### 1. Sơ đồ Cương Lĩnh Dân Tộc & Nguyên Tắc Tôn Giáo
```mermaid
graph TD
    A["CƯƠNG LĨNH DÂN TỘC CỦA V.I.LÊNIN"]
    A --> A1["Các dân tộc hoàn toàn bình đẳng"]
    A --> A2["Các dân tộc được quyền tự quyết"]
    A --> A3["Liên hiệp công nhân tất cả các dân tộc (Cốt lõi)"]

    B["NGUYÊN TẮC GIẢI QUYẾT TÔN GIÁO"]
    B --> B1["Tôn trọng tự do tín ngưỡng và không tín ngưỡng"]
    B --> B2["Phân biệt rõ mặt chính trị và mặt tư tưởng"]
    B --> B3["Khắc phục dần tác động tiêu cực qua cải tạo xã hội"]
    B --> B4["Có quan điểm lịch sử - cụ thể"]

    C["ĐẶC ĐIỂM VIỆT NAM"]
    C --> C1["54 dân tộc anh em cư trú xen kẽ, đoàn kết bền chặt"]
    C --> C2["Đa tôn giáo đồng hành cùng dân tộc"]
    C --> C3["Kiên quyết đấu tranh chống lợi dụng dân tộc, tôn giáo"]
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Dân tộc:**
  - *Nghĩa rộng (Quốc gia):* Cộng đồng có chung lãnh thổ, kinh tế, ngôn ngữ, văn hóa và thể chế nhà nước.
  - *Nghĩa hẹp (Tộc người):* Cộng đồng có chung ngôn ngữ, phong tục tập quán và ý thức tự giác tộc người.
- **Hai xu hướng phát triển dân tộc:** Xu hướng tách ra thành quốc gia độc lập và xu hướng liên hiệp lại giữa các dân tộc.
- **Bản chất tôn giáo:** Hình thái ý thức xã hội phản ánh hư ảo hiện thực khách quan; có nguồn gốc tự nhiên - kinh tế - xã hội, nguồn gốc nhận thức và nguồn gốc tâm lý.
- **Ba tính chất của tôn giáo:** Tính lịch sử, tính quần chúng, tính chính trị.
- **Chính sách của Đảng và Nhà nước Việt Nam:**
  - *Dân tộc:* "Bình đẳng, đoàn kết, tôn trọng và giúp nhau cùng phát triển".
  - *Tôn giáo:* Tôn trọng và bảo hộ quyền tự do tín ngưỡng, tôn giáo; đồng bào các tôn giáo là bộ phận không thể tách rời của khối đại đoàn kết toàn dân tộc.
""",

    "chuong_7_theory.md": """# CHƯƠNG 7: VẤN ĐỀ GIA ĐÌNH TRONG THỜI KỲ QUÁ ĐỘ LÊN CHỦ NGHĨA XÃ HỘI

### 1. Sơ đồ Vị trí & Chức năng Cốt lõi của Gia Đình
```mermaid
graph TD
    A["GIA ĐÌNH (Tế bào của Xã hội & Tổ ấm của Cá nhân)"]
    
    subgraph BonChucNang ["4 Chức Năng Cơ Bản"]
        B["1. Tái sản xuất ra con người (Đặc thù duy nhất)"]
        C["2. Nuôi dưỡng, giáo dục nhân cách"]
        D["3. Kinh tế và tổ chức tiêu dùng"]
        E["4. Thỏa mãn tâm sinh lý, duy trì tình cảm"]
    end
    A --> BonChucNang

    subgraph CoSoXayDung ["Cơ Sở Xây Dựng Gia Đình XHCN"]
        F["Kinh tế: Chế độ công hữu TLSX"]
        G["Chính trị - Pháp lý: Nhà nước XHCN & Luật Hôn nhân Gia đình"]
        H["Văn hóa: Các giá trị nhân văn tiến bộ"]
        I["Hôn nhân tiến bộ: Tự nguyện, 1 vợ 1 chồng, bình đẳng"]
    end
    A --> CoSoXayDung
```

### 2. Các Khái Niệm Nền Tảng & Luận Điểm Cốt Lõi
- **Gia đình:** Cộng đồng xã hội đặc biệt hình thành trên cơ sở quan hệ hôn nhân, quan hệ huyết thống và quan hệ nuôi dưỡng, gắn liền với quyền và nghĩa vụ giữa các thành viên.
- **Vị trí của gia đình:**
  - Là tế bào tự nhiên của xã hội; xã hội tốt đẹp khi các tế bào gia đình lành mạnh.
  - Là tổ ấm mang lại hạnh phúc cho mỗi cá nhân.
  - Là cầu nối trực tiếp giữa cá nhân và xã hội.
- **Chế độ hôn nhân tiến bộ:** Hôn nhân tự nguyện; Hôn nhân một vợ một chồng, vợ chồng bình đẳng; Hôn nhân được pháp luật thừa nhận và bảo vệ.
- **Sự biến đổi của gia đình Việt Nam hiện nay:**
  - Chuyển dịch nhanh chóng từ gia đình truyền thống sang mô hình *gia đình hạt nhân*.
  - Biến đổi quan hệ thế hệ và chức năng giáo dục đòi hỏi kết hợp hài hòa chuẩn mực gia đình truyền thống (hiếu thuận, hòa thuận) với văn minh hiện đại (bình đẳng giới, tôn trọng quyền riêng tư).
"""
}

for fname, content in theories.items():
    fpath = os.path.join(docs_cnxhkh_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    print(f"Wrote theory file: {fname}")

print("Theory files generated successfully!")
