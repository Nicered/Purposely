# 문서 타입

Purposely의 7가지 문서 타입에 대한 상세 설명입니다.

## 문서 계층 구조

```
GLOBAL_PURPOSE (프로젝트 전체)
    ├── Phase 01/
    │   ├── 00_SPEC.md
    │   ├── 01_XX_RESEARCH_*.md
    │   ├── 02_00_DESIGN_OVERVIEW.md
    │   ├── 02_XX_DESIGN_*.md
    │   ├── 03_PLAN.md
    │   └── 04_IMPLEMENTATION.md
    ├── Phase 02/
    │   └── ...
    └── Phase 03/
        └── ...
```

## 1. GLOBAL_PURPOSE

### 목적
프로젝트의 **존재 이유**를 정의합니다. 모든 문서의 기준점입니다.

### 언제 작성하나요?
프로젝트 시작 시 **단 한 번**만 작성합니다.

### 필수 섹션

#### Why
왜 이 프로젝트가 존재하는가?

**작성 팁:**
- 개인적 동기부터 시작
- "이런 게 있으면 좋겠다" 보다 "이런 문제가 있다"
- 한 문장으로 요약 가능해야 함

**예시:**
```markdown
## Why
개발자들이 프로젝트를 시작하지만 완성하지 못하는 문제를 해결하기 위해
```

#### Problem
구체적으로 어떤 문제를 해결하나?

**작성 팁:**
- 3-5개의 구체적 pain point
- "누가, 언제, 어떤 상황에서" 경험하는지
- 측정 가능한 문제라면 더 좋음

**예시:**
```markdown
## Problem
- 초기 열정으로 프로젝트를 시작하지만 70%가 완성하지 못함
- 개발 도중 "왜 만드는지"를 잊고 불필요한 기능 추가
- 팀 프로젝트에서 구성원마다 목적 이해도가 다름
- 기술 선택에만 집중하고 비즈니스 목적을 망각
```

#### Solution
어떻게 그 문제를 해결하나?

**작성 팁:**
- HOW보다 WHAT에 집중
- 핵심 접근 방식 1-2문장
- 차별화 포인트 명확히

**예시:**
```markdown
## Solution
모든 개발 단계에서 GLOBAL_PURPOSE를 참조하도록 강제하는
문서 중심 프레임워크와 AI 어시스턴트
```

#### Success Metrics
성공을 어떻게 측정하나?

**작성 팁:**
- 정량적 지표 우선
- 측정 가능해야 함
- 3-5개 핵심 지표

**예시:**
```markdown
## Success Metrics
- 사용자의 프로젝트 완성률 80% 이상
- 목적 이탈 기능 추가 10% 이하
- 문서 작성 시간 50% 단축 (vs 수동)
- 월 활성 사용자 1,000명
```

### 생성 명령어
```bash
purposely create global-purpose
# 또는
/purposely-init
```

---

## 2. SPEC (00_SPEC.md)

### 목적
각 Phase의 **목표와 범위**를 정의합니다.

### 언제 작성하나요?
각 Phase 시작 전에 작성합니다.

### 필수 섹션

#### Objective
이 Phase에서 달성할 목표

**예시:**
```markdown
## Objective
CLI 도구를 통한 프로젝트 초기화 및 기본 템플릿 제공
```

#### Scope
이 Phase에 **포함되는** 것

**예시:**
```markdown
## Scope
- `purposely init` 명령어 구현
- GLOBAL_PURPOSE.md 템플릿
- 한글/영어 i18n 지원
- .claude/ 디렉토리 및 슬래시 커맨드 생성
```

#### Out of Scope
이 Phase에 **포함되지 않는** 것

**중요:** 이게 없으면 범위가 계속 확장됩니다!

**예시:**
```markdown
## Out of Scope
- 웹 UI (Phase 2에서)
- AI 자동 검증 (Phase 3에서)
- GitHub 통합 (Phase 4에서)
```

#### Success Criteria
Phase 완료 기준 (체크리스트)

**예시:**
```markdown
## Success Criteria
- [ ] `purposely init` 실행 시 .purposely/, docs/, .claude/ 생성
- [ ] 한글 템플릿 정상 렌더링
- [ ] 영어 템플릿 정상 렌더링
- [ ] Claude Code에서 6개 슬래시 커맨드 작동
- [ ] pytest 통과율 100%
```

#### Alignment with GLOBAL_PURPOSE
GLOBAL_PURPOSE와 어떻게 연결되는지

**예시:**
```markdown
## Alignment with GLOBAL_PURPOSE
이 Phase는 "문서 중심 프레임워크 제공"이라는 Solution의
핵심 인프라를 구축함. 사용자가 쉽게 시작할 수 있게 함으로써
"프로젝트 완성률 80%" 목표에 기여.
```

### 생성 명령어
```bash
purposely create spec 01
# 또는
/purposely-phase
```

---

## 3. RESEARCH (01_XX_RESEARCH_*.md)

### 목적
중요한 결정을 위한 **조사 및 근거**를 문서화합니다.

### 언제 작성하나요?
- 기술 스택 선택 시
- 아키텍처 패턴 결정 시
- 알고리즘 선택 시
- 불확실성이 높은 결정 시

### 필수 섹션

#### Research Question
무엇을 알아내고자 하는가?

**예시:**
```markdown
## Research Question
Python CLI 프레임워크 중 무엇을 사용할 것인가?
```

#### Methodology
어떻게 조사했는가?

**예시:**
```markdown
## Methodology
- Click, Typer, argparse 비교
- GitHub stars, 유지보수 현황 확인
- 각 프레임워크로 POC 구현
- 문서 품질 및 커뮤니티 크기 평가
```

#### Findings
발견한 사실들

**예시:**
```markdown
## Findings

### Click
- Pros: 성숙함, 풍부한 기능, 많은 사용 사례
- Cons: 데코레이터 스타일

### Typer
- Pros: 타입 힌트 기반, 현대적
- Cons: Click에 비해 생태계 작음

### argparse
- Pros: 표준 라이브러리
- Cons: 보일러플레이트 많음
```

#### Decision
최종 결정과 이유

**예시:**
```markdown
## Decision
Click을 선택

**이유:**
1. 성숙도와 안정성
2. 풍부한 플러그인 생태계
3. pytest와의 좋은 통합
4. 데코레이터 스타일이 이 프로젝트에 적합
```

### 생성 명령어
```bash
purposely create research 01 01 "CLI Framework Comparison"
# 또는
/purposely-research
```

---

## 4. DESIGN_OVERVIEW (02_00_DESIGN_OVERVIEW.md)

### 목적
Phase 전체의 **아키텍처 및 설계 개요**

### 언제 작성하나요?
복잡한 Phase에서 상세 디자인 문서 작성 전

### 필수 섹션

#### Architecture
전체 구조

**예시:**
```markdown
## Architecture

```
┌─────────────┐
│     CLI     │
└──────┬──────┘
       │
   ┌───┴────┐
   │ Core   │
   └───┬────┘
       │
┌──────┼──────┐
│      │      │
Initializer Renderer Creator
```
```

#### Components
주요 컴포넌트와 책임

**예시:**
```markdown
## Components

### CLI (cli.py)
- Click 기반 명령어 인터페이스
- 사용자 입력 파싱
- Core 컴포넌트 호출

### Initializer
- 프로젝트 구조 생성
- 설정 파일 초기화

### TemplateRenderer
- Jinja2 기반 템플릿 렌더링
- i18n 처리
```

### 생성 명령어
```bash
purposely create design-overview 01
# 또는
/purposely-design
```

---

## 5. DESIGN_DETAIL (02_XX_DESIGN_*.md)

### 목적
개별 컴포넌트/모듈의 **상세 설계**

### 언제 작성하나요?
각 주요 컴포넌트마다 작성

### 필수 섹션

#### Purpose
이 컴포넌트의 목적

#### Interface
공개 API/메서드

**예시:**
```python
class TemplateRenderer:
    def __init__(self, lang: str)
    def render(self, template_name: str, **context) -> str
    def render_to_file(self, template_name: str, output_path: Path, **context)
```

#### Implementation Details
내부 구현 방식

#### Dependencies
의존하는 다른 컴포넌트

### 생성 명령어
```bash
purposely create design 01 01 "TemplateRenderer"
# 또는
/purposely-design
```

---

## 6. PLAN (03_PLAN.md)

### 목적
구현 작업의 **구체적 계획**

### 필수 섹션

#### Tasks
작업 목록 (체크리스트)

**예시:**
```markdown
## Tasks

### Phase 1: Core Infrastructure
- [ ] 프로젝트 구조 설정 (pyproject.toml, etc.)
- [ ] CLI 진입점 생성
- [ ] Initializer 구현
  - [ ] 디렉토리 생성 로직
  - [ ] config.json 생성
  - [ ] 템플릿 파일 복사

### Phase 2: Template System
- [ ] TemplateRenderer 구현
- [ ] i18n 파일 작성 (en.json, ko.json)
- [ ] Jinja2 템플릿 작성

### Phase 3: Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] CI/CD 설정
```

#### Timeline
예상 일정

#### Dependencies
작업 간 의존성

#### Risks
예상 위험과 대응책

### 생성 명령어
```bash
purposely create plan 01
# 또는
/purposely-plan
```

---

## 7. IMPLEMENTATION (04_IMPLEMENTATION.md)

### 목적
실제 구현 과정과 결과를 **로깅**

### 필수 섹션

#### What Was Done
실제로 한 작업

#### What Changed from Plan
계획과 달라진 점

**중요:** 이게 가장 가치 있는 섹션입니다!

**예시:**
```markdown
## What Changed from Plan

### Jinja2 필터 추가
계획에 없었으나 날짜 포맷팅을 위해 커스텀 필터 추가 필요

### importlib.resources 사용
원래 pkg_resources 사용 예정이었으나
Python 3.10+ 에서 importlib.resources가 표준이므로 변경
```

#### Lessons Learned
배운 점

#### Notes for Next Phase
다음 Phase를 위한 메모

### 생성 명령어
```bash
purposely create implementation 01
# 또는
/purposely-implement
```

---

## 문서 작성 순서

### 필수 순서:
```
GLOBAL_PURPOSE (한 번만)
↓
SPEC (각 Phase 시작 시)
↓
[선택] RESEARCH (필요시)
↓
[선택] DESIGN (복잡한 경우)
↓
PLAN
↓
IMPLEMENTATION (구현하며 작성)
```

### 최소 구성:
간단한 Phase라면:
- SPEC
- PLAN
- IMPLEMENTATION

만 작성해도 됩니다.

### 복잡한 Phase:
- SPEC
- RESEARCH (여러 개 가능)
- DESIGN_OVERVIEW
- DESIGN_DETAIL (여러 개 가능)
- PLAN
- IMPLEMENTATION

---

## 문서 작성 원칙

### 1. GLOBAL_PURPOSE를 항상 참조
모든 문서에 "Alignment with GLOBAL_PURPOSE" 섹션

### 2. 구체적으로 작성
추상적 표현 금지. 측정 가능하게.

### 3. 미래의 자신을 위해 작성
6개월 후 이 문서만 보고 이해할 수 있어야 함

### 4. 코드보다 먼저 작성
문서 → 코드 순서

### 5. 변경 시 함께 업데이트
코드가 바뀌면 문서도 업데이트

---

**다음:** [모범 사례](best-practices.md)
