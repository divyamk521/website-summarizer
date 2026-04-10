# 🌐 Website Summarizer

A simple AI-powered tool that scrapes any website and summarizes it using a local LLM — built entirely with free and open-source tools.

---

## 🛠️ Tech Stack
- **Python** — core language
- **BeautifulSoup4** — web scraping
- **Ollama + TinyLlama** — local AI summarization (free, runs offline)
- **Jupyter Notebook** — development environment

---

## 💡 How It Works
1. Takes any URL as input
2. Scrapes and cleans the webpage text
3. Sends it to a local LLM (TinyLlama via Ollama)
4. Returns a clean 5-bullet summary

---

## 🚀 How To Run This Project

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/website-summarizer.git
cd website-summarizer
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install Ollama and pull the model**
- Download Ollama from [ollama.com](https://ollama.com)
```bash
ollama pull tinyllama
```

**5. Run the notebook**
- Open `summarizer.ipynb` in VS Code and run all cells

---

## 📁 Project Structure
website-summarizer/
├── venv/                  # virtual environment (not pushed to GitHub)
├── summarizer.ipynb       # main notebook
├── requirements.txt       # dependencies
└── README.md              # you are here

---

## 🙋‍♀️ Author
**Divya M K** — [GitHub](https://github.com/divyamk521) 
<!-- | [LinkedIn](https://linkedin.com/in/yourprofile) -->

> 🌱 First project in my AI/ML learning journey