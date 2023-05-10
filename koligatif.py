import streamlit as st
import time

st.title('Aplikasi Sifat Koligatif Larutan')

option = st.selectbox(
    'Pilih jenis perhitungan dalam sifat koligatif larutan',
    ('Penurunan Tekanan Uap (ΔP)', 'Penurunan Titik Beku (ΔTf)', 'Kenaikan Titik Didih (ΔTb)', 'Tekanan Osmosis (π)'))

#Penurunan Tekanan Uap
if option == 'Penurunan Tekanan Uap (ΔP)':
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'))
    if Jenis_larutan == 'Larutan Non Elektrolit':
        nt = st.number_input('Mol zat terlarut (nt)')
        np = st.number_input('Mol zat pelarut (np)')
        P = st.number_input('Tekanan uap jenuh pelarut murni (P°)')
        if st.button('Hitung Penurunan Tekanan Uap (ΔP)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_P = (nt/(nt+np))*P
            st.success(f'Penurunan Tekanan Uap (ΔP) adalah: {delta_P} mmHg')
    if Jenis_larutan == 'Larutan Elektrolit':
        nt = st.number_input('Mol zat terlarut (nt)')
        np = st.number_input('Mol zat pelarut (np)')
        P = st.number_input('Tekanan uap jenuh pelarut murni (P°)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hitung Penurunan Tekanan Uap (ΔP)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_P = (nt/(nt+np))*P*(1+(n-1)*alfa)
            st.success(f'Penurunan Tekanan Uap (ΔP) adalah: {delta_P} mmHg')

#Penurunan Titik Beku
if option == 'Penurunan Titik Beku (ΔTf)':
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'))
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kf = st.number_input('Tetapan penurunan titik beku zat pelarut (Kf)')
        if st.button('Hitung Penurunan Titik Beku (ΔTf)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tf = ((massa/Mr)*(1000/P))*Kf
            st.success(f'Penurunan Titik Beku (ΔTf) adalah: {delta_Tf} °C')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kf = st.number_input('Tetapan penurunan titik beku zat pelarut (Kf)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hitung Penurunan Titik Beku (ΔTf)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tf = ((massa/Mr)*(1000/P))*Kf*(1+(n-1)*alfa)
            st.success(f'Penurunan Titik Beku (ΔTf) adalah: {delta_Tf} °C')

#Kenaikan Titik Didih
if option == 'Kenaikan Titik Didih (ΔTb)':
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'))
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kb = st.number_input('Tetapan kenaikan titik didih zat pelarut (Kb)')
        if st.button('Hitung Kenaikan Titik Didih (ΔTb)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tb = ((massa/Mr)*(1000/P))*Kb
            st.success(f'Kenaikan Titik Didih (ΔTb) adalah: {delta_Tb} °C')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kb = st.number_input('Tetapan kenaikan titik didih zat pelarut (Kb)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hitung Kenaikan Titik Didih (ΔTb)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tb = ((massa/Mr)*(1000/P))*Kb*(1+(n-1)*alfa)
            st.success(f'Kenaikan Titik Didih (ΔTf) adalah: {delta_Tb} °C')
            
#Tekanan Osmosis
if option == 'Tekanan Osmosis (π)':
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'))
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        V = st.number_input('Volume larutan (mL)')
        T = st.number_input('Suhu mutlak (K)')
        if st.button('Hitung Tekanan Osmosis (π)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            phi = ((massa/Mr)*(1000/V))*0.082*T
            st.success(f'Kenaikan Tekanan Osmosis (π) adalah: {phi} atm')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        V = st.number_input('Volume larutan (mL)')
        T = st.number_input('Suhu mutlak (K)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hitung Tekanan Osmosis (π)'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            phi = ((massa/Mr)*(1000/V))*0.082*T*(1+(n-1)*alfa)
            st.success(f'Kenaikan Tekanan Osmosis (π) adalah: {phi} atm')