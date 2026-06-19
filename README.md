# Simple Greeting MCP Server

`FastMCP`를 사용하는 아주 작은 stdio MCP 서버입니다.

제공하는 tool은 `hello` 하나이며, 호출하면 다음 문장을 반환합니다.

```text
안녕하세요. 이 문장은 직접 만든 MCP 서버에서 온 응답입니다.
```

## 실행

`mcp` 패키지가 필요합니다.

```bash
pip install -r requirements.txt
```

```bash
python3 server.py
```

MCP 클라이언트 설정 예시는 다음과 같습니다.

```json
{
  "mcpServers": {
    "simple-greeting": {
      "command": "python3",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

## 수동 테스트

```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"manual","version":"0.1.0"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
  '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"hello","arguments":{}}}' \
  | python3 server.py
```
