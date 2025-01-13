import streamlit as st

# Título y logo de la aplicación
st.image("img/neurona.jpg", use_container_width=True)  # Se cambió a use_container_width
st.title("¡Hola nuerona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")

    # Slider
    w = st.slider("Peso", min_value=0.0, max_value=5.0, value=1.0, step=0.01)

    # Input
    x = st.number_input("Introduzca el valor de la entrada", min_value=0.0, step=0.01)

    # Calculate button
    if st.button("Calcular la salida"):
        y = w * x
        st.write(f"La salida de la neurona es: {y:.2f}")

with tab2:
    st.header("Una neurona con dos entradas y dos pesos")

    # Weight Sliders
    w0 = st.slider("Peso w0", min_value=0.0, max_value=5.0, value=1.0, step=0.01)
    w1 = st.slider("Peso w1", min_value=0.0, max_value=5.0, value=1.0, step=0.01)

    # Inputs
    x0 = st.number_input("Entrada x0", min_value=0.0, step=0.01, key="x0")
    x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, key="x1")

    # Calculate button
    if st.button("Calcular la salida", key="calculate_tab2"):
        y = (w0 * x0) + (w1 * x1)
        st.write(f"La salida de la neurona es: {y:.2f}")

with tab3:
    st.header("Una neurona con tres entradas, tres pesos y sesgo")

    # Weight Sliders
    w0 = st.slider("Peso w0", min_value=0.0, max_value=5.0, value=1.0, step=0.01, key="w0_tab3")
    w1 = st.slider("Peso w1", min_value=0.0, max_value=5.0, value=1.0, step=0.01, key="w1_tab3")
    w2 = st.slider("Peso w2", min_value=0.0, max_value=5.0, value=1.0, step=0.01, key="w2_tab3")

    # Inputs
    x0 = st.number_input("Entrada x0", min_value=0.0, step=0.01, key="x0_tab3")
    x1 = st.number_input("Entrada x1", min_value=0.0, step=0.01, key="x1_tab3")
    x2 = st.number_input("Entrada x2", min_value=0.0, step=0.01, key="x2_tab3")

    # Bias input
    bias = st.number_input("Introduzca el valor del sesgo", min_value=0.0, step=0.01, key="bias_tab3")

    # Calculate button
    if st.button("Calcular la salida", key="calculate_tab3"):
        y = (w0 * x0) + (w1 * x1) + (w2 * x2) + bias
        st.write(f"La salida de la neurona es: {y:.2f}")