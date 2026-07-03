from src.core.config import groq_client, tavily_client, MODEL


def get_realtime_info(query: str) -> str:
    """Fetch and summarize real-time info for a given topic."""
    try:
        resp = tavily_client.search(query=query, max_results=3, topic="general")
        if resp and resp.get("results"):
            summaries = []
            for r in resp["results"]:
                title = r.get("title", "")
                snippet = r.get("snippet", "")
                url = r.get("url", "")
                summaries.append(f"{title}\n\n{snippet}\n\n{url}")
            source_info = "\n\n---\n\n".join(summaries)
        else:
            source_info = f"No recent updates found on '{query}'."
    except Exception as e:
        return f"Error fetching info: {e}"

    prompt = f"""
You are a professional researcher and content creator with expertise in multiple fields.
Using the following real-time information, write an accurate, engaging, and human-like summary
for the topic: '{query}'.

Requirements:
- Keep it factual, insightful, and concise (around 200 words).
- Maintain a smooth, natural tone.
- Highlight key takeaways or trends.
- Avoid greetings or self-references.

Source information:
{source_info}

Output only the refined, human-readable content.
"""
    try:
        response = groq_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating summary: {e}"