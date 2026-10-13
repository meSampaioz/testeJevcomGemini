# Sandbox JEV com Gemini

Ambiente isolado (sandbox) containerizado com Docker para análise automatizada de logs de segurança (Apache/WAF) e tickets utilizando a API do Google Gemini. O projeto implementa `Pydantic` para forçar a IA a retornar dados estruturados em formato JSON (Type Safety).

## Pré-requisitos

* Ubuntu/Linux
* Docker e Docker Compose
* Chave de API do Google Gemini (Google AI Studio)

## Configuração do Ambiente

1. Clone este repositório.
2. Na raiz do projeto, crie um arquivo `.env` para armazenar sua credencial de forma segura:

```bash
echo 'GEMINI_API_KEY="SUA_CHAVE_AQUI"' > .env# testeJevcomGemini
