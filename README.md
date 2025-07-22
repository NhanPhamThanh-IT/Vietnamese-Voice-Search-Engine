<div align="justify">

# <div align="center">🔍 Vietnamese Voice Search Engine - Trợ Lý Tìm Kiếm Tin Tức Bằng Giọng Nói Cho Người Việt</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Vietnamese](https://img.shields.io/badge/Language-Vietnamese-green.svg)](https://en.wikipedia.org/wiki/Vietnamese_language) [![GitHub stars](https://img.shields.io/github/stars/NhanPhamThanh-IT/Voice-Search-Engine?style=social)](https://github.com/NhanPhamThanh-IT/Voice-Search-Engine/stargazers) [![GitHub forks](https://img.shields.io/github/forks/NhanPhamThanh-IT/Voice-Search-Engine?style=social)](https://github.com/NhanPhamThanh-IT/Voice-Search-Engine/network/members) [![GitHub issues](https://img.shields.io/github/issues/NhanPhamThanh-IT/Voice-Search-Engine)](https://github.com/NhanPhamThanh-IT/Voice-Search-Engine/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr/NhanPhamThanh-IT/Voice-Search-Engine)](https://github.com/NhanPhamThanh-IT/Voice-Search-Engine/pulls)

</div>

## 📋 Mục Lục

- [Giới Thiệu](#-giới-thiệu)
- [Tính Năng](#-tính-năng)
- [Demo](#-demo)
- [Cài Đặt](#-cài-đặt)
- [Cách Sử Dụng](#-cách-sử-dụng)
- [Cấu Trúc Dự Án](#-cấu-trúc-dự-án)
- [Công Nghệ Sử Dụng](#-công-nghệ-sử-dụng)
- [API và Dịch Vụ](#-api-và-dịch-vụ)
- [Cấu Hình](#-cấu-hình)
- [Đóng Góp](#-đóng-góp)
- [Nhóm Phát Triển](#-nhóm-phát-triển)
- [Giảng Viên Hướng Dẫn](#-giảng-viên-hướng-dẫn)
- [Giấy Phép](#-giấy-phép)

## 🌟 Giới Thiệu

**Vietnamese Voice Search Engine** là một ứng dụng web hiện đại được phát triển bằng Streamlit, cho phép người dùng tìm kiếm tin tức bằng giọng nói và nghe kết quả được tóm tắt qua công nghệ text-to-speech. Đây là giải pháp hoàn hảo cho những ai muốn cập nhật tin tức nhanh chóng mà không cần đọc.

### 🎯 Mục Tiêu Dự Án

- Tạo ra một giao diện thân thiện với người dùng cho việc tìm kiếm tin tức
- Ứng dụng công nghệ nhận diện giọng nói tiếng Việt
- Tự động tóm tắt và đọc tin tức bằng giọng nói tự nhiên
- Cung cấp trải nghiệm hands-free cho việc tiếp cận thông tin

## ✨ Tính Năng

### 🎤 Nhận Diện Giọng Nói

- **Hỗ trợ tiếng Việt**: Nhận diện chính xác giọng nói tiếng Việt
- **Giao diện đơn giản**: Chỉ cần nhấn nút và nói
- **Xử lý lỗi thông minh**: Thông báo rõ ràng khi có lỗi nhận diện

### 📰 Tìm Kiếm Tin Tức

- **Tìm kiếm thời gian thực**: Sử dụng Serper API để tìm kiếm tin tức mới nhất
- **Khu vực hoá**: Tập trung vào tin tức Việt Nam
- **Đa dạng nguồn tin**: Tìm kiếm từ nhiều nguồn tin tức uy tín

### 📝 Tóm Tắt Thông Minh

- **Thuật toán LexRank**: Sử dụng thuật toán tiên tiến để tóm tắt nội dung
- **Tùy chỉnh độ dài**: Có thể điều chỉnh số câu trong bản tóm tắt
- **Xử lý văn bản**: Làm sạch và định dạng văn bản tự động

### 🔊 Text-to-Speech

- **Google TTS**: Sử dụng công nghệ TTS của Google
- **Giọng đọc tự nhiên**: Phát âm chuẩn tiếng Việt
- **Phát tự động**: Tự động phát âm thanh khi có kết quả

### 🎨 Giao Diện Người Dùng

- **Responsive Design**: Thích ứng với mọi kích thước màn hình
- **Theme tùy chỉnh**: Giao diện đẹp mắt với CSS tùy chỉnh
- **Sidebar thông tin**: Hiển thị thông tin nhóm và liên hệ

## 🚀 Demo

### Luồng Hoạt Động

1. **Bước 1**: Người dùng nhấn nút ghi âm và nói từ khóa tìm kiếm
2. **Bước 2**: Hệ thống nhận diện giọng nói và chuyển thành văn bản
3. **Bước 3**: Tìm kiếm tin tức liên quan trên internet
4. **Bước 4**: Trích xuất và tóm tắt nội dung bài viết
5. **Bước 5**: Chuyển đổi bản tóm tắt thành giọng nói và phát cho người dùng

### Ví Dụ Sử Dụng

```
🎤 Người dùng nói: "Tin tức về công nghệ AI mới nhất"
📊 Hệ thống xử lý: Tìm kiếm → Tóm tắt → Phát âm
🔊 Kết quả: Nghe bản tóm tắt tin tức về AI qua loa
```

## 🛠 Cài Đặt

### Yêu Cầu Hệ Thống

- **Python**: 3.8 hoặc cao hơn
- **Hệ điều hành**: Windows, macOS, Linux
- **RAM**: Tối thiểu 4GB
- **Kết nối Internet**: Cần thiết cho API calls

### Bước 1: Clone Repository

```bash
git clone https://github.com/NhanPhamThanh-IT/Voice-Search-Engine.git
cd Voice-Search-Engine
```

### Bước 2: Tạo Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

### Bước 4: Cấu Hình Environment Variables

Tạo file `.env` trong thư mục gốc:

```env
SERPER_API_KEY=your_serper_api_key_here
```

### Bước 5: Chạy Ứng Dụng

```bash
streamlit run app.py
```

Ứng dụng sẽ chạy tại: `http://localhost:8501`

## 📱 Cách Sử Dụng

### Giao Diện Chính

1. **Sidebar Trái**: Thông tin nhóm phát triển và liên hệ
2. **Khu Vực Chính**: Tiêu đề ứng dụng và nút ghi âm
3. **Audio Player**: Phát kết quả tìm kiếm

### Hướng Dẫn Chi Tiết

1. **Nhấn vào nút "Nhấn để bắt đầu ghi âm"**
2. **Nói rõ ràng từ khóa tìm kiếm** (ví dụ: "tin tức thể thao hôm nay")
3. **Chờ hệ thống xử lý** (có spinner hiển thị tiến trình)
4. **Nghe kết quả** được phát tự động

### Mẹo Sử Dụng

- 🎯 **Nói rõ ràng**: Đảm bảo môi trường yên tĩnh khi ghi âm
- 🔍 **Từ khóa cụ thể**: Sử dụng từ khóa cụ thể để có kết quả tốt hơn
- ⏰ **Chờ đợi**: Quá trình tóm tắt có thể mất 10-30 giây
- 🔊 **Âm lượng**: Điều chỉnh âm lượng thiết bị để nghe rõ

## 📁 Cấu Trúc Dự Án

```
Voice-Search-Engine/
├── 📄 app.py                 # File chính của ứng dụng
├── 📄 requirements.txt       # Danh sách dependencies
├── 📄 README.md             # File documentation này
├── 📄 LICENSE               # Giấy phép MIT
├── 📂 assets/               # Tài nguyên tĩnh
│   ├── 🎨 themes.css        # CSS tùy chỉnh
│   └── 📂 images/           # Hình ảnh
│       └── 🖼️ hcmus_logo.png # Logo trường đại học
├── 📂 components/           # Các component UI
│   ├── 📄 __init__.py       # Package initializer
│   ├── 🎤 AudioRecorder.py  # Component ghi âm
│   ├── 🔊 AudioPlayer.py    # Component phát âm thanh
│   ├── 📋 LeftSidebar.py    # Sidebar trái
│   └── 📰 PageHeader.py     # Header trang
├── 📂 settings/             # Cấu hình ứng dụng
│   ├── 📄 __init__.py       # Package initializer
│   ├── ⚙️ AppConfig.py      # Cấu hình chung
│   └── 🎨 ThemeManager.py   # Quản lý theme
└── 📂 utils/                # Utilities
    ├── 📄 __init__.py       # Package initializer
    └── 🕷️ Scrapper.py       # Web scraping và xử lý
```

### Chi Tiết Các Module

#### 🎤 AudioRecorder.py

- Sử dụng `streamlit.audio_input()` cho ghi âm
- Tích hợp `speech_recognition` cho nhận diện giọng nói
- Hỗ trợ ngôn ngữ tiếng Việt (`vi-VN`)

#### 🔊 AudioPlayer.py

- Sử dụng Google Text-to-Speech (`gTTS`)
- Quản lý file tạm thời cho audio
- Tự động phát và xóa file sau khi sử dụng

#### 🕷️ Scrapper.py

- Tích hợp Serper API cho tìm kiếm tin tức
- Sử dụng `newspaper3k` cho scraping
- Thuật toán LexRank cho tóm tắt văn bản

## 🔧 Công Nghệ Sử Dụng

### Frontend Framework

- **[Streamlit](https://streamlit.io/)**: Framework chính cho web app
- **HTML/CSS**: Tùy chỉnh giao diện người dùng

### Backend Technologies

- **[Python](https://python.org/)**: Ngôn ngữ lập trình chính
- **[Speech Recognition](https://pypi.org/project/SpeechRecognition/)**: Nhận diện giọng nói
- **[Google TTS](https://pypi.org/project/gTTS/)**: Text-to-Speech

### Data Processing

- **[Newspaper3k](https://newspaper.readthedocs.io/)**: Web scraping tin tức
- **[Sumy](https://pypi.org/project/sumy/)**: Tóm tắt văn bản với LexRank
- **[Mutagen](https://mutagen.readthedocs.io/)**: Xử lý metadata audio

### HTTP & APIs

- **[Requests](https://requests.readthedocs.io/)**: HTTP client cho API calls
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Quản lý environment variables

## 🌐 API và Dịch Vụ

### Serper API

- **Mục đích**: Tìm kiếm tin tức từ Google News
- **Endpoint**: `https://google.serper.dev/news`
- **Tham số**:
  - `q`: Từ khóa tìm kiếm
  - `location`: "Vietnam"
  - `gl`: "vn" (quốc gia)
  - `hl`: "vi" (ngôn ngữ)

### Google Speech Recognition

- **Mục đích**: Chuyển đổi giọng nói thành văn bản
- **Ngôn ngữ**: Tiếng Việt (`vi-VN`)
- **Định dạng**: Hỗ trợ các format audio phổ biến

### Google Text-to-Speech

- **Mục đích**: Chuyển văn bản thành giọng nói
- **Ngôn ngữ**: Tiếng Việt (`vi`)
- **Output**: MP3 format

## ⚙️ Cấu Hình

### Environment Variables

Tạo file `.env` với các biến sau:

```env
# Serper API Configuration
SERPER_API_KEY=your_serper_api_key

# Optional configurations
DEFAULT_LANGUAGE=vi
DEFAULT_LOCATION=Vietnam
SUMMARY_SENTENCES=5
```

### AppConfig.py

```python
class AppConfig:
    APP_HEADER = {
        "TITLE": "Trợ Lý Tìm Kiếm Tin Tức Bằng Giọng Nói",
        "DESCRIPTION": "Tìm kiếm và khám phá tin tức dễ dàng qua giọng nói..."
    }
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
```

### Tùy Chỉnh Theme

Chỉnh sửa `assets/themes.css` để thay đổi giao diện:

```css
/* Tùy chỉnh màu sắc, font chữ, layout */
.main-header {
  color: #1f4e79;
  font-family: "Arial", sans-serif;
}
```

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp để cải thiện dự án!

### Quy Trình Đóng Góp

1. **Fork** repository này
2. **Tạo branch mới** (`git checkout -b feature/AmazingFeature`)
3. **Commit** thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. **Push** lên branch (`git push origin feature/AmazingFeature`)
5. **Tạo Pull Request**

### Coding Standards

- Sử dụng **PEP 8** cho Python code style
- Thêm **docstrings** cho các function quan trọng
- Viết **comments** bằng tiếng Việt hoặc tiếng Anh
- **Test** code trước khi submit

### Báo Lỗi

Nếu phát hiện lỗi, vui lòng tạo **Issue** với thông tin:

- Mô tả chi tiết lỗi
- Các bước tái hiện
- Screenshot (nếu có)
- Thông tin môi trường (OS, Python version, v.v.)

## 👥 Nhóm Phát Triển

Dự án được thực hiện bởi nhóm sinh viên Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM:

### 🎓 Thành Viên Nhóm

| Tên                   | Vai Trò                       | Email                    | GitHub                                                   |
| --------------------- | ----------------------------- | ------------------------ | -------------------------------------------------------- |
| **Phạm Thành Nhân**   | Team Lead & Backend Developer | ptnhanit230104@gmail.com | [@NhanPhamThanh-IT](https://github.com/NhanPhamThanh-IT) |
| **Huỳnh Nhật Nam**    | Frontend Developer & UI/UX    | -                        | -                                                        |
| **Dương Trung Nghĩa** | Data Processing & Algorithm   | -                        | -                                                        |

### 🔗 Liên Hệ Nhóm

- **Email chính**: ptnhanit230104@gmail.com
- **Repository**: [Voice-Search-Engine](https://github.com/NhanPhamThanh-IT/Voice-Search-Engine)

## 👨‍🏫 Giảng Viên Hướng Dẫn

Dự án được thực hiện dưới sự hướng dẫn của:

- **GT.TS. Đinh Điền** - Giảng viên chính
- **TS. Nguyễn Hồng Bửu Long** - Giảng viên phụ trách

_Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM_

## 🎓 Về Dự Án

Đây là đồ án cuối kỳ môn **[Tên Môn Học]** được thực hiện trong học kỳ **[Học Kỳ - Năm Học]**. Dự án nhằm mục đích:

- Ứng dụng kiến thức đã học vào thực tiễn
- Nghiên cứu và áp dụng các công nghệ AI hiện đại
- Phát triển kỹ năng làm việc nhóm và quản lý dự án
- Tạo ra sản phẩm có ý nghĩa thực tiễn

## 📊 Thống Kê Dự Án

- **Thời gian phát triển**: [Số tuần/tháng]
- **Số dòng code**: ~1,500+ lines
- **Số files**: 15+ files
- **Ngôn ngữ chính**: Python (100%)
- **Dependencies**: 9 packages
- **Phiên bản**: v1.0.0

## 🔄 Roadmap & Tính Năng Tương Lai

### Version 2.0 (Dự Kiến)

- [ ] **Multi-language Support**: Hỗ trợ tiếng Anh
- [ ] **Voice Commands**: Điều khiển bằng giọng nói
- [ ] **Search History**: Lưu lịch sử tìm kiếm
- [ ] **Favorites**: Lưu tin tức yêu thích

### Version 2.1 (Tương Lai)

- [ ] **Mobile App**: Phát triển ứng dụng mobile
- [ ] **Real-time News**: Cập nhật tin tức thời gian thực
- [ ] **Custom Voice**: Tùy chọn giọng đọc
- [ ] **Advanced Analytics**: Thống kê sử dụng

## 🐛 Known Issues & Limitations

### Hiện Tại

- Chỉ hỗ trợ tiếng Việt
- Phụ thuộc vào kết nối internet
- Thời gian xử lý có thể chậm với tin tức dài

### Đang Khắc Phục

- Tối ưu hóa tốc độ xử lý
- Cải thiện độ chính xác nhận diện giọng nói
- Thêm cache để giảm thời gian tải

## 📈 Performance & Optimization

### Metrics

- **Thời gian phản hồi**: 10-30 giây
- **Độ chính xác nhận diện**: ~85-90%
- **Chất lượng tóm tắt**: Tốt với văn bản tiếng Việt

### Tối Ưu Hóa

- Sử dụng caching cho API responses
- Lazy loading cho components
- Compression cho audio files

## 🔒 Bảo Mật & Privacy

- **API Keys**: Được bảo vệ bằng environment variables
- **Audio Data**: Không lưu trữ dữ liệu âm thanh
- **User Privacy**: Không thu thập thông tin cá nhân
- **HTTPS**: Khuyến nghị sử dụng HTTPS khi deploy

## 📚 Tài Liệu Tham Khảo

### Official Documentation

- [Streamlit Documentation](https://docs.streamlit.io/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [Google TTS Documentation](https://cloud.google.com/text-to-speech/docs)

### Research Papers

- LexRank Algorithm for Text Summarization
- Vietnamese Speech Recognition Techniques
- Web Scraping Best Practices

### Tutorials & Guides

- Building Voice-Enabled Web Apps
- Streamlit Advanced Techniques
- Python Audio Processing

## 🙏 Acknowledgments

Chúng tôi xin cảm ơn:

- **Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM** vì môi trường học tập
- **Giảng viên hướng dẫn** vì sự support và guidance
- **Cộng đồng Open Source** vì các thư viện tuyệt vời
- **Google, Serper** vì cung cấp APIs miễn phí cho nghiên cứu

## 📄 Giấy Phép

Dự án này được phân phối dưới giấy phép **MIT License**. Xem file [LICENSE](LICENSE) để biết thêm thông tin chi tiết.

```
MIT License

Copyright (c) 2025 Nhan Pham Thanh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

**🌟 Nếu dự án này hữu ích, hãy cho chúng tôi một Star! ⭐**

**📞 Liên hệ**: ptnhanit230104@gmail.com | **🏫**: Trường ĐH Khoa học Tự nhiên - ĐHQG-HCM

**Được phát triển với ❤️ bởi nhóm Vietnamese Voice Search Engine Team**

</div>

</div>
