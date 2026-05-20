import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #1D1029 0%, #0F766E 46%, #F59E0B 100%) !important;
                    color: #F8FAFC !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255, 255, 255, 0.90) !important;
                    padding:2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(255,255,255,0.45) !important;
                    box-shadow: 0 24px 60px rgba(29, 16, 41, 0.24) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #F8FAFC 0%, #E0F2FE 38%, #FCE7F3 100%) !important;
                    color: #1E293B !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500..700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            .smart-title {
                font-family: 'Fredoka', sans-serif !important;
                font-weight: 700 !important;
                line-height: 1.05 !important;
                margin: 0 !important;
                background: linear-gradient(90deg, #FDE68A, #F472B6, #2DD4BF, #FDE68A);
                background-size: 300% 100%;
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent !important;
                animation: smart-title-flow 5s ease-in-out infinite;
                text-shadow: 0 10px 28px rgba(0, 0, 0, 0.16);
            }

            .smart-title-home {
                text-align:center;
                font-size: 3.8rem !important;
            }

            .smart-title-dashboard {
                text-align:left;
                font-size: 2.1rem !important;
            }

            .smart-footer {
                margin-top: 2rem;
                display:flex;
                justify-content:center;
                align-items:center;
            }

            .smart-footer-text {
                font-family: 'Outfit', sans-serif;
                font-weight: 900;
                letter-spacing: 0;
                margin: 0;
                background: linear-gradient(90deg, #F59E0B, #EC4899, #14B8A6, #F59E0B);
                background-size: 260% 100%;
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent !important;
                animation: smart-title-flow 4s ease-in-out infinite;
            }

            @keyframes smart-title-flow {
                0%, 100% { background-position: 0% 50%; transform: translateY(0); }
                50% { background-position: 100% 50%; transform: translateY(-2px); }
            }

            h1 {
                font-family: 'Fredoka', sans-serif !important;
                font-weight: 700 !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Fredoka', sans-serif !important;
                font-weight: 700 !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #1D1029 !important;
            }

            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2,
            .stApp div[data-testid="stColumn"] h3,
            .stApp div[data-testid="stColumn"] p {
                color: #1D1029 !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            h3 {
                color: #1D1029 !important;
            }

            div[data-testid="stTextInput"] label,
            div[data-testid="stTextInput"] label *,
            div[data-testid="stTextInput"] p,
            div[data-testid="stTextInput"] span {
                color: #1D1029 !important;
                -webkit-text-fill-color: #1D1029 !important;
                font-weight: 700 !important;
            }

            div[data-testid="stTextInput"] input {
                background: #272936 !important;
                color: #F8FAFC !important;
                -webkit-text-fill-color: #F8FAFC !important;
                border: 1px solid rgba(29, 16, 41, 0.24) !important;
            }

            div[data-testid="stTextInput"] input::placeholder {
                color: #A8B0C0 !important;
                -webkit-text-fill-color: #A8B0C0 !important;
                opacity: 1 !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background: linear-gradient(135deg, #0F766E, #14B8A6) !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0 10px 24px rgba(15, 118, 110, 0.25) !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button p,
            button span,
            button div {
                color: white !important;
            }

            div[data-testid="stButton"] button,
            div[data-testid="stButton"] button *,
            button[kind="tertiary"],
            button[kind="tertiary"] *,
            button[data-testid="stBaseButton-tertiary"],
            button[data-testid="stBaseButton-tertiary"] * {
                color: white !important;
                -webkit-text-fill-color: white !important;
            }

            div[data-testid="stButton"] button svg,
            div[data-testid="stButton"] button svg * {
                color: white !important;
                fill: currentColor !important;
                stroke: currentColor !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background: linear-gradient(135deg, #EC4899, #F97316) !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0 10px 24px rgba(236, 72, 153, 0.22) !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background: #1D1029 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.04);
                box-shadow: 0 14px 30px rgba(29, 16, 41, 0.26) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
