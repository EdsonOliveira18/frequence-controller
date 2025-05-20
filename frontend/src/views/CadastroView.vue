<template>
  <div class="max-w-md mx-auto p-6 mt-10 bg-white shadow-md rounded">
    <h1 class="text-2xl font-bold mb-6 text-center">Cadastro de Colaborador</h1>

    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label class="block mb-1 font-medium" for="nome">Nome</label>
        <input
          id="nome"
          v-model="form.nome"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium" for="cpf">CPF</label>
        <input
          id="cpf"
          v-model="form.cpf"
          type="text"
          maxlength="11"
          pattern="\d*"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1 font-medium" for="email">Email</label>
        <input
          id="email"
          v-model="form.email"
          type="email"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition"
      >
        Cadastrar
      </button>
    </form>

    <!-- Exibição da senha gerada -->
    <div v-if="senhaGerada" class="mt-6 bg-green-100 border border-green-400 text-green-800 p-4 rounded">
      <p class="font-semibold">Cadastro realizado com sucesso!</p>
      <p>Sua senha: <strong>{{ senhaGerada }}</strong></p>
      <p class="text-sm text-gray-600 mt-2">Anote essa senha. Ela não será exibida novamente.</p>
    </div>

    <!-- Erros -->
    <div v-if="erro" class="mt-4 bg-red-100 border border-red-400 text-red-800 p-3 rounded">
      <p>{{ erro }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { cadastrarColaborador } from '@/services/api'

interface FormularioCadastro {
  nome: string
  cpf: string
  email: string
}

const form = ref<FormularioCadastro>({
  nome: '',
  cpf: '',
  email: '',
})

const senhaGerada = ref('')
const erro = ref('')

const handleSubmit = async () => {
  erro.value = ''
  senhaGerada.value = ''

  try {
    const resposta = await cadastrarColaborador(form.value)
    senhaGerada.value = resposta.senha_gerada
  } catch (err: any) {
    erro.value = err?.response?.data?.detail || 'Erro ao cadastrar colaborador.'
  }
}
</script>

<style scoped>
input:invalid {
  border-color: red;
}
</style>
