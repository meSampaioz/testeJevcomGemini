from google import genai
from pydantic import BaseModel
import time

chave_api = os.getenv("GEMINI_API_KEY")
cliente = genai.Client(api_key=chave_api)

ticket_suporte = "Our API integration started returning 500 errors on every request about 20 minutes ago, and we can't process any customer orders until this is fixed."

class AnaliseTicket(BaseModel):
    departamento: str 
    nivel_frustracao: int 
    urgente: bool 

max_tentativas = 10
for tentativa in range(max_tentativas):
    try:
        resposta = cliente.models.generate_content(
            model='gemini-3.8-flash',
            contents=f"Analise este ticket de suporte e preencha os dados: {ticket_suporte}",
            config={
                'response_mime_type': 'application/json',
                'response_schema': AnaliseTicket,
                'temperature': 0.0
            },
        )
        print(resposta.text)
        break
    except Exception as e:
        print(f"Erro na API. Tentativa {tentativa + 1} falhou. Aguardando...")
        time.sleep(5)
