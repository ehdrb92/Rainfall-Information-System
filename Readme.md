# Account Book

서울시 강우량 정보 어플리케이션 API

## Installation

requirements.txt 파일을 이용하여 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

## Feature

- [x] 하수관로 수위 및 강우량 데이터 조회
- [x] 하수관로 수위 알람
- [x] 강우량 알람
- [x] 알람 기능 취소

## API

| Method |        URL        |             Description             |
| :----: | :---------------: | :---------------------------------: |
|  GET   |      /data/       | 하수관로 수위 및 강우량 데이터 조회 |
|  GET   | /alarm/drainpipe/ |         하수관로 수위 알람          |
|  GET   | /alarm/rainfall/  |             강우량 알람             |
|  GET   |   /alarm/stop/    |           알람 기능 취소            |