## Nội dung slide và script đã rút gọn

### Slide 1 — Phân tích và dự báo nhu cầu thuê xe đạp tại Seoul

**Trên slide**

**Phân tích và dự báo nhu cầu sử dụng dịch vụ chia sẻ xe đạp tại Seoul**

Nhóm 26 — Trường Đại học Công nghệ Thông tin

Bạch Thế Hiển · Nguyễn Thái Hòa · Đặng Quang Lợi

_Mục tiêu: nhận diện nhu cầu và dự đoán số lượt thuê theo giờ._

**Bố cục:** bìa tối giản. Mục tiêu là một dòng nhỏ dưới tên đề tài.

**Script — 35 giây**

“Kính chào thầy cô. Nhóm 26 xin trình bày đồ án Phân tích và dự báo nhu cầu sử dụng dịch vụ chia sẻ xe đạp tại Seoul. Mục tiêu của nhóm là nhận diện thời điểm nhu cầu cao và kiểm tra khả năng dự đoán số lượt thuê trong một giờ từ lịch và thời tiết. Trong khoảng 8 phút, nhóm sẽ trình bày dữ liệu, các phát hiện chính và kết quả mô hình, từ đó đánh giá khả năng hỗ trợ lập kế hoạch cung ứng xe.”

### Slide 2 — Dữ liệu và phân phối nhu cầu

**Trên slide**

- **UCI Seoul Bike Sharing Demand**, 01/12/2017–30/11/2018.
- **8.760 dòng, 14 cột**; phân tích **8.465 giờ hệ thống hoạt động**.
- Trung bình **729 lượt/giờ**, trung vị **542 lượt/giờ**.
- Nhu cầu lệch phải; giữ các giờ cao điểm hợp lệ.

**Hình chính:** histogram từ `../bao-cao/figures/4-1-histogram-phan-phoi-so-luot-thue-xe.png`. Khi dựng slide, làm rõ vị trí trung bình và trung vị. Thông tin dữ liệu đặt thành dòng ngắn phía trên biểu đồ.

**Script — 60 giây**

“Nhóm sử dụng bộ Seoul Bike Sharing Demand từ UCI. Dữ liệu có 8.760 dòng, tương ứng các giờ trong một năm, cùng 14 cột về số lượt thuê, lịch và thời tiết. Nhóm lọc bỏ 295 giờ hệ thống ngừng hoạt động, giữ lại 8.465 giờ để phân tích. Sau lọc, dữ liệu không có giá trị thiếu hay cặp ngày và giờ trùng nhau. Histogram cho thấy nhu cầu lệch phải: trung bình khoảng 729 lượt mỗi giờ, cao hơn trung vị 542 lượt. Một số giờ có lượng thuê lớn kéo trung bình lên. Nhóm giữ những giờ cao điểm hợp lệ, vì đây là tình huống cần mô hình dự đoán tốt. Phạm vi bài toán là nhu cầu tổng hợp theo giờ, chưa phải số xe cần bố trí tại từng trạm.”

**Ghi chú:** số chính xác của trung bình là 729,16 lượt/giờ. IQR = 870, Q1 = 214, Q3 = 1.084, dùng khi có câu hỏi, không cần đọc trong bài chính.

### Slide 3 — Nhu cầu theo giờ và mùa

**Trên slide**

- **18:00** có nhu cầu trung bình cao nhất: **1.554 lượt/giờ**.
- Mùa Hạ: **1.034 lượt/giờ**; mùa Đông: **226 lượt/giờ**.
- Trung bình giữa các mùa khác biệt: **ANOVA, p < 0,001**.

_Kiểm định mang tính thăm dò do các quan sát theo giờ có thể phụ thuộc nhau._

**Hình chính:** đường xu hướng theo giờ và mùa tại `../bao-cao/figures/4-3-duong-xu-huong-trung-binh-theo-gio-va-mua.png`. Ghi chú nổi bật ở 18:00, kèm hai số trung bình mùa bên cạnh.

**Script — 65 giây**

“Theo giờ trong ngày, nhu cầu trung bình đạt đỉnh lúc 18 giờ, khoảng 1.554 lượt mỗi giờ. Lúc 8 giờ sáng, nhu cầu trung bình khoảng 1.050 lượt mỗi giờ. Các mốc này gợi ý cần chú ý giờ cao điểm khi lập kế hoạch cung ứng. Theo mùa, mùa Hạ có trung bình khoảng 1.034 lượt mỗi giờ, còn mùa Đông khoảng 226 lượt. Nhóm dùng ANOVA để kiểm tra trung bình giữa bốn mùa. Kết quả p nhỏ hơn 0,001 cung cấp bằng chứng về khác biệt tổng thể, nhưng chưa xác định từng cặp mùa khác nhau như thế nào. Vì dữ liệu ghi liên tiếp theo giờ và có thể phụ thuộc nhau, nhóm xem kiểm định là bằng chứng thăm dò. Khác biệt theo mùa cũng đi kèm thay đổi thời tiết, nên chưa thể quy toàn bộ chênh lệch cho một yếu tố riêng.”

**Ghi chú:** số chưa làm tròn: 18:00 = 1.554,02; mùa Hạ = 1.034,07; mùa Đông = 225,54 lượt/giờ. ANOVA: F = 875,60. Không cần đọc F hoặc trình bày công thức trong bài chính.

### Slide 4 — Mối liên hệ với thời tiết

**Trên slide**

- Nhiệt độ: **r = 0,563**, tương quan dương mức vừa.
- Độ ẩm: **r = −0,202**, tương quan âm yếu.
- Lượng mưa: **r = −0,129**, tương quan âm yếu.

_Tương quan chưa chứng minh quan hệ nhân quả._

**Hình chính:** phần nhiệt độ và nhu cầu trong `../bao-cao/figures/4-5-bieu-do-phan-tan-theo-nhiet-do-do-am.png`, hoặc dựng lại biểu đồ tương ứng từ CSV. Không dùng toàn bộ heatmap nhiều biến trên trang này.

**Script — 45 giây**

“Trong các biến thời tiết khảo sát, nhiệt độ có tương quan dương lớn nhất với nhu cầu, r bằng 0,563, ở mức vừa. Các giờ ấm hơn thường đi kèm lượng thuê cao hơn, nhưng các điểm vẫn phân tán nhiều. Độ ẩm và lượng mưa có tương quan âm yếu. Những kết quả này giúp nhóm định hướng biến đầu vào, nhưng chỉ mô tả mối liên hệ giữa từng biến với nhu cầu. Chúng chưa kiểm soát đồng thời giờ, mùa và các yếu tố khác, nên nhóm không diễn giải tương quan thành quan hệ nhân quả.”

### Slide 5 — Thiết kế mô hình dự báo

**Trên slide**

- **9 biến đầu vào**: lịch và thời tiết.
- Pipeline: **RobustScaler**, **one-hot**, hồi quy.
- So sánh **mốc trung bình**, **tuyến tính**, **đa thức bậc hai có chọn lọc**.

| Tập theo thứ tự thời gian | Số giờ | Vai trò       |
| ------------------------- | -----: | ------------- |
| Train                     |  5.928 | Huấn luyện    |
| Validation                |  1.272 | Chọn mô hình  |
| Test                      |  1.265 | Đánh giá cuối |

**Bố cục:** bảng ba tập là phần chính, mô tả biến và mô hình nằm phía trên. Giữ chi tiết thuật toán trong ghi chú.

**Script — 65 giây**

“Nhóm dùng chín biến đầu vào, gồm bốn biến lịch là giờ, thứ, mùa, ngày lễ và năm biến thời tiết. Dữ liệu được chia theo ngày liên tiếp: 70 phần trăm số ngày đầu để huấn luyện, 15 phần trăm tiếp theo để chọn mô hình và 15 phần trăm cuối để kiểm tra. Số giờ của từng tập hiển thị trong bảng. Cách chia này mô phỏng học từ quá khứ để dự đoán giai đoạn đến sau. Pipeline học tham số chuẩn hóa và mã hóa trên tập đang huấn luyện. Nhóm so sánh mốc dự đoán bằng trung bình với hồi quy tuyến tính và hồi quy mở rộng đa thức bậc hai. Phần đa thức chỉ bổ sung bình phương và tương tác của nhiệt độ, độ ẩm để kiểm tra quan hệ phi tuyến mà vẫn giữ mô hình gọn.”

**Ghi chú:** năm biến số là nhiệt độ, độ ẩm, gió, mưa, bức xạ. Tỷ lệ 70%/15%/15% tính theo số ngày hoạt động. Train chưa có mùa Thu. Điền thiếu có trong pipeline để dự phòng, dữ liệu hiện tại không thiếu.

### Slide 6 — Kết quả đánh giá mô hình

**Trên slide**

**Chọn đa thức trên validation:** MSE **197.316,62**, thấp hơn tuyến tính **1,81%**.

**Kết quả test sau khi huấn luyện lại trên 7.200 giờ:**

| Phương án       |        MSE | RMSE (lượt/giờ) |     R² |
| --------------- | ---------: | --------------: | -----: |
| Mốc trung bình  | 320.345,38 |          565,99 | −0,052 |
| Tuyến tính      |  99.663,51 |          315,70 |  0,673 |
| Đa thức đã chọn | 100.114,19 |          316,41 |  0,671 |

**Đa thức giảm RMSE 44,1% so với mốc trung bình. Tuyến tính có sai số thấp hơn nhẹ trên test.**

**Bố cục:** bảng lớn giữa slide. Nhấn hàng mô hình đã chọn, giữ rõ cả hai kết luận. MSE có đơn vị (lượt/giờ)², ghi nhỏ dưới bảng. Không gọi R² là độ chính xác.

**Script — 75 giây**

“Nhóm chọn mô hình theo MSE trên tập validation. Đa thức đạt MSE khoảng 197 nghìn, thấp hơn tuyến tính 1,81 phần trăm, nên được chọn theo tiêu chí ban đầu. Tiếp theo, nhóm huấn luyện lại trên 7.200 giờ của hai tập đầu và đánh giá trên 1.265 giờ cuối. Bảng cho thấy cả hai mô hình hồi quy cải thiện rõ so với mốc trung bình. Mô hình đa thức đã chọn có RMSE khoảng 316 lượt mỗi giờ, giảm 44,1 phần trăm so với mốc trung bình, và R bình phương bằng 0,671. RMSE cho biết mức sai số theo đơn vị lượt mỗi giờ và nhạy với những giờ lệch nhiều. Tuy nhiên, tuyến tính có sai số thấp hơn nhẹ trên test. Vì vậy, lợi thế của đa thức chưa ổn định qua các giai đoạn. Nhóm giữ lựa chọn từ validation, đồng thời xem tuyến tính là ứng viên cần đánh giá tiếp trên dữ liệu mới.”

**Ghi chú:** MAE test: mốc trung bình 442,86; tuyến tính 229,75; đa thức 242,38 lượt/giờ. MSE tuyến tính thấp hơn đa thức khoảng 0,45% trên test. Chỉ đọc số liệu chính, không đọc từng ô của bảng.

### Slide 7 — Sai số và giới hạn ứng dụng

**Trên slide**

- Dự đoán thiếu ở nhiều giờ có nhu cầu rất cao.
- MAE cao điểm: **08:00 ≈ 635**, **18:00 ≈ 451 lượt/giờ**.
- **3 dự đoán âm** trên 1.265 giờ test.
- Giới hạn: **một năm dữ liệu**, **thời tiết thực đo cùng giờ**.

**Hình chính:** phần phân tán trong `../bao-cao/figures/chuong-6-thuc-te-du-doan.png`. Làm rõ đường chéo dự đoán hoàn hảo và vùng nhu cầu cao. Biểu đồ phần dư dành cho ghi chú hoặc phần hỏi đáp.

**Script — 60 giây**

“Sai số tổng thể chưa phản ánh hết khó khăn ở cao điểm. Trên biểu đồ, nhiều điểm có nhu cầu thực tế rất cao nằm dưới đường chéo, cho thấy mô hình dự đoán thiếu. MAE lúc 8 giờ khoảng 635 lượt, còn 18 giờ khoảng 451 lượt. Mô hình cũng có ba dự đoán âm, cần xử lý nếu đưa vào sử dụng. Bộ dữ liệu chỉ có một năm và test tập trung mùa Thu, nên chưa xác nhận khả năng ổn định qua nhiều năm. Ngoài ra, việc chọn biến đã tham khảo EDA toàn bộ dữ liệu, cần kiểm chứng trên dữ liệu mới. Thí nghiệm dùng thời tiết thực đo cùng giờ. Khi dự báo trước, phải thay bằng dự báo thời tiết và đánh giá thêm sai số phát sinh.”

**Ghi chú:** MAE chưa làm tròn: 08:00 = 634,63, 18:00 = 450,65. EDA đã định hướng chọn biến nên test chưa hoàn toàn độc lập với thiết kế biến, dù không dùng để học tham số hoặc chọn giữa hai mô hình. Không khẳng định phần dư độc lập, chuẩn hoặc có phương sai không đổi chỉ từ biểu đồ.

### Slide 8 — Dashboard phân tích dữ liệu

**Trên slide**

- **Streamlit và Plotly**: chỉ số, xu hướng thời gian, mối liên hệ thời tiết.
- Tương tác: **tooltip, phóng to, bật/tắt chuỗi**.

**Hình chính:** ảnh tổng quan dashboard từ `../bao-cao/figures/4-8-anh-chup-tong-quan-dashboard-chi-so.png`. Kiểm tra hoặc chụp lại theo code hiện tại khi dựng PPTX. Ảnh chiếm phần lớn trang.

**Script — 30 giây**

“Nhóm xây dựng dashboard bằng Streamlit và Plotly để người xem dễ khám phá dữ liệu. Dashboard hiển thị chỉ số tổng hợp và biểu đồ theo giờ, mùa, thời tiết. Người dùng có thể rê chuột, phóng to và bật tắt chuỗi dữ liệu. Dashboard hiện phục vụ phân tích, còn mô hình dự báo nằm trong notebook. Các thao tác cụ thể sẽ được giới thiệu trong phần demo riêng.”

### Slide 9 — Kết luận và hướng phát triển

**Trên slide**

- Nhu cầu biến động theo **giờ và mùa**, có liên hệ với thời tiết.
- Hồi quy cải thiện so với mốc trung bình, cần cải thiện **dự đoán cao điểm**.
- Bổ sung dữ liệu nhiều năm và đánh giá với **dự báo thời tiết thực tế**.

**Kết quả hiện phù hợp làm công cụ tham khảo cho kế hoạch cung ứng xe.**

**Bố cục:** kết luận ngắn, lời cảm ơn ở chân trang. Không thêm slide cảm ơn riêng.

**Script — 45 giây**

“Qua đồ án, nhóm nhận diện được các mẫu nhu cầu theo giờ và mùa, đồng thời xây dựng mô hình dự đoán từ lịch và thời tiết. Các mô hình hồi quy cải thiện rõ so với mốc trung bình, nhưng sai số ở cao điểm còn lớn và lợi thế của đa thức chưa ổn định. Kết quả gợi ý cần chú ý cung ứng vào giờ nhu cầu cao và mùa ấm. Bước tiếp theo là bổ sung dữ liệu nhiều năm, đánh giá riêng từng mùa, từng giờ và sử dụng dự báo thời tiết khả dụng khi lập kế hoạch. Hiện tại, mô hình phù hợp làm công cụ tham khảo. Nhóm xin cảm ơn thầy cô.”

## 4. Chuẩn bị hỏi đáp và căn thời lượng

Các chi tiết sau giữ trong ghi chú, không thêm vào lời thoại chính:

- ANOVA: giả thuyết trung bình bằng nhau giữa bốn mùa, F = 875,60, p < 0,001. Chưa có kết luận về từng cặp mùa và cần lưu ý phụ thuộc theo giờ.
- R² = 0,671 là chỉ số hiệu năng trên tập kiểm tra, không phải “độ chính xác 67,1%”.
- Đa thức được chọn ở validation. Không đổi lựa chọn sau khi xem test.
- RobustScaler điều chỉnh thang đo theo trung vị/IQR, không làm hồi quy miễn nhiễm với ngoại lệ của biến mục tiêu.
- Dashboard chưa có bộ lọc mùa/khoảng ngày hay màn hình nhập dự báo. Chưa triển khai mô hình chuỗi thời gian trong notebook hiện tại.
- Thống kê nhu cầu theo giờ tính trên toàn bộ dữ liệu sau lọc. Sai số MAE theo giờ tính trên test, là đại lượng khác.

Tập nói một lần với đồng hồ và chuyển slide thật. Ngân sách 8 phút đã dành thời gian để chỉ hình và chuyển trang, nhưng chưa được xác nhận bằng thu âm. Nếu quá giờ, rút mô tả pipeline ở slide 5 và diễn giải kiểm định ở slide 3 trước, giữ kết quả và giới hạn ứng dụng.

## 5. Nguồn đối chiếu

- `../../THONG-TIN-DO-AN.md`: đề tài, thành viên, phần demo riêng.
- `../../notebooks/analysis.ipynb`: thống kê, tương quan, ANOVA.
- `../../notebooks/build_models.ipynb`: chia tập, mô hình, validation/test, sai số.
- `../../dashboard.py`: chức năng dashboard hiện có.
- `../bao-cao/chapters/2.mo-ta-bo-du-lieu.md` đến `7.ket-luan.md`: số liệu và diễn giải báo cáo.
- `../bao-cao/chapters/8.phu-luc-phan-cong.md`: phân vai gợi ý.
- `kich-ban-video.md`: demo 5 phút.

## 6. Nội dung chờ duyệt

Mạch 9 slide, nội dung ngắn trên mỗi trang và script tương ứng ở bản này là phương án đề xuất mới. Sau khi người dùng duyệt, dựng PPTX với speaker notes theo nội dung đã chốt.
