import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Função para gerar amostras e calcular médias amostrais
def gerar_amostras_e_medias(dist_func, n, m, *params):
    amostras = dist_func(*params, size=(m, n))
    medias_amostrais = amostras.mean(axis=1)
    return amostras, medias_amostrais

# Função para plotar histogramas
def plot_histogram(medias, title, dist_name, dist_params):
    plt.figure()
    plt.hist(medias, bins=30, density=True, alpha=0.6, color='g')
    mu, sigma = np.mean(medias), np.std(medias)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)
    plt.title(f'Histograma de Médias Amostrais - {title}')
    plt.xlabel('Média Amostral')
    plt.ylabel('Densidade')
    plt.grid(True)
    st.pyplot(plt)

# Streamlit interface
st.title("Simulação de Distribuições")

# Seleção das distribuições
opcoes_distribuicoes = ['Binomial', 'Exponencial', 'Uniforme', 'Normal', 'Qui-quadrado', 'Poisson', 't de Student']
distribuicoes_selecionadas = st.multiselect('Escolha as distribuições para simular:', opcoes_distribuicoes, default=opcoes_distribuicoes)

# Sliders e entradas numéricas para número e tamanho das amostras
col1, col2, col3, col4 = st.columns(4)
with col1:
    m = st.slider('Slider - Número de amostras (m):', 1, 5000, 1000)
with col2:
    m_input = st.number_input('Entrada - Número de amostras (m):', min_value=1, max_value=5000, value=m)
with col3:
    n = st.slider('Slider - Tamanho da amostra (n):', 1, 100, 30)
with col4:
    n_input = st.number_input('Entrada - Tamanho da amostra (n):', min_value=1, max_value=100, value=n)

# Usar valores das entradas numéricas para a simulação
m = m_input
n = n_input

# Parâmetros das distribuições
p_binomial = 0.05
lambda_exp = 1.0
a_uniform, b_uniform = 0, 1
mu_normal, sigma_normal = 0, 1
df_chi2 = 2
l_poisson = 3
df_t = 5
  
# # Sliders para escolher número e tamanho das amostras
# m = st.slider('Número de amostras (m):', 100, 5000, 1000, 100)
# n = st.slider('Tamanho da amostra (n):', 10, 100, 30, 10)


# Botão para executar a simulação
if st.button('Executar Simulação'):
    if 'Binomial' in distribuicoes_selecionadas:
        amostras_binomial, medias_binomial = gerar_amostras_e_medias(np.random.binomial, n, m, 1, p_binomial)
        plot_histogram(medias_binomial, 'Binomial', 'Binomial', {'p': p_binomial, 'n': 1})

    if 'Exponencial' in distribuicoes_selecionadas:
        amostras_exponencial, medias_exponencial = gerar_amostras_e_medias(np.random.exponential, n, m, lambda_exp)
        plot_histogram(medias_exponencial, 'Exponencial', 'Exponencial', {'lambda': lambda_exp})

    if 'Uniforme' in distribuicoes_selecionadas:
        amostras_uniforme, medias_uniforme = gerar_amostras_e_medias(np.random.uniform, n, m, a_uniform, b_uniform)
        plot_histogram(medias_uniforme, 'Uniforme', 'Uniforme', {'a': a_uniform, 'b': b_uniform})

    if 'Normal' in distribuicoes_selecionadas:
        amostras_normal, medias_normal = gerar_amostras_e_medias(np.random.normal, n, m, mu_normal, sigma_normal)
        plot_histogram(medias_normal, 'Normal', 'Normal', {'mu': mu_normal, 'sigma': sigma_normal})

    if 'Qui-quadrado' in distribuicoes_selecionadas:
        amostras_chi2, medias_chi2 = gerar_amostras_e_medias(np.random.chisquare, n, m, df_chi2)
        plot_histogram(medias_chi2, 'Qui-quadrado', 'Chi-Square', {'df': df_chi2})

    if 'Poisson' in distribuicoes_selecionadas:
        amostras_poisson, medias_poisson = gerar_amostras_e_medias(np.random.poisson, n, m, l_poisson)
        plot_histogram(medias_poisson, 'Poisson', 'Poisson', {'lambda': l_poisson})

    if 't de Student' in distribuicoes_selecionadas:
        amostras_t, medias_t = gerar_amostras_e_medias(np.random.standard_t, n, m, df_t)
        plot_histogram(medias_t, 't de Student', 't-Student', {'df': df_t})
