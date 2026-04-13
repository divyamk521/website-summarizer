import streamlit as st
import requests
from bs4 import BeautifulSoup
import ollama

# Page config
st.set_page_config(page_title="Website Summarizer", page_icon="🌐")
st.title("🌐 Website Summarizer")
st.write("Paste multiple URLs and get instant AI summaries!")

# Functions
def get_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    return text[:2000]

def summarize(url, prompt):
    website = get_website_text(url)
    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes websites. Always respond in English."},
            {"role": "user", "content": prompt + "\n\n" + website}
        ]
    )
    return response["message"]["content"]

# UI
st.markdown("### Enter URLs")
st.write("Add one URL per line:")

urls_input = st.text_area(
    "URLs",
    placeholder="https://example.com\nhttps://wikipedia.org/wiki/Python\nhttps://edwarddonner.com",
    height=150
)

style = st.radio(
    "Choose summary style:",
    ["5 Bullet Points", "Short Paragraph", "Key Facts Only"]
)

styles = {
    "5 Bullet Points": "Summarize this in 5 bullet points in English",
    "Short Paragraph": "Summarize this in one short paragraph in English",
    "Key Facts Only": "List only the key facts in English"
}

save_to_file = st.checkbox("Save summaries to file")

if st.button("Summarize All 🚀"):
    urls = [url.strip() for url in urls_input.strip().split("\n") if url.strip()]
    
    if urls:
        all_summaries = ""
        
        for url in urls:
            st.markdown(f"---")
            st.markdown(f"**🔗 {url}**")
            
            with st.spinner(f"Summarizing {url}..."):
                try:
                    summary = summarize(url, styles[style])
                    st.markdown(summary)
                    all_summaries += f"URL: {url}\n{summary}\n{'─'*50}\n\n"
                except Exception as e:
                    st.error(f"Could not fetch {url} — {str(e)}")
        
        if save_to_file and all_summaries:
            with open("summaries.txt", "w") as f:
                f.write(all_summaries)
            st.success("✅ Summaries saved to summaries.txt!")
    else:
        st.warning("Please enter at least one URL!")