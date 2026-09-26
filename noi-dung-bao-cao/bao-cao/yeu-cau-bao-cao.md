# Yêu cầu báo cáo đồ án môn học

**Các tiêu chí kiểm duyệt cần đối chiếu:**

**1. Hình thức và Cấu trúc chung:**


* Tên đề tài ở trang bìa phải được viết in hoa và giới hạn tối đa 3 dòng.


* Phần thông tin sinh viên thực hiện không được ghi tên Giảng viên hướng dẫn.


* Tổng số trang của các phần chính (Giới thiệu, Mô tả bộ dữ liệu, Phương pháp phân tích, Phân tích thăm dò/sơ bộ, Kết quả phần tích, Kết luận) phải nằm trong khoảng từ 05 đến 10 trang, không tính trang bìa, tài liệu tham khảo và phụ lục.


* Báo cáo tuyệt đối không được chứa lời cảm ơn, phần tóm tắt hay mục lục.


* Không được trình bày mã nguồn (code) bên trong nội dung bài thu hoạch; mã nguồn chỉ được phép đưa vào phần phụ lục nếu cần.


**2. Nội dung chi tiết từng phần:**

**Cấu trúc báo cáo**

Nội dung báo cáo được chia thành các chương như sau:

| Chương    | Nội dung                             | Độ dài     | Mô tả chi tiết                                                                                                               |
| --------- | ------------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1         | Giới thiệu                           | 0.5 trang  | Nêu bối cảnh bài toán, mục tiêu nghiên cứu và các công cụ/thuật toán áp dụng.                                                |
| 2         | Mô tả bộ dữ liệu                     | 1.0 trang  | Nguồn gốc dữ liệu, số lượng mẫu, định nghĩa chi tiết biến số và phân loại kiểu dữ liệu.                                      |
| 3         | Thống kê mô tả tổng quan             | 1.5 trang  | Đánh giá xu hướng tập trung (Mean, Median), mức độ phân tán (Variance, Std Dev) và hình dáng phân phối (Skewness, Kurtosis). |
| 4         | Phân tích thăm dò (EDA) & Tương quan | 2.5 trang  | Trực quan hóa dữ liệu (Histogram, Boxplot), đánh giá tương quan (Heatmap) và kiểm định ANOVA/groupby cho các biến phân loại. |
| 5         | Xây dựng mô hình dự báo              | 2.5 trang  | Tiền xử lý dữ liệu (Outlier, Encoding), xây dựng Pipeline và huấn luyện các mô hình dự báo (Linear/Polynomial Regression).   |
| 6         | Kết quả và Đánh giá                  | 1.5 trang  | Đánh giá thang đo ($MSE, R^2$) và phân tích biểu đồ (Regression/Residual plot) để kiểm tra độ tin cậy của mô hình.           |
| 7         | Kết luận                             | 0.5 trang  | Tóm tắt các phát hiện cốt lõi, khẳng định tính hiệu quả của mô hình và đề xuất ứng dụng thực tiễn.                           |
| Tổng cộng | (Không tính phụ lục)                 | 10.0 trang |                                                                                                                              |

* **Giới thiệu:** Phải được viết trong khoảng 10 dòng hoặc nửa trang, gồm đúng 2 đoạn văn và không sử dụng gạch đầu dòng. Đoạn 1 cần nêu rõ mục tiêu, công cụ/thuật toán áp dụng và tóm tắt kết quả đạt được. Đoạn 2 phải cam kết minh bạch về nguồn gốc bộ dữ liệu.

* **Mô tả bộ dữ liệu:** Giới hạn trong khoảng 1 trang, bao gồm bảng mô tả các cột dữ liệu (Tên cột, Kiểu dữ liệu, Phạm vi, Giải thích) và các thống kê sơ bộ về dữ liệu.

* **Thống kê mô tả tổng quan:** Đánh giá xu hướng tập trung (Mean, Median), mức độ phân tán (Variance, Std Dev) và hình dáng phân phối (Skewness, Kurtosis) của các biến quan trọng.

* **Phân tích thăm dò (EDA) & Tương quan:** Trình bày kết quả trực quan hóa dữ liệu (Histogram, Boxplot), ma trận tương quan (Heatmap) và kết quả kiểm định ANOVA/groupby cho các biến phân loại.

* **Xây dựng mô hình dự báo:** Trình bày quy trình tiền xử lý dữ liệu (Outlier, Encoding), xây dựng Pipeline và chi tiết các mô hình đã huấn luyện (Linear/Polynomial Regression).

* **Kết quả và Đánh giá:** Trình bày kết quả đánh giá thông qua các thang đo ($MSE, R^2$) và phân tích đồ thị (Regression/Residual plot) để kiểm tra độ tin cậy của mô hình.

* **Kết luận:** Độ dài khoảng 10 dòng hoặc nửa trang, tóm tắt các phát hiện cốt lõi, khẳng định tính hiệu quả của mô hình và đề xuất ứng dụng thực tiễn.


* **Tài liệu tham khảo:** Sinh viên không được phép tham khảo các nguồn từ blog công nghệ, wikipedia, facebook, youtube hoặc mạng xã hội. Trình bày sai định dạng tài liệu tham khảo sẽ bị trừ 1 điểm.


* **Phụ lục:** Bắt buộc phải có Phụ lục phân công nhiệm vụ, trong đó ghi rõ từng nhiệm vụ chi tiết của mỗi thành viên nhóm.



**3. Quy định nộp bài & Các mức trừ điểm:**

* Tên tất cả các file nộp phải bắt đầu bằng tên nhóm (ví dụ: Nhom18_Bao_cao.docx).


* Các file sản phẩm (Báo cáo, Slide, Code) phải được nộp dưới dạng từng file riêng lẻ, tuyệt đối không được nén lại.


* Nếu sinh viên không sử dụng đúng Template này, bài làm sẽ bị trừ 2 điểm.


* Bất cứ vi phạm nào thuộc nhóm các điều "KHÔNG nên làm" sẽ bị trừ 0.5 điểm cho mỗi lần vi phạm.


* Bài báo cáo sẽ nhận 0 điểm ngay lập tức nếu phát hiện copy y chang trên Internet.



**Định dạng đầu ra yêu cầu:**
Sau khi rà soát, hãy trả về kết quả định dạng Markdown bao gồm 3 phần:

1. **Bảng đánh giá tổng quan:** Trạng thái Đạt / Không đạt cho từng hạng mục cấu trúc.
2. **Danh sách vi phạm:** Liệt kê các tiêu chí bị vi phạm, trích dẫn phần văn bản lỗi của sinh viên và tính tổng điểm trừ dự kiến.
3. **Đề xuất hành động:** Liệt kê các gạch đầu dòng ngắn gọn để sinh viên sửa lại cho đúng chuẩn tài liệu.