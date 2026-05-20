import streamlit as st


def header_home():
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <div style="height:104px; width:104px; display:grid; place-items:center; border-radius:28px; background:linear-gradient(135deg,#FDE68A,#2DD4BF); box-shadow:0 18px 38px rgba(0,0,0,0.22); border:3px solid rgba(255,255,255,0.75);">
                <svg width="66" height="66" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Smart attendance logo">
                    <rect x="10" y="12" width="46" height="34" rx="7" fill="#1D1029"/>
                    <rect x="15" y="17" width="36" height="24" rx="4" fill="#F8FAFC"/>
                    <path d="M21 27H34" stroke="#0F766E" stroke-width="4" stroke-linecap="round"/>
                    <path d="M21 34H29" stroke="#EC4899" stroke-width="4" stroke-linecap="round"/>
                    <circle cx="43" cy="32" r="6" fill="#F59E0B"/>
                    <path d="M29 52H37" stroke="#1D1029" stroke-width="5" stroke-linecap="round"/>
                    <path d="M22 56H44" stroke="#1D1029" stroke-width="5" stroke-linecap="round"/>
                </svg>
            </div>
            <h1 class='smart-title smart-title-home'>Smart<br/>Class</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <div style="height:78px; width:78px; display:grid; place-items:center; border-radius:22px; background:linear-gradient(135deg,#FDE68A,#2DD4BF); box-shadow:0 14px 30px rgba(15,118,110,0.18); border:2px solid rgba(255,255,255,0.8);">
                <svg width="50" height="50" viewBox="0 0 66 66" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Smart attendance logo">
                    <rect x="10" y="12" width="46" height="34" rx="7" fill="#1D1029"/>
                    <rect x="15" y="17" width="36" height="24" rx="4" fill="#F8FAFC"/>
                    <path d="M21 27H34" stroke="#0F766E" stroke-width="4" stroke-linecap="round"/>
                    <path d="M21 34H29" stroke="#EC4899" stroke-width="4" stroke-linecap="round"/>
                    <circle cx="43" cy="32" r="6" fill="#F59E0B"/>
                    <path d="M29 52H37" stroke="#1D1029" stroke-width="5" stroke-linecap="round"/>
                    <path d="M22 56H44" stroke="#1D1029" stroke-width="5" stroke-linecap="round"/>
                </svg>
            </div>
            <h2 class='smart-title smart-title-dashboard'>Smart<br/>Class</h2>
        </div>   
                
                """, unsafe_allow_html=True)
