# Purposely 시작하기

## Purposely란?

Purposely는 개발팀이 전체 개발 생명주기 동안 프로젝트의 목적을 유지할 수 있도록 돕는 CLI 프레임워크입니다. Claude Code와 완벽하게 통합되어 구조화된 문서화와 워크플로우 관리를 제공합니다.

## 설치

### uvx 사용 (권장)

`uvx`를 사용하면 설치 없이 바로 실행할 수 있습니다:

```bash
uvx --from git+https://github.com/nicered/purposely purposely init
```

### 전역 설치

반복 사용을 위해 전역으로 설치:

```bash
pip install git+https://github.com/nicered/purposely
```

### Bash 별칭 (선택사항)

`~/.bashrc` 또는 `~/.zshrc`에 추가하면 더 쉽게 사용할 수 있습니다:

```bash
alias purposely="uvx --from git+https://github.com/nicered/purposely purposely"
```

## 빠른 시작

### 1. 프로젝트 초기화

새 프로젝트:

```bash
purposely init
```

기존 프로젝트:

```bash
purposely init --existing
```

다음 파일들이 생성됩니다:
- `.purposely/config.json` - 프로젝트 설정
- `.claude/` - Claude Code 통합 파일
- `docs/` - 문서 구조

### 2. 언어 설정

`.purposely/config.json`에서 원하는 언어 설정:

```json
{
  "language": "ko",  // 또는 "en"
  "version": "0.1.3"
}
```

### 3. 첫 페이즈 시작

Claude Code의 슬래시 커맨드 사용:

```
/purposely-phase
```

다음을 수행합니다:
- 새 개발 페이즈 생성
- SPEC 문서 생성
- 페이즈 목표 설정

## 다음 단계

- [워크플로우 가이드](workflow-ko.md) - 전체 개발 워크플로우 학습
- [명령어 레퍼런스](commands-ko.md) - 사용 가능한 모든 CLI 및 슬래시 명령어
- [베스트 프랙티스](best-practices-ko.md) - 효과적인 목적 중심 개발 팁

## 도움이 필요하신가요?

- [GitHub Issues](https://github.com/nicered/purposely/issues)
- [기여 가이드](https://github.com/nicered/purposely/blob/main/CONTRIBUTING.md)
