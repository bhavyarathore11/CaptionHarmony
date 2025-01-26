CSS_STYLE = """
    <style>
    body {{
        background-image: url('{bg_image}');
        background-size: cover;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        height: 100vh;
    }}
    .stApp {{
        background-color: rgba(0, 0, 0, 0);
        background-image: url('{bg_image}');
        background-size: cover;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0);
        padding: 0 1rem;
    }}
    h1, h2, h3, p {{
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        text-align: center;
    }}
    .stButton > button {{
        background-color: #ff6f61;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 20px;
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: #ff856b;
        box-shadow: 0px 4px 15px rgba(255, 111, 97, 0.4);
        transform: scale(1.05);
    }}
    .section-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    .footer {{
        text-align: center;
        color: white;
        margin-top: 30px;
        font-size: 14px;
    }}
    </style>
"""
