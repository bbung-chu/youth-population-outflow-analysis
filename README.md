# 청년 지역 이탈 분석

이 프로젝트는 전국 시군구별 청년 인구 이동 데이터를 분석해, 청년들이 어떤 지역을 떠나는지와 유출 지역의 특징을 살펴보는 작업입니다.

## 프로젝트 목적

- 전국 시군구별 청년 순이동 현황 파악
- 청년 순유출 지역 식별
- 유출 지역과 유입 지역 간 이동 패턴 분석
- 지역 특성과 청년 유출 간 관계 탐색
- 분석 결과를 바탕으로 정책적 시사점 도출

## 데이터

- 원본 데이터: `data/raw/`
- 전처리 데이터: `data/processed/`
- 주요 파일:
  - `kosis_sgg_sex_age_net_migration_raw.csv`
  - `youth_net_migration.csv`
  - `youth_net_migration_processed.csv`

## 저장소 구조

```text
README.md
requirements.txt
notebooks/
    01_youth_net_migration_analysis.ipynb
src/
    preprocessing.py
data/
    raw/
    processed/
results/
    figures/
```

## 분석 흐름

1. 원본 인구 이동 데이터 수집
2. 청년층(19~34세) 기준 데이터 전처리
3. 시군구별 순유출/순유입 현황 산출
4. 지역별 이동 패턴과 시각화
5. 결과 해석 및 정책 제안

## 현재 상태

- 원본 데이터 수집 완료
- 전처리 및 분석 노트북 진행 중
- 시각화 결과는 `results/figures/`에 저장 예정

## 실행 환경

```bash
pip install -r requirements.txt
```

본 프로젝트는 청년 인구 유출 현상을 데이터 기반으로 이해하고, 지역 간 인구 이동 구조를 탐색하는 데 초점을 둡니다.