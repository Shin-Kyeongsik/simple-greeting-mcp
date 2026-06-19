#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("simple-greeting-mcp")


@mcp.tool()
def hello() -> str:
    """직접 만든 MCP 서버의 인사 응답을 반환합니다."""
    return "안녕하세요. 이 문장은 직접 만든 MCP 서버에서 온 응답입니다."


if __name__ == "__main__":
    mcp.run(transport="stdio")
