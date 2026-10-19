# Guia Rápido: Como Ativar o Ambiente Virtual (Django)

O ambiente virtual **`meuAmbiente`** fica na pasta **`Projetos Django/`** para servir a **todos os projetos** (`001_projeto`, `002_projeto`, etc.), sem que você precise criar um novo a cada projeto.

---

## 1. Como ativar o ambiente virtual

Abra o terminal e escolha uma das opções abaixo conforme a pasta onde você estiver:

### Opção A: Se o terminal estiver na pasta `Projetos Django`
```powershell
.\meuAmbiente\Scripts\Activate.ps1
```

### Opção B: Se o terminal já estiver dentro de um projeto (ex: `Projetos Django\001_projeto`)
```powershell
..\meuAmbiente\Scripts\Activate.ps1
```

### Opção C: Se o terminal estiver na raiz do repositório (`IFB-Estudos`)
```powershell
.\Projetos` Django\meuAmbiente\Scripts\Activate.ps1
```

> **Como saber se funcionou?**
> Aparecerá **`(meuAmbiente)`** em verde no começo da linha do seu terminal.

---

## 2. Caso dê erro de permissão no PowerShell

Se aparecer uma mensagem vermelha dizendo que *"a execução de scripts foi desabilitada neste sistema"*, rode este comando uma única vez no terminal e depois tente ativar novamente:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

*(Alternativa pelo Prompt de Comando / CMD: use `.\meuAmbiente\Scripts\activate.bat`)*

---

## 3. Como rodar seu projeto Django após ativar

Com o `(meuAmbiente)` ativo, entre na pasta do projeto desejado (onde fica o `manage.py`):

```powershell
cd "001_projeto"
```

> **Atenção (Primeira vez que roda o projeto):**
> O banco de dados SQLite (`db.sqlite3`) também fica no `.gitignore`. Por isso, crie as tabelas antes de iniciar o servidor:
> ```powershell
> python manage.py migrate
> ```

Depois, inicie o servidor:

```powershell
python manage.py runserver
```


---

## 4. Como desativar o ambiente virtual

Quando quiser sair do ambiente virtual, basta digitar:

```powershell
deactivate
```

---

## 5. E se eu clonar o repositório em outro computador?

Por boas práticas, a pasta `meuAmbiente/` fica no `.gitignore` (não sobe para o GitHub por ser muito pesada e específica de cada máquina). Se você abrir o repositório em outro PC onde a pasta `meuAmbiente` ainda não exista, basta rodar estes 3 comandos dentro de `Projetos Django`:

```powershell
python -m venv meuAmbiente
.\meuAmbiente\Scripts\Activate.ps1
pip install -r requirements.txt
```

