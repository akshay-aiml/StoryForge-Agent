import streamlit as st
from src.core import get_realtime_info, generate_video_transcription

st.set_page_config(
    page_title="StoryForge Agent",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

.stApp {
    background-color: #0D0F14 !important;
    font-family: 'DM Sans', sans-serif !important;
}
section[data-testid="stAppViewContainer"] {
    background-color: #0D0F14;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(99,102,241,0.18) 0%, transparent 70%),
        radial-gradient(ellipse 40% 30% at 80% 80%, rgba(20,184,166,0.10) 0%, transparent 60%);
}
.block-container {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
    max-width: 760px !important;
}
.hero-eyebrow {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.18em;
    text-transform: uppercase; color: #818CF8 !important; text-align: center;
}
.hero-title {
    font-family: 'DM Serif Display', serif; font-size: 2.8rem;
    font-weight: 400; color: #F1F2F7 !important; text-align: center; line-height: 1.15;
}
.hero-title .accent {
    background: linear-gradient(95deg, #818CF8 0%, #34D399 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-sub {
    font-size: 0.97rem; color: #7B7F96 !important; text-align: center;
    max-width: 500px; margin: 0 auto 2rem auto; line-height: 1.65;
}
.stTextInput label {
    font-size: 0.78rem !important; font-weight: 600 !important;
    letter-spacing: 0.08em !important; text-transform: uppercase !important; color: #5B5F76 !important;
}
.stTextInput input {
    background-color: #13161F !important; border: 1.5px solid #252836 !important;
    border-radius: 10px !important; color: #E2E4EC !important; font-size: 0.96rem !important;
}
.stTextInput input:focus {
    border-color: #6366F1 !important; box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}
.stButton button {
    background: linear-gradient(135deg, #6366F1, #4F46E5) !important;
    color: #fff !important; border: none !important; border-radius: 8px !important;
    font-weight: 600 !important; box-shadow: 0 2px 12px rgba(99,102,241,0.35) !important;
}
[data-testid="stDownloadButton"] button {
    background: transparent !important; color: #818CF8 !important;
    border: 1.5px solid #2E3148 !important; border-radius: 8px !important;
}
.sf-card {
    background: linear-gradient(160deg, #13161F 0%, #0F1219 100%);
    border: 1px solid #1E2130; border-top: 2px solid #6366F1;
    border-radius: 14px; padding: 1.5rem 1.75rem; margin: 1rem 0;
}
.sf-card-label {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em;
    text-transform: uppercase; color: #4E5272 !important; margin-bottom: 0.85rem;
}
.sf-card-body {
    font-size: 0.96rem; line-height: 1.75; color: #C2C5D6 !important; white-space: pre-wrap;
}
.sf-footer { font-size: 0.75rem; color: #3A3D52 !important; text-align: center; }
</style>
""", unsafe_allow_html=True)


def main():
    st.markdown("<p class='hero-eyebrow'>AI-Powered Research &amp; Storytelling</p>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Story<span class='accent'>Forge</span> Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-sub'>Search any topic and get AI-powered insights &amp; video scripts instantly.</p>", unsafe_allow_html=True)

    query = st.text_input("Topic or question", placeholder="e.g. Latest breakthroughs in quantum computing…")

    if query:
        with st.spinner("Gathering the latest information…"):
            info_result = get_realtime_info(query)

        if info_result:
            st.markdown(
                f"<div class='sf-card'>"
                f"<div class='sf-card-label'>✦ AI-Generated Summary</div>"
                f"<div class='sf-card-body'>{info_result}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

            generate_script = st.radio(
                "Generate a short video script?",
                ("No", "Yes"), index=0, horizontal=True
            )

            if generate_script == "Yes":
                with st.spinner("Crafting your video script…"):
                    script = generate_video_transcription(info_result)

                if script:
                    st.markdown(
                        f"<div class='sf-card'>"
                        f"<div class='sf-card-label'>▶ Video Script</div>"
                        f"<div class='sf-card-body'>{script}</div>"
                        f"</div>",
                        unsafe_allow_html=True
                    )
                    st.download_button("Download script", data=script, file_name="video_script.txt", mime="text/plain")
                else:
                    st.warning("Could not generate a video script. Please try again.")
        else:
            st.warning("No valid information found. Try a different query.")

    st.markdown("<hr style='border-top:1px solid #1A1D2A; margin:2rem 0'>", unsafe_allow_html=True)
    st.markdown("<p class='sf-footer'>Made with ♥</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()