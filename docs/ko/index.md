# Purposely

**목적 중심 개발 프레임워크**

Purposely는 개발팀이 전체 개발 생명주기 동안 프로젝트의 목적을 유지할 수 있도록 돕는 CLI 프레임워크입니다. Claude Code와 완벽하게 통합되어 구조화된 문서화와 워크플로우 관리를 제공합니다.

## ✨ 주요 기능

<div class="grid cards" markdown>

- :material-file-document: **구조화된 문서화**

    ---

    SPEC, 리서치, 디자인, 계획, 구현 문서를 일관된 형식으로 유지

- :material-sync: **페이즈 관리**

    ---

    명확한 목표와 결과물을 가진 관리 가능한 단계로 프로젝트를 나눔

- :material-robot: **AI 기반 협업**

    ---

    Claude Code용 커스텀 슬래시 커맨드로 목적 인식 개발 안내

- :material-translate: **다국어 지원**

    ---

    영어와 한국어 문서 및 워크플로우 완벽 지원

- :material-update: **자동 업그레이드**

    ---

    프로젝트 문서를 보존하면서 템플릿을 원활하게 업그레이드

- :material-code-braces: **기존 프로젝트 지원**

    ---

    기존 코드베이스에 목적 중심 문서화 추가 가능

</div>

## 🚀 빠른 시작

몇 초 만에 설치하고 초기화:

```bash
# uvx 사용 (권장)
uvx --from git+https://github.com/nicered/purposely purposely init

# 또는 전역 설치
pip install git+https://github.com/nicered/purposely
purposely init
```

## 📖 문서

- **[시작하기](getting-started.md)** - 설치 및 설정
- **[워크플로우 가이드](workflow.md)** - 완전한 개발 프로세스
- **[명령어 레퍼런스](commands.md)** - 모든 CLI 및 슬래시 명령어
- **[기여하기](../contributing.md)** - 기여 방법

## 🌏 English

English documentation is available [here](../).

## 🎯 왜 목적 중심 개발인가?

!!! success "집중력 유지"
    개발 전체 과정에서 프로젝트 목표를 절대 잃지 않습니다

!!! success "더 나은 결정"
    모든 선택이 프로젝트 목적에 따라 평가됩니다

!!! success "명확한 문서화"
    전체 스토리를 전달하는 구조화된 문서

!!! success "팀 정렬"
    모든 사람이 코드 뒤의 "왜"를 이해합니다

## 📦 설치 방법

=== "uvx (권장)"

    ```bash
    uvx --from git+https://github.com/nicered/purposely purposely init
    ```

=== "pip install"

    ```bash
    pip install git+https://github.com/nicered/purposely
    ```

=== "Bash 별칭"

    ```bash
    echo 'alias purposely="uvx --from git+https://github.com/nicered/purposely purposely"' >> ~/.bashrc
    ```

## 🔗 링크

- [GitHub 저장소](https://github.com/nicered/purposely)
- [이슈 보고](https://github.com/nicered/purposely/issues)
- [라이선스](https://github.com/nicered/purposely/blob/main/LICENSE)
