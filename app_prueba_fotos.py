import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Prueba independiente de fotografías", page_icon="📷")
st.title("Prueba independiente de carga de fotografías")
st.write(
    "Esta página prueba únicamente el selector de archivos de Streamlit. "
    "No utiliza Cloudinary, Google Sheets ni el formulario inmobiliario."
)

st.info("Selecciona primero una fotografía JPG o PNG desde el teléfono.")

archivos = st.file_uploader(
    "Seleccionar fotografía",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True,
    key="prueba_independiente_fotos",
)

if archivos is None:
    st.warning("El selector devolvió un valor None.")
elif len(archivos) == 0:
    st.warning("Streamlit todavía no ha recibido ningún archivo.")
else:
    st.success(f"Streamlit recibió {len(archivos)} archivo(s).")
    for indice, archivo in enumerate(archivos, start=1):
        st.markdown(f"### Fotografía {indice}")
        st.write("Nombre:", archivo.name)
        st.write("Tipo MIME:", archivo.type)
        st.write("Tamaño:", f"{archivo.size:,} bytes")
        try:
            contenido = archivo.getvalue()
            st.write("Bytes recibidos:", len(contenido))
            imagen = Image.open(BytesIO(contenido))
            imagen.verify()
            imagen = Image.open(BytesIO(contenido))
            st.image(imagen, caption=archivo.name, use_container_width=True)
            st.success(f"Imagen válida: {imagen.format}, {imagen.width} × {imagen.height} píxeles.")
        except Exception as error:
            st.error(f"El archivo llegó, pero no se pudo interpretar como imagen: {type(error).__name__}: {error}")

st.divider()
st.caption("Diagnóstico: si aparece el nombre, el tipo y el tamaño, el selector funciona. "
           "Si no aparece ningún archivo después de seleccionarlo, el problema está en la entrega "
           "del archivo al componente o en el navegador/dispositivo.")
