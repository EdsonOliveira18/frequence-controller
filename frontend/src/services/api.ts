import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export interface CadastroPayload {
  nome: string
  cpf: string
  email: string
}

export interface CadastroResponse {
  mensagem: string
  senha_gerada: string
}

export async function cadastrarColaborador(
  dados: CadastroPayload
): Promise<CadastroResponse> {
  const response = await axios.post(`${API_BASE_URL}/cadastro`, dados)
  return response.data
}
