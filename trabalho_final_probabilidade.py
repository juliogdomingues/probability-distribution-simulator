import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Função para gerar amostras e calcular médias amostrais
def gerar_amostras_e_medias(dist_func, n, m, *params):
    amostras = dist_func(*params, size=(m, n))
    medias_amostrais = amostras.mean(axis=1)
    return amostras, medias_amostrais

# Função para padronizar as médias amostrais
def padronizar_medias(medias, media_verdadeira, desvio_padrao_verdadeiro, tamanho_amostra):
    return (medias - media_verdadeira) / (desvio_padrao_verdadeiro / np.sqrt(tamanho_amostra))

# Função para plotar ambos os histogramas lado a lado
def plot_histograms_lado_a_lado(amostras, medias_padronizadas, title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Histograma das amostras originais
    ax1.hist(amostras.flatten(), bins=30, density=True, alpha=0.6, color='b')
    ax1.set_title(f'Histograma das Amostras - {title}')
    ax1.set_xlabel('Amostras')
    ax1.set_ylabel('Densidade')
    ax1.grid(True)

    # Histograma das médias amostrais padronizadas
    ax2.hist(medias_padronizadas, bins=30, density=True, alpha=0.6, color='g')
    mu, sigma = np.mean(medias_padronizadas), np.std(medias_padronizadas)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax2.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2)
    ax2.set_title(f'Histograma de Médias Amostrais - {title}')
    ax2.set_xlabel('Média Amostral')
    ax2.set_ylabel('Densidade')
    ax2.grid(True)

    # Mostrar a figura no Streamlit
    st.pyplot(fig)

# Streamlit interface
st.title("Simulação de Distribuições")

# Seleção da distribuição
opcoes_distribuicoes = ['Binomial', 'Exponencial', 'Uniforme', 'Normal', 'Qui-quadrado', 'Poisson', 't de Student']
distribuicao_selecionada = st.selectbox('Escolha a distribuição para simular:', opcoes_distribuicoes)

# Sliders para escolher número e tamanho das amostras
m = st.slider('Número de amostras (m):', 2, 1000, 300)
n = st.slider('Tamanho da amostra (n):', 2, 1000, 300)

# Parâmetros das distribuições com entrada do usuário
if distribuicao_selecionada == 'Binomial':
    p_binomial = st.number_input('Probabilidade de sucesso (p):', 0.0, 1.0, 0.5)
    amostras, medias = gerar_amostras_e_medias(np.random.binomial, n, m, n, p_binomial)
elif distribuicao_selecionada == 'Exponencial':
    lambda_exp = st.number_input('Taxa (lambda):', 0.0, 10.0, 1.0)
    amostras, medias = gerar_amostras_e_medias(np.random.exponential, n, m, 1/lambda_exp)
elif distribuicao_selecionada == 'Uniforme':
    a_uniform = st.number_input('Limite inferior (a):', 0.0, 10.0, 0.0)
    b_uniform = st.number_input('Limite superior (b):', a_uniform, 20.0, 1.0)
    amostras, medias = gerar_amostras_e_medias(np.random.uniform, n, m, a_uniform, b_uniform)
elif distribuicao_selecionada == 'Normal':
    mu_normal = st.number_input('Média (mu):', -10.0, 10.0, 0.0)
    sigma_normal = st.number_input('Desvio padrão (sigma):', 0.01, 10.0, 1.0)
    amostras, medias = gerar_amostras_e_medias(np.random.normal, n, m, mu_normal, sigma_normal)
elif distribuicao_selecionada == 'Qui-quadrado':
    df_chi2 = st.number_input('Graus de liberdade (df):', 1, 30, 2)
    amostras, medias = gerar_amostras_e_medias(np.random.chisquare, n, m, df_chi2)
elif distribuicao_selecionada == 'Poisson':
    l_poisson = st.number_input('Lambda (taxa de ocorrência):', 0.0, 10.0, 3.0)
    amostras, medias = gerar_amostras_e_medias(np.random.poisson, n, m, l_poisson)
elif distribuicao_selecionada == 't de Student':
    df_t = st.number_input('Graus de liberdade (df):', 1, 30, 5)
    amostras, medias = gerar_amostras_e_medias(np.random.standard_t, n, m, df_t)

# Cálculo da média e do desvio padrão das médias amostrais
media_verdadeira = np.mean(amostras) 
desvio_padrao_verdadeiro = np.std(amostras, ddof=1) / np.sqrt(n)  

# Plotar histograma das médias amostrais padronizadas e comparar com a distribuição normal padrão (0, 1)
medias_padronizadas = padronizar_medias(medias, media_verdadeira, desvio_padrao_verdadeiro, n)
plot_histograms_lado_a_lado(amostras, medias_padronizadas, distribuicao_selecionada)

footer = """
<hr style="border:1px solid #f1f1f1; margin-bottom: 25px">
<b>Autores:</b><br>
Júlio Guerra Domingues (2022431280)<br>
Samuel Sales Nogueira Viana (2021078455)<br><br>

Trabalho prático da disciplina Probabilidade (EST032) do Departamento de Estatística<br>
Instituto de Ciências Exatas - Universidade Federal de Minas Gerais
"""

st.markdown(footer, unsafe_allow_html=True)