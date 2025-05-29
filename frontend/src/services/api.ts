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

// export const loginColaborador = async (dados: { cpf: string; senha: string }) => {
//   const response = await axios.post(`${API_BASE_URL}/login`, dados)
//   return response.data
// }

export async function loginColaborador(cpf: string, senha: string) {
  const response = await axios.post(`${API_BASE_URL}/login`, { cpf, senha })
  return response.data
}

export async function registrarPonto(colaborador_id: number) {
  console.log('Payload enviado para /registro:', { colaborador_id })

  const response = await axios.post(`${API_BASE_URL}/registro`, {
    colaborador_id: colaborador_id
  })

  console.log('Resposta do backend:', response.data)
  console.log('Resposta bruta do login:', response)
  return response.data
}
