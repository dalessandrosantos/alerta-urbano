#  Alerta Urbano

Sistema web desenvolvido em Django para reporte e gerenciamento de problemas urbanos.

Projeto desenvolvido como parte dos meus estudos de Análise e Desenvolvimento de Sistemas, com foco em back-end.

---

## O que o sistema faz

- **Qualquer cidadão** pode reportar um problema urbano, sem precisar de cadastro: escolhe a categoria, descreve o problema, informa o local e (opcionalmente) anexa uma foto.
- **A prefeitura** (usuário administrador logado) acompanha todos os reportes num painel, podendo visualizar detalhes, editar informações e atualizar o status de cada ocorrência conforme o problema é resolvido.

Fluxo de status de um reporte:
```
Reportado → Em análise → Resolvido
```

---

## Como usar

### Se você é um cidadão (reportar um problema)

1. Acesse a página inicial do site.
2. Preencha o formulário: escolha a categoria do problema, descreva o que está acontecendo e informe o endereço.
3. Se tiver uma foto do problema, anexe — ajuda a prefeitura a entender melhor a situação.
4. Clique em **Enviar**. Pronto, seu reporte foi registrado.

### Se você é administrador (gerenciar reportes)

1. Clique em **Login**, no canto superior direito.
2. Entre com seu usuário e senha.
3. Você será direcionado ao **Painel**, com a lista de todos os reportes recebidos.
4. Para cada reporte, você pode:
   - **Editar**: atualizar categoria, descrição, localização, imagem ou status.
   - **Deletar**: remover um reporte (o sistema pede confirmação antes de excluir).

---

## Tecnologias utilizadas

- **Python** + **Django** — back-end e lógica da aplicação
- **SQLite** — banco de dados
- **Bootstrap 5** — estilização
- **django-crispy-forms** — renderização dos formulários
- **Pillow** — manipulação de imagens enviadas
- **python-decouple** — gerenciamento de variáveis de ambiente

---

## Como rodar o projeto localmente

```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd alerta-urbano

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Criar um usuário administrador
python manage.py createsuperuser

# Rodar o servidor
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` no navegador.

---

## Screenshots

*Em breve.*

## 👤 Autor

[LinkedIn](https://www.linkedin.com/in/dalessandrosantos) 
