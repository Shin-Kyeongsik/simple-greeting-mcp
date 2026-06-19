# Simple Greeting MCP Server

`FastMCP`를 사용하는 아주 작은 streamable HTTP MCP 서버입니다.

제공하는 tool은 `hello` 하나이며, 호출하면 다음 문장을 반환합니다.

```text
안녕하세요. 이 문장은 Render에 배포된 MCP 서버에서 온 응답입니다.
```

## 설치

```bash
pip install -r requirements.txt
```

## 실행

기본 포트는 `8000`입니다.

```bash
python3 server.py
```

포트를 바꾸려면 `PORT` 환경 변수를 지정합니다.

```bash
PORT=8080 python3 server.py
```

서버가 실행되면 다음 URL을 사용합니다.

```text
Health check: http://localhost:8000/health
MCP endpoint: http://localhost:8000/mcp
```

## Codex에 등록

streamable HTTP MCP 서버는 `url`로 등록합니다.

로컬 실행 서버를 등록하는 예시는 다음과 같습니다.

```toml
[mcp_servers.simple-greeting]
url = "http://localhost:8000/mcp"
```

Render에 배포한 경우에는 Render 서비스 URL의 `/mcp` 경로를 사용합니다.

```toml
[mcp_servers.simple-greeting]
url = "https://your-render-service.onrender.com/mcp"
```

설정 파일은 보통 `~/.codex/config.toml`에 둡니다. 프로젝트에만 적용하려면 신뢰된 프로젝트의 `.codex/config.toml`에 둘 수도 있습니다.

## 확인

헬스체크:

```bash
curl http://localhost:8000/health
```

응답 예시:

```json
{"status":"ok"}
```

Codex에서는 새 세션을 시작한 뒤 `/mcp`로 등록된 서버와 tool 목록을 확인할 수 있습니다.
