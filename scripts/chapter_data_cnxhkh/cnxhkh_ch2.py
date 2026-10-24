# -*- coding: utf-8 -*-
"""Chapter 2 Exercises: Sứ mệnh lịch sử của giai cấp công nhân"""

DATA = {
    "chapter_id": "chuong_2",
    "chapter_title": "Chương 2: Sứ mệnh lịch sử của giai cấp công nhân",
    "multiple_choice": [
        {
            "id": 1,
            "difficulty": "easy",
            "question": "Theo chủ nghĩa Mác - Lênin, giai cấp công nhân ra đời và phát triển gắn liền với sự phát triển của:",
            "options": {
                "A": "Nền sản xuất nông nghiệp phong kiến",
                "B": "Nền sản xuất đại công nghiệp cơ khí",
                "C": "Nền kinh tế tự nhiên tự cung tự cấp",
                "D": "Kinh tế tiểu thủ công nghiệp phường hội"
            },
            "correct_answer": "B",
            "explanation": "Giai cấp công nhân hiện đại là sản phẩm của bản thân nền đại công nghiệp, phát triển tỷ lệ thuận với sự phát triển của máy móc công nghiệp."
        },
        {
            "id": 2,
            "difficulty": "easy",
            "question": "Phương diện nào xác định giai cấp công nhân dựa trên vị trí làm thuê và bị bóc lột giá trị thặng dư dưới CNTB?",
            "options": {
                "A": "Phương diện kinh tế - kỹ thuật",
                "B": "Phương diện kinh tế - xã hội",
                "C": "Phương diện văn hóa - tư tưởng",
                "D": "Phương diện chính trị thuần túy"
            },
            "correct_answer": "B",
            "explanation": "Phương diện kinh tế - xã hội xem xét vị trí của công nhân trong quan hệ sản xuất TBCN: không có TLSX, phải bán sức lao động cho nhà tư bản."
        },
        {
            "id": 3,
            "difficulty": "easy",
            "question": "Giai cấp nào là đại biểu cho lực lượng sản xuất tiên tiến và phương thức sản xuất hiện đại nhất của xã hội loài người?",
            "options": {
                "A": "Giai cấp nông dân",
                "B": "Tầng lớp trí thức",
                "C": "Giai cấp công nhân",
                "D": "Giai cấp tư sản"
            },
            "correct_answer": "C",
            "explanation": "Giai cấp công nhân là lực lượng lao động trực tiếp hoặc gián tiếp vận hành hệ thống máy móc đại công nghiệp hiện đại, đại biểu cho LLSX tiên tiến."
        },
        {
            "id": 4,
            "difficulty": "easy",
            "question": "Nội dung sứ mệnh lịch sử của giai cấp công nhân trên lĩnh vực chính trị - xã hội là gì?",
            "options": {
                "A": "Lập các công ty đa quốc gia",
                "B": "Lật đổ nhà nước tư sản, thiết lập nhà nước XHCN của nhân dân lao động",
                "C": "Ủng hộ chế độ đa nguyên đa đảng",
                "D": "Kêu gọi xóa bỏ mọi đảng phái chính trị"
            },
            "correct_answer": "B",
            "explanation": "Về chính trị, GCCN lãnh đạo quần chúng lật đổ ách thống trị tư sản, giành lấy chính quyền và xây dựng nhà nước chuyên chính vô sản / XHCN."
        },
        {
            "id": 5,
            "difficulty": "easy",
            "question": "Đâu là nhân tố chủ quan hàng đầu, có ý nghĩa quyết định nhất để giai cấp công nhân hoàn thành sứ mệnh lịch sử?",
            "options": {
                "A": "Số lượng công nhân đông đảo",
                "B": "Sự viện trợ kinh tế từ nước ngoài",
                "C": "Sự lãnh đạo của Đảng Cộng sản",
                "D": "Sự ủng hộ của các tập đoàn tư bản"
            },
            "correct_answer": "C",
            "explanation": "Đảng Cộng sản là đội tiên phong chiến đấu của giai cấp công nhân, đề ra cương lĩnh, đường lối đúng đắn để lãnh đạo cách mạng thắng lợi."
        },
        {
            "id": 6,
            "difficulty": "easy",
            "question": "Đảng Cộng sản là sản phẩm của sự kết hợp giữa chủ nghĩa Mác - Lênin với yếu tố nào?",
            "options": {
                "A": "Phong trào nông dân",
                "B": "Phong trào công nhân",
                "C": "Phong trào yêu nước nói chung",
                "D": "Phong trào văn hóa tiến bộ"
            },
            "correct_answer": "B",
            "explanation": "Theo V.I.Lênin, Đảng Cộng sản ra đời là kết quả của sự kết hợp giữa chủ nghĩa Mác với phong trào công nhân."
        },
        {
            "id": 7,
            "difficulty": "easy",
            "question": "Tại sao giai cấp công nhân có tính tổ chức và kỷ luật lao động cao?",
            "options": {
                "A": "Do phẩm chất đạo đức bẩm sinh",
                "B": "Do được tôi luyện trong môi trường sản xuất dây chuyền đại công nghiệp hiện đại",
                "C": "Do các hiệp hội tôn giáo rèn luyện",
                "D": "Do luật pháp phong kiến quy định"
            },
            "correct_answer": "B",
            "explanation": "Môi trường sản xuất đại công nghiệp với quy trình công nghệ nghiêm ngặt, chuyên môn hóa cao rèn luyện cho công nhân tính tổ chức, kỷ luật cao."
        },
        {
            "id": 8,
            "difficulty": "easy",
            "question": "Giai cấp công nhân Việt Nam ra đời trong hoàn cảnh lịch sử nào?",
            "options": {
                "A": "Trước khi thực dân Pháp xâm lược Việt Nam",
                "B": "Trong các cuộc khai thác thuộc địa của thực dân Pháp đầu thế kỷ XX",
                "C": "Sau Cách mạng Tháng Tám năm 1945",
                "D": "Trong thời kỳ Đổi mới năm 1986"
            },
            "correct_answer": "B",
            "explanation": "Giai cấp công nhân Việt Nam ra đời trong quá trình khai thác thuộc địa lần thứ nhất và thứ hai của thực dân Pháp (cuối thế kỷ XIX - đầu thế kỷ XX)."
        },
        {
            "id": 9,
            "difficulty": "easy",
            "question": "Một đặc điểm nổi bật của giai cấp công nhân Việt Nam so với công nhân ở các nước tư bản phát triển là:",
            "options": {
                "A": "Ra đời sau giai cấp tư sản dân tộc",
                "B": "Ra đời trước giai cấp tư sản dân tộc và sớm tiếp thu chủ nghĩa Mác - Lênin",
                "C": "Không có tinh thần yêu nước",
                "D": "Không có quan hệ gắn bó với nông dân"
            },
            "correct_answer": "B",
            "explanation": "GCCN Việt Nam ra đời trước giai cấp tư sản dân tộc, sớm thành lập được chính đảng của mình (1930) và nắm quyền lãnh đạo duy nhất đối với cách mạng."
        },
        {
            "id": 10,
            "difficulty": "easy",
            "question": "Đảng Cộng sản Việt Nam ra đời là sản phẩm của sự kết hợp giữa chủ nghĩa Mác - Lênin với phong trào công nhân và:",
            "options": {
                "A": "Phong trào nông dân",
                "B": "Phong trào yêu nước",
                "C": "Phong trào thanh niên",
                "D": "Phong trào trí thức"
            },
            "correct_answer": "B",
            "explanation": "Chủ tịch Hồ Chí Minh khẳng định Đảng Cộng sản Việt Nam là sản phẩm kết hợp giữa chủ nghĩa Mác - Lênin với phong trào công nhân và phong trào yêu nước."
        },
        {
            "id": 11,
            "difficulty": "medium",
            "question": "Điều kiện khách quan quy định sứ mệnh lịch sử của giai cấp công nhân bao gồm:",
            "options": {
                "A": "Địa vị kinh tế và địa vị chính trị - xã hội của giai cấp công nhân",
                "B": "Trình độ ngoại ngữ và khả năng giao tiếp",
                "C": "Lòng căm thù cá nhân đối với giới chủ tư bản",
                "D": "Sự giúp đỡ tài chính từ các tổ chức phi chính phủ"
            },
            "correct_answer": "A",
            "explanation": "Địa vị kinh tế (đại biểu LLSX tiên tiến) và địa vị chính trị - xã hội (triệt để cách mạng, có tinh thần quốc tế) tạo nên điều kiện khách quan của sứ mệnh."
        },
        {
            "id": 12,
            "difficulty": "medium",
            "question": "Vì sao giai cấp công nhân là giai cấp cách mạng triệt để nhất?",
            "options": {
                "A": "Vì công nhân có nhiều tài sản nhất",
                "B": "Vì công nhân chỉ có thể giải phóng mình bằng cách giải phóng toàn thể nhân loại khỏi mọi chế độ áp bức bóc lột",
                "C": "Vì công nhân không sợ nguy hiểm",
                "D": "Vì công nhân muốn thay thế địa vị của giai cấp tư sản để bóc lột lại"
            },
            "correct_answer": "B",
            "explanation": "Lợi ích căn bản của GCCN thống nhất với lợi ích nhân dân lao động; công nhân xóa bỏ tư hữu chứ không nhằm thay thế chế độ bóc lột này bằng chế độ bóc lột khác."
        },
        {
            "id": 13,
            "difficulty": "medium",
            "question": "Trong xã hội tư bản hiện đại, xu hướng 'trí tuệ hóa' của công nhân thể hiện ở đặc điểm nào?",
            "options": {
                "A": "Công nhân chỉ làm việc tại nhà",
                "B": "Hàm lượng tri thức, kỹ năng công nghệ cao và tự động hóa ngày càng gia tăng trong lao động (công nhân tri thức / áo trắng)",
                "C": "Công nhân chuyển sang làm chủ ngân hàng",
                "D": "Không còn lao động trong các nhà máy"
            },
            "correct_answer": "B",
            "explanation": "Cuộc cách mạng khoa học công nghệ làm xuất hiện lớp công nhân hiện đại với trình độ chuyên môn cao, lao động trí óc chiếm tỷ trọng lớn."
        },
        {
            "id": 14,
            "difficulty": "medium",
            "question": "Hiện tượng một bộ phận công nhân ở các nước tư bản phát triển sở hữu cổ phiếu nhỏ lẻ ('trung lưu hóa') có làm thay đổi bản chất làm thuê của họ không?",
            "options": {
                "A": "Có, họ đã trở thành nhà tư bản thực thụ",
                "B": "Không, họ vẫn là người bán sức lao động và bị bóc lột giá trị thặng dư bởi các tập đoàn nắm cổ phần chi phối",
                "C": "Làm cho chủ nghĩa tư bản hoàn toàn biến mất",
                "D": "Biến công nhân thành chủ sở hữu toàn bộ xí nghiệp"
            },
            "correct_answer": "B",
            "explanation": "Cổ phiếu nhỏ lẻ không mang lại quyền quyết định phương thức sản xuất; các nhà tài phiệt nắm đa số cổ phần vẫn chiếm hữu toàn bộ giá trị thặng dư."
        },
        {
            "id": 15,
            "difficulty": "medium",
            "question": "Nội dung kinh tế trong sứ mệnh lịch sử của giai cấp công nhân Việt Nam hiện nay là gì?",
            "options": {
                "A": "Chỉ tập trung khai thác tài nguyên thô để xuất khẩu",
                "B": "Là lực lượng nòng cốt đi đầu trong sự nghiệp công nghiệp hóa, hiện đại hóa đất nước gắn với kinh tế tri thức",
                "C": "Kêu gọi xóa bỏ hoàn toàn khu vực kinh tế tư nhân",
                "D": "Hạn chế đầu tư nước ngoài"
            },
            "correct_answer": "B",
            "explanation": "Công nhân Việt Nam là lực lượng chủ đạo đẩy mạnh CNH, HĐH đất nước, làm chủ khoa học công nghệ hiện đại và nâng cao năng suất quốc gia."
        },
        {
            "id": 16,
            "difficulty": "medium",
            "question": "Để giai cấp công nhân hoàn thành sứ mệnh lịch sử, việc xây dựng khối liên minh nào là nguyên tắc chiến lược có tính sống còn?",
            "options": {
                "A": "Liên minh giữa công nhân với giai cấp tư sản lớn",
                "B": "Khối liên minh giai cấp giữa công nhân với nông dân và tầng lớp trí thức",
                "C": "Liên minh giữa công nhân với các phe phái đối lập",
                "D": "Liên minh với quân đội nước ngoài"
            },
            "correct_answer": "B",
            "explanation": "Liên minh công - nông - trí thức dưới sự lãnh đạo của Đảng là nền tảng chính trị - xã hội bảo đảm cho thắng lợi của cách mạng XHCN."
        },
        {
            "id": 17,
            "difficulty": "medium",
            "question": "Mục tiêu tối thượng và cao cả nhất trong sứ mệnh lịch sử của giai cấp công nhân là gì?",
            "options": {
                "A": "Tăng lương và giảm giờ làm cho công nhân",
                "B": "Giải phóng giai cấp công nhân, giải phóng nhân dân lao động và toàn thể nhân loại khỏi ách áp bức, bóc lột",
                "C": "Trở thành tầng lớp thượng lưu giàu có",
                "D": "Chiếm hữu toàn bộ tài nguyên thế giới"
            },
            "correct_answer": "B",
            "explanation": "Chủ nghĩa Mác khẳng định sứ mệnh của GCCN không nhằm mục đích ích kỷ cho riêng mình mà là giải phóng toàn thể loài người khỏi nô dịch, tha hóa."
        },
        {
            "id": 18,
            "difficulty": "medium",
            "question": "Nội dung văn hóa - tư tưởng trong sứ mệnh lịch sử của giai cấp công nhân đòi hỏi phải làm gì?",
            "options": {
                "A": "Xóa bỏ toàn bộ các nền văn hóa truyền thống",
                "B": "Xây dựng hệ tư tưởng tiên tiến của giai cấp công nhân (chủ nghĩa Mác - Lênin), xây dựng nền văn hóa mới XHCN",
                "C": "Nhập khẩu nguyên xi lối sống phương Tây",
                "D": "Cấm đoán mọi hoạt động văn nghệ dân gian"
            },
            "correct_answer": "B",
            "explanation": "Xác lập hệ tư tưởng tiến bộ, kế thừa tinh hoa văn hóa dân tộc và nhân loại, xây dựng con người mới XHCN phát triển toàn diện."
        },
        {
            "id": 19,
            "difficulty": "medium",
            "question": "Tại sao đa số công nhân Việt Nam khi mới ra đời lại có mối quan hệ tự nhiên gắn bó máu thịt với giai cấp nông dân?",
            "options": {
                "A": "Vì họ đều sinh sống tại vùng miền núi",
                "B": "Vì phần lớn công nhân Việt Nam xuất thân từ người nông dân bị thực dân, địa chủ cướp đoạt ruộng đất",
                "C": "Vì công nhân và nông dân cùng làm nghề nông",
                "D": "Do các nhà tư bản ép buộc ký cam kết"
            },
            "correct_answer": "B",
            "explanation": "Chính sách cướp bóc ruộng đất của thực dân Pháp đã biến hàng loạt nông dân bần cùng hóa thành phu đồn điền, thợ mỏ, thợ nhà máy."
        },
        {
            "id": 20,
            "difficulty": "medium",
            "question": "Tổ chức chính trị - xã hội nào là đại diện bảo vệ quyền và lợi ích hợp pháp, chính đáng của công nhân, người lao động Việt Nam?",
            "options": {
                "A": "Hội Cựu chiến binh",
                "B": "Công đoàn Việt Nam",
                "C": "Hội Nông dân Việt Nam",
                "D": "Đoàn Thanh niên"
            },
            "correct_answer": "B",
            "explanation": "Công đoàn là tổ chức đại diện, chăm lo và bảo vệ quyền, lợi ích hợp pháp của người lao động; tập hợp và giáo dục công nhân."
        },
        {
            "id": 21,
            "difficulty": "hard",
            "question": "Luận điểm nào sau đây chứng minh tính chất quốc tế của sứ mệnh lịch sử giai cấp công nhân?",
            "options": {
                "A": "Các nhà máy công nghiệp chỉ được xây dựng gần cảng biển quốc tế",
                "B": "Chủ nghĩa tư bản là một lực lượng quốc tế, bản chất bóc lột mang tính toàn cầu; cuộc đấu tranh giải phóng công nhân đòi hỏi sự đoàn kết quốc tế của giai cấp vô sản",
                "C": "Công nhân bắt buộc phải sử dụng chung một ngôn ngữ quốc tế",
                "D": "Mọi công nhân đều phải ra nước ngoài làm việc"
            },
            "correct_answer": "B",
            "explanation": "Tư bản mang tính toàn cầu, các tập đoàn đa quốc gia bóc lột không biên giới; vì vậy 'vô sản tất cả các nước đoàn kết lại' là tất yếu khách quan."
        },
        {
            "id": 22,
            "difficulty": "hard",
            "question": "Điểm khác biệt căn bản giữa giai cấp công nhân hiện nay so với công nhân thế kỷ XIX là:",
            "options": {
                "A": "Công nhân hiện nay không còn bị bóc lột giá trị thặng dư",
                "B": "Công nhân hiện nay có trình độ tri thức, tay nghề công nghệ thông tin cao hơn và cơ cấu ngành nghề chuyển dịch mạnh mẽ",
                "C": "Công nhân hiện nay không còn nhu cầu đấu tranh giai cấp",
                "D": "Công nhân hiện nay đã nắm giữ hầu hết các tập đoàn kinh tế tư bản lớn"
            },
            "correct_answer": "B",
            "explanation": "Công nhân hiện đại gắn liền với nền kinh tế tri thức và công nghệ 4.0; tuy vậy bản chất quan hệ sản xuất làm thuê bóc lột vẫn còn nguyên vẹn."
        },
        {
            "id": 23,
            "difficulty": "hard",
            "question": "Tại sao các thế lực thù địch lại ra sức rêu rao rằng 'giai cấp công nhân đã tan rã hoặc biến chất trong thời đại 4.0'?",
            "options": {
                "A": "Để giúp công nhân thành lập nhiều công đoàn tự do hơn",
                "B": "Nhằm phủ nhận vai trò lãnh đạo cách mạng của giai cấp công nhân và phủ nhận vai trò lãnh đạo của Đảng Cộng sản",
                "C": "Để khuyến khích công nhân học tập công nghệ thông tin",
                "D": "Nhằm giúp các nước đang phát triển thu hút vốn FDI"
            },
            "correct_answer": "B",
            "explanation": "Âm mưu xuyên tạc nhằm tước bỏ vũ khí tư tưởng của công nhân, phá hoại nền tảng chính trị và chế độ XHCN từ bên trong."
        },
        {
            "id": 24,
            "difficulty": "hard",
            "question": "Theo V.I.Lênin, muốn thực hiện thành công sự chuyển biến tư tưởng từ 'tự phát' lên 'tự giác', phong trào công nhân cần có yếu tố nào?",
            "options": {
                "A": "Chủ nghĩa Mác phải được thâm nhập, truyền bá từ bên ngoài vào phong trào công nhân thông qua đội tiên phong là Đảng Cộng sản",
                "B": "Tự động chờ đợi công nhân tích lũy kinh nghiệm đấu tranh đòi tăng lương",
                "C": "Dựa vào các bài thuyết giảng từ thiện của giới chủ tư bản",
                "D": "Nhờ sự can thiệp của tòa án quốc tế"
            },
            "correct_answer": "A",
            "explanation": "Đấu tranh kinh tế tự phát chỉ dừng lại ở ý thức công đoàn chủ nghĩa; lý luận chủ nghĩa Mác phải được Đảng Cộng sản truyền bá vào mới nâng lên ý thức chính trị tự giác."
        },
        {
            "id": 25,
            "difficulty": "hard",
            "question": "Sự thống nhất biện chứng giữa tính giai cấp và tính dân tộc của giai cấp công nhân Việt Nam biểu hiện ở điểm nào?",
            "options": {
                "A": "Giai cấp công nhân chỉ quan tâm đến lợi ích giai cấp mà hy sinh lợi ích dân tộc",
                "B": "Lợi ích cơ bản của giai cấp công nhân hoàn toàn phù hợp và thống nhất hữu cơ với lợi ích độc lập, tự do và phát triển phồn vinh của toàn thể dân tộc Việt Nam",
                "C": "Giai cấp công nhân hoàn toàn hòa tan vào các giai cấp khác",
                "D": "Không thừa nhận giá trị văn hóa truyền thống dân tộc"
            },
            "correct_answer": "B",
            "explanation": "Đảng và GCCN Việt Nam đại biểu cho lợi ích của giai cấp công nhân, đồng thời đại biểu trung thành cho lợi ích của nhân dân lao động và của toàn dân tộc."
        },
        {
            "id": 26,
            "difficulty": "hard",
            "question": "Khái niệm 'Công nhân tri thức' (Knowledge Workers) được hiểu chính xác nhất là:",
            "options": {
                "A": "Những nhà khoa học hàn lâm không bao giờ tham gia sản xuất vật chất",
                "B": "Những người lao động sử dụng tri thức khoa học, công nghệ cao trực tiếp hoặc gián tiếp vào quá trình sản xuất vật chất hiện đại",
                "C": "Tất cả những ai có bằng tiến sĩ",
                "D": "Chỉ những người làm việc trong cơ quan nhà nước"
            },
            "correct_answer": "B",
            "explanation": "Họ trực tiếp làm chủ các công nghệ cao, tự động hóa, lập trình điều khiển máy móc sản xuất tạo ra của cải vật chất cho xã hội."
        },
        {
            "id": 27,
            "difficulty": "hard",
            "question": "Thách thức lớn nhất đối với việc phát triển giai cấp công nhân Việt Nam trong bối cảnh cuộc Cách mạng công nghiệp 4.0 là:",
            "options": {
                "A": "Thiếu hụt trầm trọng lao động phổ thông giá rẻ",
                "B": "Trình độ học vấn, kỹ năng tay nghề và tác phong công nghiệp nhìn chung còn hạn chế trước nguy cơ máy móc tự động hóa thay thế lao động giản đơn",
                "C": "Có quá nhiều công nhân tham gia nghiên cứu khoa học cơ bản",
                "D": "Không còn nguồn bổ sung công nhân từ khu vực nông thôn"
            },
            "correct_answer": "B",
            "explanation": "Tỷ lệ lao động qua đào tạo còn thấp; nguy cơ mất việc do robot hóa đòi hỏi cấp bách phải đào tạo lại và nâng cao tay nghề chất lượng cao."
        },
        {
            "id": 28,
            "difficulty": "hard",
            "question": "Đặc trưng nào chứng minh giai cấp công nhân là lực lượng duy nhất có khả năng lãnh đạo cách mạng vô sản đi đến thắng lợi cuối cùng?",
            "options": {
                "A": "Có quân đội trang bị vũ khí hạt nhân",
                "B": "Có hệ tư tưởng cách mạng khoa học dẫn đường (chủ nghĩa Mác - Lênin) và chính đảng có tính kỷ luật sắt lãnh đạo",
                "C": "Là giai cấp duy nhất tham gia biểu tình đường phố",
                "D": "Có nguồn tài trợ khổng lồ từ các quỹ tiền tệ quốc tế"
            },
            "correct_answer": "B",
            "explanation": "Các tầng lớp khác (nông dân, tiểu tư sản) có tinh thần yêu nước nhưng thiếu hệ tư tưởng độc lập và tính tổ chức tập trung nghiêm ngặt."
        },
        {
            "id": 29,
            "difficulty": "hard",
            "question": "Trong nền kinh tế thị trường định hướng XHCN ở nước ta, giai cấp công nhân công tác trong các doanh nghiệp có vốn đầu tư nước ngoài (FDI):",
            "options": {
                "A": "Không còn thuộc vào giai cấp công nhân Việt Nam",
                "B": "Vẫn là một bộ phận hữu cơ cấu thành của giai cấp công nhân Việt Nam, đóng góp tích cực cho đất nước nhưng cần được bảo đảm quyền lợi chính đáng",
                "C": "Đã trở thành tư sản ngoại bang",
                "D": "Bị tước bỏ quyền công dân"
            },
            "correct_answer": "B",
            "explanation": "Họ là bộ phận tiếp cận công nghệ hiện đại, tác phong công nghiệp quốc tế, cần sự bảo vệ và chăm lo quyền lợi từ tổ chức Công đoàn."
        },
        {
            "id": 30,
            "difficulty": "hard",
            "question": "Ý nghĩa phương pháp luận của việc nghiên cứu sứ mệnh lịch sử giai cấp công nhân đối với sinh viên là:",
            "options": {
                "A": "Thụ động chờ đợi giai cấp công nhân giải phóng xã hội",
                "B": "Nỗ lực học tập, rèn luyện kỹ năng chuyên môn, chuẩn bị gia nhập đội ngũ công nhân tri thức và củng cố niềm tin vào Đảng Cộng sản Việt Nam",
                "C": "Tìm kiếm học bổng để định cư vĩnh viễn ở nước ngoài",
                "D": "Xem nhẹ các môn lý luận chính trị trong nhà trường"
            },
            "correct_answer": "B",
            "explanation": "Sinh viên chính là nguồn bổ sung tinh hoa cho đội ngũ công nhân tri thức và trí thức cách mạng, đóng vai trò xung kích xây dựng đất nước phồn vinh."
        }
    ],
    "short_answers": [
        {
            "id": 1,
            "question": "Nêu định nghĩa giai cấp công nhân và làm rõ hai phương diện nhận diện cơ bản.",
            "expected_answer": "- **Định nghĩa:** Giai cấp công nhân là một tập đoàn xã hội ổn định, hình thành và phát triển cùng với nền đại công nghiệp; đại diện cho LLSX tiên tiến; là lực lượng chủ yếu của tiến trình quá độ lên CNXH.\n- **Phương diện kinh tế - kỹ thuật:** Lao động trực tiếp/gián tiếp vận hành máy móc công nghiệp hiện đại, có tính xã hội hóa cao.\n- **Phương diện kinh tế - xã hội:** Dưới CNTB là người làm thuê không có TLSX, bị bóc lột giá trị thặng dư.",
            "explanation": "Được C.Mác và Ph.Ăngghen chỉ rõ trong nhiều tác phẩm kinh điển."
        },
        {
            "id": 2,
            "question": "Trình bày ba nội dung chính trong sứ mệnh lịch sử của giai cấp công nhân.",
            "expected_answer": "1. **Nội dung kinh tế:** Xác lập chế độ công hữu về các TLSX chủ yếu, giải phóng và phát triển LLSX đáp ứng nhu cầu nhân dân.\n2. **Nội dung chính trị - xã hội:** Lật đổ ách thống trị tư sản, thiết lập nhà nước XHCN, củng cố quyền làm chủ của nhân dân lao động.\n3. **Nội dung văn hóa - tư tưởng:** Xác lập hệ tư tưởng Mác - Lênin, xây dựng nền văn hóa mới và con người mới XHCN.",
            "explanation": "Ba nội dung bao quát toàn diện các lĩnh vực của đời sống xã hội."
        },
        {
            "id": 3,
            "question": "Liệt kê hai điều kiện khách quan quy định sứ mệnh lịch sử của giai cấp công nhân.",
            "expected_answer": "1. **Địa vị kinh tế:** Đại diện cho lực lượng sản xuất tiên tiến nhất, là chủ thể của nền đại công nghiệp hiện đại quyết định sự tồn tại xã hội.\n2. **Địa vị chính trị - xã hội:** Là giai cấp bị bóc lột nặng nề nhất dưới CNTB, có tinh thần cách mạng triệt để nhất, có tính tổ chức và kỷ luật cao do môi trường sản xuất rèn luyện.",
            "explanation": "Khách quan nghĩa là bắt nguồn từ chính phương thức sản xuất TBCN chứ không do ý muốn chủ quan."
        },
        {
            "id": 4,
            "question": "Giải thích vai trò của Đảng Cộng sản đối với việc thực hiện sứ mệnh lịch sử của giai cấp công nhân.",
            "expected_answer": "Đảng Cộng sản là đội tiên phong của giai cấp công nhân, là bộ tham mưu chiến đấu kết hợp chủ nghĩa Mác - Lênin với phong trào công nhân. Đảng đề ra đường lối chiến lược cách mạng đúng đắn, tổ chức, giác ngộ và lãnh đạo quần chúng nhân dân biến sứ mệnh lịch sử thành hiện thực.",
            "explanation": "Không có Đảng lãnh đạo, phong trào công nhân chỉ dừng lại ở mức đấu tranh kinh tế tự phát."
        },
        {
            "id": 5,
            "question": "Chỉ ra 2 điểm biến đổi mới của giai cấp công nhân trong các nước tư bản hiện đại ngày nay.",
            "expected_answer": "1. **Xu hướng trí tuệ hóa (công nhân tri thức):** Lao động trí óc và tỷ lệ áp dụng tự động hóa, công nghệ cao tăng mạnh.\n2. **Xu hướng 'trung lưu hóa' và đa dạng hóa ngành nghề:** Đời sống được cải thiện, sở hữu cổ phiếu nhỏ lẻ, chuyển dịch từ công nghiệp nặng sang công nghệ thông tin, dịch vụ kỹ thuật.",
            "explanation": "Dù vậy, bản chất bóc lột giá trị thặng dư vẫn không thay đổi."
        },
        {
            "id": 6,
            "question": "Nêu những đặc điểm lịch sử nổi bật của giai cấp công nhân Việt Nam khi mới hình thành.",
            "expected_answer": "1. Ra đời trước giai cấp tư sản dân tộc trong cuộc khai thác thuộc địa của Pháp.\n2. Trực tiếp đối kháng với thực dân và phong kiến, mang truyền thống yêu nước sâu sắc.\n3. Gắn bó tự nhiên máu thịt với nông dân.\n4. Sớm được Đảng Cộng sản Việt Nam lãnh đạo và trung thành tuyệt đối với chủ nghĩa Mác - Lênin.",
            "explanation": "Tạo nên vị thế độc tôn lãnh đạo cách mạng của GCCN Việt Nam."
        },
        {
            "id": 7,
            "question": "Sứ mệnh lịch sử của giai cấp công nhân Việt Nam trong giai đoạn hiện nay trên lĩnh vực kinh tế là gì?",
            "expected_answer": "Là lực lượng tiên phong, nòng cốt trong sự nghiệp công nghiệp hóa, hiện đại hóa đất nước gắn với phát triển kinh tế tri thức; tích cực làm chủ khoa học kỹ thuật hiện đại; nâng cao năng suất lao động và xây dựng nền kinh tế độc lập tự chủ.",
            "explanation": "Phát huy vai trò đầu tàu trong phát triển lực lượng sản xuất."
        },
        {
            "id": 8,
            "question": "Nêu 2 giải pháp chủ yếu nhằm xây dựng giai cấp công nhân Việt Nam hiện đại, lớn mạnh theo tinh thần Nghị quyết của Đảng.",
            "expected_answer": "1. Đẩy mạnh đào tạo nghề, nâng cao trình độ học vấn, chuyên môn kỹ thuật, tác phong công nghiệp và kỷ luật lao động cho công nhân.\n2. Chăm lo đời sống vật chất, tinh thần, nhà ở, điều kiện lao động và củng cố vai trò của tổ chức Công đoàn, tổ chức Đảng trong các doanh nghiệp.",
            "explanation": "Đặc biệt chú trọng trong các khu công nghiệp, khu chế xuất."
        }
    ],
    "essays": [
        {
            "id": 1,
            "title": "Phân tích Điều kiện Khách quan và Nhân tố Chủ quan Quy định Sứ mệnh Lịch sử của Giai cấp Công nhân",
            "problem": "Hãy phân tích sâu sắc các yếu tố quy định sứ mệnh lịch sử của giai cấp công nhân:\n1. Phân tích địa vị kinh tế và địa vị chính trị - xã hội (điều kiện khách quan).\n2. Phân tích vai trò của Đảng Cộng sản và sự lớn mạnh của GCCN (nhân tố chủ quan).\n3. Phê phán luận điệu cho rằng trong thời đại 4.0, giai cấp công nhân đã mất đi sứ mệnh lịch sử.",
            "solution_steps": [
                "Bước 1: Điều kiện khách quan quy định sứ mệnh\n- **Địa vị kinh tế:** GCCN là con đẻ của nền đại công nghiệp, trực tiếp vận hành công cụ sản xuất hiện đại và đại biểu cho phương thức sản xuất tiên tiến nhất. Nền sản xuất TBCN càng phát triển thì số lượng và vai trò kinh tế của công nhân càng tăng.\n- **Địa vị chính trị - xã hội:** Dưới CNTB, công nhân không có TLSX, bị bóc lột nặng nề nhất nên có tinh thần cách mạng triệt để nhất (xóa bỏ chế độ tư hữu bóc lột). Môi trường sản xuất dây chuyền quy định tính tổ chức, kỷ luật cao và tinh thần đoàn kết quốc tế sâu sắc.",
                "Bước 2: Nhân tố chủ quan quyết định thắng lợi\n- **Sự phát triển của bản thân GCCN:** Tăng trưởng về số lượng và giác ngộ về chất lượng (từ đấu tranh tự phát đòi quyền lợi kinh tế lên đấu tranh tự giác với ý thức chính trị giai cấp).\n- **Đảng Cộng sản - đội tiên phong chiến đấu:** Là nhân tố chủ quan quyết định nhất. Đảng mang hệ tư tưởng Mác - Lênin, vạch ra cương lĩnh, chiến lược đúng đắn và tổ chức lãnh đạo quần chúng nhân dân.\n- **Khối liên minh công - nông:** Xây dựng mặt trận đoàn kết rộng rãi tạo sức mạnh áp đảo kẻ thù.",
                "Bước 3: Phê phán quan điểm sai trái, phủ nhận sứ mệnh GCCN\n- Các thế lực cơ hội lập luận rằng máy tính, robot làm thay đổi tất cả nên công nhân không còn nữa. Thực tế: máy móc và AI dù hiện đại đến đâu cũng chỉ là tư liệu sản xuất do con người chế tạo và vận hành. Tầng lớp công nhân tri thức, công nhân phần mềm, công nhân logistics ngày càng đông đảo và vẫn là người làm thuê tạo ra giá trị thặng dư cho các tập đoàn công nghệ lớn.",
                "Bước 4: Kết luận\n- Sứ mệnh lịch sử của GCCN vẫn giữ nguyên tính thời sự và tính cách mạng trong thế giới đương đại."
            ]
        },
        {
            "id": 2,
            "title": "Đặc Điểm Giai Cấp Công Nhân Việt Nam và Sự Lãnh Đạo Cách Mạng của Đảng Cộng Sản",
            "problem": "Phân tích những đặc điểm hình thành và phát triển của giai cấp công nhân Việt Nam. Tại sao nói giai cấp công nhân Việt Nam là lực lượng duy nhất có khả năng lãnh đạo cách mạng Việt Nam?",
            "solution_steps": [
                "Bước 1: Hoàn cảnh ra đời và đặc điểm của GCCN Việt Nam\n- Ra đời trong cuộc khai thác thuộc địa của Pháp trước cả khi giai cấp tư sản dân tộc xuất hiện.\n- Chịu ba tầng áp bức bóc lột tàn bạo: đế quốc Pháp, phong kiến tay sai và tư sản mại bản, do đó có tinh thần yêu nước và căm thù giặc sâu sắc.\n- Xuất thân chủ yếu từ nông dân mất đất, có mối liên hệ tự nhiên, máu thịt với đại đa số nhân dân lao động.\n- Sớm tiếp thu ánh sáng của chủ nghĩa Mác - Lênin qua con đường của Nguyễn Ái Quốc và thành lập Đảng Cộng sản Việt Nam (1930).",
                "Bước 2: Vì sao GCCN là lực lượng duy nhất lãnh đạo cách mạng?\n- **Thất bại của các giai cấp khác:** Các phong trào cứu nước theo khuynh hướng phong kiến (Cần Vương) hay dân chủ tư sản (Phan Bội Châu, Phan Châu Trinh, Việt Nam Quốc dân Đảng) đều lần lượt thất bại vì bế tắc về đường lối và thiếu một giai cấp tiên tiến dẫn dắt.\n- **Khả năng nắm ngọn cờ lãnh đạo:** GCCN Việt Nam tuy số lượng ban đầu nhỏ bé nhưng sớm có Đảng Cộng sản lãnh đạo, kết hợp nhuần nhuyễn mục tiêu độc lập dân tộc với chủ nghĩa xã hội, đáp ứng trúng khát vọng ngàn đời của toàn thể dân tộc Việt Nam.",
                "Bước 3: Thành tựu thực tiễn chứng minh\n- Dưới sự lãnh đạo của Đảng và GCCN: Cách mạng Tháng Tám 1945 thành công khai sinh nước Việt Nam Dân chủ Cộng hòa; đánh thắng hai đế quốc to lớn (Pháp và Mỹ); thống nhất non sông và tiến hành công cuộc Đổi mới gặt hái nhiều thành tựu rực rỡ."
            ]
        },
        {
            "id": 3,
            "title": "Nội Dung Sứ Mệnh Lịch Sử Giai Cấp Công Nhân Việt Nam Hiện Nay",
            "problem": "Trình bày cụ thể nội dung sứ mệnh lịch sử của giai cấp công nhân Việt Nam trong bối cảnh đẩy mạnh công nghiệp hóa, hiện đại hóa và hội nhập quốc tế trên ba phương diện: Kinh tế, Chính trị - Xã hội và Văn hóa - Tư tưởng.",
            "solution_steps": [
                "Bước 1: Phương diện kinh tế\n- Là lực lượng sản xuất nòng cốt, đi đầu trong sự nghiệp công nghiệp hóa, hiện đại hóa đất nước gắn với phát triển kinh tế tri thức và chuyển đổi số.\n- Nâng cao năng suất lao động, chất lượng sản phẩm, thúc đẩy tăng trưởng kinh tế bền vững và xây dựng nền kinh tế độc lập, tự chủ.",
                "Bước 2: Phương diện chính trị - xã hội\n- Giữ vững và tăng cường vai trò lãnh đạo tuyệt đối của Đảng Cộng sản Việt Nam đối với xã hội.\n- Tham gia xây dựng Nhà nước pháp quyền XHCN của nhân dân, do nhân dân, vì nhân dân.\n- Củng cố vững chắc khối liên minh công - nông - trí thức và khối đại đoàn kết toàn dân tộc; giữ vững an ninh chính trị và chủ quyền quốc gia.",
                "Bước 3: Phương diện văn hóa - tư tưởng\n- Giữ vững nền tảng tư tưởng là chủ nghĩa Mác - Lênin và tư tưởng Hồ Chí Minh.\n- Xây dựng nền văn hóa Việt Nam tiên tiến, đậm đà bản sắc dân tộc; rèn luyện con người mới có tác phong công nghiệp, kỷ luật, yêu nước, sáng tạo.\n- Kiên quyết đấu tranh phản bác các quan điểm sai trái, thù địch chống phá Đảng và chế độ XHCN."
            ]
        },
        {
            "id": 4,
            "title": "Giải Pháp Xây Dựng Giai Cấp Công Nhân Việt Nam Lớn Mạnh Trong Thời Kỳ Mới",
            "problem": "Nghị quyết số 20-NQ/TW của Ban Chấp hành Trung ương Đảng (khóa X) về 'Tiếp tục xây dựng giai cấp công nhân Việt Nam thời kỳ đẩy mạnh công nghiệp hóa, hiện đại hóa đất nước' đã đề ra các nhiệm vụ trọng tâm nào? Trách nhiệm của sinh viên đối với sự phát triển của giai cấp công nhân?",
            "solution_steps": [
                "Bước 1: Các nhiệm vụ, giải pháp trọng tâm của Đảng\n- Nâng cao bản lĩnh chính trị, giác ngộ giai cấp và tinh thần dân tộc cho giai cấp công nhân.\n- Đổi mới, nâng cao chất lượng giáo dục nghề nghiệp, đào tạo lại để công nhân tiếp cận công nghệ cao, nâng cao năng suất và khả năng cạnh tranh.\n- Chăm lo đời sống vật chất, văn hóa tinh thần, cải thiện điều kiện làm việc, an toàn lao động, nhà ở xã hội và chính sách tiền lương thỏa đáng.\n- Đổi mới nội dung, phương thức hoạt động của Công đoàn; phát triển tổ chức Đảng và đoàn thể vững mạnh trong mọi thành phần kinh tế, nhất là doanh nghiệp tư nhân và FDI.",
                "Bước 2: Trách nhiệm của sinh viên\n- Sinh viên là trí thức tương lai, bộ phận gắn bó khăng khít với giai cấp công nhân.\n- Tích cực rèn luyện đạo đức, chuyên môn, kỹ năng mềm và tác phong công nghiệp.\n- Chủ động nghiên cứu khoa học, đổi mới sáng tạo, làm chủ các công nghệ mới (AI, dữ liệu lớn, tự động hóa) để sẵn sàng cống hiến vào sự nghiệp phát triển của đất nước."
            ]
        }
    ]
}
