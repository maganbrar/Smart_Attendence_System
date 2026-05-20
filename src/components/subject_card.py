import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:rgba(255,255,255,0.92); border-left: 8px solid #14B8A6; padding:25px; border-radius: 18px; border: 1px solid rgba(15,118,110,0.18); box-shadow: 0 18px 45px rgba(29,16,41,0.10); margin-bottom:20px;">
        <h3 style="margin:0; color: #1D1029; font-size: 1.5rem ">{name}</h3>
        <p style="color:#475569; margin:10px 0;">Code : <span style="background:#CCFBF1; color:#0F766E; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #FCE7F3; color:#831843; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
