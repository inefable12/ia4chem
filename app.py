import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gpu_data = {
    'Sistemas Operativos': ['Linux', 'Windows', 'macOS'],
    'Soporte Manual de GPU (NVIDIA/AMD)': [8, 9, 5],
    'Optimización para Computación Científica': [9, 7, 4],
    'Facilidad de Integración con eGPU': [6, 8, 9]
}

df_gpu = pd.DataFrame(gpu_data)

fig, ax = plt.subplots()
df_gpu.set_index('Sistemas Operativos').plot(kind='bar', ax=ax)
ax.set_ylabel('Puntuación (0-10)')
ax.set_title('Comparación de Soporte de GPU por Sistema Operativo')
st.pyplot(fig)

if __name__ == "__main__":
    main()
