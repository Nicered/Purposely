# 시작하기

Purposely로 목적 중심 개발을 시작하는 단계별 가이드입니다.

## 설치

### 1. uv 설치 (권장)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Purposely 실행

설치 없이 바로 사용:

```bash
# 프로젝트 디렉토리에서
uvx --from git+https://github.com/nicered/purposely purposely init --lang ko
```

> PyPI 배포 후: `uvx purposely init --lang ko`

## 프로젝트 초기화

### Step 1: 프로젝트 구조 생성

```bash
cd your-project
uvx --from git+https://github.com/nicered/purposely purposely init --lang ko
```

생성되는 구조:
```
your-project/
├── .purposely/
│   └── config.json      # 언어 설정 등
├── docs/                # 문서 저장소
└── .claude/             # Claude Code 통합
    ├── commands/        # 슬래시 커맨드
    └── instructions.md  # AI 가이드
```

### Step 2: GLOBAL_PURPOSE 작성

이것이 **가장 중요한 단계**입니다.

#### CLI로 생성:

```bash
purposely create global-purpose
```

#### 또는 Claude Code에서:

```
/purposely-init
```

Claude가 다음 질문들을 통해 작성을 도와드립니다:

1. **왜 이 프로젝트를 만드나요?**
   - 어떤 불편함/문제를 겪었나요?
   - 기존 솔루션의 한계는?

2. **누가 사용하나요?**
   - 주 사용자는?
   - 어떤 상황에서 사용하나요?

3. **어떻게 문제를 해결하나요?**
   - 핵심 접근 방식은?
   - 차별화 포인트는?

4. **성공을 어떻게 측정하나요?**
   - 구체적인 지표는?
   - 언제 "성공했다"고 말할 수 있나요?

#### GLOBAL_PURPOSE 예시:

```markdown
# GLOBAL_PURPOSE

## Why
개발자들이 프로젝트 도중 목적을 잃고 불필요한 기능을 추가하다가
프로젝트를 완성하지 못하는 문제를 해결하기 위해

## Problem
- 초기에는 명확했던 목적이 개발 중 희미해짐
- Feature creep으로 범위가 무한정 확장됨
- 팀원마다 프로젝트 목적 이해도가 다름
- 완성하지 못한 채 방치되는 프로젝트들

## Solution
모든 개발 단계에서 GLOBAL_PURPOSE를 참조하도록 강제하는
문서화 프레임워크와 AI 어시스턴트 제공

## Success Metrics
- 사용자의 프로젝트 완성률 80% 이상
- 목적 이탈 기능 추가 10% 이하
- 문서 작성 시간 50% 단축 (AI 지원)
```

## Phase 1 시작

### Step 3: Phase 계획

프로젝트를 Phase로 나눕니다. 각 Phase는:
- **독립적으로 완성 가능**한 단위
- **GLOBAL_PURPOSE와 정렬**됨
- 1-4주 안에 완료 가능

#### Phase 1 SPEC 생성:

```bash
purposely create spec 01
```

또는 Claude Code에서:
```
/purposely-phase
```

#### SPEC 예시:

```markdown
# Phase 1 SPEC

## Objective
CLI를 통한 프로젝트 초기화 및 기본 문서 템플릿 제공

## Scope
- `purposely init` 명령어
- GLOBAL_PURPOSE 템플릿
- 한/영 i18n 지원
- Claude Code 슬래시 커맨드

## Out of Scope
- 웹 UI (Phase 2)
- AI 자동 검증 (Phase 3)

## Success Criteria
- [ ] init 명령어가 .purposely/, docs/, .claude/ 생성
- [ ] 한글/영어 템플릿 정상 작동
- [ ] Claude Code에서 슬래시 커맨드 사용 가능
```

### Step 4: 리서치 (선택적)

복잡한 결정이 필요하면 리서치 문서 작성:

```bash
purposely create research 01 01 "CLI 프레임워크 비교"
```

또는:
```
/purposely-research
```

### Step 5: 디자인

시스템 디자인을 문서화:

```bash
# 전체 디자인 개요
purposely create design-overview 01

# 개별 컴포넌트 디자인
purposely create design 01 01 "Initializer"
purposely create design 01 02 "TemplateRenderer"
```

또는:
```
/purposely-design
```

### Step 6: 구현 계획

```bash
purposely create plan 01
```

또는:
```
/purposely-plan
```

구현 계획에는:
- 작업 목록 (체크리스트)
- 의존성 관계
- 예상 일정
- 리스크와 대응책

### Step 7: 구현 및 추적

```bash
purposely create implementation 01
```

또는:
```
/purposely-implement
```

구현하면서 로그를 기록:
- 실제로 한 작업
- 계획과 달랐던 점
- 배운 점
- 다음 Phase를 위한 노트

## 워크플로우 요약

```
1. GLOBAL_PURPOSE 작성 (한 번만)
   ↓
2. Phase SPEC 작성 (각 Phase마다)
   ↓
3. RESEARCH (필요시)
   ↓
4. DESIGN
   ↓
5. PLAN
   ↓
6. IMPLEMENTATION
   ↓
7. 다음 Phase로
```

## 실전 팁

### ✅ Do

1. **GLOBAL_PURPOSE를 자주 읽어라**
   - 주 1회 이상 다시 읽기
   - 새 기능 추가 전 반드시 확인

2. **Phase를 작게 유지하라**
   - 1-4주 안에 완성 가능한 크기
   - 너무 크면 쪼개기

3. **문서를 먼저 작성하라**
   - 코드 작성 전 디자인 문서화
   - "일단 코딩"은 금물

4. **Claude Code를 활용하라**
   - 슬래시 커맨드로 대화형 작성
   - AI가 정렬 여부 자동 확인

### ❌ Don't

1. **GLOBAL_PURPOSE를 자주 바꾸지 마라**
   - 정말 근본적 문제라면 변경 가능
   - 하지만 신중히 결정

2. **문서를 건너뛰지 마라**
   - "나중에 쓰지 뭐" → 절대 안 씀
   - 지금 쓰지 않으면 영원히 안 씀

3. **Phase 범위를 무한정 늘리지 마라**
   - "하나만 더" → Feature creep의 시작
   - SPEC을 지켜라

4. **문서를 코드와 분리하지 마라**
   - 문서는 코드와 함께 버전 관리
   - 코드가 바뀌면 문서도 업데이트

## Claude Code 통합

Purposely는 Claude Code와 완벽히 통합됩니다.

### 사용 가능한 슬래시 커맨드:

| 커맨드 | 용도 | 생성 파일 |
|--------|------|-----------|
| `/purposely-init` | GLOBAL_PURPOSE 작성 | `docs/GLOBAL_PURPOSE.md` |
| `/purposely-phase` | Phase SPEC 작성 | `docs/phase-XX/00_SPEC.md` |
| `/purposely-research` | 리서치 문서 작성 | `docs/phase-XX/01_XX_RESEARCH_*.md` |
| `/purposely-design` | 디자인 문서 작성 | `docs/phase-XX/02_XX_DESIGN_*.md` |
| `/purposely-plan` | 구현 계획 작성 | `docs/phase-XX/03_PLAN.md` |
| `/purposely-implement` | 구현 로그 작성 | `docs/phase-XX/04_IMPLEMENTATION.md` |

### 슬래시 커맨드의 장점:

1. **대화형 작성**: Claude가 질문하며 내용 채움
2. **자동 검증**: GLOBAL_PURPOSE와 정렬 여부 확인
3. **컨텍스트 유지**: 이전 문서들 자동 참조
4. **시간 절약**: 템플릿 채우는 시간 50% 단축

## 다음 단계

- [문서 타입](document-types.md): 7가지 문서 타입 상세 설명
- [모범 사례](best-practices.md): 효과적인 PDD를 위한 팁
- [PDD란 무엇인가?](what-is-pdd.md): PDD 철학과 원칙

## 문제 해결

### Q: GLOBAL_PURPOSE를 어떻게 써야 할지 모르겠어요

A: Claude Code의 `/purposely-init`을 사용하세요. Claude가 질문을 통해 작성을 도와드립니다.

### Q: Phase를 어떻게 나눠야 하나요?

A: 다음 기준을 참고하세요:
- 1-4주 안에 완성 가능
- 독립적으로 테스트/배포 가능
- 명확한 성공 기준 존재

### Q: 모든 문서를 다 써야 하나요?

A: 필수는 GLOBAL_PURPOSE, SPEC, IMPLEMENTATION입니다. RESEARCH는 복잡한 결정이 필요할 때만, DESIGN은 시스템이 복잡할 때만 작성하세요.

### Q: 혼자 하는 프로젝트에도 유용한가요?

A: 오히려 더 유용합니다! 혼자 할 때 목적을 잃기 쉽기 때문입니다.

---

**다음**: [문서 타입 상세 설명](document-types.md)
