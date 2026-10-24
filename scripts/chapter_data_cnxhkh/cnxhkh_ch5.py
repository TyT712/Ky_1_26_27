# -*- coding: utf-8 -*-
"""Chapter 5 Exercises: Cơ cấu xã hội - giai cấp và liên minh giai cấp, tầng lớp"""

DATA = {
    "chapter_id": "chuong_5",
    "chapter_title": "Chương 5: Cơ cấu xã hội - giai cấp và liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên chủ nghĩa xã hội",
    "multiple_choice": [
        {
            "id": 1,
            "difficulty": "easy",
            "question": "Hệ thống các giai cấp, tầng lớp xã hội tồn tại khách quan trong một chế độ xã hội nhất định cùng các mối quan hệ giữa chúng được gọi là:",
            "options": {
                "A": "Cơ cấu xã hội - dân số",
                "B": "Cơ cấu xã hội - giai cấp",
                "C": "Cơ cấu xã hội - nghề nghiệp",
                "D": "Cơ cấu xã hội - tôn giáo"
            },
            "correct_answer": "B",
            "explanation": "Cơ cấu xã hội - giai cấp là hệ thống các giai cấp, tầng lớp xã hội và các mối quan hệ giữa chúng về sở hữu, địa vị chính trị và phân phối của cải."
        },
        {
            "id": 2,
            "difficulty": "easy",
            "question": "Trong hệ thống cơ cấu xã hội, cơ cấu nào giữ vị trí trung tâm, có ý nghĩa quyết định nhất?",
            "options": {
                "A": "Cơ cấu xã hội - dân số",
                "B": "Cơ cấu xã hội - dân tộc",
                "C": "Cơ cấu xã hội - giai cấp",
                "D": "Cơ cấu xã hội - tôn giáo"
            },
            "correct_answer": "C",
            "explanation": "Cơ cấu xã hội - giai cấp giữ vị trí trung tâm chi phối các loại cơ cấu khác vì nó gắn liền trực tiếp với quan hệ sở hữu và phương thức sản xuất."
        },
        {
            "id": 3,
            "difficulty": "easy",
            "question": "Yếu tố nào quy định trực tiếp sự biến đổi của cơ cấu xã hội - giai cấp trong thời kỳ quá độ lên CNXH?",
            "options": {
                "A": "Cơ cấu địa lý hành chính",
                "B": "Sự biến đổi của cơ cấu kinh tế",
                "C": "Số lượng các tôn giáo",
                "D": "Khí hậu thời tiết hàng năm"
            },
            "correct_answer": "B",
            "explanation": "Cơ cấu kinh tế (nền kinh tế nhiều thành phần) quyết định tính đa dạng và xu hướng biến đổi của cơ cấu xã hội - giai cấp."
        },
        {
            "id": 4,
            "difficulty": "easy",
            "question": "Lực lượng nào giữ vai trò lãnh đạo khối liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên CNXH?",
            "options": {
                "A": "Giai cấp nông dân",
                "B": "Giai cấp công nhân (thông qua Đảng Cộng sản)",
                "C": "Đội ngũ doanh nhân",
                "D": "Tầng lớp tiểu thương"
            },
            "correct_answer": "B",
            "explanation": "Giai cấp công nhân là lực lượng lãnh đạo liên minh thông qua đội tiên phong là Đảng Cộng sản."
        },
        {
            "id": 5,
            "difficulty": "easy",
            "question": "Nền tảng chính trị - xã hội của Nhà nước XHCN Việt Nam là khối liên minh giữa giai cấp công nhân với:",
            "options": {
                "A": "Giai cấp nông dân và đội ngũ trí thức",
                "B": "Giai cấp tư sản và địa chủ",
                "C": "Các đảng phái chính trị đối lập",
                "D": "Các nhà đầu tư nước ngoài"
            },
            "correct_answer": "A",
            "explanation": "Hiến pháp Việt Nam khẳng định nền tảng của Nhà nước là liên minh công nhân với nông dân và đội ngũ trí thức."
        },
        {
            "id": 6,
            "difficulty": "easy",
            "question": "Trong các nội dung của liên minh giai cấp, tầng lớp, nội dung nào giữ vai trò cốt lõi, quyết định nhất?",
            "options": {
                "A": "Nội dung chính trị",
                "B": "Nội dung kinh tế",
                "C": "Nội dung văn hóa - xã hội",
                "D": "Nội dung quân sự quốc phòng"
            },
            "correct_answer": "B",
            "explanation": "Liên minh về kinh tế là nội dung quan trọng nhất, giữ vai trò quyết định vì nó bảo đảm lợi ích vật chất thiết thân của các giai cấp, tầng lớp."
        },
        {
            "id": 7,
            "difficulty": "easy",
            "question": "Giai cấp nào chiếm số lượng đông đảo nhất trong dân cư và là lực lượng chiến lược trong phát triển nông nghiệp, nông thôn Việt Nam?",
            "options": {
                "A": "Giai cấp công nhân",
                "B": "Giai cấp nông dân",
                "C": "Đội ngũ trí thức",
                "D": "Đội ngũ doanh nhân"
            },
            "correct_answer": "B",
            "explanation": "Giai cấp nông dân là lực lượng đông đảo nhất, có đóng góp to lớn trong sự nghiệp xây dựng nông thôn mới và bảo đảm an ninh lương thực."
        },
        {
            "id": 8,
            "difficulty": "easy",
            "question": "Đội ngũ nào là lực lượng lao động sáng tạo đặc biệt quan trọng trong tiến trình đẩy mạnh CNH, HĐH và kinh tế tri thức?",
            "options": {
                "A": "Đội ngũ trí thức",
                "B": "Giai cấp địa chủ",
                "C": "Tầng lớp thợ thủ công cá thể",
                "D": "Lao động chưa qua đào tạo"
            },
            "correct_answer": "A",
            "explanation": "Trí thức là lực lượng tinh hoa sáng tạo tri thức, phát triển khoa học công nghệ, giáo dục đào tạo và chuyển đổi số quốc gia."
        },
        {
            "id": 9,
            "difficulty": "easy",
            "question": "Lực lượng nào đang phát triển nhanh chóng và được xác định là rường cột phát triển kinh tế, giải quyết việc làm trong thời kỳ đổi mới?",
            "options": {
                "A": "Đội ngũ doanh nhân",
                "B": "Giai cấp phong kiến",
                "C": "Tầng lớp thương nhân độc quyền",
                "D": "Lực lượng lao động tự do"
            },
            "correct_answer": "A",
            "explanation": "Đội ngũ doanh nhân đóng vai trò nòng cốt trong quản trị doanh nghiệp, đầu tư kinh doanh và hội nhập kinh tế quốc tế."
        },
        {
            "id": 10,
            "difficulty": "easy",
            "question": "Xu hướng biến đổi tiến bộ của cơ cấu xã hội - giai cấp dưới sự định hướng của Đảng Cộng sản là:",
            "options": {
                "A": "Khoét sâu mâu thuẫn đối kháng giai cấp",
                "B": "Các giai cấp, tầng lớp từng bước xích lại gần nhau về lợi ích căn bản và bình đẳng xã hội",
                "C": "Tái lập chế độ phong kiến cát cứ",
                "D": "Đồng nhất hóa hoàn toàn mọi cá nhân"
            },
            "correct_answer": "B",
            "explanation": "Định hướng XHCN thúc đẩy sự hòa hợp, xích lại gần nhau về cơ hội phát triển, thu hẹp khoảng cách giàu nghèo và thành thị - nông thôn."
        },
        {
            "id": 11,
            "difficulty": "medium",
            "question": "Vì sao sự tồn tại của nền kinh tế nhiều thành phần lại dẫn đến sự đa dạng, phức tạp của cơ cấu xã hội - giai cấp?",
            "options": {
                "A": "Vì nhà nước chia đất đai cho nhiều nước khác nhau",
                "B": "Vì mỗi thành phần kinh tế dựa trên một hình thức sở hữu nhất định, sinh ra các giai cấp, tầng lớp xã hội tương ứng với lợi ích khác nhau",
                "C": "Do dân số tăng quá nhanh",
                "D": "Do các biến đổi khí hậu toàn cầu"
            },
            "correct_answer": "B",
            "explanation": "Cơ sở kinh tế quyết định kiến trúc xã hội; sở hữu nhà nước, tập thể, tư nhân sinh ra công nhân, nông dân, doanh nhân, trí thức và lao động tư nhân."
        },
        {
            "id": 12,
            "difficulty": "medium",
            "question": "Nội dung chính trị của khối liên minh giai cấp, tầng lớp ở Việt Nam nhằm mục đích gì?",
            "options": {
                "A": "Thực hiện chế độ đa đảng đối lập",
                "B": "Giữ vững vai trò lãnh đạo tuyệt đối của Đảng Cộng sản Việt Nam, củng cố chế độ chính trị và bảo vệ vững chắc độc lập chủ quyền Tổ quốc",
                "C": "Loại bỏ vai trò của Quốc hội",
                "D": "Giải tán các đoàn thể chính trị - xã hội"
            },
            "correct_answer": "B",
            "explanation": "Liên minh chính trị tạo nên sự thống nhất ý chí và hành động của cả dân tộc, bảo vệ thành quả cách mạng và an ninh quốc gia."
        },
        {
            "id": 13,
            "difficulty": "medium",
            "question": "Nội dung kinh tế của liên minh công - nông - trí thức ở nước ta được cụ thể hóa bằng hoạt động nào?",
            "options": {
                "A": "Cấm buôn bán nông sản ra thành thị",
                "B": "Gắn kết chặt chẽ công nghiệp chế biến, chuyển giao tiến bộ khoa học kỹ thuật với sản xuất nông nghiệp và tiêu thụ sản phẩm theo chuỗi giá trị",
                "C": "Thu hồi toàn bộ ruộng đất không bồi thường",
                "D": "Bao cấp 100% chi phí sinh hoạt cho mọi công dân"
            },
            "correct_answer": "B",
            "explanation": "Công nhân cung cấp vật tư máy móc; trí thức chuyển giao công nghệ giống, phân bón; nông dân sản xuất nông sản chất lượng cao."
        },
        {
            "id": 14,
            "difficulty": "medium",
            "question": "Thách thức lớn nhất đối với giai cấp nông dân Việt Nam trong quá trình công nghiệp hóa, đô thị hóa hiện nay là:",
            "options": {
                "A": "Diện tích đất nông nghiệp bị thu hẹp, đòi hỏi phải chuyển đổi nghề nghiệp và nâng cao tay nghề để tránh rơi vào cảnh thất nghiệp",
                "B": "Không có thị trường xuất khẩu gạo",
                "C": "Giá nông sản luôn quá cao",
                "D": "Không có máy móc hiện đại nào hỗ trợ"
            },
            "correct_answer": "A",
            "explanation": "Quá trình đô thị hóa thu hồi đất nông nghiệp đặt ra bài toán đào tạo nghề, tạo sinh kế bền vững và nâng cao chất lượng lao động nông thôn."
        },
        {
            "id": 15,
            "difficulty": "medium",
            "question": "Nội dung văn hóa - xã hội của khối liên minh giai cấp, tầng lớp đòi hỏi phải thực hiện tốt điều gì?",
            "options": {
                "A": "Chỉ tập trung xây dựng các rạp chiếu phim ở thành phố lớn",
                "B": "Xây dựng lối sống văn hóa mới, nâng cao dân trí, phát triển y tế giáo dục, giảm nghèo bền vững và bảo đảm an sinh xã hội cho nhân dân",
                "C": "Nhập khẩu toàn bộ các trào lưu âm nhạc ngoại lai",
                "D": "Xóa bỏ các lễ hội truyền thống dân gian"
            },
            "correct_answer": "B",
            "explanation": "Bảo đảm mọi người dân ở thành thị và nông thôn đều được tiếp cận công bằng các dịch vụ y tế, giáo dục, văn hóa cơ bản."
        },
        {
            "id": 16,
            "difficulty": "medium",
            "question": "Để củng cố khối liên minh công - nông - trí thức về mặt kinh tế, nguyên tắc căn bản nhất cần quán triệt là:",
            "options": {
                "A": "Chỉ bảo vệ lợi ích của công nhân nhà máy",
                "B": "Kết hợp hài hòa giữa lợi ích cá nhân, lợi ích tập thể và lợi ích toàn xã hội",
                "C": "Ưu tiên tuyệt đối lợi ích của doanh nghiệp nước ngoài",
                "D": "Triệt tiêu mọi lợi ích kinh tế cá nhân"
            },
            "correct_answer": "B",
            "explanation": "Lợi ích kinh tế là động lực trực tiếp; kết hợp hài hòa lợi ích mới tạo động lực gắn kết tự nguyện, bền chặt giữa các lực lượng."
        },
        {
            "id": 17,
            "difficulty": "medium",
            "question": "Trong sự nghiệp đổi mới ở Việt Nam, đội ngũ trí thức có vai trò nổi bật nào?",
            "options": {
                "A": "Trực tiếp khai thác mỏ than",
                "B": "Cung cấp luận cứ khoa học cho việc hoạch định đường lối, chính sách của Đảng và làm nòng cốt trong nghiên cứu, ứng dụng KH-CN",
                "C": "Quản lý toàn bộ hệ thống bán lẻ vỉa hè",
                "D": "Chỉ làm nhiệm vụ dịch thuật sách báo nước ngoài"
            },
            "correct_answer": "B",
            "explanation": "Trí thức đóng góp sáng kiến chiến lược, tham mưu chính sách và trực tiếp tạo ra các phát minh, công nghệ phục vụ sản xuất."
        },
        {
            "id": 18,
            "difficulty": "medium",
            "question": "Tầng lớp doanh nhân Việt Nam có vị trí như thế nào trong cơ cấu xã hội hiện nay?",
            "options": {
                "A": "Bị coi là đối tượng bóc lột cần phải xóa bỏ",
                "B": "Là lực lượng nòng cốt phát triển kinh tế, tạo ra của cải vật chất, giải quyết việc làm và nâng cao vị thế kinh tế quốc gia",
                "C": "Chỉ hoạt động trong lĩnh vực tài chính phi chính thức",
                "D": "Không có quyền tham gia các tổ chức chính trị - xã hội"
            },
            "correct_answer": "B",
            "explanation": "Đảng và Nhà nước tôn vinh, khuyến khích xây dựng đội ngũ doanh nhân có tinh thần dân tộc, trách nhiệm xã hội và văn hóa kinh doanh lành mạnh."
        },
        {
            "id": 19,
            "difficulty": "medium",
            "question": "Khái niệm 'Liên minh giai cấp' theo quan điểm Mác - Lênin là sự liên kết giữa các giai cấp dựa trên:",
            "options": {
                "A": "Sự ép buộc hành chính của nhà nước",
                "B": "Sự thống nhất về những lợi ích cơ bản về kinh tế và chính trị trong một giai đoạn cách mạng nhất định",
                "C": "Các thỏa ước ngầm của các thủ lĩnh phe nhóm",
                "D": "Ngẫu nhiên nhất thời không có quy luật"
            },
            "correct_answer": "B",
            "explanation": "Sự thống nhất về lợi ích cơ bản (độc lập dân tộc, tự do, hạnh phúc, cùng xây dựng xã hội công bằng) là nền tảng khách quan của liên minh."
        },
        {
            "id": 20,
            "difficulty": "medium",
            "question": "Nghị quyết của Đảng về công tác phụ nữ khẳng định phụ nữ Việt Nam có vai trò như thế nào?",
            "options": {
                "A": "Chỉ có vai trò nội trợ gia đình",
                "B": "Là lực lượng quan trọng trong sự nghiệp đổi mới, vừa giữ gìn hạnh phúc gia đình vừa đóng góp to lớn trên mọi lĩnh vực chính trị, kinh tế, xã hội",
                "C": "Không được tham gia lãnh đạo cơ quan nhà nước",
                "D": "Không thuộc cơ cấu xã hội"
            },
            "correct_answer": "B",
            "explanation": "Phụ nữ chiếm hơn một nửa dân số, phát huy truyền thống 'Anh hùng, bất khuất, trung hậu, đảm đang' trong thời đại mới."
        },
        {
            "id": 21,
            "difficulty": "hard",
            "question": "V.I.Lênin nhấn mạnh: 'Nguyên tắc cao nhất của chuyên chính vô sản là duy trì khối liên minh giữa giai cấp vô sản và nông dân' nhằm mục đích sâu xa gì?",
            "options": {
                "A": "Để giai cấp vô sản có thể giữ vững được vai trò lãnh đạo và chính quyền nhà nước trước sự bao vây của các thế lực thù địch",
                "B": "Để tăng sản lượng lúa mì cho thủ đô Mát-xcơ-va",
                "C": "Để chia nhỏ các trang trại nông nghiệp",
                "D": "Để loại trừ tầng lớp trí thức khỏi bộ máy"
            },
            "correct_answer": "A",
            "explanation": "Nếu giai cấp vô sản cô độc, không liên minh được với nông dân (lực lượng chiếm đa số dân số), chuyên chính vô sản tất yếu sẽ sụp đổ."
        },
        {
            "id": 22,
            "difficulty": "hard",
            "question": "Điểm mới trong nhận thức của Đảng ta về cơ cấu xã hội - giai cấp trong nền kinh tế thị trường định hướng XHCN là gì?",
            "options": {
                "A": "Xem các giai cấp tư nhân là kẻ thù đối kháng cần tiêu diệt",
                "B": "Thừa nhận sự tồn tại khách quan của nhiều giai cấp, tầng lớp xã hội; coi các giai cấp, tầng lớp này đều là thành viên bình đẳng trong khối đại đoàn kết toàn dân tộc",
                "C": "Không còn phân biệt giai cấp công nhân và nông dân",
                "D": "Khuyến khích phân hóa giàu nghèo ngày càng gay gắt"
            },
            "correct_answer": "B",
            "explanation": "Từ bỏ tư duy đấu tranh giai cấp đối kháng cực đoan trong nội bộ nhân dân; tập hợp mọi người Việt Nam yêu nước vào mặt trận chung vì dân giàu nước mạnh."
        },
        {
            "id": 23,
            "difficulty": "hard",
            "question": "Hiện tượng nào sau đây phản ánh mặt tiêu cực cần phòng tránh trong sự biến đổi của cơ cấu xã hội - giai cấp ở nước ta hiện nay?",
            "options": {
                "A": "Số lượng công nhân có trình độ đại học tăng lên",
                "B": "Sự phân hóa giàu nghèo quá mức và bất bình đẳng cơ hội phát triển giữa các vùng miền, nhóm dân cư",
                "C": "Nhiều doanh nhân tham gia đóng góp quỹ khuyến học",
                "D": "Nông dân áp dụng nông nghiệp công nghệ cao"
            },
            "correct_answer": "B",
            "explanation": "Khoảng cách phân hóa giàu nghèo quá mức đe dọa làm suy yếu khối liên minh giai cấp và làm tổn hại tính ưu việt của chế độ XHCN."
        },
        {
            "id": 24,
            "difficulty": "hard",
            "question": "Tại sao trong nội dung liên minh kinh tế, Đảng ta đặc biệt chú trọng mô hình 'Tam nông' (Nông nghiệp, Nông dân, Nông thôn)?",
            "options": {
                "A": "Vì ngân sách nhà nước chỉ đầu tư cho khu vực nông thôn",
                "B": "Vì nông dân chiếm số đông, nông thôn là địa bàn chiến lược về quốc phòng an ninh và an ninh lương thực; phát triển nông thôn giúp bảo đảm nền tảng vững chắc cho CNH, HĐH",
                "C": "Vì các nước tư bản từ chối mua nông sản Việt Nam",
                "D": "Vì không muốn nông dân chuyển về các thành phố lớn"
            },
            "correct_answer": "B",
            "explanation": "Nông nghiệp là trụ đỡ của nền kinh tế quốc gia, nông dân là chủ thể, nông thôn là địa bàn ổn định xã hội."
        },
        {
            "id": 25,
            "difficulty": "hard",
            "question": "Mối quan hệ biện chứng giữa 'sự thống nhất' và 'sự khác biệt' trong lợi ích giữa các giai cấp, tầng lớp trong thời kỳ quá độ được giải quyết theo nguyên tắc nào?",
            "options": {
                "A": "Tuyệt đối hóa sự khác biệt để tiến hành đấu tranh thanh trừng giai cấp",
                "B": "Thừa nhận sự khác biệt về lợi ích cụ thể, cục bộ nhưng đặt lợi ích quốc gia - dân tộc và mục tiêu XHCN lên trên hết để tìm kiếm sự đồng thuận, hợp tác",
                "C": "Bắt buộc mọi người phải từ bỏ thu nhập chính đáng",
                "D": "Phó mặc cho thị trường tự do điều tiết mà nhà nước không can thiệp"
            },
            "correct_answer": "B",
            "explanation": "Lấy mục tiêu chung 'Dân giàu, nước mạnh, dân chủ, công bằng, văn minh' làm mẫu số chung để dung hòa và giải quyết hài hòa các lợi ích khác biệt."
        },
        {
            "id": 26,
            "difficulty": "hard",
            "question": "Yếu tố nào đóng vai trò là 'chất keo kết dính' bền chặt khối liên minh công - nông - trí thức và các tầng lớp nhân dân ở Việt Nam?",
            "options": {
                "A": "Lòng căm thù ngoại bang trong quá khứ",
                "B": "Lợi ích kinh tế hài hòa, mục tiêu độc lập dân tộc gắn liền với CNXH và sự lãnh đạo sáng suốt của Đảng Cộng sản Việt Nam",
                "C": "Nguồn viện trợ kinh tế từ nước ngoài",
                "D": "Sự kiểm soát nghiêm ngặt của lực lượng công an"
            },
            "correct_answer": "B",
            "explanation": "Sự gắn kết hữu cơ giữa lợi ích thiết thực hàng ngày với lý tưởng chính trị chung tạo nên sức mạnh bất hoại của khối đại đoàn kết."
        },
        {
            "id": 27,
            "difficulty": "hard",
            "question": "Thế hệ trẻ (thanh niên, sinh viên) có vị trí chiến lược như thế nào trong cơ cấu xã hội Việt Nam thời kỳ đổi mới?",
            "options": {
                "A": "Là lực lượng thụ hưởng thành quả mà không cần có nghĩa vụ gì",
                "B": "Là rường cột của nước nhà, chủ nhân tương lai của đất nước, lực lượng xung kích trong học tập, nghiên cứu khoa học, đổi mới sáng tạo và bảo vệ Tổ quốc",
                "C": "Chỉ là người quan sát sự biến đổi xã hội",
                "D": "Lực lượng dự bị không quan trọng"
            },
            "correct_answer": "B",
            "explanation": "Đảng coi thanh niên là rường cột quốc gia; đầu tư cho thanh niên là đầu tư cho tương lai phát triển bền vững của chế độ."
        },
        {
            "id": 28,
            "difficulty": "hard",
            "question": "Để củng cố khối liên minh công - nông - trí thức trong bối cảnh cuộc Cách mạng công nghiệp lần thứ tư, khâu đột phá cần thực hiện là:",
            "options": {
                "A": "Ngừng sử dụng internet ở khu vực nông thôn",
                "B": "Đẩy mạnh chuyển đổi số nông nghiệp, đào tạo kỹ năng số cho nông dân và thúc đẩy thương mại điện tử kết nối chuỗi cung ứng nông - công nghiệp",
                "C": "Khuyến khích nông dân quay lại dùng cày gỗ và trâu",
                "D": "Chỉ hỗ trợ vốn cho các doanh nghiệp xuất khẩu lớn"
            },
            "correct_answer": "B",
            "explanation": "Chuyển đổi số nông nghiệp là cầu nối đưa tri thức công nghệ cao vào đồng ruộng, nâng tầm giá trị nông sản và cải thiện đời sống nông dân."
        },
        {
            "id": 29,
            "difficulty": "hard",
            "question": "Nguyên nhân chính khiến cơ cấu xã hội - giai cấp ở Việt Nam trong thời kỳ quá độ vừa có sự 'hợp tác' vừa có sự 'đấu tranh' là:",
            "options": {
                "A": "Do luật pháp chưa nghiêm minh",
                "B": "Hợp tác vì có chung mục tiêu xây dựng đất nước phồn vinh; đấu tranh để ngăn chặn các biểu hiện làm ăn phi pháp, trốn thuế, bóc lột quá mức và chệch hướng XHCN",
                "C": "Do ảnh hưởng của phong tục truyền thống",
                "D": "Do nhà nước khuyến khích mâu thuẫn"
            },
            "correct_answer": "B",
            "explanation": "Tính biện chứng của thời kỳ quá độ: vừa phát huy tinh thần đoàn kết hợp tác cùng làm giàu, vừa kiên quyết quản lý đấu tranh chống vi phạm pháp luật."
        },
        {
            "id": 30,
            "difficulty": "hard",
            "question": "Trách nhiệm của sinh viên các trường đại học trong việc củng cố khối liên minh công - nông - trí thức là:",
            "options": {
                "A": "Tách mình khỏi quần chúng lao động, tự coi mình là tầng lớp quý tộc tri thức",
                "B": "Tích cực rèn luyện tri thức, tham gia các hoạt động tình nguyện mùa hè xanh, chuyển giao kỹ thuật công nghệ về cơ sở và tôn trọng giá trị của lao động chân tay",
                "C": "Phê phán người nông dân lạc hậu",
                "D": "Chỉ học tập để tìm kiếm thu nhập cá nhân cao nhất"
            },
            "correct_answer": "B",
            "explanation": "Trí thức trẻ phải hòa mình vào thực tiễn đời sống nhân dân lao động, dùng tri thức phục vụ sản xuất và phụng sự nhân dân."
        }
    ],
    "short_answers": [
        {
            "id": 1,
            "question": "Định nghĩa cơ cấu xã hội - giai cấp và nêu vị trí của nó trong hệ thống cơ cấu xã hội.",
            "expected_answer": "- **Định nghĩa:** Là hệ thống các giai cấp, tầng lớp xã hội tồn tại khách quan trong một chế độ xã hội nhất định cùng mối quan hệ giữa chúng về sở hữu TLSX, tổ chức quản lý và phân phối của cải.\n- **Vị trí:** Giữ vị trí trung tâm, chi phối các loại hình cơ cấu xã hội khác (dân số, dân tộc, tôn giáo, nghề nghiệp) vì gắn liền trực tiếp với quan hệ sản xuất.",
            "explanation": "Nắm vững khái niệm cốt lõi của Chương 5."
        },
        {
            "id": 2,
            "question": "Trình bày tính tất yếu của liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên CNXH.",
            "expected_answer": "1. **Về kinh tế:** Xuất phát từ yêu cầu khách quan của nền sản xuất lớn hiện đại gắn kết hữu cơ công nghiệp, nông nghiệp và khoa học - dịch vụ.\n2. **Về chính trị - xã hội:** GCCN muốn giữ vững chính quyền và vai trò lãnh đạo phải tập hợp được đa số nhân dân lao động thành lập khối liên minh vững chắc làm nền tảng chế độ.",
            "explanation": "Luận điểm của V.I.Lênin về tính tất yếu của liên minh công nông."
        },
        {
            "id": 3,
            "question": "Nêu ba nội dung cơ bản của liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên CNXH.",
            "expected_answer": "1. **Nội dung kinh tế (cốt lõi, quan trọng nhất):** Kết hợp hài hòa lợi ích kinh tế, hợp tác sản xuất kinh doanh theo chuỗi giá trị.\n2. **Nội dung chính trị:** Giữ vững sự lãnh đạo của Đảng, bảo vệ an ninh trật tự và độc lập chủ quyền Tổ quốc.\n3. **Nội dung văn hóa - xã hội:** Nâng cao dân trí, phát triển nguồn nhân lực, bảo đảm an sinh xã hội.",
            "explanation": "Ba nội dung gắn bó mật thiết, hỗ trợ lẫn nhau."
        },
        {
            "id": 4,
            "question": "Kể tên các giai cấp, tầng lớp xã hội cơ bản trong cơ cấu xã hội - giai cấp ở Việt Nam hiện nay.",
            "expected_answer": "1. Giai cấp công nhân (lực lượng lãnh đạo).\n2. Giai cấp nông dân (lực lượng đông đảo, chiến lược nông thôn).\n3. Đội ngũ trí thức (lao động sáng tạo đặc biệt quan trọng).\n4. Đội ngũ doanh nhân (lực lượng nòng cốt phát triển kinh tế).\n5. Phụ nữ và thế hệ thanh niên.",
            "explanation": "Cùng chung sức xây dựng và bảo vệ đất nước."
        },
        {
            "id": 5,
            "question": "Tại sao nội dung kinh tế lại là nội dung giữ vai trò quyết định nhất của khối liên minh giai cấp, tầng lớp?",
            "expected_answer": "Vì lợi ích kinh tế là động lực trực tiếp và thiết thân nhất thúc đẩy các giai cấp, tầng lớp tham gia vào liên minh. Nếu không bảo đảm được lợi ích kinh tế (nâng cao thu nhập, ổn định đời sống), liên minh sẽ chỉ mang tính hình thức, khẩu hiệu và không thể bền vững.",
            "explanation": "Vấn đề kinh tế là nền tảng của mọi mối quan hệ xã hội."
        },
        {
            "id": 6,
            "question": "Chỉ ra 2 đóng góp nổi bật của đội ngũ doanh nhân Việt Nam trong công cuộc Đổi mới.",
            "expected_answer": "1. Đóng góp to lớn vào tăng trưởng GDP, thu ngân sách nhà nước, tạo công ăn việc làm và thu nhập cho hàng triệu lao động.\n2. Đi đầu trong đổi mới sáng tạo, phát triển công nghệ, xây dựng thương hiệu quốc gia và đưa hàng hóa Việt Nam vươn ra thị trường toàn cầu.",
            "explanation": "Được Đảng và Nhà nước ghi nhận qua Ngày Doanh nhân Việt Nam (13/10)."
        },
        {
            "id": 7,
            "question": "Nêu 2 giải pháp nhằm củng cố liên minh công - nông - trí thức trên lĩnh vực nông nghiệp, nông thôn Việt Nam hiện nay.",
            "expected_answer": "1. Đẩy mạnh chuyển giao khoa học công nghệ, giống cây trồng, vật nuôi tiên tiến và kỹ thuật số cho nông dân.\n2. Xây dựng chuỗi liên kết '4 nhà' (Nhà nước - Nhà nông - Nhà khoa học - Doanh nghiệp) trong sản xuất, chế biến và bao tiêu nông sản.",
            "explanation": "Nâng cao năng suất và giá trị kinh tế cho nông sản Việt Nam."
        },
        {
            "id": 8,
            "question": "Thanh niên, sinh viên cần làm gì để phát huy vai trò trong khối đại đoàn kết toàn dân tộc?",
            "expected_answer": "Chủ động học tập nâng cao trình độ chuyên môn, làm chủ công nghệ mới, rèn luyện tác phong công nghiệp và tinh thần yêu nước; tích cực tham gia các phong trào tình nguyện, vì cộng đồng và sẵn sàng cống hiến xây dựng quê hương.",
            "explanation": "Phát huy tinh thần xung kích của tuổi trẻ."
        }
    ],
    "essays": [
        {
            "id": 1,
            "title": "Phân tích Tính Tất Yếu và Các Nội Dung Cơ Bản của Khối Liên Minh Giai Cấp, Tầng Lớp",
            "problem": "Hãy phân tích:\n1. Tính tất yếu khách quan của khối liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên CNXH (về kinh tế và về chính trị).\n2. Nội dung kinh tế, chính trị và văn hóa - xã hội của liên minh.\n3. Vì sao nói nội dung kinh tế giữ vai trò quyết định nhất?",
            "solution_steps": [
                "Bước 1: Tính tất yếu của khối liên minh\n- **Về kinh tế:** Xuất phát từ quy luật khách quan của nền sản xuất lớn hiện đại. Công nghiệp (công nhân) không thể phát triển nếu thiếu nguyên liệu, lương thực và thị trường rộng lớn từ nông nghiệp (nông dân); ngược lại nông nghiệp không thể cơ giới hóa nếu thiếu máy móc công nghiệp và tiến bộ khoa học công nghệ (trí thức).\n- **Về chính trị - xã hội:** GCCN là giai cấp lãnh đạo nhưng chiếm tỷ số không lớn trong toàn bộ dân số ở các nước nông nghiệp; muốn đánh bại kẻ thù và bảo vệ chính quyền nhà nước XHCN, bắt buộc phải liên minh với nông dân và trí thức để tạo nên lực lượng đa số áp đảo.",
                "Bước 2: Nội dung của liên minh\n- **Kinh tế:** Xác định cơ cấu kinh tế hợp lý; kết hợp hài hòa lợi ích giữa các bên; chuyển giao công nghệ, mở rộng thị trường và xây dựng nông thôn mới.\n- **Chính trị:** Giữ vững sự lãnh đạo của Đảng; xây dựng Nhà nước pháp quyền XHCN; bảo vệ quyền làm chủ của nhân dân và độc lập chủ quyền quốc gia.\n- **Văn hóa - xã hội:** Nâng cao dân trí, phát triển y tế giáo dục, xây dựng nếp sống văn minh và thực hiện an sinh xã hội, giảm nghèo bền vững.",
                "Bước 3: Vì sao nội dung kinh tế giữ vai trò quyết định?\n- Lợi ích kinh tế là cơ sở vật chất bảo đảm đời sống hàng ngày của người lao động. Nếu kinh tế không phát triển, đời sống người dân khó khăn thì mọi khẩu hiệu chính trị đều trở nên sáo rỗng. Khi kinh tế gắn bó chặt chẽ, các giai cấp thấy rõ lợi ích gắn bó thì liên minh chính trị mới thực sự vững như bàn thạch."
            ]
        },
        {
            "id": 2,
            "title": "Đặc Điểm Cơ Cấu Xã Hội - Giai Cấp ở Việt Nam Trong Thời Kỳ Quá Độ",
            "problem": "Trình bày những biến đổi cơ bản và đặc điểm của cơ cấu xã hội - giai cấp ở Việt Nam trong giai đoạn phát triển kinh tế thị trường định hướng XHCN hiện nay. Phân tích vai trò của giai cấp công nhân, nông dân, trí thức và doanh nhân.",
            "solution_steps": [
                "Bước 1: Đặc điểm tổng quát của cơ cấu xã hội - giai cấp ở Việt Nam\n- Mang tính đa dạng và đan xen phức tạp do sự tồn tại của nền kinh tế nhiều thành phần.\n- Vừa có sự hợp tác gắn bó, vừa có sự khác biệt về lợi ích cục bộ nhưng có xu hướng từng bước xích lại gần nhau dưới sự lãnh đạo của Đảng Cộng sản.\n- Cơ cấu giai cấp vận động theo hướng tích cực: tỷ lệ lao động công nghiệp và dịch vụ tăng, tỷ lệ lao động nông nghiệp giản đơn giảm.",
                "Bước 2: Vai trò của các giai cấp, tầng lớp nòng cốt\n- **Giai cấp công nhân:** Giữ vai trò lãnh đạo cách mạng thông qua Đảng; là lực lượng tiên phong trong sự nghiệp công nghiệp hóa, hiện đại hóa đất nước.\n- **Giai cấp nông dân:** Lực lượng đông đảo nhất, giữ vị trí chiến lược trong bảo đảm an ninh lương thực quốc gia, phát triển kinh tế nông nghiệp và giữ gìn văn hóa truyền thống nông thôn.\n- **Đội ngũ trí thức:** Lực lượng lao động sáng tạo đặc biệt quan trọng, dẫn dắt đổi mới sáng tạo, phát triển kinh tế tri thức và đào tạo nguồn nhân lực chất lượng cao.\n- **Đội ngũ doanh nhân:** Là động lực quan trọng thúc đẩy kinh tế phát triển, đầu tư kinh doanh, giải quyết việc làm và nâng cao năng lực cạnh tranh quốc gia.",
                "Bước 3: Kết luận\n- Sự phối hợp nhịp nhàng giữa các giai cấp, tầng lớp tạo thành sức mạnh tổng hợp của khối đại đoàn kết toàn dân tộc dưới sự lãnh đạo của Đảng."
            ]
        },
        {
            "id": 3,
            "title": "Phương Hướng và Giải Pháp Tăng Cường Khối Liên Minh Công - Nông - Trí Thức ở Việt Nam",
            "problem": "Đại hội XIII của Đảng đã đề ra những phương hướng, giải pháp chủ yếu nào nhằm củng cố và phát huy sức mạnh của khối liên minh giai cấp công nhân với giai cấp nông dân và đội ngũ trí thức trong giai đoạn mới?",
            "solution_steps": [
                "Bước 1: Đẩy mạnh phát triển kinh tế và hài hòa lợi ích\n- Tiếp tục hoàn thiện thể chế kinh tế thị trường định hướng XHCN, khuyến khích liên kết '4 nhà' (Nhà nước, Nhà nông, Nhà khoa học, Doanh nghiệp).\n- Đầu tư thỏa đáng cho phát triển nông nghiệp sinh thái, nông thôn hiện đại, nông dân văn minh ('Tam nông'); thu hẹp khoảng cách giàu nghèo giữa thành thị và nông thôn.",
                "Bước 2: Nâng cao chất lượng nguồn nhân lực và đời sống văn hóa\n- Đổi mới căn bản giáo dục và đào tạo; đẩy mạnh đào tạo nghề cho nông dân bị thu hồi đất; phổ cập giáo dục kỹ năng số cho công nhân và người lao động.\n- Xây dựng thiết chế văn hóa, nhà ở xã hội cho công nhân khu công nghiệp; chăm lo y tế, bảo hiểm xã hội và an sinh cho người yếu thế.",
                "Bước 3: Tăng cường sự lãnh đạo của Đảng và quản lý của Nhà nước\n- Giữ vững vai trò lãnh đạo tuyệt đối của Đảng đối với khối liên minh; đổi mới phương thức hoạt động của Mặt trận Tổ quốc và các đoàn thể chính trị - xã hội.\n- Kịp thời phát hiện và giải quyết thỏa đáng các mâu thuẫn lợi ích nảy sinh trong xã hội; đấu tranh kiên quyết chống tham nhũng, lãng phí và lợi ích nhóm.",
                "Bước 4: Nêu cao tinh thần cảnh giác cách mạng\n- Đấu tranh làm thất bại mọi âm mưu chia rẽ giai cấp, kích động khiếu kiện đông người của các thế lực thù địch nhằm phá hoại khối đại đoàn kết toàn dân tộc."
            ]
        },
        {
            "id": 4,
            "title": "Vai Trò Của Trí Thức và Trách Nhiệm Của Sinh Viên Trong Khối Liên Minh Giai Cấp",
            "problem": "Tại sao trong kỷ nguyên kinh tế số và cách mạng công nghiệp 4.0, vai trò của đội ngũ trí thức lại càng trở nên đặc biệt quan trọng? Sinh viên cần chuẩn bị hành trang gì để trở thành những trí thức cách mạng chân chính?",
            "solution_steps": [
                "Bước 1: Vai trò đặc biệt quan trọng của trí thức trong thời đại mới\n- Tri thức khoa học và công nghệ đã trở thành lực lượng sản xuất trực tiếp có sức mạnh đột phá hàng đầu.\n- Đội ngũ trí thức trực tiếp nghiên cứu, sáng tạo ra các công nghệ lõi (trí tuệ nhân tạo, bán dẫn, sinh học, năng lượng xanh), quyết định vị thế cạnh tranh của quốc gia trên trường quốc tế.\n- Trí thức đóng vai trò tham mưu chính sách, cung cấp cơ sở khoa học để Đảng và Nhà nước ban hành các quyết sách phát triển đúng đắn, kịp thời.",
                "Bước 2: Mối quan hệ giữa trí thức với công nhân và nông dân\n- Trí thức không phải là giai cấp độc lập mà là một tầng lớp xã hội gắn bó mật thiết với công nhân và nông dân. Mọi phát minh khoa học của trí thức chỉ phát huy giá trị khi được công nhân vận hành trong nhà máy và nông dân ứng dụng trên đồng ruộng.",
                "Bước 3: Trách nhiệm và hành trang của sinh viên hôm nay\n- **Về chuyên môn:** Nỗ lực học tập xuất sắc, làm chủ tri thức chuyên ngành, thành thạo ngoại ngữ và công nghệ số.\n- **Về lý tưởng:** Giữ vững bản lĩnh chính trị, kiên định lý tưởng độc lập dân tộc gắn liền với CNXH, không dao động trước các cám dỗ vật chất hay luận điệu xấu độc.\n- **Về đạo đức và thực tiễn:** Rèn luyện phẩm chất 'Vừa hồng vừa chuyên' theo lời dạy của Bác Hồ; tích cực tham gia các hoạt động nghiên cứu khoa học phục vụ cộng đồng, sẵn sàng cống hiến cho sự phồn vinh của Tổ quốc."
            ]
        }
    ]
}
