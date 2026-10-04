# Bike Sharing Data Analysis

Phân tích và dự báo nhu cầu sử dụng dịch vụ chia sẻ xe đạp tại Seoul — Nhóm 26, UIT.

> Thông tin về đồ án (thành viên, mục tiêu, mốc thời gian, báo cáo): xem [THONG-TIN-DO-AN.md](THONG-TIN-DO-AN.md).

## Yêu cầu

- Python 3.14 (môi trường đã được kiểm thử với 3.14.6)
- Dữ liệu có sẵn tại `data/SeoulBikeData.csv`

## Cài đặt

Chạy các lệnh sau tại thư mục gốc của repo:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Chạy dashboard

Chạy từ thư mục gốc của repo (dashboard đọc dữ liệu qua đường dẫn `./data/...`):

```bash
streamlit run dashboard.py
```

Sau đó mở http://localhost:8501 trên trình duyệt.

## Chạy notebooks

Notebooks nằm trong thư mục `notebooks/` và đọc dữ liệu qua đường dẫn `../data/...`, nên cần chạy với thư mục làm việc là `notebooks/`.

| Notebook | Nội dung |
| --- | --- |
| `notebooks/analysis.ipynb` | Phân tích khám phá và trực quan hóa dữ liệu |
| `notebooks/build_models.ipynb` | Xây dựng và đánh giá mô hình dự báo |

Cách chạy:

- **VS Code**: mở file `.ipynb`, chọn kernel là `.venv` vừa tạo, rồi bấm *Run All*.
- **Jupyter Lab** (đã có trong `requirements.txt`):

  ```bash
  jupyter lab notebooks/
  ```

## Cấu trúc thư mục

```
bike-sharing-data-analysis/
├── data/                # Tập dữ liệu SeoulBikeData.csv
├── notebooks/           # Notebook phân tích và xây dựng mô hình
├── src/                 # Mã nguồn hỗ trợ (helper, đường dẫn)
├── noi-dung-bao-cao/    # Nội dung báo cáo và thuyết trình
├── meeting-notes/       # Biên bản họp nhóm
├── dashboard.py         # Dashboard Streamlit
├── requirements.txt     # Các gói Python cần thiết
├── README.md            # Hướng dẫn chạy (tệp này)
└── THONG-TIN-DO-AN.md   # Thông tin về đồ án
```
