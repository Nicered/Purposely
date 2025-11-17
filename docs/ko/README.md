# Purposely 문서

Purposely - 목적 중심 개발(PDD) 프레임워크에 오신 것을 환영합니다.

## 목차

- [PDD란 무엇인가?](what-is-pdd.md) - 목적 중심 개발 이해하기
- [시작하기](getting-started.md) - 빠른 시작 가이드
- [문서 타입](document-types.md) - 7가지 문서 타입 개요
- [모범 사례](best-practices.md) - 효과적인 PDD를 위한 팁

## 빠른 링크

- [메인 README](../../README.md)
- [English Documentation](../en/README.md)

---

# Purposely 빠른 시작

**목적 중심 개발(Purpose-Driven Development, PDD) 프레임워크**

Purposely는 개발 생애주기 전체에 걸쳐 프로젝트의 핵심 목적과의 정렬을 유지하도록 돕습니다.

## 🎯 핵심 개념

모든 프로젝트는 다음을 정의하는 **GLOBAL_PURPOSE**를 가져야 합니다:
- 왜 이 프로젝트가 존재하는가? (Why)
- 어떤 문제를 해결하는가? (Problem)
- 어떻게 문제를 해결할 것인가? (Solution)
- 성공을 어떻게 측정하는가? (Success Metrics)

모든 Phase, Design, Implementation은 이 GLOBAL_PURPOSE와 **지속적으로 정렬**되어야 합니다.

## 🚀 빠른 시작

### 사전 준비

[uv](https://github.com/astral-sh/uv) 설치 (권장):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 프로젝트 초기화

설치 없이 `uvx`로 바로 실행:

```bash
# 프로젝트 디렉토리에서
uvx --from git+https://github.com/nicered/purposely purposely init --lang ko

# 영어로 하려면
uvx --from git+https://github.com/nicered/purposely purposely init --lang en
```

> **참고**: PyPI 배포 후에는 `uvx purposely init --lang ko`로 간단하게 사용 가능합니다

이 명령은 다음을 생성합니다:
- `.purposely/config.json` - 프로젝트 설정
- `docs/` - 문서 디렉토리
- `.claude/` - Claude Code 슬래시 커맨드와 템플릿

### 문서 생성하기

`purposely create` 명령어로 문서를 생성합니다:

```bash
# GLOBAL_PURPOSE 생성
purposely create global-purpose

# 새 Phase 생성
purposely create spec 01

# 리서치 문서 생성
purposely create research 01 01 "기술 스택 조사"

# 디자인 문서 생성
purposely create design-overview 01
purposely create design 01 01 "UserService"

# 계획 및 구현 문서 생성
purposely create plan 01
purposely create implementation 01
```

### Claude Code와 함께 사용하기

Purposely는 **AI 협업 기반 개발**을 위해 설계되었습니다. 슬래시 커맨드로 대화형 문서 작성:

1. **GLOBAL_PURPOSE 생성**: `/purposely-init`
   - AI가 깊이 있는 질문으로 진짜 목적 파악
   - 모호한 답변 거부, 측정 가능한 메트릭 요구
   - 대화 기반으로 문서 작성

2. **Phase 시작**: `/purposely-phase`
   - AI가 먼저 GLOBAL_PURPOSE 읽고 정렬 검증
   - Scope creep 무자비하게 거부
   - 모든 목표가 GLOBAL_PURPOSE와 연결되는지 확인

3. **리서치 문서화**: `/purposely-research`
   - AI가 SPEC 대비 리서치 필요성 검증
   - Analysis paralysis 방지
   - 결과를 디자인 결정과 연결

4. **디자인 작성**: `/purposely-design`
   - AI가 GLOBAL_PURPOSE + SPEC + RESEARCH 모두 읽기
   - 과잉 엔지니어링 도전
   - Success Criteria 대비 디자인 검증

5. **계획 수립**: `/purposely-plan`
   - AI가 모든 이전 문서 읽기
   - 계획이 모든 Success Criteria 달성하는지 검증
   - 타임라인 실현 가능성 확인

6. **구현 추적**: `/purposely-implement`
   - AI가 실제 vs 계획 비교
   - 정직한 배움 추출
   - 다음 Phase를 위한 노트 준비

**AI는 정렬의 수호자입니다** - 모든 이전 문서를 읽고 GLOBAL_PURPOSE 대비 모든 결정을 검증합니다.

## 📁 문서 구조

```
your-project/
├── .purposely/
│   └── config.json
├── docs/
│   ├── GLOBAL_PURPOSE.md
│   └── phase-01/
│       ├── 00_SPEC.md
│       ├── 01_XX_RESEARCH_*.md
│       ├── 02_XX_DESIGN_*.md
│       ├── 03_PLAN.md
│       └── 04_IMPLEMENTATION.md
└── .claude/
    ├── commands/
    └── instructions.md
```

## 🌟 주요 기능

- **목적 중심 개발**: 모든 문서가 GLOBAL_PURPOSE를 참조
- **구조화된 문서화**: 명확한 계층 구조를 가진 7가지 문서 타입
- **다국어 지원**: 한국어와 영어
- **Claude Code 통합**: 슬래시 커맨드로 쉬운 문서 생성
- **일관성 검사**: AI가 자동으로 목적과의 정렬 여부 확인

## 📚 문서 타입

### GLOBAL_PURPOSE
프로젝트의 핵심 목적. **모든 것의 기반**.

### SPEC (00_SPEC.md)
각 Phase의 목표, 범위, 성공 기준 정의.

### RESEARCH (01_XX_RESEARCH_*.md)
리서치 및 조사 결과. 디자인 결정을 위한 근거.

### DESIGN (02_XX_DESIGN_*.md)
시스템 디자인. 어떻게 구현할 것인가?

### PLAN (03_PLAN.md)
구체적인 구현 계획. 일정, 의존성, 위험 요소.

### IMPLEMENTATION (04_IMPLEMENTATION.md)
실제 구현 로그. 무엇을 배웠는가? 계획과 어떻게 달랐는가?

## 🔧 개발

### 로컬 설치

```bash
git clone https://github.com/nicered/purposely
cd purposely

# uv 사용 (권장)
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"

# 또는 pip 사용
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### 테스트 실행

```bash
pytest tests/ -v
```

### 빌드

```bash
uv build
# 또는: python -m build
```

## 🤝 기여하기

Issue와 Pull Request를 환영합니다!

## 📄 라이센스

MIT License

## 🙏 감사의 말

Purposely는 개발자들이 목적을 잃지 않고 프로젝트를 완성할 수 있도록 돕기 위해 만들어졌습니다.

---

**Made with Purpose** ❤️
