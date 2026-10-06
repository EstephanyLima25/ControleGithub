# Controle de Versões com GitHub

Projeto da disciplina de Desenvolvimento Web - atividade ANP (GitHub).

## Estrutura
- `alpha.py` - aplicação Flask principal (versão aula 07, templates de `t_templates/`)
- `Templates/` - versão da aula 06 (sem herança de template)
- `t_templates/` - versão da aula 07 com herança de template (`base.html`)
- `static/` - arquivos estáticos (css, js, img)
- A venv fica na pasta `ambvirtu/` e **não** é versionada (ver `.gitignore`)

## Branches
- `main` - versões das aulas 04 a 07 (commits incrementais)
- `aula6` - versão que utiliza a pasta `Templates` (aula 06)

## Como executar
```
ambvirtu\Scripts\activate
python alpha.py
```
