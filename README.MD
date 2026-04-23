# Projeto PCP

## Instalação

1. Clone o repositório:

   git clone <URL_DO_REPOSITORIO>
   cd Projeto_PCP

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   python -m venv .venv
   .venv\Scripts\activate

3. Instale as dependências:

   pip install -r requirements.txt

## Uso

Para executar a interface Streamlit:

   streamlit run interface.py

Para rodar o módulo de salvamento de relatório diretamente:

   python -m db.salvar_relatorio
