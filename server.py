import os

from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse


port = int(os.environ.get("PORT", "8000"))

mcp = FastMCP(
    "simple-greeting-mcp",
    host="0.0.0.0",
    port=port,
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def hello() -> str:
    """직접 만든 MCP 서버의 인사 응답을 반환합니다."""
    return "안녕하세요. 이 문장은 Render에 배포된 MCP 서버에서 온 응답입니다."


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    mcp.run(transport="streamable-http")