import streamlit as st
from query_data import query_rag
import os

# Configuración de la página
st.set_page_config(
    page_title="Agente de Ayuda",
    page_icon="🎲",
    layout="centered"
)

# Título y descripción
st.title("Agente de Ayuda")
st.markdown("""
Este sistema te permite hacer preguntas sobre los documentos de la empresa.
""")

# Sidebar para información adicional
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    ### ¿Cómo funciona?
    1. Escribe tu pregunta en el campo de texto
    2. El sistema buscará información relevante en la base de datos
    3. Enviar la pregunta al agente (Enviar pregunta)
    4. Se generará una respuesta basada en el contexto encontrado
    """)
    
    # Verificar si la base de datos existe
    if not os.path.exists("chroma"):
        st.warning("⚠️ La base de datos no está inicializada. Por favor, ejecuta `populate_database.py` primero.")

# Campo de entrada para la pregunta
question = st.text_input(
    "¿Qué te gustaría saber sobre la empresa?",
    placeholder="Ej: ¿Cuáles son los productos de la empresa?"
)

# Botón para enviar la pregunta
if st.button("Enviar pregunta"):
    if question:
        with st.spinner("Buscando información y generando respuesta..."):
            try:
                # Obtener la respuesta
                response = query_rag(question)
                
                # Mostrar la respuesta
                st.markdown("### Respuesta:")
                st.write(response)
                
            except Exception as e:
                st.error(f"Ocurrió un error: {str(e)}")
    else:
        st.warning("Por favor, ingresa una pregunta.")

# Footer
st.markdown("---")
st.markdown("Desarrollado por @2AQ") 