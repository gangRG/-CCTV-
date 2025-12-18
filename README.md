# 🎥 AI-based Object Detection & Video Analysis Platform

YOLOv8 기반 실시간 객체 탐지 및 영상 분석 통합 플랫폼

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://ultralytics.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-orange.svg)](https://streamlit.io)

## 📌 프로젝트 개요

다양한 영상 소스(CCTV, 카메라, 비디오 파일)에서 실시간 객체 탐지 및 분석을 수행하는 통합 플랫폼입니다. YOLOv8 모델을 활용하여 높은 정확도와 빠른 처리 속도를 제공합니다.

### ✨ 주요 기능

- **🎬 실시간 카메라 분석**: 웹캠/USB 카메라를 통한 실시간 객체 탐지
- **📹 비디오 배치 처리**: 다중 영상 파일 동시 분석 및 결과 저장
- **📁 파일 업로드 분석**: 드래그 앤 드롭 방식의 간편한 영상 분석
- **🚦 CCTV 교통 모니터링**: 실시간 차량 탐지 및 교통량 분석 (웹 대시보드)

### 🎯 탐지 기능

- **사람 탐지** (Person Detection)
- **세그멘테이션** (Instance Segmentation)
- **마스크 착용 감지** (Face Mask Detection)
- **차량 탐지 및 추적** (Vehicle Detection & Tracking)

## 🏗️ 시스템 아키텍처

```
📦 Project Root
├── 📄 main.py                    # 통합 실행기 (Streamlit)
├── 📁 카메라 모드
│   ├── camera.py                 # 카메라 탐지 엔진
│   └── ui_camera.py              # 카메라 UI
├── 📁 비디오 모드
│   ├── video.py                  # 비디오 분석 엔진
│   └── ui_video.py               # 비디오 UI
├── 📁 영상 모니터 모드
│   ├── video_loader.py           # 파일 처리 엔진
│   └── ui_video_loader.py        # 로더 UI
└── 📁 CCTV 모드
    ├── app.py                    # Flask 백엔드
    ├── cctv_analyzer.py          # CCTV 분석 엔진
    ├── traffic_api.py            # 교통 API
    └── index.html                # 웹 대시보드
```

**아키텍처 특징**:
- **Streamlit**: 통합 프론트엔드/백엔드 (카메라, 비디오, 로더)
- **Flask**: CCTV 모듈 전용 백엔드 (REST API + WebSocket)
- **멀티스레딩**: 모듈 간 독립 실행 및 장애 격리
- **유연한 확장성**: 모듈별 독립 배포 가능

## 🚀 설치 및 실행

### 1. 환경 요구사항

```
Python 3.8+
RAM 8GB+ (GPU 사용 시 VRAM 4GB+ 권장)
```

### 2. 설치

```bash
# 저장소 클론
git clone https://github.com/yourusername/ai-object-detection-platform.git
cd ai-object-detection-platform

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# Flask 관련 패키지 (CCTV 모드용)
pip install flask flask-cors flask-socketio python-socketio requests python-multipart
```

### 3. 실행

```bash
# 통합 실행 (모든 모드 선택 가능)
streamlit run main.py

# 개별 모드 실행
streamlit run ui_camera.py      # 카메라 모드
streamlit run ui_video.py       # 비디오 모드
streamlit run ui_video_loader.py # 영상 모니터 모드
python app.py                    # CCTV 모드 (Flask 서버)
```

## 📊 성능 최적화

### CPU/GPU 자동 최적화

시스템은 사용 가능한 하드웨어를 자동 감지하여 최적 설정을 적용합니다.

**CPU 최적화**:
- 프레임 리사이징 (640x480)
- 스레드 자동 조정
- FPS: **20-25fps**

**GPU 최적화**:
- CUDA 벤치마크 활성화
- 원본 해상도 처리
- FPS: **30-40fps**

### 메모리 관리

- 프레임 버퍼 최적화
- 불필요한 데이터 즉시 해제
- **메모리 사용량 30% 감소**

## 🔧 기술 스택

**AI/ML**:
- YOLOv8 (Ultralytics)
- PyTorch

**Backend**:
- Streamlit (통합 UI)
- Flask (CCTV 전용)
- Flask-SocketIO (실시간 통신)

**Frontend**:
- HTML/CSS/JavaScript
- Chart.js (시각화)
- Leaflet.js (지도)

**Computer Vision**:
- OpenCV
- NumPy
- Pillow

## 📁 사용 가이드

### 카메라 모드

1. "카메라 모드" 선택
2. 카메라 소스 선택 (기본 웹캠: 0)
3. 탐지 모드 선택 (사람/세그멘테이션/마스크)
4. 신뢰도 임계값 조정
5. "시작" 버튼 클릭

### 비디오 모드

1. "비디오 모드" 선택
2. 비디오 파일 업로드 (MP4, MOV, AVI, MKV, WEBM)
3. 탐지 설정 및 분석 시작
4. 프레임별 결과 확인 및 저장

### CCTV 모드

1. "CCTV 모드" 선택
2. Flask 서버 자동 시작
3. 브라우저에서 `http://localhost:5000` 접속
4. 지도에서 CCTV 선택 및 실시간 분석

## 🎓 핵심 알고리즘

### 다중 모델 검증 시스템

영상 분석 모듈에서 정확도 향상을 위해 **3개의 YOLOv8 모델을 순차적으로 적용**:

```python
# 1차: 일반 탐지 모델
# 2차: 세그멘테이션 모델
# 3차: 마스크 탐지 전용 모델
```

이를 통해 개별 모델의 한계를 보완하고 **False Positive 50% 감소** 달성

### 차량 추적 알고리즘

CCTV 모듈에서 **Centroid Tracker** 기반 차량 추적:
- 유클리드 거리 기반 매칭
- 30프레임 미감지 시 트랙 삭제
- 실시간 속도 계산 및 교통량 집계

## 🔒 데이터 보안 및 규정 준수

**프라이버시 고려사항**:
- 공공 CCTV 데이터 접근 시 개인정보보호법 준수
- 실시간 처리 후 원본 영상 미저장
- 통계 데이터만 DB 저장

**API 키 관리**:
```python
# 환경변수 사용 (권장)
import os
os.environ['ITS_API_KEY'] = 'your_api_key'
```

## 📈 개발 로드맵

- [ ] 모바일 앱 개발
- [ ] 클라우드 배포 (AWS/GCP)
- [ ] 커스텀 데이터셋 학습
- [ ] 이상행동 탐지 기능
- [ ] 다국어 지원

## 🤝 기여

Pull Request는 언제나 환영합니다!

1. Fork
2. Feature Branch 생성 (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

## 📄 라이선스

MIT License

## 👤 개발자

**김대영**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

⭐ **이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**
