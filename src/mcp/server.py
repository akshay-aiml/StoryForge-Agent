from mcp.server.fastmcp import FastMCP
from src.core import get_realtime_info, generate_video_transcription

mcp = FastMCP("StoryForge Agent - Real-time news and video script generator")


@mcp.tool()
async def fetch_news_mcp(query: str) -> str:
    """Fetch and summarize real-time information for a given topic or question."""
    return get_realtime_info(query=query)


@mcp.tool()
async def generate_video_script_mcp(query: str) -> str:
    """Fetch real-time info on a topic and generate a short video script for it."""
    news = get_realtime_info(query=query)
    return generate_video_transcription(info_text=news)


if __name__ == "__main__":
    mcp.run(transport="stdio")