**Chuẩn bị trước khi quay**
- Chạy sẵn toàn bộ cell của hai notebook để có output, tránh chờ khi quay.
- Mở sẵn dashboard ở một tab trình duyệt và để nó cache dữ liệu.
- Phóng to font VS Code và trình duyệt lên khoảng 125%, rồi tắt thông báo.

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Kịch bản chi tiết

**Cảnh 1. Mở đầu (0:00 – 0:20)**
- *Hành động:* Mở README trên VS Code, dừng ở tên đề tài và bảng thành viên.
- *Lời thoại:* "Xin chào thầy cô, nhóm 26 xin demo đề tài Phân tích và dự báo nhu cầu sử dụng dịch vụ chia sẻ xe đạp tại Seoul. Trong 5 phút, nhóm sẽ trình bày dữ liệu, phân tích khám phá, dashboard tương tác và mô hình dự báo."

**Cảnh 2. Cấu trúc dự án và dữ liệu (0:20 – 0:50)**
- *Hành động:* Mở cây thư mục, sau đó mở file SeoulBikeData.csv và cuộn qua vài dòng.
- *Lời thoại:* "Dự án gồm dữ liệu gốc, hai notebook, một dashboard Streamlit và các chương báo cáo. Bộ dữ liệu ghi số lượt thuê xe theo từng giờ trong một năm, kèm nhiệt độ, độ ẩm, lượng mưa, mùa và ngày lễ. Nhóm chỉ giữ 8.465 giờ hệ thống thực sự hoạt động."

**Cảnh 3. Phân tích khám phá trong notebook (0:50 – 1:50)**
- *Hành động:* Mở analysis.ipynb. Cuộn đến bảng thống kê mô tả, rồi histogram, violin theo mùa, ma trận tương quan và kết quả ANOVA.
- *Lời thoại:*
  - "Số lượt thuê trung bình khoảng 729 lượt mỗi giờ, cao hơn trung vị, nên phân phối lệch phải."
  - "Theo mùa, mùa Hạ cao nhất với hơn 1.000 lượt mỗi giờ, còn mùa Đông chỉ khoảng 225."
  - "Nhiệt độ có tương quan dương mức vừa với nhu cầu, r bằng 0,56. Độ ẩm có tương quan âm yếu."
  - "Kiểm định ANOVA bác bỏ giả thuyết trung bình bằng nhau giữa bốn mùa. Đây là bằng chứng thăm dò, không phải quan hệ nhân quả."

**Cảnh 4. Dashboard tương tác, phần trọng tâm (1:50 – 3:20)**
- *Hành động:* Chuyển sang terminal và gõ lệnh streamlit run, rồi chuyển qua tab trình duyệt đã mở sẵn.
- *Lời thoại:* "Để người không chuyên cũng đọc được kết quả, nhóm xây dựng dashboard bằng Streamlit và Plotly."
- *Hành động:* Dừng ở hàng thẻ chỉ số.
- *Lời thoại:* "Hàng đầu là các chỉ số chính: tổng lượt thuê, trung bình theo ngày và giờ cao điểm là 18 giờ."
- *Hành động:* Rê chuột trên biểu đồ theo giờ để hiện tooltip ở 8 giờ và 18 giờ.
- *Lời thoại:* "Biểu đồ theo giờ có hai đỉnh lúc 8 giờ sáng và 18 giờ chiều, trùng giờ đi làm và tan làm. Điều này gợi ý xe đạp được dùng nhiều cho việc đi lại hằng ngày."
- *Hành động:* Cuộn qua biểu đồ ngày trong tuần, ngày lễ và độ ẩm, rồi zoom vào biểu đồ mưa.
- *Lời thoại:* "Ngày thường có nhu cầu cao hơn ngày lễ. Độ ẩm cao và trời mưa đi kèm nhu cầu giảm rõ rệt. Người dùng có thể rê chuột, phóng to hoặc tắt từng chuỗi dữ liệu để xem chi tiết."

**Cảnh 5. Mô hình dự báo (3:20 – 4:30)**
- *Hành động:* Mở build_models.ipynb, chỉ vào cell chia dữ liệu theo thời gian.
- *Lời thoại:* "Dữ liệu được chia theo thời gian để tránh dùng tương lai dự đoán quá khứ. Nhóm so sánh ba phương án: mốc trung bình, hồi quy tuyến tính và hồi quy có mở rộng đa thức bậc hai."
- *Hành động:* Cuộn tới bảng kết quả trên tập kiểm tra.
- *Lời thoại:* "Trên 1.265 giờ kiểm tra cuối, mô hình được chọn đạt R² khoảng 0,67. RMSE giảm khoảng 44% so với mốc trung bình."
- *Hành động:* Mở biểu đồ thực tế so với dự đoán và biểu đồ phần dư.
- *Lời thoại:* "Mô hình còn dự đoán thiếu ở giờ cao điểm. Sai số lớn nhất là lúc 8 giờ sáng, khoảng 635 lượt mỗi giờ. Vì vậy nhóm xem mô hình là công cụ tham khảo, chưa phải căn cứ duy nhất để điều phối xe."

**Cảnh 6. Kết luận (4:30 – 5:00)**
- *Hành động:* Quay lại ảnh tổng quan dashboard.
- *Lời thoại:* "Tóm lại, nhu cầu thuê xe phụ thuộc rõ vào giờ trong ngày, mùa và thời tiết. Nhóm đề xuất tăng xe sẵn sàng ở giờ cao điểm và mùa ấm, đồng thời giảm xe khi trời mưa hoặc vào mùa Đông. Hướng phát triển là bổ sung dữ liệu nhiều năm và thử mô hình chuỗi thời gian. Cảm ơn thầy cô đã theo dõi."

## Mẹo quay

- **Phân vai theo người phụ trách:** Hiển có thể nói cảnh 2, Hòa nói cảnh 3 và 4, Lợi nói cảnh 5 và 6, giống cách nhóm đã chia chương.
- **Thu âm lời thoại riêng** rồi ghép với phần quay màn hình sẽ dễ khớp thời gian hơn quay một lần liền.
- **Dùng OBS Studio** để quay màn hình 1080p, và bật hiệu ứng làm nổi con trỏ chuột khi rê trên biểu đồ.
- **Dashboard hiện chưa có bộ lọc** như chọn mùa hay khoảng ngày. Nếu muốn phần demo tương tác hơn, có thể thêm một bộ lọc mùa ở sidebar trước ngày quay.