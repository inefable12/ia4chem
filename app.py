import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
ax.set_ylabel('Puntuación (0-10)')
ax.set_title('Comparación de Soporte de GPU por Sistema Operativo')
st.pyplot(fig)
