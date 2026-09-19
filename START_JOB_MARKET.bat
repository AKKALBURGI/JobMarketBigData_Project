@echo off
title Job Market Analytics - Big Data Project

cd /d D:\JobMarketBigData_Project

echo ================================================
echo       JOB MARKET ANALYTICS - BIG DATA
echo ================================================
echo.
echo Starting Streamlit application...
echo.

D:\JobMarketBigData_Project\venv\Scripts\python.exe -m streamlit run app.py

pause