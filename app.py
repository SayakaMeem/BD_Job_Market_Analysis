import streamlit as st
import pathlib
import warnings
import pandas as pd
import os
import datetime

# Suppress that yellow deprecation warning
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide", page_title="BD Job Market Intelligence 2026", page_icon="🇧🇩")

html_path = pathlib.Path("Bd-Job-Market-Dashboard.html")

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    
    # Renders 100% like my premium demo - 500 / 39,085 / 68.2%
    st.components.v1.html(html_content, height=1200, scrolling=True)

    # --- LIVE BACKEND SYNC CHECKER ---
    st.markdown("---")
    st.subheader("🔴 LIVE BACKEND CHECK — Is Dashboard in sync with CSV?")
    
    try:
        csv_path = pathlib.Path("data/cleaned_jobs.csv")
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            
            backend_total = len(df)
            backend_avg = df["salary_avg"].mean() if "salary_avg" in df.columns else 0
            backend_remote = len(df[df["location"] == "Remote"]) if "location" in df.columns else 0
            last_mod = datetime.datetime.fromtimestamp(os.path.getmtime(csv_path)).strftime("%Y-%m-%d %H:%M:%S")

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Backend Total Jobs", backend_total)
            c2.metric("Backend Avg Salary", f"{backend_avg:.0f} BDT")
            c3.metric("Backend Remote", backend_remote)
            c4.metric("CSV Last Updated", last_mod)

            # Compare with frontend static values (from your HTML)
            frontend_total = 500
            frontend_avg = 39085

            if backend_total == frontend_total and int(backend_avg) == frontend_avg:
                st.success(f"✅ SYNCED — Frontend ({frontend_total} / {frontend_avg}) matches Backend CSV ({backend_total} / {backend_avg:.0f}). Dashboard is keeping pace!")
            else:
                st.error(f"❌ OUT OF SYNC — Frontend says {frontend_total} / {frontend_avg} but Backend CSV is {backend_total} / {backend_avg:.0f}. Run analysis.py to regenerate Bd-Job-Market-Dashboard.html")
        else:
            st.warning("⚠️ data/cleaned_jobs.csv not found — cannot check backend sync")
    except Exception as e:
        st.warning(f"Backend check failed: {e}")

else:
    st.error("Bd-Job-Market-Dashboard.html not found - make sure file is in same folder as app.py")