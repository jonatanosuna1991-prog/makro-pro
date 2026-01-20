import streamlit as st

st.set_page_config(page_title="makro PRO", layout="centered")
st.markdown("<h1 style='text-align: center; color: #b30000;'>🥩 makro PRO</h1>", unsafe_allow_html=True)

# ENTRADAS
c1, c2 = st.columns(2)
peso_res = c1.number_input("Peso Media Res (kg)", value=115.630, format="%.3f")
costo_act = c2.number_input("Costo $/kg Hoy", value=6500)
nuevo_c = st.number_input("SIMULAR COSTO NUEVO ($/kg)", value=7200)

st.divider()

cortes = [
    ("NALGA", 4.520, 18200.0), ("VACIO", 3.650, 18799.0),
    ("ASADO", 8.715, 15999.0), ("MATAMBRE", 1.325, 14999.0),
    ("PECETO", 1.600, 19500.0), ("HUESO PELADO", 7.515, 390.0)
]

total_kg = 0
for nombre, kg_d, p_d in cortes:
    with st.expander(f"🍖 {nombre}", expanded=True):
        col_a, col_b = st.columns(2)
        k = col_a.number_input(f"Kilos {nombre}", value=kg_d, key=f"k_{nombre}")
        p = col_b.number_input(f"Precio {nombre}", value=p_d, key=f"p_{nombre}")
        ind = p / costo_act if costo_act > 0 else 0
        st.error(f"💰 SUGERIDO: ${nuevo_c * ind:,.0f}")
        total_kg += k

st.divider()
st.metric("MERMA TOTAL", f"{peso_res - total_kg:.2f} kg")
