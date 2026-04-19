# Cantina Igreja

Sistema simples de gestão de vendas para a cantina da igreja.

## Objetivo

Controlar produtos, vendas, status de pagamento e estoque de forma simples, intuitiva e segura.

## Stack

- Frontend: React, TypeScript, Vite, Tailwind CSS e shadcn/ui
- Backend: Python, FastAPI
- Banco de dados: PostgreSQL

## Arquitetura

O projeto segue um monólito modular com separação clara entre frontend e backend.

- `frontend/`: interface web organizada por feature
- `backend/`: API e regras de negócio organizadas por módulo
- `docs/`: documentação do projeto

## Estrutura inicial

```text
cantina-igreja/
  frontend/
    public/
    src/
      app/
      components/
        layout/
        ui/
      features/
        dashboard/
          api/
          components/
          hooks/
          pages/
        products/
          api/
          components/
          context/
          hooks/
          pages/
        sales/
          api/
          components/
          context/
          hooks/
          pages/
      hooks/
      lib/
      styles/
      types/
  backend/
    app/
      core/
      db/
      modules/
        dashboard/
        products/
        sales/
    tests/
  docs/
```

## Diretrizes

- Clean Code como padrão de implementação
- Conventional Commits como padrão de versionamento
- Responsabilidade de negócio concentrada no backend
- Frontend orientado por features com contextos locais quando fizer sentido

## Conventional Commits

Exemplos:

- `feat: add sales creation flow`
- `fix: prevent stock update on pending payment`
- `chore: configure frontend linting`
- `docs: describe project architecture`

## Próximos passos

1. Inicializar o frontend com Vite e React + TypeScript
2. Configurar Tailwind CSS e shadcn/ui
3. Inicializar o backend com FastAPI
4. Configurar PostgreSQL e migrações
5. Implementar os módulos `products`, `sales` e `dashboard`
